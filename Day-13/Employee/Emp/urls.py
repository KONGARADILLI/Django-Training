from django.urls import path
from Emp import views


urlpatterns = [
path('',views.home,name="hm"),
path('abt/',views.about,name="ab"),
path('con/',views.contact,name="cont"),
path('login/',views.login,name="log"),
path('reg/',views.regis,name="register"),
path('cr/',views.crud,name="cd"),
path('delt/<str:id>',views.deletedata,name='delete'),
path('df/',views.dform,name='dff'),
]