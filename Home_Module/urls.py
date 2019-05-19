from django.urls import path,include
from django.conf.urls import url
from Home_Module.views import *

urlpatterns = [
	url('compete',compete),
	url('all_problem',all_problem),
	url('view_problem',view_problem),
	url('practice',practice),
]
