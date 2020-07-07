from django.urls import path, include

from rest_framework import routers

from accounts.api.views import (
    UserProfileViewSet,
    JobpostViewSet,
    UserViewSet
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'jobpost', JobpostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]