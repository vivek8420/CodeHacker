from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.context_processors import csrf
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from Login.templates import *
from Profile.models import *
import smtplib

def f_password(request):
	print("f_password")
	c={}
	c.update(csrf(request))
	return render(request,'f_pass.html')

def send_email(request):
	try:
		print("send_email")
		c={}
		c.update(csrf(request))
		user_id=request.POST.get('user_id')
		user=Profile_det.objects.filter(user_id=user_id)
		if user:
			server=smtplib.SMTP('smtp.gmail.com',587)
			server.ehlo()
			server.starttls()
			server.login("savaliyavivek00@gmail.com","vivek@123")
			email_id= user[0].email
			otp = get_random_string(6, allowed_chars='0123456789')
			c['user_id']=user_id
			c['otp']=otp
			print(otp)
			msg='To:'+ email_id+'\n'+'From:savaliyavivek00@gmail.com'+'\n'+'Subject:otp\n'
			msg=msg + "hello your verify otp is "+otp
			server.sendmail("savaliyavivek00@gmail.com",email_id,msg)
			return render(request,'otp_verify.html',c)
		else:
			messages.add_message(request, messages.INFO, 'No Such User Exist')
			return render(request,'f_pass.html',c)
	except:
		print("hii")
		return HttpResponseRedirect('/forgot_pass/f_password/')

def otp_verify(request):
	try:
		print("otp_verify")
		c={}
		c.update(csrf(request))
		user_otp=request.POST.get('user_otp')
		otp=request.POST.get('otp')
		user_id=request.POST.get('u_id')
		c['user_id']=user_id
		if user_otp == otp:
			return render(request,'new_pass.html',c)
		else:
			messages.add_message(request, messages.INFO, 'your otp verification fail')
			return render(request,'f_pass.html',c)
	except:
		return HttpResponseRedirect('/forgot_pass/f_password/')

def set_password(request):
	try:
		print("set_password")
		c={}
		c.update(csrf(request))
		new_pass=request.POST.get('pass')
		user_id=request.POST.get('u_id')
		u=User.objects.get(username__exact=user_id)
		u.set_password(new_pass)
		u.save()
		return render(request,'login.html')
	except:
		return HttpResponseRedirect('/forgot_pass/f_password/')
