"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from pages.views import home_view, about_view, resume_view, logout_view
from pics.views import pic_view, success

from UserProfile.views import signup_view, account_activation_sent_view, activate_view

urlpatterns = [
    path('', home_view, name="Start page"),
    path('about', about_view, name="About page"),
    path('resume', resume_view, name="Resume"),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='signin'),
    path('logout/', logout_view),
    path('pics/', pic_view, name="pics"),
    path('success/', success, name='success'),


                  #url(r'^signup/$', signup_view, name='signup'),
  ##  url(r'^account_activation_sent/$', account_activation_sent_view, name='account_activation_sent'),
   # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    activate_view, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
