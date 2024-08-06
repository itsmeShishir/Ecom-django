from django.shortcuts import render
from .serialization import *
from rest_framework import viewsets

# Create your views here.
class product_view(viewsets.ModelViewSet):
    serializer_class = Producterializations
    queryset = User.objects.all()


