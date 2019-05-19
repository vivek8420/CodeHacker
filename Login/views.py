from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User,Group
from Profile.models import *
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import *
from Login.models import *

def login(request):
	try:
		print("login")
		if request.user.is_authenticated:
			return HttpResponseRedirect('/Profile/home')
		else:
			c={}
			c.update(csrf(request))
			return render(request,'login.html',c)
	except:
		return render(request,'login.html',c)

@login_required(login_url='/Login/login/')
def admin(request):
	try:
		if request.user.is_superuser:
			return render(request,'admin.html')
		else:
			return HttpResponseRedirect('/Profile/home/')
	except:
		return HttpResponseRedirect('/Profile/home/')

def auth_view(request):
	try:
		print("auth_view")
		if request.user.is_authenticated:
			return HttpResponseRedirect('/Profile')

		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user=authenticate(username=username,password=password)
		if user:
			auth.login(request,user)
			return HttpResponseRedirect('/Profile/home')
		else:
			messages.add_message(request,messages.WARNING,'Incorrect Username or Password')
			return render(request,'login.html')
	except:
		return HttpResponseRedirect('/Login/')

@login_required(login_url='/Login/login/')
def logout(request):
	try:
		print("L.logout")
		c={}
		c.update(csrf(request))
		auth.logout(request)
		return HttpResponseRedirect('/Login/')
	except:
		return HttpResponseRedirect('/Profile/')

@login_required(login_url='/Login/login/')
def add_problem(request):
	try:
		c={}
		c.update(csrf(request))
		return render(request,'add_problem.html',c)
	except:
		return HttpResponseRedirect('/Login/admin/')

@login_required(login_url='/Login/login/')
def store_problem(request):
	try:
		c={}
		c.update(csrf(request))
		challenge_code=request.POST.get('ch_code')
		problem_name=request.POST.get('p_name')
		problem_code=request.POST.get('p_code')
		difficulty=request.POST.get('diff')
		s=problem_details(challenge_code=challenge_code,problem_name=problem_name,
													problem_code=problem_code,difficulty=difficulty)
		s.save()
		messages.add_message(request, messages.WARNING, 'Problem add successfully')
		return render(request,'add_problem.html',c)
	except:
		return HttpResponseRedirect('/Login/add_problem/')

@login_required(login_url='/Login/login/')
def add_compete(request):
	try:
		c={}
		c.update(csrf(request))
		return render(request,'add_compete.html',c)
	except:
		return HttpResponseRedirect('/Login/admin/')

@login_required(login_url='/Login/login/')	
def store_compete(request):
	try:
		c={}
		c.update(csrf(request))
		c_name=request.POST.get('c_name')
		c_code=request.POST.get('c_code')
		start_time=request.POST.get('start_time')
		end_time=request.POST.get('end_time')
		temp_stime=datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")
		temp_etime=datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
		s=compete_details(challenge_name=c_name,challenge_code=c_code,challenge_status='future',start_time=temp_stime,end_time=temp_etime)
		s.save()
		messages.add_message(request, messages.WARNING, 'Challenge add successfully')
		return render(request,'add_compete.html',c)
	except:
		return HttpResponseRedirect('/Login/add_compete/')

@login_required(login_url='/Login/login/')
def about(request):
	c={}
	c.update(csrf(request))
	return render(request,'about.html',c)

@login_required(login_url='/Login/login/')
def contact(request):
	c={}
	c.update(csrf(request))
	return render(request,'contact.html',c)	