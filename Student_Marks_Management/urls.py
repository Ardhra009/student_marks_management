"""
URL configuration for Student_Marks_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from app.views import TotalMarksView, PercentageView, AverageMarksView,GradeView,PassFailView,AttendanceView,BonusMarksView,HighestMarksView,LowestMarksView,ScholarshipView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('total/', TotalMarksView.as_view(), name='total'),
    path('percentage/', PercentageView.as_view(), name='percentage'),
    path('average/', AverageMarksView.as_view(), name='average'),
    path('grade/', GradeView.as_view(), name='grade'),
    path('passfail/', PassFailView.as_view(), name='passfail'),
    path('attendance/', AttendanceView.as_view(), name='attendance'),
    path('bonus/', BonusMarksView.as_view(), name='bonus'),
    path('highest/', HighestMarksView.as_view(), name='highest'),
    path('lowest/', LowestMarksView.as_view(), name='lowest'),
    path('scholarship/', ScholarshipView.as_view(), name='scholarship')
]
