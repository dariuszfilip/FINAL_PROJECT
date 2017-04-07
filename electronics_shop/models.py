from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model



# class Profile(AbstractUser):
#     address = models.TextField(blank=True, null=True)


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, default=None)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address = models.TextField()
    tel = models.CharField(max_length=32)
    
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    
    def __str__(self):
        return "{}".format(self.name)

    

class Product(models.Model):
    name = models.CharField(max_length=128)
    descritpion = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name="category")
#     owner = models.ForeignKey(User)
    
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.price, self.category)
      
    

class Order(models.Model):
    title = models.CharField(max_length = 128)
    customer = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    date = models.DateField()
    realised = models.BooleanField(default=False)


    def __str__(self):
        return "{} {} {}".format(self.title, self.product, self.quantity)
    



    
    
    