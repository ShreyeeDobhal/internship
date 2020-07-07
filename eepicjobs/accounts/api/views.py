from django.contrib.auth.models import User

from rest_framework import viewsets, permissions

from accounts.models import (
    UserProfile,
    Jobpost,
)

from accounts.api.serializers import (
    UserProfileSerializer,
    UserSerializer,
    JobpostSerializer
)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for handling low-end apis
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for handling low-end apis
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class JobpostViewSet(viewsets.ModelViewSet):
    """
    Simple viewset for handling low-end apis
    """
    serializer_class = JobpostSerializer
    queryset = Jobpost.objects.all()
    permission_classes = [permissions.IsAuthenticated]