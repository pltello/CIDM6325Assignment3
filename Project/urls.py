"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from degree_checklist import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('degree_checklist/student_list',
         views.student_list, name='student_list'),
    path('degree_checklist/degree_list',
         views.degree_list, name='degree_list'),
    path('degree_checklist/core_requirement_list',
         views.core_requirement_list, name='core_requirement_list'),
    path('degree_checklist/university_requirement_list',
         views.university_requirement_list, name='university_requirement_list'),
    path('degree_checklist/department_requirements_list',
         views.department_requirements_list, name='department_requirements_list'),
    path('degree_checklist/major_requirements_list',
         views.major_requirements_list, name='major_requirements_list'),
]
