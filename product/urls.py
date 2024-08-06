from django.urls import path
from .views import *

urlpatterns = [
    path("product/", product_view.as_view({'get':'list'}), name="product" )
]
