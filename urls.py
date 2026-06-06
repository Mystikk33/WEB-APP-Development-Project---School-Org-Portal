"""
URL configuration for ACERA_FORMARAN_RICO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from hello.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='Signup'),
    path('register/', registerPage, name='RegisterPage'),
    path('', loginPage, name='LoginPage'),
    path('logout/', loginPage, name='logout'),

    path('home/', home, name='Home'),
    path('about/', about, name='About'),
    path('editProfile/', editProfile, name='editProfile'),
    path('ac/', ac, name='AC'),
    path('ae/', ae, name='AE'),
    path('mv/', mv, name='MV'),

]