from rest_framework import serializers
from api_app.models import *


class StudentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = StudentModel
        fields = "__all__"
        
    

