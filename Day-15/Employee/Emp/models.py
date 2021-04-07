from django.db import models

# Create your models here.
class UserRg(models.Model):
	username = models.CharField(max_length = 120)
	password = models.CharField(max_length = 120 )
	email = models.CharField(max_length = 120)
	age = models.IntegerField(default=21)
	def __str__(self):
		return self.username+" "+self.email

class NewData(models.Model):
	ch=[('M','Male'),('F','Female')]
	phoneno = models.IntegerField(default=9398753723)
	gender = models.CharField(max_length=10,choices=ch)
	pid=models.OneToOneField(UserRg,on_delete=models.CASCADE)




