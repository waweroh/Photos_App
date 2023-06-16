from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    
    def save_category(self):
        self.save()
    
    def update_category(self, name):
        self.name = name
        self.save()
    
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name



class Photos(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField("image",null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    



    # categories,likes comments
    
    