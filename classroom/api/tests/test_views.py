import pytest

from classroom.models import Student

from mixer.backend.django import mixer

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestStudentAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_student_list_works(self):
        # create a student

        student = mixer.blend(Student, first_name="Geoffrey")
        student2 = mixer.blend(Student, first_name="Naomi")

        url = reverse("student_list_api")

        # call the url
        response = self.client.get(url)

        # print(dir(response), "response")

        # aseertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

