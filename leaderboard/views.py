from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import generic
from django.template.context_processors import csrf
from django.contrib import messages
from CodeHacker.settings import *
from online_judge.templates  import *
from leaderboard.models import *
from Login.models import *
import os,io
from datetime import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.template import Context

@login_required(login_url='/Login/login/')
def view_leaderboard(request):
	print("view_leaderboard")
	c={}
	c.update(csrf(request))
	return HttpResponseRedirect('/leaderboard/compute_leaderboard/')

@login_required(login_url='/Login/login/')
def compute_leaderboard(request):
	try:
		print("compute_leaderboard")
		code=request.session.get('challenge')
		print(code)
		data=point_table.objects.filter(challenge_code=code).order_by('-maxscore')
		return render(request,'leaderboard.html',{'temp':data})
	except:
		return HttpResponseRedirect('/Home_Module/all_problem/')

@login_required(login_url='/Login/login/')
def update_leaderboard(request):
	try:
		user_id=request.user.username
		challenge=request.session.get('challenge')
		cur_time=datetime.now()
		compete=compete_details.objects.filter(challenge_code=challenge)
		s_time=compete[0].start_time
		e_time=compete[0].end_time
		
		
		t1=cur_time.replace(year=s_time.year,month=s_time.month,day=s_time.day,hour=s_time.hour,
								minute=s_time.minute,second=s_time.second,microsecond=0)
		t2=cur_time.replace(year=e_time.year,month=e_time.month,day=e_time.day,hour=e_time.hour,
								minute=e_time.minute,second=e_time.second,microsecond=0)
		if t1 <= cur_time and t2 >= cur_time:
			problem=request.session.get('problem')
			status=request.session.get('status')

			details=problem_score.objects.filter(challenge_code=challenge,user_id=user_id,problem_code=problem)
			point_details=point_table.objects.filter(user_id=user_id,challenge_code=challenge)
			#print(details.exists())
			#if details.exist() and point_details.exist():
				#print("not change")
			if not details.exists():
				if status:
					#print("if")
					s=problem_score(challenge_code=challenge,user_id=user_id,problem_code=problem,score=100)
					s.save()
					print(point_details.exists())
					if not point_details.exists():
						save=point_table(user_id=user_id,challenge_code=challenge,maxscore=100)
						save.save()
					else:
						prev_score=point_details[0].maxscore+100
						#print(prev_score)
						point_details.update(maxscore = prev_score)
				else:
					s=problem_score(challenge_code=challenge,user_id=user_id,problem_code=problem,score=0)
					s.save()
					if point_details is not None:
						save=point_table(user_id=user_id,challenge_code=challenge,maxscore=0)
						save.save()
			else:
				if status:
					#print("else")
					details.update(score=100)
					point_details.update(maxscore=100)
		c={}
		c.update(csrf(request))
		c['object_list']=status
		return render(request,'upload.html',c)
	except:
		return HttpResponseRedirect('/online_judge/upload_file/')