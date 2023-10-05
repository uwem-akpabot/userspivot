from django.db import models
from school.models import School, Classs

class ParentAccess(models.Model):
    GENDER = (
		('Female', 'Female'), 
		('Male', 'Male'), 
		('Other', 'Other'), 
    )
    school = models.ForeignKey(School, related_name='parent', on_delete=models.CASCADE)
    title = models.CharField(max_length=15, blank=True, null=True)
    fname = models.CharField(max_length=45)
    sname = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER)
    phoneno = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True)
    address = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=15, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # passport photo

class Result(models.Model):
    pass
    # school = models.ForeignKey(School, related_name='person', on_delete=models.CASCADE)
    # classs = models.ForeignKey(Classs, related_name='person', on_delete=models.CASCADE)

class Attendance(models.Model):
    pass
    # school = models.ForeignKey(School, related_name='person', on_delete=models.CASCADE)
    # classs = models.ForeignKey(Classs, related_name='person', on_delete=models.CASCADE)

class Fee(models.Model):
    pass
    # school = models.ForeignKey(School, related_name='person', on_delete=models.CASCADE)
    # classs = models.ForeignKey(Classs, related_name='person', on_delete=models.CASCADE)

class EmployeePayroll(models.Model):
    pass
    # school = models.ForeignKey(School, related_name='person', on_delete=models.CASCADE)
    # classs = models.ForeignKey(Classs, related_name='person', on_delete=models.CASCADE)

class Pta(models.Model):
    pass
    # school = models.ForeignKey(School, related_name='person', on_delete=models.CASCADE)
    # classs = models.ForeignKey(Classs, related_name='person', on_delete=models.CASCADE)

class Alumni(models.Model):
    pass
    # school = models.ForeignKey(School, related_name='person', on_delete=models.CASCADE)
    # classs = models.ForeignKey(Classs, related_name='person', on_delete=models.CASCADE)
