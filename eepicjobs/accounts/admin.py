from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import *

admin.site.register(SeekerProfile)
admin.site.register(OrganizationAdmin)


class UserProfileInline(admin.TabularInline):
    model = UserProfile
    extra = 0


class OrganizationAdminInline(admin.TabularInline):
    model = OrganizationAdmin
    extra = 0



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'added', 'active']
    list_filter = ['added', 'updated', 'active']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    This is for admin layout of the Organization
    """
    list_display = ['slug', 'name', 'phone_number', 'email']
    list_filter = ['organization_type', 'added', 'updated', 'city', 'state', 'country']
    search_fields = ['name', 'city', 'state', 'country']
    