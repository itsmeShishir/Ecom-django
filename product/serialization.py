from rest_framework import serializers
from .models import *

class CategorySerializations(serializers.ModelSerializer):
    class Meta:
        models=Category
        fields= "__all__"

class Producterializations(serializers.ModelSerializer):
    class Meta:
        models=Product
        fields= "__all__"