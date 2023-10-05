# Generated by Django 4.2.6 on 2023-10-05 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feature', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('mname', models.CharField(blank=True, max_length=25, null=True)),
                ('sname', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=6)),
                ('dob', models.CharField(blank=True, max_length=10, null=True)),
                ('phoneno', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=45)),
                ('address', models.TextField(blank=True, null=True)),
                ('contactperson1', models.CharField(max_length=30)),
                ('contactperson1_phoneno', models.CharField(max_length=12)),
                ('contactperson1_relationship', models.CharField(choices=[('Parent', 'Parent'), ('Guardian', 'Guardian'), ('Sibling', 'Sibling'), ('Uncle/Aunt', 'Uncle/Aunt'), ('Relative', 'Relative'), ('Sponsor', 'Sponsor')], max_length=10)),
                ('contactperson2', models.CharField(blank=True, max_length=25, null=True)),
                ('contactperson2_phoneno', models.CharField(blank=True, max_length=12, null=True)),
                ('contactperson2_relationship', models.CharField(blank=True, choices=[('Parent', 'Parent'), ('Guardian', 'Guardian'), ('Sibling', 'Sibling'), ('Uncle/Aunt', 'Uncle/Aunt'), ('Relative', 'Relative'), ('Sponsor', 'Sponsor')], max_length=10, null=True)),
                ('contactperson_email', models.EmailField(blank=True, max_length=45)),
                ('contactperson_address', models.TextField(blank=True, null=True)),
                ('admissiondate', models.CharField(blank=True, max_length=10, null=True)),
                ('enddate', models.CharField(blank=True, max_length=10, null=True)),
                ('created_by', models.CharField(blank=True, max_length=15, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('classs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='school.classs')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='feature.parentaccess')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='school.school')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('Teacher', 'Teacher'), ('Administrator', 'Administrator'), ('Other Staff', 'Other Staff')], max_length=20)),
                ('fname', models.CharField(max_length=45)),
                ('mname', models.CharField(blank=True, max_length=30, null=True)),
                ('sname', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=6)),
                ('dob', models.CharField(max_length=10)),
                ('phoneno', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=45)),
                ('address', models.TextField(blank=True, null=True)),
                ('classrole', models.CharField(blank=True, max_length=20, null=True)),
                ('subjectrole', models.CharField(blank=True, max_length=20, null=True)),
                ('otherrole', models.CharField(blank=True, max_length=20, null=True)),
                ('contactperson1', models.CharField(max_length=30)),
                ('contactperson1_phone', models.CharField(max_length=12)),
                ('contactperson1_relationship', models.CharField(choices=[('Parent', 'Parent'), ('Guardian', 'Guardian'), ('Sibling', 'Sibling'), ('Uncle/Aunt', 'Uncle/Aunt'), ('Relative', 'Relative'), ('Sponsor', 'Sponsor')], max_length=12)),
                ('contactperson_email', models.EmailField(blank=True, max_length=45)),
                ('contactperson_address', models.TextField(blank=True, null=True)),
                ('employmentdate', models.CharField(blank=True, max_length=10, null=True)),
                ('enddate', models.CharField(blank=True, max_length=10, null=True)),
                ('created_by', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='school.school')),
            ],
        ),
    ]
