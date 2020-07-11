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
        CGPA_For_masters = models.FloatField(default=0.0)

        class Meta:
            verbose_name = 'Education'
            def __str__(self):
                return "{} - {}".format(str(self.id), self.school,self. CGPA_For_bachelors)



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
                return "{} - {}".format(str(self.id), self.project1,self.project10)


        

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
    contractchoices=(('0',"Contract"),('1',"Internship"),('2',"Temporary"),('3',"Walk-In"),('4',"Fresher"))
    hearchoices=(('0',"Mail"),('1',"Tv"),('2',"Newspapaer"),('3',"other"))
    jobchoice= (('0',"Full time"),('1',"Part time"))

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
            return "{} - {}".format(str(self.id), self.email,self.job)
        
        
        

class Employer(models.Model):
    """
    This model is for creating a UserProfile that contains more information about the user
    """
    USER_PROFILE_PHOTO = 'user__profilephoto'
    pchoice= (('0',"Public"),('1',"Private"))
    empuser = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=USER_PROFILE_PHOTO, null=True, blank=True)
    name=models.CharField(max_length=255, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    Website=models.URLField(blank=True, null=True)
    set_your_profile=models.CharField(max_length=20,choices=pchoice,default='Public')
    about_yourself=models.CharField(max_length=2000, null=True)
    email =  models.EmailField(validators=[validators.EmailValidator], null=True)
    compchoice=(('0',"Php"),('1',"JS"),('2',"Designing"),('3',"Application development"),('4',"Painting"),('5',"Arts"),('6',"Development"),('7',"Modeling"),('8','SEO'),('9',"Architecture"),('10',"Management"),('11',"SMM"),('12',"Culinary Arts"),('13',"Peruvian Cuisine"),('14',"Team Management"),('15',"patience"),('16',"Commitment"),('17',"Team Work"),('18',"Flexibility"),('19',"Stress Management"),('20',"Analytical skills"),('21',"trainings"),('22','communication skills'),('23',"Food Products"),('24',"Education"),('25',"cooking"))
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



class savedresume(models.Model):
    resid=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    empid=models.ForeignKey(Employer,on_delete=models.CASCADE)
    class Meta:
            verbose_name = 'savedresume'
            verbose_name_plural = 'savedresumes'
    def __str__(self):
        return "{} - {}".format(str(self.id))
        

class subscriptionpack(models.Model):
    empid=models.ForeignKey(Employer,on_delete=models.CASCADE)
    subscription_choice=(('1','499 per month'),('2','700 for two months',),('3','Yearly subscription @3400',))
    subscriptionid=models.CharField(max_length=20,choices=subscription_choice,default='499 per month')
    statuschoice=(('0','expired'),('1','active'))
    status=models.CharField(max_length=20,choices=statuschoice,default='expired')
    purchasedate=models.DateField(verbose_name='Enter date in yy-mm-dd format')
    class Meta:
            verbose_name = 'subscriptionpack'
            verbose_name_plural = 'subscriptionpacks'
    def __str__(self):
        return "{} - {}".format(str(self.id))
        





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