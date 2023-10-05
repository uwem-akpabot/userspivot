from django.db import models
from school.models import School, Classs
from feature.models import ParentAccess

class Student(models.Model):
    GENDER = (
		('Female', 'Female'), 
		('Male', 'Male'), 
		('Other', 'Other'), 
    )
    CONTACT_RELATION = (
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Sibling', 'Sibling'),
        ('Uncle/Aunt', 'Uncle/Aunt'),
        ('Relative', 'Relative'),
        ('Sponsor', 'Sponsor')
    )
    school = models.ForeignKey(School, related_name='student', on_delete=models.CASCADE)
    classs = models.ForeignKey(Classs, related_name='student', on_delete=models.CASCADE)
    parent = models.ForeignKey(ParentAccess, related_name='student', on_delete=models.CASCADE)
    fname = models.CharField(max_length=40)
    mname = models.CharField(max_length=25, blank=True, null=True)
    sname = models.CharField(max_length=25)
    gender = models.CharField(max_length=6, choices=GENDER)
    dob = models.CharField(max_length=10, blank=True, null=True)
    phoneno = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True)
    address = models.TextField(blank=True, null=True)
    contactperson1 = models.CharField(max_length=30)
    contactperson1_phoneno = models.CharField(max_length=12)
    contactperson1_relationship = models.CharField(max_length=10, choices=CONTACT_RELATION)
    contactperson2 = models.CharField(max_length=25, blank=True, null=True)
    contactperson2_phoneno = models.CharField(max_length=12, blank=True, null=True)
    contactperson2_relationship = models.CharField(max_length=10, blank=True, null=True, choices=CONTACT_RELATION)
    contactperson_email = models.EmailField(max_length=45, blank=True)
    contactperson_address = models.TextField(blank=True, null=True)
    admissiondate = models.CharField(max_length=10, blank=True, null=True)
    enddate = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.CharField(max_length=15, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # passport photo

class Staff(models.Model):
    USERTYPE = (
        ('Teacher', 'Teacher'),
        ('Administrator', 'Administrator'),
        ('Other Staff', 'Other Staff'),
    )
    GENDER = (
		('Female', 'Female'), 
		('Male', 'Male'), 
		('Other', 'Other'), 
    )
    CONTACT_RELATION = (
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Sibling', 'Sibling'),
        ('Uncle/Aunt', 'Uncle/Aunt'),
        ('Relative', 'Relative'),
        ('Sponsor', 'Sponsor')
    )
    school = models.ForeignKey(School, related_name='staff', on_delete=models.CASCADE)
    usertype = models.CharField(max_length=20, choices=USERTYPE)
    fname = models.CharField(max_length=45)
    mname = models.CharField(max_length=30, blank=True, null=True)
    sname = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER)
    dob = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True)
    address = models.TextField(blank=True, null=True)
    classrole = models.CharField(max_length=20, blank=True, null=True)
    subjectrole = models.CharField(max_length=20, blank=True, null=True)
    otherrole = models.CharField(max_length=20, blank=True, null=True)
    contactperson1 = models.CharField(max_length=30)
    contactperson1_phone = models.CharField(max_length=12)
    contactperson1_relationship = models.CharField(max_length=12, choices=CONTACT_RELATION)
    contactperson_email = models.EmailField(max_length=45, blank=True)
    contactperson_address = models.TextField(blank=True, null=True)
    employmentdate = models.CharField(max_length=10, blank=True, null=True)
    enddate = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # passport photo