from django.urls import path
from api_app.views import *

urlpatterns = [
    path('student-list/', student_list_add, name='student_list_add'),
    # path('add-student/', add_student, name='add_student'),
]

