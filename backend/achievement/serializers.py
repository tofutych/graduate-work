from rest_framework import serializers

from .models import Faculty, Speciality, YearOfAdmission, Student, Achievement


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url"
        )
