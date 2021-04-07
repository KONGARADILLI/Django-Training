from django.shortcuts import render,redirect
from django.http import HttpResponse
from Emp.models import UserRg,NewData
from Emp.forms import UsregForm,Userupdate,NewUsrForm

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
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			data = UserRg.objects.all()
			return redirect('/sd')
			return render(request,'html/data.html',{'info':data})

	e=UsregForm()
	return render(request,'html/dyform.html',{'tu':e})

def sdata(request):
	data = UserRg.objects.all()
	return render(request,'html/show.html',{'info':data})

def deledata(req,id):
	data=UserRg.objects.get(id=id)
	if req.method=="POST":
		data.delete()
		return redirect('/sd')
	return render(req,'html/userdelete.html',{'sd':data})

# def edit(req,id):
# 	data=UserRg.objects.get(id=id)
# 	if req.method=="POST":
# 		data.username= req.POST['username']
# 		data.age=req.POST['age']
# 		data.email = req.POST['email']
# 		data.password = req.POST['password']
# 		data.save()
# 		return redirect('/sd')
# 	return render(req,'html/useredit.html',{'info':data})

def update(up,si):
	t=UserRg.objects.get(id=si)
	h=NewData.objects.get(pid=si)
	if up.method=="POST":
		d= Userupdate(up.POST,instance=t)
		k= NewUsrForm(up.POST,instance=h)
		if d.is_valid() and k.is_valid():
			d.save()
			k.save()
			return redirect('/sd')
	d=Userupdate(instance=t)
	k = NewUsrForm(instance=h)
	return render(up,'html/updateuser.html',{'us':d,'nt':k})

def userinfo(req,uname):
	p= UserRg.objects.get(username=uname)
	h=NewData.objects.get(pid=p.id)
	return render(req,'html/viewinfo.html',{'y':p,'yu':h})