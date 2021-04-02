from django.shortcuts import render

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
		d = {'f':firstname,'l':lastname,'e':Mail}
		return render(request,'html/details.html',{'d':d})
	return render(request,'html/register.html')

