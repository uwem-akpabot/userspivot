from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school.views import SesssionViewSet, TermViewSet, SchoolViewSet, ClasssViewSet
# from school.views import sesssion, term, school, classs
from person.views import student, staff
from feature.views import parentaccess

router = DefaultRouter()
router.register(r'session', SesssionViewSet, basename='session')
router.register(r'term', SesssionViewSet, basename='term')
router.register(r'school', SesssionViewSet, basename='school')
router.register(r'classs', SesssionViewSet, basename='classs')

urlpatterns = [
    path('', include(router.urls)),
    # path('session/', sesssion),
    # path('term/', term),
    # path('school/', school),
    # path('class/', classs),
    #person
    path('student/', student),
    path('staff/', staff),
    #feature
    path('parentaccess/', parentaccess),
]