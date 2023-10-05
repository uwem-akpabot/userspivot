from rest_framework import serializers
from feature.models import ParentAccess
# Result, Attendance, Fee, EmployeePayroll, Alumni

class ParentAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentAccess
        fields = '__all__'
