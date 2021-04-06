from Emp.models import UserRg
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model= UserRg
		#fields = "__all__"
		fields=['username','email','password']

		widgets= {
		"username":forms.TextInput(attrs = {"class": "form-control","placeholder":"Enter your name","required":True}),
		"email":forms.EmailInput(attrs = {"class": "form-control","placeholder":"Enter your Email","required":True}),
		"password":forms.PasswordInput(attrs = {"class": "form-control","placeholder":"Enter your Password","required":True}),
		
		}
class Userupdate(forms.ModelForm):
	class Meta:
		model = UserRg
		fields=['username','email','age']
		widgets= {
		"username":forms.TextInput(attrs = {"class": "form-control","placeholder":"Update your name","required":True}),
		"email":forms.EmailInput(attrs = {"class": "form-control","placeholder":"Update your Email","required":True}),
		"age":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Update your Age","required":True}),
		
		}