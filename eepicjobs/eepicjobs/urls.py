from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name="main/register.html")), #
    #path('google/', include('allauth.urls')), # <--
    path('', include('main.urls'), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    #path('', include('social_django.urls', namespace='social'))
    path('oauth/', include('social_django.urls', namespace='social')),
    #path('logout/',  LogoutView.as_view(),name="logout"),
    #path("alauth",include('social_django.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
