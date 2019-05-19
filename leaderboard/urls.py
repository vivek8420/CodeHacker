from django.urls import path,include
from leaderboard import views
from django.conf.urls import url

urlpatterns=[
	url('view_leaderboard',views.view_leaderboard),
	url('compute_leaderboard',views.compute_leaderboard),
	url('update_leaderboard',views.update_leaderboard),
]