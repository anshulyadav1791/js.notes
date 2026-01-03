from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()   # ✅ correct
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_students(request):
    serializer = StudentSerializers(data = request.data)
    if serializer.is_valid():    
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
   
    