# Generated by Django 4.2.6 on 2023-10-05 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('subclass', models.CharField(blank=True, max_length=25, null=True)),
                ('created_by', models.CharField(blank=True, max_length=15, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('school_phoneno', models.CharField(blank=True, max_length=12, null=True)),
                ('school_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('contactperson_name', models.CharField(max_length=35)),
                ('contactperson_phoneno', models.CharField(max_length=12)),
                ('motto', models.CharField(blank=True, max_length=45, null=True)),
                ('school_primarycolour', models.CharField(blank=True, max_length=45, null=True)),
                ('school_secondarycolour', models.CharField(blank=True, max_length=45, null=True)),
                ('sections_available', models.CharField(blank=True, choices=[('Nursery', 'Nursery'), ('Primary', 'Primary'), ('Secondary', 'Secondary'), ('College', 'College'), ('University', 'University'), ('Other', 'Other')], max_length=10, null=True)),
                ('class_level_count', models.CharField(blank=True, choices=[('0-6', '0-6'), ('7-15', '7-15'), ('Above 15', 'Above 15')], max_length=10, null=True)),
                ('created_by', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sesssion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionname', models.CharField(choices=[('2023/2024', '2023/2024'), ('2024/2025', '2024/2025'), ('2025/2026', '2025/2026'), ('2026/2027', '2026/2027'), ('2027/2028', '2027/2028'), ('2028/2029', '2028/2029'), ('2029/2030', '2029/2030'), ('2030/2031', '2030/2031'), ('2031/2032', '2031/2032'), ('2032/2033', '2032/2033'), ('2033/2034', '2033/2034'), ('2034/2035', '2034/2035')], max_length=10, unique=True)),
                ('duration_start', models.CharField(blank=True, max_length=20, null=True)),
                ('duration_end', models.CharField(blank=True, max_length=20, null=True)),
                ('created_by', models.CharField(blank=True, max_length=15, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termname', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=10, unique=True)),
                ('is_current', models.BooleanField(default=False)),
                ('duration_start', models.CharField(blank=True, max_length=20, null=True)),
                ('duration_end', models.CharField(blank=True, max_length=20, null=True)),
                ('created_by', models.CharField(blank=True, max_length=15, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('orientation', models.CharField(blank=True, max_length=15, null=True)),
                ('created_by', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('classs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='school.classs')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='school.school')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='set_current_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='school.sesssion'),
        ),
        migrations.AddField(
            model_name='school',
            name='set_current_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='school.term'),
        ),
        migrations.AddField(
            model_name='classs',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classs', to='school.school'),
        ),
    ]
