from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from  accounts.models import Jobpost
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


    
def searchindustry(request):
    match=Jobpost.objects.filter(Q(Jobindustry__icontains="automotive"))
    if(match.exists()):
        #dataJSON = dumps(match) 
        dataJSON = serializers.serialize("json",match)
        tmpObj = json.loads(dataJSON)
        return render(request, 'automation.html', {'sr':dataJSON}) 
        #return HttpResponse(json.dumps(tmpObj))
    else:
        messages.error(request,"Sorry! No results found.")



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
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        "form": form,}
    return render(request, 'resume.html',context)

def education(request):
    form=EducationForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        #message of success
        messages.success(request,"Successfully created")
        return redirect('home')
    context = {
        "form": form,}
    return render(request, 'education.html',context)

  

    




def updateresume(request,pk):
    up=UserProfile.objects.get(id=pk)
    form=UserProfileForm(instance=up)
    if(request.method=='POST'):
        form=UserProfileForm(request.POST,instance=up)
        if form.is_valid():  
                form.save()
                return redirect('/') 
    context={'form':form}
    return render(request,'resume.html',context)  



def show(request):  
    employees = UserProfile.objects.filter(user=request.user)  
    
    
    edu=Education.objects.filter(resume=request.user.userprofile)
    context={"employees":employees,"edu" : edu}
    return render(request, "show.html", context)

     
                    

def applyjob(request, jid):
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

def employeev(request):
    return render(request,'employee/view.html')

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
    context={"ress":ress,
    "edu" : edu}
    return render(request, 'resumebuilder.html', context)
