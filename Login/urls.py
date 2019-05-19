from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from Login.views import *

urlpatterns = [
	 url(r'login',login),
	 url(r'auth_view',auth_view),
     url(r'logout',logout),
	 url(r'add_problem',add_problem),
	 url(r'store_problem',store_problem),
     url(r'add_compete',add_compete),
	 url(r'store_compete',store_compete),
	 url(r'admin',admin),
	 url(r'about',about),
	 url(r'contact',contact),
	 url(r'',login),
]
