from rest_framework import serializers
from .models import Ipad

class Ipadserializer(serializers.ModelSerializer):
    class Meta:
        model =Ipad
        fields =['name','year','description']

