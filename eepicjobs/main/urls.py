from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
#from mysite.core import views as core_views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
				path('', views.index, name='index'),


        #path('order/<int:pk>',views.edit_order,name='edit_order'),
        path('order',views.order,name='order'),
        #url(r'^settings/$', core_views.settings, name='settings'),
   # url(r'^settings/password/$', core_views.password, name='password'),
        url(r'^oauth/', include('social_django.urls', namespace='social')),
                path('login/', views.login, name='login'),
                path('order',views.order,name='order'),
                path('adtype/<str:addtype>/',views.adtype,name='adtype'),
                path('adtypes/<str:addtype>/',views.adtypes,name='adtypes'),
                path('updatejob/<str:pk>/',views.updatejob,name='updatejob'),
                path('deletejob/<str:pk>/',views.deletejob,name='deletejob'),
                path('register/', views.register, name='register'),
                path('jobloc/<str:loc>/',views.jobloc,name="jobloc"),
                path("loc/",views.loc,name="loc"),
                path('types/<str:ctype>/',views.types,name="types"),
                path('logout/', views.logout, name='logout'),
                path('home/', views.home, name='home'),
                ########### CURRENT URLS ##########################
                path('sendmsg/', views.addmsg, name='sendmsg'),
                path('jobpost/', views.jobpost_create, name='jobpost'),
                path('home/jobpost/', views.jobpost_create, name='jobpost'),
                path('viewmsg/', views.viewmsg, name='viewmsg'),
                path('search/', views.searchjob, name='search'),
                path('searchJob/', views.searchjobb, name='searchJob'),
                path('automotive/', views.automotive, name='automotive'),
                path('health/', views.health, name='health'),
                path('food/', views.food, name='food'),
                path('educationIndustry/', views.educationIndustry, name='educationIndustry'),
                path('designer/', views.designer, name='designer'),
                path('cutomerService/', views.cutomerService, name='cutomerService'),
                path('createresume/', views.createresume, name='createresume'),
                path('project/', views.project, name='project'),
                path('education/', views.education, name='education'),
                path('change_password/', views.change_password, name='change_password'),
               # path('payment_method/',views.payment_method,name="payment_method"),
                path('card/',views.card,name="card"),
                path('noappli',views.noappli,name="noappli"),
                path('saved_jobs/',views.saved_jobs,name="saved_jobs"),
                 path('check_status_employee/', views.check_status_employee, name='check_status_employee'),
                path('show/', views.show, name='show'),
                
                path('applyjob/<jid>/', views.applyjob, name='applyjob'),
                path('applyjobb/<str:jid>/', views.applyjobb, name='applyjobb'),
                path('showmyjobs/', views.showmyjobs, name='showmyjobs'),
                 path('empview/', views.empview, name='empview'),
                  path('employerview/', views.employerview, name='employerview'),
                path('dashboard/', views.dashboard, name='dashboard'),
                path('updateEmp/<str:pk>/', views.updateEmp, name='updateEmp'),
                path('dashboard/employer/', views.employerin, name='employerin'),
                path('dashboard/employer/Profile/update', views.employerup, name='employerup'),
                path('updateresume/<str:pk>/', views.updateresume, name='updateresume'),
                path('dashboard/employee/', views.employeein, name='employeein'),
                path('dashboard/employee/Profile/update', views.employeeup, name='employeeup'),
                path('dashboard/employee/Profile/view', views.eeview, name='eeview'),
                path('dashboard/employee/alerts', views.employeeal, name='employeeal'),
                path('dashboard/employee/Jobs/applied', views.employeeapp, name='employeeapp'),
                path('dashboard/employee/order', views.employeeor, name='employeeor'),
                path('dashboard/employee/package', views.employeepack, name='employeepack'),
                path('dashboard/employee/Jobs/saved', views.employeesa, name='employeesa'),
                path('dashboard/employee/Resume', views.employeeresume, name='employeeresume'),
                path('dashboard/employerdetails/', views.employerdetails, name='employerdetails'),
                path('checksubscription/',views.check_status,name='check_status'),
                 path('rr/', views.rr, name='rr'),
                path("jobss",views.jobss,name='jobss'),
                 path('saveresum/<str:e>/<str:r>/', views.saveresum, name='saveresum'),
                 path('sav_jobs/<str:ee>/<str:jid>/', views.sav_jobs, name='sav_jobs'),
                 path('rrr/<str:pk>', views.rrr, name='rrr'),
                  path('savedresume', views.saved_resume, name='saved_resume'),
                  path('subsform/',views.sub,name='sub'),
                  path('showapplicants/<str:jid>/', views.showapplicants, name='showapplicants'),
                 path('sendemail/<str:apid>', views.sendemail, name='sendemail'), 
                 path('sending/<str:apid>/', views.sending, name='sending'), 
                 path('seeing/<str:apid>/', views.seeing, name='seeing'),
                 path('eeup/<str:pk>/', views.eeup, name='eeup'),
                 path('eduup/<str:pk>/', views.eduup, name='eduup'),
                path('updateJobexp/<str:pk>/', views.updateJobexp, name='updateJobexp'),
                 path('proup/<str:pk>/', views.proup, name='proup'),
                 path('updatesubs/<str:pk>/', views.updatesubs, name='updatesubs'), 
                 path('employeedetails/', views.employeedetails, name='employeedetails'),
                 path('jobexpe', views.jobexpe, name='jobexpe'),
                 path('eeview', views.eeview, name='eeview'),
                 path('showapplied/<str:pk>', views.showapplied, name='showapplied'),
                  path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    url(r'^recharge/$', views.recharge, name='recharge'),
    url(r'^charge/$', views.charge, name='charge'),
    path('contract', views.contract, name='contract'),
path('internship', views.internn, name='internn'),
path('walk', views.walk, name='walk'),
path('premium', views.premium, name='premium'),
path('feature', views.feat, name='feat'),
path('indust', views.indust, name='indust'),
path('typesss', views.typesss, name='typesss'),
path('jobpostt', views.jobpostt, name='jobpostt'),
path('req', views.req, name='req'),
path('coun', views.coun, name='coun'),
path('sal', views.sal, name='sal'),
path('latest', views.latest, name='latest'),
path('multistepform', views.multistepform, name='multistepform'),

]