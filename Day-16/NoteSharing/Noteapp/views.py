from django.shortcuts import render,redirect
from Noteapp.forms import UsForm

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def regi(request):
	if request.method == "POST":
		t = UsForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/lg')
	t = UsForm()
	return render(request,'html/register.html',{'u':t})

def dashboard(req):
	return render(req,'html/dashboard.html')