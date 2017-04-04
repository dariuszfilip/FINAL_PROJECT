from django.db import models
from django.urls import reverse




class Customer(models.Model):
    login = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address = models.TextField()
    tel = models.CharField(max_length=32)


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    

class Product(models.Model):
    name = models.CharField(max_length=128)
    descritpion = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category)
      
    
class Order(models.Model):
    title = models.CharField(max_length = 128)
    customer = models.OneToOneField(Customer)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()




    
    
    