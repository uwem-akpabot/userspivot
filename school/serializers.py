from rest_framework import serializers
from .models import School, Sesssion, Term, Classs, Subject

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SesssionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesssion
        fields = '__all__'

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class ClasssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classs
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'