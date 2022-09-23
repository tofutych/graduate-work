from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Faculty, Speciality
from .serializers import FacultySerializer


class FacultyList(APIView):
    def get(self, request, format=None):
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)

# class SpecialityList(APIView):
#     def get(self, requests, faculty_slug, format=None):
#
