from rest_framework import serializers

from .models import Faculty, Speciality, YearOfAdmission, Student, Achievement


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'
