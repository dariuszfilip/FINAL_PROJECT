from django import forms
from .models import Product, Category, Order, Customer



class BuyProductForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'
    
    
    
#     title = forms.CharField(max_length=128)
#     customer = 
#     product =
#     quantity = forms.IntegerField()