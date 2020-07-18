import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core import validators
from django.urls import reverse
from django import forms
from django_countries.fields import CountryField

from eepicjobs.utils import unique_slug_generator


phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class UserProfile(models.Model):
    """
    This model is for creating a UserProfile that contains more information about the user
    """
    USER_PROFILE_PHOTO = 'user__profilephoto'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=USER_PROFILE_PHOTO, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    hobbies = models.CharField(max_length=255, null=True, help_text="Mention Your hobbies")
    updated = models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=255, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    is_emp = models.BooleanField(default=False)
    is_seek = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    email =  models.EmailField(validators=[validators.EmailValidator], null=True)
    skills=models.CharField(max_length=255, null=True, help_text="Mention Your Skils")
    experience= models.CharField(max_length=255, null=True, verbose_name='experience')
    address= models.CharField(max_length=255, null=True, verbose_name='address')
    prev_Employments= models.CharField(max_length=255, null=True, help_text="Mention Your Previous employments")
    education_details= models.CharField(max_length=255, null=True, verbose_name='Mention Your Education Details')
    projects= models.CharField(max_length=255, null=True, verbose_name='Give a beief about your projects')
    accomplishments= models.CharField(max_length=255, null=True, verbose_name='accomplishments')
    linkedin=models.URLField(blank=True, null=True)
    github=models.URLField(blank=True, null=True)
    hackerrank=models.URLField(blank=True, null=True)
    codechef=models.URLField(blank=True, null=True)
    otherLinks=models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return "{} - {}".format(str(self.id), self.user.username)
    

class Education(models.Model):
        resume=models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='resume')
        school= models.CharField(max_length=255, null=True, verbose_name='Mention Your School Name')
        college = models.CharField(max_length=255, null=True, verbose_name='Mention Your college name')
        tenth_percentage = models.FloatField(default=0.0)
        yop_for_tenth= models.IntegerField(blank=True, null=True)
        twelth_percentage = models.FloatField(default=0.0)
        yop_for_twelfth = models.IntegerField(blank=True, null=True)
        bachelor_degree=models.CharField(max_length=255, null=True, verbose_name='Mention Your Bachelor Degree')
        yop_for_bachelors= models.IntegerField(blank=True, null=True)
        CGPA_For_bachelors = models.FloatField(default=0.0)
        masters_degree = models.CharField(max_length=255, null=True, verbose_name='Mention Your Master Degree if any')
        yop_for_masters = models.IntegerField(blank=True, null=True)
        CGPA_For_masters = models.FloatField(blank=True, null=True)

        class Meta:
            verbose_name = 'Education'
            def __str__(self):
                return "{} - {}".format(str(self.id),self.resume, self.school,self. CGPA_For_bachelors)



class Project(models.Model):
        projectuser=models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='projectuser')
        project1=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project2=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project3=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project4=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project5=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project6=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project7=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project8=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project9=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        project10=models.CharField(max_length=255, null=True, verbose_name='Mention project name and give a small desciption about it')
        class Meta:
            verbose_name = 'Projects'
            def __str__(self):
                return "{} - {}".format(str(self.id),self.projectuser)


        

class Orgphoto(models.Model):
    """
    This model contains gallery photos for company.
    """
    OID = models.ForeignKey('Organization', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='comp_gallery', null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Organization Photo'
        verbose_name_plural = 'Organization Gallery'

    def __str__(self):
        return "{}".format(str(self.id))

class Organization(models.Model):
    """
    This model contains the information about the college. It can be added or approved by the Super User 
    """
    ORGANIZATION_TYPE = [
        ('school', 'School'),
        ('college', 'College'),
        ('other', 'Other'),
    ]
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255, null=True, help_text="This is the name of Organization")
    organization_type = models.CharField(max_length=255, choices=ORGANIZATION_TYPE, default='school')
    address_1 = models.CharField(max_length=255, null=True, verbose_name='address_line_1')
    about = models.CharField(max_length=2000, null=True, verbose_name='about')
    landmark = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    email = models.EmailField(validators=[validators.EmailValidator], null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    website = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    emp = models.IntegerField(default=0)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return "{} - {}".format(str(self.id), self.name)

    
    # def get_absolute_url(self):
    #     kwargs = {
    #         'slug': self.slug
    #     }
    #     return reverse('organization_detail', kwargs=kwargs)

    
class OrganizationAdmin(models.Model):
    """
    This model for the admin or the handler of the Organization
    """
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_normaladmin = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Organization Handler'
        verbose_name_plural = 'Organization Handlers'

    def __str__(self):
        return str(self.id)


# *******************************************************************
# ********* THESE ARE FOR STUDENT MANAGEMENT FOR ORGANIZATIONS ******
# *******************************************************************
class Orgsocial(models.Model):
    """
    This model has Organization social media links
    """
    fb = models.URLField(blank=True,null=True)
    insta = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    linked = models.URLField(blank=True,null=True)
    oid = models.ForeignKey('Organization',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Organization Social Accounts'

    def __str__(self):
        return str(self.id)


    
class SeekerProfile(models.Model):
    """
    This model gonna handle the details of the students under particular course and organization
    """
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Student\'s Profile'
        verbose_name_plural = 'Student\'s Profiles'

    

    def __str__(self):
        return str(self.id)    

class Jobpost(models.Model):

    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    JobTitle=models.CharField(max_length=250)
    JobDesciption=models.TextField()
    CompanyName=models.CharField(max_length=250)
    Jobindustry=models.CharField(max_length=250,null=True)
    email = models.EmailField(validators=[validators.EmailValidator], null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    contractchoices=(('Contract',"Contract"),('Internship',"Internship"),('Temporary',"Temporary"),('Walk-In',"Walk-In"),('Fresher',"Fresher"))
    hearchoices=(('Mail',"Mail"),('Tv',"Tv"),('Newspapaer',"Newspapaer"),('other',"other"))
    jobchoice= (('Full time',"Full time"),('Part time',"Part time"))
    company_logo=models.ImageField(upload_to='images/',null=True,blank=True)
    hear = models.CharField(max_length=20,choices=hearchoices,default='Newspaper')
    contractType = models.CharField(max_length=20,choices=contractchoices,default='Fresher')
    jobType=models.CharField(max_length=20,choices=jobchoice,default='Full time')
    country = CountryField()
    location = models.CharField(max_length=255, null=True)
    

    class Meta:
        verbose_name = 'Jobpost'
        verbose_name_plural = 'Jobposts'

    def __str__(self):
        return "{} - {}".format(str(self.id), self.JobTitle,self.Jobindustry,self.jobType,self.JobDesciption,self.CompanyName)
    
    
class applicant(models.Model):
        user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
        job=models.ForeignKey(Jobpost,on_delete=models.CASCADE,default=0)
        
        email = models.EmailField(validators=[validators.EmailValidator], null=True)
        
        phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
        is_emp = models.BooleanField(default=False)
        is_seek = models.BooleanField(default=False)
        name=models.CharField(max_length=255, null=True, blank=True)
        skills=models.CharField(max_length=255, null=True, help_text="Mention Your Skils")
        experience= models.CharField(max_length=255, null=True, verbose_name='experience')
        address= models.CharField(max_length=255, null=True, verbose_name='address')
        prev_Employments= models.CharField(max_length=255, null=True, help_text="Mention Your Previous employments")
        education_details= models.CharField(max_length=255, null=True, verbose_name='Mention Your Education Details')
        projects= models.CharField(max_length=255, null=True, verbose_name='Give a beief about your projects')
        accomplishments= models.CharField(max_length=255, null=True, verbose_name='accomplishments')
        otherLinks=models.URLField(blank=True, null=True)
        

        class Meta:
            verbose_name = 'applicant'
            verbose_name_plural = 'applicants'

        def __str__(self):
            return "{} - {}".format(str(self.id), self.email,self.job,self.user,self.job)
        
        
        

class Employer(models.Model):
    """
    This model is for creating a UserProfile that contains more information about the user
    """
    USER_PROFILE_PHOTO = 'user__profilephoto'
    pchoice= (('Public',"Public"),('Private',"Private"))
    empuser = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=USER_PROFILE_PHOTO, null=True, blank=True)
    name=models.CharField(max_length=255, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    Website=models.URLField(blank=True, null=True)
    set_your_profile=models.CharField(max_length=20,choices=pchoice,default='Public')
    about_yourself=models.CharField(max_length=2000, null=True)
    email =  models.EmailField(validators=[validators.EmailValidator], null=True)
    compchoice=(('Php',"Php"),('JS',"JS"),('Designing',"Designing"),('Application development',"Application development"),('Painting',"Painting"),('Arts',"Arts"),('Development',"Development"),('Modeling',"Modeling"),('SEO','SEO'),('Architecture',"Architecture"),('Management',"Management"),('SMM',"SMM"),('Culinary Arts',"Culinary Arts"),('Peruvian Cuisine',"Peruvian Cuisine"),('Team Management',"Team Management"),('patience',"patience"),('Commitment',"Commitment"),('Team Work',"Team Work"),('Flexibility',"Flexibility"),('Stress Management',"Stress Management"),('Analytical skills',"Analytical skills"),('trainings',"trainings"),('communication skills','communication skills'),('Food Products',"Food Products"),('Education',"Education"),('cooking',"cooking"))
    company_specialization=models.CharField(max_length=20,choices=compchoice,default='Php')
    no_of_employees=models.IntegerField(blank=True, null=True)
    Established_Date= models.DateField(verbose_name='Enter date in yy-mm-dd format') 
    location = models.CharField(max_length=255, null=True)
    Facebook= models.URLField(blank=True,null=True)
    
    insta = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    linked_in = models.URLField(blank=True,null=True)
    #company_logo=models.ImageField(upload_to='', null=True, blank=True)
    youtube_url=models.URLField(blank=True,null=True)
    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return "{} - {}".format(str(self.id), self.name,self.email)


class Jobexperience(models.Model):
    USER_PROFILE_PHOTO = 'user__profilephoto'
    euser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Organization_name1=models.CharField(max_length=255,blank=True,verbose_name='Mention Organization Name')
    your_role1=models.CharField(max_length=255,blank=True,verbose_name='Mention Your Role')
    jobtenure1=models.IntegerField(blank=True, null=True,verbose_name='Mention Job Tenure For the above role')
    Organization_name2=models.CharField(max_length=255,blank=True,verbose_name='Mention Organization Name')
    jobtenure2=models.IntegerField(blank=True, null=True,verbose_name='Mention Job Tenure')
    your_role2=models.CharField(max_length=255,blank=True,verbose_name='Mention Your Role')
    Organization_name3=models.CharField(max_length=255,blank=True,verbose_name='Mention Organization Name')
    jobtenure3=models.IntegerField(blank=True, null=True,verbose_name='Mention Job Tenure')
    your_role3=models.CharField(max_length=255,blank=True,verbose_name='Mention Your Role')
    Organization_name4=models.CharField(max_length=255,blank=True,verbose_name='Mention Organization Name')
    jobtenure4=models.IntegerField(blank=True, null=True,verbose_name='Mention Job Tenure')
    your_role4=models.CharField(max_length=255,blank=True,verbose_name='Mention Your Role')
    Organization_name5=models.CharField(max_length=255,blank=True,verbose_name='Mention Organization Name')
    jobtenure5=models.IntegerField(blank=True, null=True,verbose_name='Mention Job Tenure')
    your_role5=models.CharField(max_length=255,blank=True,verbose_name='Mention Your Role')
    Organization_name6=models.CharField(max_length=255,blank=True,verbose_name='Mention Organization Name')
    jobtenure6=models.IntegerField(blank=True, null=True,verbose_name='Mention Job Tenure')
    your_role6=models.CharField(max_length=255,blank=True,verbose_name='Mention Your Role') 
    class Meta:
            verbose_name = 'Jobexperience'
            verbose_name_plural = 'Jobexperiences'

    def __str__(self):
            return "{} - {}".format(str(self.id), self.euser)
        

    


class Employee(models.Model):
    """
    This model is for creating a UserProfile that contains more information about the user
    """
    USER_PROFILE_PHOTO = 'user__profilephoto'
    pchoice= (('Public',"Public"),('Private',"Private"))
    employeeuser = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    #projuser=models.ForeignKey(Project, on_delete=models.CASCADE)
    #eduuser=models.ForeignKey(Education, on_delete=models.CASCADE)
    #jobexp=models.ForeignKey(Jobexperience, on_delete=models.CASCADE)
    
    profile_photo = models.ImageField(upload_to=USER_PROFILE_PHOTO, null=True, blank=True)
    name=models.CharField(max_length=255, null=True)
    profession=models.CharField(max_length=255, null=True)
    genderchoice=(('Male','Male'),('Female','Female'),('Other','Other'))
    gender=models.CharField(max_length=10,choices=genderchoice,default='Male')
    tenurechoice=(('Fresher','Fresher'),('1 year','1 year'),('2 years','2 years'),('3 years','3 year'),('4 years','4years'),('5 years','5 years'))
    experience_tenure=models.CharField(max_length=10,choices=tenurechoice,default='Fresher')
    level=(('Manager','Manager'),('Student',"Student"),("Officer","Officer"),("Executive","Executive"))
    experience_level=models.CharField(max_length=10,choices=level,default='Student')
    qchoice=(('Bachelor','Bachelor'),('Master',"Master"),("PHD","PHD"))
    qualification=models.CharField(max_length=10,choices=qchoice,default='Bachelor')
    contractchoices=(('Contract',"Contract"),('Internship',"Internship"),('Temporary',"Temporary"),('Freelance',"Freelance"),('Part Time',"Part Time"),('Full Time',"Full Time"))
    contract_type =models.CharField(max_length=10,choices=contractchoices,default='Internship')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
   
    marital=(("Single","Single"),("Married","Married"))
    salt=(("Monthly","Monthly"),("Weekly","Weekly"),("Hourly","Hourly"),("Yearly","Yearly"))
    
    sal_c=(("Rupees","Rupees"),("Dollar","Dollar"),("Euro","Euro"),("Pound","Pound"))
    salry_type=models.CharField(max_length=10,choices=salt,default='Monthly')
    salary_amount=models.IntegerField(null=True,blank=True)
    salary_currency=models.CharField(max_length=10,choices=sal_c,default='Rupees')
    Marital_status=models.CharField(max_length=10,choices=marital,default='Single')
    set_your_profile=models.CharField(max_length=20,choices=pchoice,default='Public')
    about_yourself=models.CharField(max_length=2000, null=True)
    email =  models.EmailField(validators=[validators.EmailValidator], null=True)
    compchoice=(('Php',"Php"),('JS',"JS"),('Designing',"Designing"),('Application development',"Application development"),('Painting',"Painting"),('Arts',"Arts"),('Development',"Development"),('Modeling',"Modeling"),('SEO','SEO'),('Architecture',"Architecture"),('Management',"Management"),('SMM',"SMM"),('Culinary Arts',"Culinary Arts"),('Peruvian Cuisine',"Peruvian Cuisine"),('Team Management',"Team Management"),('patience',"patience"),('Commitment',"Commitment"),('Team Work',"Team Work"),('Flexibility',"Flexibility"),('Stress Management',"Stress Management"),('Analytical skills',"Analytical skills"),('trainings',"trainings"),('communication skills','communication skills'),('Food Products',"Food Products"),('Education',"Education"),('cooking',"cooking"))
    company_specialization=models.CharField(max_length=20,choices=compchoice,default='Php')
    location = models.CharField(max_length=255, null=True)
    Facebook= models.URLField(blank=True,null=True)
    
    insta = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    linked_in = models.URLField(blank=True,null=True)
    #company_logo=models.ImageField(upload_to='', null=True, blank=True)
    youtube_url=models.URLField(blank=True,null=True)
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return "{} - {}".format(str(self.id), self.name,self.email)

    




class savedresume(models.Model):
    resid=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    empid=models.ForeignKey(Employer,on_delete=models.CASCADE)
    class Meta:
            verbose_name = 'savedresume'
            verbose_name_plural = 'savedresumes'
    def __str__(self):
        return "{} - {}".format(str(self.id))

class savedjobs(models.Model):
    jid=models.ForeignKey(Jobpost,on_delete=models.CASCADE)
    empid=models.ForeignKey(Employee,on_delete=models.CASCADE)
    class Meta:
            verbose_name = 'savedjob'
            verbose_name_plural = 'savedjobs'
    def __str__(self):
        return "{} - {}".format(str(self.id))
        


class subscriptionpack(models.Model):
    empid=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    subscription_choice=(('499 per month','499 per month'),('700 for two months','700 for two months',),('Yearly subscription @3400','Yearly subscription @3400',))
    subscriptionid=models.CharField(max_length=20,choices=subscription_choice,default='499 per month')
    statuschoice=(('expired','expired'),('active','active'))
    status=models.CharField(max_length=20,choices=statuschoice,default='expired')
    purchasedate=models.DateField(verbose_name='Enter date in yy-mm-dd format')
    class Meta:
            verbose_name = 'subscriptionpack'
            verbose_name_plural = 'subscriptionpacks'
    def __str__(self):
        return "{} - {}".format(str(self.id),self.empid)
    
class Pay(models.Model):
    amount=models.IntegerField(blank=True, null=True)
    subscription_choice=(('499 per month','499 per month'),('700 for two months','700 for two months',),('Yearly subscription @3400','Yearly subscription @3400',))
    plan_id=models.CharField(max_length=20,choices=subscription_choice,default='499 per month')
    curren=(('Rupees','Rupees'),('Dollar','Dollar'))
    currency=models.CharField(max_length=20,choices=curren,default='Rupees')
    paychoice=(('card','card'),('paypal','paypal'))
    payment_method_types=models.CharField(max_length=20,choices=paychoice,default='card')


class settime(models.Model):
    indate=models.DateField(auto_now=False, auto_now_add=False,verbose_name='Enter date in yyyy-mm-dd format')
    intime=models.TimeField(auto_now=False, auto_now_add=False,verbose_name='Enter time in IST date time format(hh:mm:ss)')
    empid=models.ForeignKey(Employer,on_delete=models.CASCADE)
    apliid=models.ForeignKey(applicant, on_delete=models.CASCADE)
    class Meta:
            verbose_name = 'settime'
            
    def __str__(self):
        return "{} - {}".format(str(self.id),self.empid,self.indate,self.intime,self.apliid)





# *****************************************************************************************************************
# *************** SIGNALS AND RECEIVERS  **************************************************************************
# *****************************************************************************************************************



def pre_save_slug_receiver(sender, instance, *args, **kwargs): 
    """
    This is reciever for the slug
    """
    if not instance.slug:
        slug = unique_slug_generator(instance)
        object_id = instance.id
        instance.slug = '{}-{}'.format(object_id, slug)


def pre_save_org_admin_receiver(sender, instance, *args, **kwargs):
    """
    This is receiver for the pre save operations for organization admin
    """
    if instance.is_superadmin is True:
        instance.is_normaladmin = False
    else:
        instance.is_normaladmin = False    


pre_save.connect(pre_save_slug_receiver, sender=Organization)
pre_save.connect(pre_save_org_admin_receiver, sender=OrganizationAdmin)