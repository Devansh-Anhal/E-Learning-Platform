"""Elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from home import views as h
from accounts import views as ac
from courses import views as c
from forum import views as fr
from donate import views as don
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',h.home,name='home'),
    url(r'^about/$',h.about, name='about'),
    url(r'^donate/$',don.pay,name='donate'),
    url(r'^register/$',ac.register, name='register' ),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'), name='login' ),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout' ),
    url(r'^profile/$',ac.profile, name='profile' ),
    url(r'^profile_update/$',ac.profile_update, name='profile_update'),
    url('discussion_forum/',include('forum.urls')),
    url(r'^courses/$', c.courses, name='courses'),
    url(r'^course/$', c.course),

]
urlpatterns += staticfiles_urlpatterns();
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)