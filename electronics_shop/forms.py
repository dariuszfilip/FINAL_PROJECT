from django import forms
from .models import Product, Category, Order, Customer
from django.contrib.auth.hashers import make_password
from django.template.defaultfilters import default


# class BuyProductForm(forms.ModelForm):
#       
#     class Meta:
#         model = Order
#         fields = '__all__'

    


class BuyProductForm(forms.Form):    
#     title = forms.CharField(max_length = 128, label='title', widget=forms.TextInput(attrs={'placeholder': Order.title}))
#     customer = forms.CharField
#     product = forms.CharField
    quantity = forms.IntegerField()




class SearchForm(forms.Form):
    product = forms.CharField(label='produkt', max_length=100)