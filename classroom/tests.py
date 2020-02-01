from django.test import TestCase
from classroom.models import Student


class TestStudentModel(TestCase):
    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a + b

        self.assertEqual(c, 3)

    def test_student_can_be_created(self):

        student1 = Student.objects.create(
            first_name="Tom", last_name="Mboya", admission_number=1234
        )

        student_result = Student.objects.last()  # getting the last student

        self.assertEqual(student_result.first_name, "Tom")

    def test_str_return(self):
        student1 = Student.objects.create(
            first_name="Tom", last_name="Mboya", admission_number=1234
        )

        student_result = Student.objects.last()  # getting the last student

        self.assertEqual(str(student_result), "Tom")

    def test_grade_fail(self):

        student1 = Student.objects.create(
            first_name="Tom", last_name="Mboya", admission_number=1234, average_score=10
        )

        student_result = Student.objects.last()  # getting the last student

        self.assertEqual(student_result.get_grade(), "Fail")

    def test_grade_pass(self):

        student1 = Student.objects.create(
            first_name="Tom", last_name="Mboya", admission_number=1234, average_score=60
        )

        student_result = Student.objects.last()  # getting the last student

        self.assertEqual(student_result.get_grade(), "Pass")

    def test_grade_excellent(self):

        student1 = Student.objects.create(
            first_name="Tom", last_name="Mboya", admission_number=1234, average_score=90
        )

        student_result = Student.objects.last()  # getting the last student

        self.assertEqual(student_result.get_grade(), "Excellent")

