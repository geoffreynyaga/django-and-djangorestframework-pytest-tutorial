from rest_framework.serializers import ModelSerializer

from classroom.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "username",
            "admission_number",
            "is_qualified",
            "average_score",
        )
