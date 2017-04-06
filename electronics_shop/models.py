from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




class Customer(models.Model):
    user = models.OneToOneField(User, null=True, default=None)
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
    category = models.ForeignKey(Category, related_name="category")
#     owner = models.ForeignKey(User)
    
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.price, self.category)
      
    
# class Order(models.Model):
#     title = models.CharField(max_length = 128)
#     customer = models.OneToOneField(Customer)
#     product = models.ForeignKey(Product)
#     quantity = models.IntegerField()
# 
# 
#     def __str__(self):
#         return "{} {} {}".format(self.title, self.product, self.quantity)



class Order(models.Model):
    title = models.CharField(max_length = 128)
    customer = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    date = models.DateField()
    realised = models.BooleanField(default=False)


    def __str__(self):
        return "{} {} {}".format(self.title, self.product, self.quantity)
    



    
    
    