from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm
from .models import Task

# Create your views here.


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def login_page(request):
	return render(request,'login_page.html')

def signup_page(request):
	return render(request,'signup_page.html')

def register(request):
	#import pdb;pdb.set_trace();
	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']

	if request.method == 'POST':
		if (firstname != '')  and (lastname != '') and (username != '') and (email != '') and (password == confirm_password) :
			user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname , email=email, password=password)
			user.save()
			return redirect('login_page')
		else:
			messages.error(request,'Please Enter Valid Details')
	else:
		return render(request,'signup_page.html')


def signin(request):
	#import pdb;pdb.set_trace();
	username = request.POST['username']
	password = request.POST['password']
	 
	if request.method == 'POST':
		user = authenticate(request, username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('dashboard')
		else:
			messages.error(request,'username or password not correct')
			return redirect('login_page')
	else:

		return render(request,'login_page.html')

def logout_user(request):
	logout(request)
	return redirect('login_page')

def profile(request):
	return render(request,'profile.html')


@login_required
def dashboard_page(request):
	form = TaskForm()
	if request.method == "POST":
		form = TaskForm(request.POST)	
		if  form.is_valid():
			form.save()
			return redirect('dashboard')
	tasks = Task.objects.all()
	return render(request,'dashboard.html', {"task_form": form, "tasks":tasks})


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    return render(request, "update_task.html", {"task_edit_form": form})

def delete_task(request,pk):
	task = Task.objects.get(id=pk)
	task.delete()
	return redirect("dashboard")