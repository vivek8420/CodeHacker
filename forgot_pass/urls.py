from django.urls import path,include
from forgot_pass.views import *
from django.conf.urls import url

urlpatterns=[
	url('f_password',f_password),
	url('send_email',send_email),
	url('otp_verify',otp_verify),
	url('set_password',set_password),
]