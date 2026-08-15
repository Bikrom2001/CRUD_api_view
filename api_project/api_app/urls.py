from django.urls import path
from api_app.views import *

urlpatterns = [
    path('student-list/', student_list, name='student_list')
]

