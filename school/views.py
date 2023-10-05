from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import School, Sesssion, Term, Classs, Subject
from .serializers import SchoolSerializer, SesssionSerializer, TermSerializer, ClasssSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated

"""
Session
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def sesssion(request):
    if request.method == 'GET':
        ses = Sesssion.objects.all()
        serializer = SesssionSerializer(ses, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = SesssionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = Sesssion.objects.get(id= data['id'])
        serializer = SesssionSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = Sesssion.objects.get(id= data['id'])
        serializer = SesssionSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Sesssion.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Session deleted'})

"""
Term
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def term(request):
    if request.method == 'GET':
        tm = Term.objects.all()
        serializer = TermSerializer(tm, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = TermSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = Term.objects.get(id= data['id'])
        serializer = TermSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = Term.objects.get(id= data['id'])
        serializer = TermSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Term.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Term deleted'})
    
"""
School
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def school(request):
    if request.method == 'GET':
        sch = School.objects.all()
        serializer = SchoolSerializer(sch, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = SchoolSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = School.objects.get(id= data['id'])
        serializer = SchoolSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = School.objects.get(id= data['id'])
        serializer = SchoolSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = School.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'School deleted'})
    
"""
Class
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def classs(request):
    if request.method == 'GET':
        cls = Classs.objects.all()
        serializer = ClasssSerializer(cls, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = ClasssSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = Classs.objects.get(id= data['id'])
        serializer = ClasssSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = Classs.objects.get(id= data['id'])
        serializer = ClasssSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Classs.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Class deleted'})