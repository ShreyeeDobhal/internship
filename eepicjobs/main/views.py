import stripe
from django.core.files.storage import FileSystemStorage
from datetime import timedelta
from django.db.models import F
from django.conf import settings
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import settime
from accounts.models import Pay
from  accounts.setime import settimeForm
from  accounts.setime import set_TimeForm
from datetime import date

from django.contrib.auth.hashers import make_password
from  accounts.models import Jobpost
from  accounts.models import Jobpostt
from  accounts.models import Jobexperience
from accounts.Jobexp import JobexperienceForm
from  accounts.models import Employee
from  accounts.employee import EmployeeForm
from  accounts.models import Employer
from  accounts.models import Svedresume
from  accounts.models import subscription
from  accounts.subsform import subscriptionForm
from  accounts.employer import EmployerForm
from  accounts.projects import ProjectsForm
from  accounts.models import UserProfile
from accounts.models import applicant
from accounts.models import Education
from accounts.education import EducationForm
from accounts.Jobforms import JobPostform
from accounts.applyjob import applicantform
from accounts.applyjob import applicanttform
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

stripe.api_key="sk_test_51H55s7EqYDD5vPrpoPYOjFkBpY9BjqS72mY8R1e9u1aiB2SL9ZjheHIttbyCaBSXFFLwttyxxKtZykHJwNjPXEyX00lzRgnd54"


def index(request):
    match=Jobpostt.objects.all().order_by("-posted_on")[:9]
    featu=Jobpostt.objects.filter(ad__icontains="feature")[:4]
    pre=Jobpostt.objects.filter(ad__icontains="premium")[:4]
    contr=Jobpostt.objects.filter(contractType__icontains="Contract")[:4]
    inter=Jobpostt.objects.filter(contractType__icontains="internship")[:4]
    context={"lat":match,"featu":featu,"pre":pre,"contr":contr,"inter":inter}
    return render(request, 'index.html',context)
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
                        if cat==1:
                            return redirect('employerdetails')
                        if cat!=1:
                            return redirect("employeedetails")

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
    match=Jobpostt.objects.all().order_by("-posted_on")[:9]
    featu=Jobpostt.objects.filter(ad__icontains="feature")[:4]
    pre=Jobpostt.objects.filter(ad__icontains="premium")[:4]
    contr=Jobpostt.objects.filter(contractType__icontains="Contract")[:4]
    inter=Jobpostt.objects.filter(contractType__icontains="internship")[:4]
    context={"lat":match,"featu":featu,"pre":pre,"contr":contr,"inter":inter}
    return render(request, 'index.html',context)

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






def check_stat(request):
    #to check if subscription of logged in user is expired or not
    eevalue=subscription.objects.filter(user=request.user)
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
        return context
def jobpostt(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("multistepform"))
    else:
        jd=request.POST.get("jd")
        qu=request.POST.get("job_qualification")
        jt=request.POST.get("jt")
        contract=request.POST.get("contract")
        ji=request.POST.get("ji")
        sal1=request.POST.get("sal1")
        sal2=request.POST.get("sal2")
        hear=request.POST.get("hear")
        adtype=request.POST.get("ad")
        jobType=request.POST.get("jobtype")
        phone=request.POST.get("phone")
        comp=request.POST.get("twitter")
        no_of=request.POST.get("facebook")
        valid_till=request.POST.get("valid_till")
        email=request.POST.get("email")
        job_shift=request.POST.get("job_shift")
        job_experience=request.POST.get("job_experience")
        job_level=request.POST.get("job_level")
        company_logo=request.FILES["myfile"]
        fs=FileSystemStorage()
        name=fs.save(company_logo.name,company_logo)
        url=fs.url(name)
        print(url)
        co=request.POST.get("co")
        loc=request.POST.get("loc")
        req=request.POST.get("req")
        updates_email=request.POST.get("updates_email")
        salary=request.POST.get("salary")
        print(company_logo.name)
        print(company_logo.size)
        try:
            if(adtype=="Premium"):
                try:
                    if(request.user.subscription.id):
                        context=check_stat(request)
                        if context["stat"]=="expired":
                            adtype="Featured"
                        else:
                            adtype="Premium"
                except:
                    adtype="Featured"
                    
  
            multistepform=Jobpostt(user=request.user.userprofile,job_shift=job_shift,job_experience=job_experience,job_level=job_level,salary=salary,qualification=qu,updates_email=updates_email,requirements=req,valid_till=valid_till,location=loc,company_logo=company_logo,country=co,salary_type=sal1,salary_currency=sal2,contractType=contract,JobTitle=jt,JobDesciption=jd,Jobindustry=ji,jobType=jobType,phone_number=phone,no_of_employees=no_of,CompanyName=comp,hear=hear,email=email,ad=adtype)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return redirect("employerin")
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepform'))


def multistepform(request):
    return render(request,"multistepform.html")



def jobpost_create(request):
    form=JobPostform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user.userprofile
        if(instance.ad=="Premium"):
            try:
                if(request.user.subscription.id):
                    context=check_stat(request)
                    if context["stat"]=="expired":
                        instance.ad="Featured"
                        #Jobpost.objects.filter(user=request.user.userprofile).update(ad="Featured")
                        messages.error(request,"you don't have subscriptionpack , your add will be saved as featured")
                    else:
                        instance.ad="Premium"
            except:
                instance.ad="Featured"
                messages.error(request,"you don't have subscriptionpack , your add will be saved as featured")
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('employerin')
    #form= JobPostform()
    context = {
        "form": form,}
    return render(request, 'jobPostForm.html',context)

def searchjob(request):
    if(request.method=='POST'):
        srch=request.POST['srh']
        if srch:
            match=Jobpostt.objects.filter(Q(JobTitle__icontains=srch) | Q(JobDesciption__icontains=srch) | Q(jobType__iexact=srch))
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
            match=Jobpostt.objects.filter(Q(JobTitle__icontains=srch) | Q(JobDesciption__icontains=srch) | Q(jobType__iexact=srch))
            if(match.exists()):
                return render(request,'index.html',{'sr':match})
            else:
                messages.error(request,"Sorry! No results found.")
        else:
            return HttpResponseRedirect("/searchJob/")
    return render(request,'index.html')




def indust(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        categ=request.GET.get("categ")
        match = Jobpostt.objects.filter(Jobindustry__icontains=categ)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')
    
def automotive(request):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains="automotive") | Q(JobDesciption__icontains="automotive") | Q(Jobindustry__icontains="automotion"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')
    
def industries(request,ind):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains=ind))
    if (match.exists()):
        return render(request, 'searchjob.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')
    


def food(request):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains="food") | Q(JobDesciption__icontains="food service") | Q(Jobindustry__icontains="food"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')


def educationIndustry(request):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains="education"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')

def designer(request):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains="designer"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')


def cutomerService(request):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains="Customer Service") | Q(Jobindustry__icontains="Customer Care"))
    if (match.exists()):
        return render(request, 'industry.html', {'sr': match})
    
    else:
        messages.error(request, "Sorry! No results found.")
        return redirect('home')


def health(request):
    match = Jobpostt.objects.filter(Q(Jobindustry__icontains="Health"))
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
    s=UserProfile.objects.filter(user=request.user)
    if(s.exists):
        messages.error(request,"You have already created your resume, you may update existing one")
        return redirect(employeein)
    else:
        form=UserProfileForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            #message of success
            messages.success(request,"Successfully created")
            return redirect('employeein')
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
                return redirect('employeein') 
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
        instance.resume=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('project')
    context = {
        "form": form,}
    return render(request, 'education.html',context)

     
                    

def applyjob(request, jid):

    form=applicanttform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user.userprofile
        job = Jobpostt.objects.get(id=jid)
        instance.job=job
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('employeein')
    #form= JobPostform()
    job = Jobpostt.objects.get(id=jid)
    context = {
        "form": form,
        "job": job,}
    return render(request, 'applyjob.html',context)







def showmyjobs(request):
    jobdisplay=Jobpostt.objects.filter(user=request.user.userprofile)
    return render(request,'showmyjobs.html',{'jobdisplay':jobdisplay})

def noappli(request):
    
    return render(request,'employee/noappli.html')


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
'''
def sr(request,pk):
    ress = UserProfile.objects.get(id=pk)
    edu=Education.objects.filter(resume=ress)
    pro = Project.objects.filter(projectuser=ress)
    context={"ress":ress,
    "edu" : edu,
    "pro":pro}
    return render(request, 'resumebuilder.html', context)'''

def rrr(request,pk):
    ap=applicantt.objects.get(id=pk)
    
    edu=Education.objects.filter(resume=ap.user)
    pro = Project.objects.filter(projectuser=ap.user)
    context={"ap":ap,"edu":edu,"pro":pro}
    print(ap)
    print(pro)
    print(edu)
    return render(request, 'applicantresume.html', context)


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
    '''try:
        if(request.user.userprofile.employer.email is not None):
            messages.success(request,"Welcome")
            context={}
            return redirect('employerin')'''
    
    form=EmployerForm(request.POST or None,request.FILES or None)
    if form.is_valid():
            instance=form.save(commit=False)
            instance.empuser=request.user.userprofile
            instance.save()
            #message of success
            messages.success(request,"Successfully created")
            return redirect('employerin')
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
            return redirect('employerin') 
    context={'form':form}
    return render(request,'e.html',context) 

def employerview(request):
    employees=Employer.objects.filter(empuser=request.user.userprofile)
    return render(request,'employer/index.html',{'employees':employees})


def showapplicants(request, jid):
    ap=Jobpostt.objects.filter(user=request.user.userprofile)
    jobb = ap.get(id=jid)
    appli=applicantt.objects.filter(job=jobb)
    if appli.exists():
        return render(request,'showapplicants.html',{'appli':appli})
    else:
        messages.error(request,'There are no applicants to this job yet')
        return redirect('employerin')

@login_required
def applyjobb(request, jid):
    form=applicanttform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user.userprofile
        instance.job=Jobpostt.objects.get(id=jid)
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('employeein')
    #form= JobPostform()
    job = Jobpostt.objects.get(id=jid)
    context = {
        "form": form,
        "job": job,}
    return render(request, 'applyjobb.html',context)

def saveresum(request,e,r):
    emp=Employer.objects.get(id=e)
    ap=applicantt.objects.get(id=r)
    
    Svedresume.objects.create(empid=emp,aplid=ap)
    messages.success(request,"Successfully saved")
    return redirect("employerin")


def saved_resume(request):
    sav=Svedresume.objects.filter(empid=request.user.userprofile.employer)
    return render(request,'saved_resume.html',{"sav": sav})



def sav_jobs(request,ee,jid):
    eemp=Employee.objects.get(id=ee)
    job=Jobpostt.objects.get(id=jid)
    sav=savedjobs.objects.create(empid=request.user.userprofile.employee,jid=job)
    messages.success(request,"Successfully saved")
    return redirect("employeein")

def saved_jobs(request):
    sav=savedjobs.objects.filter(empid=request.user.userprofile.employee)
    context={"sav":sav}
    return render(request,'employee/saved_jobs.html',context)



def check_status(request):
    #to check if subscription of logged in user is expired or not
    value=subscription.objects.filter(user=request.user)
    stat=""
    if (value.exists()):
        for k in value:
            d0 =k.last_date
            d1=date.today()
            delta = d0 - d1
            note=""
            if(k.subscriptionid=="499 per month"):
                if(delta.days>30):
                    subscription.objects.filter(status=request.user.subscription.status).update(status="expired")

                    k.status="expired"
                    stat='expired'
                else:
                    subscription.objects.filter(status=request.user.subscription.status).update(status="active")
                    k.status="active"
                    stat='active'

                note="There are "+str(delta.days)+" days left for your subscription to get over"


            elif(k.subscriptionid=="Yearly subscription @3400"):
                if(delta.days>365):
                    subscription.objects.filter(status=request.user.subscription.status).update(status="expired")
                    k.status="expired"
                    stat='expired'
                else:
                    subscription.objects.filter(status=request.user.subscription.status).update(status="active")
                    k.status="active"
                    stat='active'

                note="There are "+str(delta.days)+" days left for your subscription to get over"

            subs=k.subscriptionid    
            
        context={'subs':subs,'stat':stat,"note":note} 
        return render(request,'subscription.html',context)
    else:
        messages.error(request, "Sorry! No valid subscriptions")
        return redirect('employerin')

def check_status_employee(request):
    #to check if subscription of logged in user is expired or not
    eevalue=subscription.objects.filter(user=request.user)
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
        return redirect('employeein')

def sub(request):
    if(subscription.objects.filter(user=request.user)):
        messages.error(request,"Your subscription id exists, kindly update your pack by clicking on Update subscription")
        return redirect('dashboard')
    else:
        form=subscriptionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            #message of success
            messages.success(request,"Successfully created")
            return redirect('recharge')
        context = {
            "form": form,}
        return render(request, 'subsformm.html',context)

def updatesubs(request,pk):
    up=subscription.objects.get(id=pk)
    form=subscriptionForm(instance=up)
    if(request.method=='POST'):
        form=subscriptionForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('recharge') 
    context={'form':form}
    return render(request,'subsformm.html',context) 



def sendemail(request,apid):
    '''if(request.method=='GET'):
        return render(request,'settime.html')'''
    
    ap=applicantt.objects.get(id=apid)
    s=settime.objects.filter(Q(empid=request.user.userprofile.employer),Q(apliid=ap))
    print(s)
    for k in s:
        print("Regarding the Interview Process","Congratulations on being selected for the interview.Your interview will be held on "+str(k.indate)+" timings are "+str(k.intime) +" hrs .","eepicjob.com",["recipent@gmail.com"])
        send_mail("Regarding the Interview Process","Dear "+str(k.apliid.name)+", Congratulations on being selected for the interview.Your interview will be held on "+str(k.indate)+" timings are "+str(k.intime),"eepicjob.com",[k.apliid.email],fail_silently=False)
        #send_mail("Regarding the Interview Process","Dear "+str(k.apliid.name)+", Congratulations on being selected for the interview.Your interview will be held on "+str(k.indate)+", timings are "+str(k.intime),"agritadobhal.21864@gmail.com",["agritadobhal.21864@gmail.com"],fail_silently=False)
    return render(request,'sendemail.html')

'''
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
    return render(request, 'set_time.html',context)'''



def sending(request,apid):
    form=settimeForm(request.POST or None,request.FILES or None)
    a=apid
    if form.is_valid():
        ap=applicantt.objects.get(id=apid)
        instance=form.save(commit=False)
        instance.empid=request.user.userprofile.employer
        instance.apliid=ap
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect("sendemail",apid=a)
        #return redirect('home')
    context = {
        "form": form,}
    return render(request, 'set_time.html',context)

def seeing(request,apid):
    a=applicantt.objects.get(id=apid)
    ss=settime.objects.filter(empid=request.user.userprofile.employer,apliid=a )
    if(ss.exists()):
            context={'ss':ss}
            return render(request,"seeing.html",context)
    else:
        messages.error(request,'no time set')
        return redirect('home')

def employeedetails(request):
    '''if(request.user.userprofile.employee.email is not None):
        messages.success(request,"Welcome")
        return redirect("employeein")'''
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
    form=EmployeeForm(instance=up)
    if(request.method=='POST'):
        form=EmployeeForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('employeein') 
    context={'form':form}
    return render(request,'employee/ee.html',context) 

def eduup(request,pk):
    up=Education.objects.get(id=pk)
    form=EducationForm(instance=up)
    if(request.method=='POST'):
        form=EducationForm(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('employeein') 
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
            return redirect('employeein') 
    context={'form':form}
    return render(request,'projects.html',context) 


def showapplied(request,pk):
     appli=applicantt.objects.filter(user=request.user.userprofile)
     return render(request,'showapplied.html',{'appli':appli})

def upgrade(request):
    logger.info("upgrade")
    return render(request,"payments.upgrade.html")
    
def card(request):
    return render(request,"payments/thankyou.html")

'''def payment_method(request):
    plan=request.POST.get('plan','m')
    automatic=request.POST.get("automatic",'on')
    payment_method=request.POST.get("payment_method",'card')
    context={}
    plan_inst= Plan(plan_id=plan)
    payment_intent=stripe.PaymentIntent.create(amount=plan_inst.amount,currency=plan_inst.currency,payment_method_types=['card'])
    if payment_method=="card":
        context['secret_key']=payment_intent.client.secret_key
        context['STRIPE_PUBLISHABLE_KEY']=settings.STRIPE_PUBLISHABLE_KEY
        context["customer_email"]=request.user.email
        context["payment_intent_id"]=payment_intent_id
        return render(request,"payments/card.html",context)'''

def join(request):
    return render(request, 'payment/a.html')


@login_required
def checkout(request):
    if(request.method =="POST"):
        stripe_customer=stripe.Customer.create(email=request.user.email,source=request.POST['stripeToken'])
        if request.POST['price']=="Subscription@499pm":
            price="prod_HejhyUxVSoZhAt"
        if request.POST['price']=="Subscription@1400for three months":
            price="prod_HejiWQVbLXRdYy"
        if request.POST['price']=="Subscription@3000 for a year":
            price="prod_Hejk6aN99DhNaY"
        
        subscription=stripe.Subscription.create(customer=stripe_customer.id,items=[{"price":price}],coupon="none")
        customer=Customer()
        customer.user=request.user
        customer.stripeid=stripe_customer.stripe_id
        customer.membership=True
        customer.cancel_at_period_end=False
        customer.stripe_subscription_id=subscription.stripe_id
        customer.save()
        return redirect("home")
    else:
        price="Subscription@499pm"
        coupon="none"
        amount=499
        original_amt=499
        coupon_amt=0
        final_amt=499
        if request.method=="GET" and "price" in request.GET:
            if request.GET["price"] == "Subscription@1400 for three months":
                amount = 1400
                price="subscription@1400for three months"
                original_amt = 1400
                final_amt = 1400
            if request.GET["price"]=="Subscription@3000 for a year":
                price="Subscription@3000 for a year"
                amount = 3000
                original_amt = 3000

                final_amt = 3000
        amount=amount*100
        return render(request, 'payment/checkout.html',{"price":price,"coupon":coupon,"amount":amount,"original_amt":original_amt,"final_amt":final_amt,
                                                            "coupon_amt":coupon_amt })

    


def order(request):
    form=subscriptionForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.empid=request.user.userprofile
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'payment/order.html',context)
    


def charge(request):
    if request.method == "POST":
        amount = int(request.POST['amount'])

        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.user.email,
            name=request.user.username,
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='INR',
            description="Subscription"
            )

        subscription.objects.filter(price=request.user.subscription.price).update(price=F('price')+ amount)
        #subscription.objects.filter(purchasedate=request.user.subscription.purchasedate).update(=F('price')+ amount)
        s=subscription.objects.filter(user=request.user)
        for k in s:
            sub=k.subscriptionid
            if(sub=="499 per month"):
                lastt_date=date.today()+timedelta(days=30)
                subscription.objects.filter(last_date=request.user.subscription.last_date).update(last_date=(date.today()+timedelta(days=30)))
            
            if(sub=="Yearly subscription @3400"):
                lastt_date=date.today()+timedelta(days=365)
                subscription.objects.filter(last_date=request.user.subscription.last_date).update(last_date=(date.today()+timedelta(days=365)))
        messages.success(request,"Payment Succesfull")   
        return redirect('dashboard')
    return redirect('recharge')



def recharge(request):
    return render(request,'recharge.html')

def jobss(request):
    
    match=Jobpostt.objects.all().order_by('-valid_till')
    return render(request,'searchjob.html',{'sr':match})

def loc(request):
    match=Jobpostt.objects.all().order_by('-valid_till').distinct()
    #match = Jobpost.objects.values_list('location', flat=True).distinct()
    return render(request,'base.html',{'sr':match})

def jobloc(request,loc):
    #m=Jobpost.objects.filter(valid_date__lte='-date.today').delete()
    #m.save()
    m=Jobpostt.objects.get(id=loc)
    
    match=Jobpostt.objects.filter(location__icontains=m.location).order_by('-valid_till')
    return render(request,'searchjob.html',{'sr':match})


def types(request,ctype):
    c=Jobpost.objects.filter(contractType__icontains=ctype)
    context={"sr":c}
    return render(request,'searchjob.html',context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def typesss(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_type")
        match = Jobpostt.objects.filter(contractType__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')


def adtypesss(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_type")
        match = Jobpostt.objects.filter(ad__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')
    

def adtype(request,addtype):
    typee=Jobpostt.objects.filter(ad__icontains=addtype)
    
    context={"sr":typee}
    return render(request,'searchjob.html',context)

def adtypes(request,addtype):
    typee=Jobpostt.objects.filter(ad__icontains=addtype)
    
    context={"srrr":typee}
    return render(request,'index.html',context)


def updatejob(request,pk):
    up=Jobpost.objects.get(id=pk)
    form=JobPostform(instance=up)
    if(request.method=='POST'):
        form=JobPostform(request.POST,instance=up)
        if form.is_valid(): 
            messages.success(request,"Successfully created") 
            form.save()
            return redirect('employerin') 
    context={'form':form}
    return render(request,'jobpostForm.html',context)

def deleteold(request,pk):
    up=Jobpost.objects.get(id=pk)
    context={'item':up}
    if request.method=="POST":
        up.delete()
        messages.success(request,"Succesfully deleted")
        return redirect('employerin')
    return render(request,"employer/deletejob.html",context)

def deletejob(request,pk):
    up=Jobpostt.objects.get(id=pk)
    context={'item':up}
    if request.method=="POST":
        up.delete()
        messages.success(request,"Succesfully deleted")
        return redirect('employerin')
    return render(request,"employer/deletejob.html",context)


def internn(request):
    w=Jobpostt.objects.filter(contractType__icontains="Internship")
    context={"i":i}
    return render(request,"frontpage/internship.html",context)
def walk(request):
    i=Jobpostt.objects.filter(contractType__icontains="Walk-In")
    context={"i":i}
    return render(request,"frontpage/walk.html",context)

def contract(request):
    i=Jobpostt.objects.filter(contractType__icontains="contract")
    context={"i":i}
    return render(request,"frontpage/contract.html",context)

def premium(request):
    i=Jobpostt.objects.filter(ad__icontains="premium")
    context={"i":i}
    return render(request,"frontpage/premium.html",context)

def feat(request):
    typee=Jobpostt.objects.filter(ad__icontains="feature")
    context={"i":i}
    return render(request,"frontpage/feature.html",context)

def req(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_qualifications")
        match = Jobpostt.objects.filter(requirements__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')

def coun(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("coun")
        match = Jobpostt.objects.filter(Q(country__icontains=ty)|Q(location__icontains = ty))
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')


def curren(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_currency")
        match = Jobpostt.objects.filter(salary_currency__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')





def sal(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_salary")
        match = Jobpostt.objects.filter(salary__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')

def saltyp(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_salary_type")
        match = Jobpostt.objects.filter(salary_type__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')

def joblev(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_level")
        match = Jobpostt.objects.filter(job_level__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')

def jobexperiences(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_experience")
        match = Jobpostt.objects.filter(job_experience__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')

def jobshift(request):
    if(request.method != "GET"):
        return HttpResponseRedirect("/searchJob/")
    else:
        ty=request.GET.get("job_shift")
        match = Jobpostt.objects.filter(job_shift__icontains=ty)
        if (match.exists()):
            return render(request, 'searchjob.html', {'sr': match})
        
        else:
            messages.error(request, "Sorry! No results found.")
            return redirect('home')





def latest(request):
    match=Jobpostt.objects.all().order_by("-posted_on")
    context={"sr":match}
    return render(request,"searchjob.html",context)



def front_type(request):
    sr=Jobpostt.objects.filter(ad__icontains="feature")
    context={"sr":sr}
    return render(request,"index.html",context)

def searchh(request,pk):
    sr=Jobpostt.objects.filter(id=int(pk))
    context={"sr":sr}
    return render(request,"searchjob.html",context)