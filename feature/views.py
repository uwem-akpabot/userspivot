from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ParentAccess
from .serializers import ParentAccessSerializer

"""
ParentAccess
"""
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def parentaccess(request):
    if request.method == 'GET':
        par = ParentAccess.objects.all()
        serializer = ParentAccessSerializer(par, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data #grab the data input from user
        serializer = ParentAccessSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data #grab the data input from user
        obj = ParentAccess.objects.get(id= data['id'])
        serializer = ParentAccessSerializer(obj, data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data #grab the data input from user
        obj = ParentAccess.objects.get(id= data['id'])
        serializer = ParentAccessSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = ParentAccess.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Session deleted'})
