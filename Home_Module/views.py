from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from Profile.models import Profile_det
from django.template.context_processors import csrf
from django.contrib import messages
from Home_Module.views import *
from Profile.views import *
from Login.templates import *
from Login.views import *

def compete(request):
	c={}
	c.update(csrf(request))
	cur_time=datetime.now()
	challenge=compete_details.objects.all()
	for ch in challenge:
		s_time=ch.start_time
		e_time=ch.end_time
		t1=cur_time.replace(year=s_time.year,month=s_time.month,day=s_time.day,hour=s_time.hour,
							minute=s_time.minute,second=s_time.second,microsecond=0)
		t2=cur_time.replace(year=e_time.year,month=e_time.month,day=e_time.day,hour=e_time.hour,
							minute=e_time.minute,second=e_time.second,microsecond=0)
		print(cur_time,t1,t2)
		if t2 < cur_time:
			ch.challenge_status='past'
			ch.save()
		elif t1<=cur_time and t2>cur_time:
			ch.challenge_status='present'
			ch.save()
		else:
			ch.challenge_status='future'
			ch.save()
	challenge1=compete_details.objects.filter(challenge_status='future')
	challenge2=compete_details.objects.filter(challenge_status='present')
	challenge3=compete_details.objects.filter(challenge_status='past')
	return render(request,'compete.html',{'temp1':challenge1,'temp2':challenge2,'temp3':challenge3})

def all_problem(request):
	c={}
	c.update(csrf(request))
	challenge_code=request.GET.get('challenge')
	request.session['challenge']=challenge_code
	challenge=compete_details.objects.filter(challenge_code=challenge_code)
	if challenge[0].challenge_status == 'future':
		messages.add_message(request,messages.INFO,'This is future contest ,so you can not view problems')
		return render(request,'problem.html')
	else:
		problem=problem_details.objects.filter(challenge_code=challenge_code)
		return render(request,'problem.html',{'temp':problem})

def view_problem(request):
	c={}
	c.update(csrf(request))
	problem=request.GET.get('problem')
	request.session['problem']=problem
	file_name=str(problem).lower()+'.html'
	return render(request,file_name,c)

def practice(request):
	c = {}
	c.update(csrf(request))
	ch_list=compete_details.objects.filter(challenge_status='past')
	problem=problem_details.objects.filter(challenge_code='practice')
	for i in ch_list:
		past=problem_details.objects.filter(challenge_code=i.challenge_code)
		problem=problem | past
	return render(request,'practice.html', {'temp':problem})
	