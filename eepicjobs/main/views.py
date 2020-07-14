from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import settime
from  accounts.setime import settimeForm
from datetime import date
from django.contrib.auth.hashers import make_password
from  accounts.models import Jobpost
from  accounts.models import Jobexperience
from accounts.Jobexp import JobexperienceForm
from  accounts.models import Employee
from  accounts.employee import EmployeeForm
from  accounts.models import Employer
from  accounts.models import savedresume
from  accounts.models import subscriptionpack
from  accounts.subsform import subscriptionpackForm
from  accounts.employer import EmployerForm
from  accounts.projects import ProjectsForm
from  accounts.models import UserProfile
from accounts.models import applicant
from accounts.models import Education
from accounts.education import EducationForm
from accounts.Jobforms import JobPostform
from accounts.applyjob import applicantform
from accounts.resume import UserProfileForm
from .models import *
from json import dumps 
import json
from django.core import serializers
from datetime import date
from django.conf import settings
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import os
import json
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import uuid
import time
from django.db.models import Q
from accounts.models import *
from eepicjobs.utils import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index.html')
@csrf_exempt
def login(request):
    """
    The main login view for any particular user that have already registered on the platform
    """
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print("It runs")
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            username_status = valid_username(username)
            print("1-{}".format(username_status))
            if username_status:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                        return redirect('dashboard')
                    else:
                        messages.error(request, 'Your account has been suspended')
                        return redirect('login')
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('login')
            else:
                return redirect('login')
    else:
        return redirect('home')
    return render(request, 'login.html')

def stupro(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please Login!')
        return redirect('login')
    if request.method == 'POST':
        course = Course.objects.get(id=request.POST.get('course'))

        student = StudentProfile()
        student.course = course
        student.profile = request.user.userprofile
        student.bio = request.POST.get('bio')
        student.save()
        messages.success(request,'Profile Completed !')
        return redirect('home')
    else:
        return render(request,'stureg.html')
@csrf_exempt
def register(request):
    """
    The main registration handler for the users who visits the platform. When a user registers, it basically automatically login.
    """
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # Getting the data from the front-end
            username = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            cat = int(request.POST.get('type'))
            phone_number = request.POST.get('phone_number')
            hashed_password = make_password(str(password))

            try:
                user = User.objects.get(username=username)
                messages.warning(request,'ID Already Exists PID : '+str(user.username))
                return redirect(register)
            except User.DoesNotExist:
                try:
                    user = User.objects.create(username=username, email=email, password=hashed_password, first_name=first_name, last_name=last_name)
                    if user.is_active:
                        auth_login(request, user)
                        profile = UserProfile()
                        profile.user = user
                        if cat == 1:
                            profile.is_emp = True
                        else:
                            profile.is_seek = True
                        #if request.FILES['pic']:
                        #    profile.profile_photo=request.FILES['pic']
                        try:
                            profile.phone_number = phone_number
                        except:
                            messages.warning(request,'Invalid Phone Number')
                        profile.save()
                        return redirect('dashboard')
                    else:
                        messages.error(request, 'Your account has been suspended')
                        return redirect('login')
                except:
                    messages.error(request, 'Something Unusual Happened')
                    return redirect('home')
        else:
            return render(request, 'register.html')
    else:
        return redirect('home')

def home(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please Login')
        return redirect(index)
    else:
        messages.success(request,'Welcome '+ str(request.user.first_name))
    return render(request, 'index.html')

def logout(request):
    auth_logout(request)
    try:
        del request.session['pid']
    except:
        pass
    messages.success(request,'Logged Out Successfully')
    return redirect(index)


@csrf_exempt
def addmsg(request): #takes 'msg' as post variable
    if request.method == 'POST':
        try:
            setmsg = Discuss()
            try:
                try:cid = request.session['CID']
                except:cid = request.POST['cid']
                topid = request.POST['topid']
                frompid = request.POST['frompid']
            except:
                return JsonResponse({'status':'Improper Request'})
            #print("\n##################\n",request.POST['topid'],request.POST['frompid'],"\n",topid,frompid,request.POST['type'],"\n##################\n")
            setmsg.fromPID = UserProfile.objects.get(id=frompid).id
            setmsg.CID = Chat.objects.get(CID=cid)
            setmsg.toPID = UserProfile.objects.get(id=topid)
            setmsg.message = request.POST['msg'].replace('%3B',';').replace('%2B','+')
            try: setmsg.type = request.POST['type']
            except:pass
            setmsg.save()
            return JsonResponse({'status':'Success'})
        except:
            return JsonResponse({'status':'Failed'})
    else:
        return JsonResponse({'status':'Improper Request'})

@csrf_exempt
def viewmsg(request): #takes CID and PID in request GET
    if request.method == 'GET':
        try:
            try:
                cid = request.GET['cid']
                topid = request.GET['topid']
            except:
                return JsonResponse({'status':'Something went Wrong!'})
            z=[]
            z.append(Discuss.objects.filter(toPID=topid,CID=cid,type='noramlmessage'))
            cpid = Chat.objects.filter(CID=cid)[0].PID.id
            if str(cpid)!=str(topid):
                z.append(Discuss.objects.filter(toPID=cpid,CID=cid))
            else:
                z.append(Discuss.objects.filter(CID=cid).exclude(toPID=cpid))
            wett={}
            wet={}
            try:
                wq={}
                zil=Participant.objects.filter(CID=Chat.objects.get(CID=cid))
                for e in zil:
                    wq[e.PID.id]=e.PID.user.first_name
                wet['participants']=wq
            except:
                wet['participants']={"0":"No Participants in this Chat"}
            c=0
            for u in z:
                for i in u:
                    q={}
                    q['CID']=i.CID.CID
                    q['ID']=i.ID
                    q['PID']=i.PID.id
                    q['time']=i.time
                    q['dislayname']=User.objects.filter(id=i.PID.user.id)[0].first_name+" ("+User.objects.filter(id=i.PID.user.id)[0].username+")"
                    q['message']=i.message
                    wett[c]=q
                    c+=1
            wet['messages']=wett
            return JsonResponse(wet)
        except:
            return JsonResponse({'status':'Something went Wrong!'})

def delmsg(request):
    try:
        aaaa=False
        try:
            cid=request.GET['cid']
            try:
                topid=request.GET['topid']
            except:
                aaaa=True
            frompid=request.GET['frompid']
        except:
            return JsonResponse({'Status':'Invalid request'})
        aaa=True
        try:
            msg=unquote(request.GET['msg'])
            print(msg)
            aaa=False
        except:pass
        per1=UserProfile.objects.get(id=topid)
        per2=UserProfile.objects.get(id=frompid)
        if aaa:   
            ey=Discuss.objects.filter(Q(CID=cid),Q(fromPID=per1.id),Q(toPID=per2)).exclude(type='msg')
            eyy=Discuss.objects.filter(Q(CID=cid),Q(toPID=per1),Q(fromPID=per2.id)).exclude(type='msg')
            #print("@@@@@@@@@@Deleting ",len(ey)+len(eyy),"records@@@@@@@@@@@@")
            eyy.delete()
            ey.delete()
        elif aaaa:   
            ey=Discuss.objects.filter(Q(CID=cid),Q(fromPID=per1.id)).exclude(type='msg')
            ey.delete()
        else:
            eey=Discuss.objects.filter(Q(CID=cid),Q(message=msg),Q(fromPID=per1.id),Q(toPID=per2)).exclude(type='msg')
            eeey=Discuss.objects.filter(Q(CID=cid),Q(message=msg),Q(toPID=per1),Q(fromPID=per2.id)).exclude(type='msg')
            #print("##########Deleting ",str(len(eey)+len(eeey)),"records#######")
            eey.delete()
            eeey.delete()
        
        #print("\n\nSuccess\n\n")
        return JsonResponse({'Status':'Success'})
    except:
        return JsonResponse({'Status':'Something went wrong :-('})




def jobpost_create(request):
    form=JobPostform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    #form= JobPostform()
    context = {
        "form": form,}
    return render(request, 'jobPostForm.html',context)

def searchjob(request):
    if(request.method=='POST'):
        srch=request.POST['srh']
        if srch:
            match=Jobpost.objects.filter(Q(JobTitle__icontains=srch) | Q(JobDesciption__icontains=srch) | Q(jobType__iexact=srch))
            if(match.exists()):
                return render(request,'searchjob.html',{'sr':match})
            else:
                messages.error(request,"Sorry! No results found.")
        else:
            return HttpResponseRedirect("/search/")
    return render(request,'searchjob.html')

def searchjobb(request):
    if(request.method=='POST'):
        srch=request.POST['srh']
        if srch:
            match=Jobpost.objects.filter(Q(JobTitle__icontains=srch) | Q(JobDesciption__icontains=srch) | Q(jobType__iexact=srch))
            if(match.exists()):
                return render(request,'index.html',{'sr':match})
            else:
                messages.error(request,"Sorry! No results found.")
        else:
            return HttpResponseRedirect("/searchJob/")
    return render(request,'index.html')


    
def automotive(request):
    match = Jobpost.objects.filter(Q(Jobindustry__icontains="automotive") | Q(JobDesciption__icontains="automotive") | Q(Jobindustry__icontains="automotion"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')
    



def food(request):
    match = Jobpost.objects.filter(Q(Jobindustry__icontains="food") | Q(JobDesciption__icontains="food service") | Q(Jobindustry__icontains="food"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')


def educationIndustry(request):
    match = Jobpost.objects.filter(Q(Jobindustry__icontains="education"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')

def designer(request):
    match = Jobpost.objects.filter(Q(Jobindustry__icontains="designer"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')


def cutomerService(request):
    match = Jobpost.objects.filter(Q(Jobindustry__icontains="Customer Service") | Q(Jobindustry__icontains="Customer Care"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')


def health(request):
    match = Jobpost.objects.filter(Q(Jobindustry__icontains="Health"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')




def project(request):
    form=ProjectsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.projectuser=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'projects.html',context)
    
def createresume(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created")
            return redirect('education')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        "form": form,}
    return render(request, 'resume.html',context)



def updateresume(request,pk):
    up=UserProfile.objects.get(id=pk)
    form=UserProfileForm(instance=up)
    if(request.method=='POST'):
        form=UserProfileForm(request.POST,instance=up)
        if form.is_valid():  
                form.save()
                messages.success(request,"Successfully created")
                return redirect('/') 
    context={'form':form}
    return render(request,'resume.html',context)  



def show(request):  
    employees = UserProfile.objects.filter(user=request.user)  
    pro = Project.objects.filter(projectuser=request.user.userprofile)
    edu=Education.objects.filter(resume=request.user.userprofile)
    context={"employees":employees,"edu" : edu,"pro":pro}
    return render(request, "show.html", context)

def education(request):
    form=EducationForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('project')
    context = {
        "form": form,}
    return render(request, 'education.html',context)

     
                    

def applyjob(request, jid):
    form=applicantform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    #form= JobPostform()
    job = Jobpost.objects.get(id=jid)
    context = {
        "form": form,
        "job": job,}
    return render(request, 'applyjob.html',context)

def showmyjobs(request):
    jobdisplay=Jobpost.objects.filter(user=request.user.userprofile)
    return render(request,'showmyjobs.html',{'jobdisplay':jobdisplay})

def dashboard(request):
    try:
        if request.user.userprofile :
            if request.user.userprofile.is_emp:
                return render(request,'employer/index.html')
            elif request.user.userprofile.is_seek:
                return render(request,'employee/index.html')
            else:
                return render(request,'dashboard.html')
    except:
        return render(request,'dashboard.html')

def employerin(request):
    return render(request,'employer/index.html')
    
def employerup(request):
    return render(request,'employer/update.html')



def employeein(request):
    return render(request,'employee/index.html')
    
def employeeup(request):
    return render(request,'employee/update.html')


    

def employeeapp(request):
    return render(request,'employee/applied.html')

def employeeor(request):
    return render(request,'employee/order.html')

def employeeal(request):
    return render(request,'employee/alerts.html')

def employeepack(request):
    return render(request,'employee/packages.html')

def employeeresume(request):
    return render(request,'employee/resume.html')

def employeesa(request):
    return render(request,'employee/saved.html')


def rr(request):
    ress = UserProfile.objects.filter(user=request.user)
    edu=Education.objects.filter(resume=request.user.userprofile)
    pro = Project.objects.filter(projectuser=request.user.userprofile)
    context={"ress":ress,
    "edu" : edu,
    "pro":pro}
    return render(request, 'resumebuilder.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


def employerdetails(request):
    form=EmployerForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'e.html',context)

def empview(request):
    employees=Employer.objects.filter(empuser=request.user.userprofile)
    return render(request,'employer/view.html',{'employees':employees})
    
    
def updateEmp(request,pk):
    up=Employer.objects.get(id=pk)
    form=EmployerForm(instance=up)
    if(request.method=='POST'):
        form=EmployerForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('/') 
    context={'form':form}
    return render(request,'e.html',context) 

def employerview(request):
    employees=Employer.objects.filter(empuser=request.user.userprofile)
    return render(request,'employer/index.html',{'employees':employees})


def showapplicants(request, jid):
    ap=Jobpost.objects.filter(user=request.user.userprofile)
    jobb = ap.get(id=jid)
    appli=applicant.objects.filter(job=jobb)
    if appli.exists():
        return render(request,'showapplicants.html',{'appli':appli})
    else:
        messages.error(request,'There are no applicants to this job yet')
        return redirect('home')

def applyjobb(request, jid):
    form=applicantform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    #form= JobPostform()
    job = Jobpost.objects.get(id=jid)
    context = {
        "form": form,
        "job": job,}
    return render(request, 'applyjobb.html',context)

def saved_resume(request):
    sav=savedresume.objects.filter(empid=request.user.userprofile.employer)
    return render(request,'saved_resume.html',{"sav": sav})


def check_status(request):
    #to check if subscription of logged in user is expired or not
    value=subscriptionpack.objects.filter(empid=request.user.userprofile.employer)
    stat=""
    if (value.exists()):
        for k in value:
            d0 =k.purchasedate
            d1=date.today()
            delta = d1 - d0
            if(delta.days>30):
                k.status="expired"
                stat='expired'
            else:
                k.status="active"
                stat="active"
            subs=k.subscriptionid    
            
        context={'subs':subs,'stat':stat} 
        return render(request,'subscription.html',context)
    else:
        messages.error(request, "Sorry! No valid subscriptions")
        return redirect('home')

def check_status_employee(request):
    #to check if subscription of logged in user is expired or not
    eevalue=subscriptionpack.objects.filter(empid=request.user.userprofile)
    stat=""
    if (eevalue.exists()):
        for k in eevalue:
            d0 =k.purchasedate
            d1=date.today()
            delta = d1 - d0
            if(delta.days>30):
                k.status="expired"
                stat='expired'
            else:
                k.status="active"
                stat="active"
            subs=k.subscriptionid    
            
        context={'subs':subs,'stat':stat} 
        return render(request,'subscription.html',context)
    else:
        messages.error(request, "Sorry! No valid subscriptions")
        return redirect('home')

def sub(request):
    form=subscriptionpackForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.empid=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'subsformm.html',context)

def updatesubs(request,pk):
    up=subscriptionpack.objects.get(id=pk)
    form=subscriptionpackForm(instance=up)
    if(request.method=='POST'):
        form=subscriptionpackForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('/') 
    context={'form':form}
    return render(request,'subsformm.html',context) 



def sendemail(request,aid):
    '''if(request.method=='GET'):
        return render(request,'settime.html')'''
    s=settime.objects.filter(empid=request.user.userprofile)
    ap=applicant.objects.get(id=aid)
    a=s.objects.filter(appliid=a)

    send_mail("Regarding the Interview Process","Congratulations on being selected for the interview.Your interview will be held on "+s.indate+" timings are "+s.intime,"eepicjob.com",["recipent@gmail.com"],fail_silently=False)
    return render(request,'sendemail.html')


def settiiiime(request):
    form=settimeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'set_time.html',context)



def sending(request,apid):
    form=settimeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'set_time.html',context)

def seeing(request,apid):
    a=applicant.objects.get(id=apid)
    ss=settime.objects.filter(empid=request.user.userprofile.employer,apliid=a )
    if(ss.exists()):
            context={'ss':ss}
            return render(request,"seeing.html",context)
    else:
        messages.error(request,'no time set')
        return redirect('home')

def employeedetails(request):
    form=EmployeeForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.employeeuser=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('jobexpe')
    context = {"form":form}
    return render(request, 'employee/ee.html',context)


    

def jobexpe(request):
    form=JobexperienceForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.euser=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('education')
    context = {
        "form": form,}
    return render(request, 'employee/Jobexp.html',context)


def updateJobexp(request,pk):
    up=Jobexperience.objects.get(id=pk)
    form=JobexperienceForm(instance=up)
    if(request.method=='POST'):
        form=JobexperienceForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('employeein') 
    context={'form':form}
    return render(request,'employee/Jobexp.html',context)



def eeview(request):
    ress = Employee.objects.filter(employeeuser=request.user.userprofile)
    edu=Education.objects.filter(resume=request.user.userprofile)
    pro = Project.objects.filter(projectuser=request.user.userprofile)
    jobb=Jobexperience.objects.filter(euser=request.user.userprofile)
    context={"ress":ress,
    "edu" : edu,
    "pro":pro,"jobb":jobb}
    return render(request, 'employee/eevieww.html', context)

def eeup(request,pk):
    up=Employee.objects.get(id=pk)
    form=EmployerForm(instance=up)
    if(request.method=='POST'):
        form=EmployeeForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('dashboard/employee/') 
    context={'form':form}
    return render(request,'employee/ee.html',context) 

def eduup(request,pk):
    up=EducationForm.objects.get(id=pk)
    form=EmployerForm(instance=up)
    if(request.method=='POST'):
        form=EmployerForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('dashboard/employee/') 
    context={'form':form}
    return render(request,'education.html',context) 


def proup(request,pk):
    up=Project.objects.get(id=pk)
    form=ProjectsForm(instance=up)
    if(request.method=='POST'):
        form=ProjectsForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('dashboard/employee/') 
    context={'form':form}
    return render(request,'projects.html',context) 


def showapplied(request,pk):
     appli=applicant.objects.filter(user=request.user.userprofile)
     return render(request,'showapplied.html',{'appli':appli})
    