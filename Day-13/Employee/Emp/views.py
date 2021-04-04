from django.shortcuts import render,redirect
from django.http import HttpResponse
from Emp.models import UserRg
from Emp.forms import UsregForm

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):

	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def regis(request):
	if request.method=="POST":
		firstname = request.POST['fname']
		lastname = request.POST['lname']
		password = request.POST['pwd1']
		Mail = request.POST['email']
		Age = request.POST['age']
		d = {'f':firstname,'l':lastname,'e':Mail,'a': Age}
		return render(request,'html/details.html',{'d':d})
	return render(request,'html/register.html')
def crud(request):
	if request.method=="POST":
		un = request.POST['username']
		email = request.POST['email']
		pas = request.POST['password']
		ag = request.POST['age']
		if len(un)!=0:
			data = UserRg.objects.create(username=un, password=pas ,email=email, age= ag)
			data2 = UserRg.objects.all()
			return render(request,'html/actions.html', {'info':data2})
	data2 = UserRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})
def deletedata(req,id):
	data=UserRg.objects.get(id=id)
	data.delete()
	#return render(request,'html/actions.html')
	return redirect('/cr')
def dform(request):
	if request.method=="POST":
		e=UsregForm(request.POST)
		if e.is_valid():
			e.save()
			data = UserRg.objects.all()
			return render(request,'html/data.html',{'info':data})

	e=UsregForm()
	return render(request,'html/dyform.html',{'tu':e})

