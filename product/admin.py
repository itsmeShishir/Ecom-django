from django.contrib import admin
from .models import Category, Contact, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Product)