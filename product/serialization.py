from rest_framework import serializers
from .models import *

class CategorySerializations(serializers.ModelSerializer):
    class Meta:
        models=Category
        fields= "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'Brand', 'img', 'price', 'is_slider', 'is_featured']