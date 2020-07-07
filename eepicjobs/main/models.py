from django.db import models
from django.utils import timezone
import pytz
from accounts.models import * 
# Create your models here.


class Chat(models.Model):
    CID = models.AutoField(primary_key=True)
    ClassID = models.CharField(max_length=2000)
    Name = models.CharField(max_length=2000)
    Subject = models.CharField(max_length=2000)
    Topic = models.CharField(max_length=2000,blank=True,null=True)
    PID = models.ForeignKey('accounts.UserProfile',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Name}'

class Discuss(models.Model):
    ID = models.AutoField(primary_key=True)
    toPID = models.ForeignKey('accounts.UserProfile',on_delete=models.CASCADE)
    fromPID = models.IntegerField()
    message = models.CharField(max_length=20000)
    CID = models.ForeignKey('Chat',on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now, blank=True)
    type = models.CharField(max_length=100,default='msg')
    def __str__(self):
        return f'{self.message}'

class Participant(models.Model):
    ID = models.AutoField(primary_key=True)
    PID = models.ForeignKey('accounts.UserProfile',on_delete=models.CASCADE)
    CID = models.ForeignKey('Chat',on_delete=models.CASCADE)
    VID = models.CharField(max_length=2000,blank=True,null=True)
    status = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return f'{self.VID}'

class Skill(models.Model):
    """
    This model is for Skills
    """
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)


class Job(models.Model):
    """
    This model is for Job Posts
    """
    JOB_IMP = [
        ('Featured', 'Featured'),
        ('Urgent', 'Urgent'),
        ('Private', 'Private'),
    ]

    JOB_TYPE = [
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
    ]

    JOB_STATUS = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Closed', 'Closed'),
    ]

    SALARY_DURATION= [
        ('Year', 'Year'),
        ('Month', 'Month'),
        ('Day', 'Day'),
        ('Hour', 'Hour'),
        ('Project', 'Project'),
    ]

    Company = models.ForeignKey('accounts.OrganizationAdmin', on_delete=models.CASCADE)
    added_by = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    Position = models.CharField(max_length=300,blank=True, null=True)
    Exp = models.IntegerField(default=0)
    Salary = models.IntegerField(default=0)
    Salary_Type = models.CharField(max_length=100, choices=SALARY_DURATION, default='Year')
    Salary_Currency = models.CharField(max_length=20,default="INR")
    NOO = models.IntegerField(default=1)
    Qualification = models.CharField(max_length=400,blank=True,null=True)
    Shift = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=2000,blank=True,null=True)
    Category = models.CharField(max_length=200,null=True,default='Other')
    Location = models.CharField(max_length=200,blank=True,null=True)
    Imp = models.CharField(max_length=100, choices=JOB_IMP, default='Private')
    Posted = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=100, choices=JOB_STATUS, default='Draft')
    Type = models.CharField(max_length=150, choices=JOB_TYPE, default='Full Time')

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return str(self.id)

class Jobskills(models.Model):
    """
    skills in Job Listing 
    """
    JID = models.ForeignKey('Job',on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)