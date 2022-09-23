from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Faculty, Speciality
from .serializers import FacultySerializer, SpecialitySerializer


@api_view(['GET', 'PUT', 'DELETE'])
def faculty_detail(request, slug, format=None):
    try:
        faculty = Faculty.objects.get(slug=slug)
    except Faculty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def faculty_list(request, format=None):
    if request.method == 'GET':
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def speciality_detail(request, faculty_slug, speciality_slug, format=None):
    try:
        speciality = Speciality.objects.filter(faculty__slug=faculty_slug).get(slug=speciality_slug)
    except Faculty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpecialitySerializer(speciality)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacultySerializer(speciality, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        speciality.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def speciality_list(request, faculty_slug, format=None):
    if request.method == 'GET':
        specialities = Speciality.objects.filter(faculty__slug=faculty_slug)

        serializer = SpecialitySerializer(specialities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SpecialitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
