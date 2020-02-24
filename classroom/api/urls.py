from django.contrib import admin
from django.urls import path

from .views import StudentListAPIView

urlpatterns = [
    path("student/list/", StudentListAPIView.as_view(), name="student_list_api"),
]
