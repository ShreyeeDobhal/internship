from django.contrib.auth.models import User

from rest_framework import serializers

from accounts.models import (
    UserProfile,
    Organization,
    OrganizationAdmin,
    SeekerProfile,
    Jobpost
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_staff'
        ]


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing the UserProfile Model
    """
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'profile_photo',
            'added',
            'updated',
            'phone_number',
            'active'
        ]

    
class JobpostSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing the Jobpost Model
    """
    class Meta:
        model = UserProfile
        fields=['user',
    'JobTitle',
    'JobDesciption',
    'CompanyName',
    'phone_number', 
    'email' ,
    'hear' ,
    'contractType', 
    'jobType',
    'country',
    'location'
        ]

