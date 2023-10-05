from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Staff
from .serializers import StudentSerializer, StaffSerializer

"""
Student
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = Student.objects.get(id= data['id'])
        serializer = StudentSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = Student.objects.get(id= data['id'])
        serializer = StudentSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Student.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Session deleted'})

"""
Staff
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def staff(request):
    if request.method == 'GET':
        stf = Staff.objects.all()
        serializer = StaffSerializer(stf, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = StaffSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = Staff.objects.get(id= data['id'])
        serializer = StaffSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = Staff.objects.get(id= data['id'])
        serializer = StaffSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Staff.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Term deleted'})
    