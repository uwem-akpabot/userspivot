from django.urls import path
from school.views import sesssion, term, school, classs
from person.views import student, staff
from feature.views import parentaccess

urlpatterns = [
    #school
    path('session/', sesssion),
    path('term/', term),
    path('school/', school),
    path('class/', classs),
    #person
    path('student/', student),
    path('staff/', staff),
    #feature
    path('parentaccess/', parentaccess),
]