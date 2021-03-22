from django.urls import path
from . import views

urlpatterns = [

	path('',views.index, name='index'),
	path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
	path('login_page',views.login_page,name='login_page'),
	path('signup_page',views.signup_page,name='signup_page'),
	path('register',views.register,name='register'),
	path('login',views.signin,name='login'),
	path('logout',views.logout_user,name='logout'),
	path('dashboard',views.dashboard_page,name='dashboard'),
	path('profile',views.profile,name='profile'),
	path("update/<int:pk>/", views.update_task, name="update_task"),
	path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]