from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad

urlpatterns=[
path('',views.home,name='hm'),
path('about/',views.about,name='ab'),
path('contact/',views.contact,name='con'),
path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name='log'),
path('re/',views.regi,name='rg'),
path('ds/',views.dashboard,name='dash'),
path('lgot/',ad.LogoutView.as_view(template_name='html/logout.html'),name='logo'),
] 
