from rest_framework.generics import ListAPIView


from .serializers import StudentSerializer
from classroom.models import Student


class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

