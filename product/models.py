from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(("category_img"), upload_to=None, height_field=None, width_field=None, max_length=None)
    username = models.ForeignKey(User,blank = True, null= True , on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"


class Contact(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField(blank= True, null=True)
    description = models.TextField()
    number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Brand = models.CharField(max_length=255)
    img = models.ImageField(upload_to="product/", height_field=None, width_field=None, max_length=None, blank= True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"
   


