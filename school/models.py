from django.db import models

class Sesssion(models.Model):
	SESSIONS = (
		('2023/2024', '2023/2024'), 
		('2024/2025', '2024/2025'), 
		('2025/2026', '2025/2026'), 
		('2026/2027', '2026/2027'), 
		('2027/2028', '2027/2028'), 
		('2028/2029', '2028/2029'), 
		('2029/2030', '2029/2030'), 
		('2030/2031', '2030/2031'), 
		('2031/2032', '2031/2032'), 
		('2032/2033', '2032/2033'), 
		('2033/2034', '2033/2034'), 
		('2034/2035', '2034/2035'), 
    ) 
	sessionname = models.CharField(max_length=10, choices=SESSIONS, unique=True)
	duration_start = models.CharField(max_length=20, blank=True, null=True) 
	duration_end = models.CharField(max_length=20, blank=True, null=True)
	created_by = models.CharField(max_length=15, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
class Term(models.Model):
	# will work for both secondary sch terms and college semesters
	TERMS = (
		('First', 'First'), 
		('Second', 'Second'),
		('Third', 'Third'), 
    )
	termname = models.CharField(max_length=10, choices=TERMS, unique=True)
	is_current = models.BooleanField(default=False)
	duration_start = models.CharField(max_length=20, blank=True, null=True) 
	duration_end = models.CharField(max_length=20, blank=True, null=True)
	created_by = models.CharField(max_length=15, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

class School(models.Model):
	SECTIONS_AVAILABLE = (
		('Nursery', 'Nursery'), 
		('Primary', 'Primary'),
		('Secondary', 'Secondary'), 
		('College', 'College'), 
		('University', 'University'), 
		('Other', 'Other'), 
    )
	CLASS_LEVEL_COUNT = (
		('0-6', '0-6'), 
		('7-15', '7-15'), 
		('Above 15', 'Above 15'), 
    )
	set_current_session = models.ForeignKey(Sesssion, related_name='school', on_delete=models.CASCADE)
	set_current_term = models.ForeignKey(Term, related_name='school', on_delete=models.CASCADE)
	schoolname = models.CharField(max_length=50)
	address = models.TextField()
	state = models.CharField(max_length=15, blank=True, null=True)
	school_phoneno = models.CharField(max_length=12, blank=True, null=True)
	school_email = models.EmailField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=15, blank=True, null=True)
	contactperson_name = models.CharField(max_length=35)
	contactperson_phoneno = models.CharField(max_length=12)
	motto = models.CharField(max_length=45, blank=True, null=True)
	school_primarycolour = models.CharField(max_length=45, blank=True, null=True)
	school_secondarycolour = models.CharField(max_length=45, blank=True, null=True)
	sections_available = models.CharField(max_length=10, blank=True, null=True, choices=SECTIONS_AVAILABLE)
	class_level_count = models.CharField(max_length=10, blank=True, null=True, choices=CLASS_LEVEL_COUNT)
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
	# logo

class Classs(models.Model):
	school = models.ForeignKey(School, related_name='classs', on_delete=models.CASCADE)
	name = models.CharField(max_length=25) 
	subclass = models.CharField(max_length=25, blank=True, null=True) 
	created_by = models.CharField(max_length=15, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

class Subject(models.Model):
	school = models.ForeignKey(School, related_name='subject', on_delete=models.CASCADE)
	classs = models.ForeignKey(Classs, related_name='subject', on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	orientation = models.CharField(max_length=15, blank=True, null=True) 
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

