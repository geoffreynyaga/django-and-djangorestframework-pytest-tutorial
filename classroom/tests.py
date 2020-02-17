from django.test import TestCase
import pytest
from classroom.models import Student, Classroom

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestStudentModel(TestCase):
    # def setUp(self):

    #     self.student1 = Student.objects.create(
    #         first_name="Tom", last_name="Mboya", admission_number=12345
    #     )

    # setting up new users
    # getting access tokens / logged in users
    # setup up timers

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a + b

        assert c == 3

    def test_student_can_be_created(self):

        student1 = mixer.blend(Student, first_name="Tom")

        student_result = Student.objects.last()  # getting the last student

        assert student_result.first_name == "Tom"

    def test_str_return(self):

        student1 = mixer.blend(Student, first_name="Tom")

        student_result = Student.objects.last()  # getting the last student

        assert str(student_result) == "Tom"

    def test_grade_fail(self):

        student1 = mixer.blend(Student, average_score=10)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Fail"

    def test_grade_pass(self):

        student1 = mixer.blend(Student, average_score=60)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Pass"

    def test_grade_excellent(self):

        student1 = mixer.blend(Student, average_score=90)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Excellent"

    def test_grade_error(self):

        student1 = mixer.blend(Student, average_score=101)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Error"


class TestClassroomModel:
    def test_classroom_create(self):
        classroom = mixer.blend(Classroom, name="Physics")

        classroom_result = Classroom.objects.last()  # getting the last student

        assert str(classroom_result) == "Physics"
