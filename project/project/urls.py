"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Registration/',views.Registration,name='Registration'),
    path('Login/',views.Login,name='Login'),
    path('userdeshboard/',views.userdeshboard,name='userdeshboard'),
    path('logout/',views.logout,name='logout'),
    path('admindeshboard/',views.admindeshboard,name='admindeshboard'),
    path('admindeshboard/add_dep/',views.add_dep,name='add_dep'),
    path('admindeshboard/show_dep/',views.show_dep,name='show_dep'),
    path('admindeshboard/save_dep/',views.save_dep,name='save_dep'),
    path('admindeshboard/aad_emp/',views.aad_emp,name='aad_emp'),
    path('admindeshboard/save_emp/',views.save_emp,name='save_emp'),
    path('admindeshboard/show_emp/',views.show_emp,name='show_emp'),
    path('empdeshbord/',views.empdeshbord,name='empdeshbord'),
    path('empdeshbord/profile/',views.profile,name='profile'),
    path('empdeshbord/setting/',views.setting,name='setting'),
    path('empdeshbord/Query/',views.Query,name='Query'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
