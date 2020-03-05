# from django.test import TestCase
from hypothesis.extra.django import TestCase
import pytest
from hypothesis import strategies as st, given
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

    # @given(st.characters())
    # def test_slugify(self, name):

    #     print(name, "name")

    #     student1 = mixer.blend(Student, first_name=name)
    #     student1.save()

    #     student_result = Student.objects.last()  # getting the last student

    #     assert len(str(student_result.username)) == len(name)

    @given(st.floats(min_value=0, max_value=40))
    def test_grade_fail(self, fail_score):

        print(fail_score, "this is failscore")

        student1 = mixer.blend(Student, average_score=fail_score)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Fail"

    @given(st.floats(min_value=40, max_value=70))
    def test_grade_pass(self, pass_grade):

        student1 = mixer.blend(Student, average_score=pass_grade)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Pass"

    @given(st.floats(min_value=70, max_value=100))
    def test_grade_excellent(self, excellent_grade):

        student1 = mixer.blend(Student, average_score=excellent_grade)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Excellent"

    @given(st.floats(min_value=100))
    def test_grade_error(self, error_grade):

        student1 = mixer.blend(Student, average_score=error_grade)

        student_result = Student.objects.last()  # getting the last student

        assert student_result.get_grade() == "Error"


class TestClassroomModel:
    def test_classroom_create(self):
        classroom = mixer.blend(Classroom, name="Physics")

        classroom_result = Classroom.objects.last()  # getting the last student

        assert str(classroom_result) == "Physics"
