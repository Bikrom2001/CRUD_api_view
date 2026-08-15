from django.urls import path
from api_app.views import *

urlpatterns = [
    path('student-list/', student_list_add, name='student_list_add'),
    path('student-details/<int:pk>/', student_details, name='student_details')
    # path('add-student/', add_student, name='add_student'),
]

