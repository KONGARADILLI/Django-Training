from django.urls import path
from Emp import views


urlpatterns = [
path('',views.home,name="hm"),
path('abt/',views.about,name="ab"),
path('con/',views.contact,name="cont"),
path('login/',views.login,name="log"),
path('reg/',views.regis,name="register"),
path('cr/',views.crud,name="cd"),
path('delt/<int:id>/',views.deletedata,name='delete'),
path('df/',views.dform,name='dff'),
path('sd/',views.sdata,name='showdata'),
path('deldata/<int:id>/',views.deledata,name='delete1'),
#path('edit/<int:id>/',views.edit,name='editdata'),
path('e/<int:si>/',views.update,name='ue'),
]