from django.db import models
from django.urls import reverse



class Customer(models.Model):
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
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    date = models.DateField()
    realised = models.BooleanField(default=False)


    def __str__(self):
        return "{} {} {}".format(self.title, self.product, self.quantity)
    



    
    
    