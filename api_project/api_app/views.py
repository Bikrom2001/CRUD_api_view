from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app.serializers import *
from api_app.models import *


@api_view(['GET'])

def student_list(request):
    
    if request.method == 'GET':
        student_data = StudentModel.objects.all()
        serializer_data = StudentSerializers(student_data, many=True) 
        return Response(serializer_data.data)

