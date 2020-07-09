from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
				path('', views.index, name='index'),
                path('login/', views.login, name='login'),
                path('register/', views.register, name='register'),
                path('logout/', views.logout, name='logout'),
                path('home/', views.home, name='home'),
                ########### CURRENT URLS ##########################
                path('sendmsg/', views.addmsg, name='sendmsg'),
                path('jobpost/', views.jobpost_create, name='jobpost'),
                path('home/jobpost/', views.jobpost_create, name='jobpost'),
                path('viewmsg/', views.viewmsg, name='viewmsg'),
                path('search/', views.searchjob, name='search'),
                path('auto/', views.searchindustry, name='auto'),
                path('searchJob/', views.searchjobb, name='searchJob'),
                path('createresume/', views.createresume, name='createresume'),
                path('project/', views.project, name='project'),
                 path('education/', views.education, name='education'),
                path('show/', views.show, name='show'),
                path('applyjob/<jid>', views.applyjob, name='applyjob'),
                path('showmyjobs/', views.showmyjobs, name='showmyjobs'),
                path('dashboard/', views.dashboard, name='dashboard'),
                path('dashboard/employer/', views.employerin, name='employerin'),
                path('dashboard/employer/Profile/update', views.employerup, name='employerup'),
                path('updateresume/<str:pk>/', views.updateresume, name='updateresume'),
                path('dashboard/employee/', views.employeein, name='employeein'),
                path('dashboard/employee/Profile/update', views.employeeup, name='employeeup'),
                path('dashboard/employee/Profile/view', views.employeev, name='employeev'),
                path('dashboard/employee/alerts', views.employeeal, name='employeeal'),
                path('dashboard/employee/Jobs/applied', views.employeeapp, name='employeeapp'),
                path('dashboard/employee/order', views.employeeor, name='employeeor'),
                path('dashboard/employee/package', views.employeepack, name='employeepack'),
                path('dashboard/employee/Jobs/saved', views.employeesa, name='employeesa'),
                path('dashboard/employee/Resume', views.employeeresume, name='employeeresume'),
                 path('rr/', views.rr, name='rr'),
]