from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app.serializers import *
from api_app.models import *


@api_view(['GET', "POST"])

def student_list_add(request):
    
    if request.method == 'GET':
        student_data = StudentModel.objects.all()
        serializer_data = StudentSerializers(student_data, many=True) 
        return Response({
            "success": True,
            "message": "student Data Successfully",
            'data': serializer_data.data
        })
    
    if request.method == 'POST':
            serializer_data = StudentSerializers(data = request.data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response({
                    "success": True,
                    "message": "student created Successfully",
                    'data': serializer_data.data  
                })
            return Response({
                'success': False,
                'error': serializer_data.errors
            })



# @api_view(['POST'])

# def add_student(request):
    
#     if request.method == 'POST':
#         serializer_data = StudentSerializers(data = request.data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return Response({
#                 "success": True,
#                 "message": "student created Successfully",
#                 'data': serializer_data.data  
#             })
#         return Response({
#             'success': False,
#             'error': serializer_data.errors
#         })


@api_view(['GET', "PATCH", "DELETE"])
def student_details(request, pk):
    if request.method == 'GET':
        student_data = StudentModel.objects.get(id = pk)
        serializer_data = StudentSerializers(student_data)
        return Response({
                    "success": True,
                    "message": "student Data Successfully",
                    'data': serializer_data.data
                })
        