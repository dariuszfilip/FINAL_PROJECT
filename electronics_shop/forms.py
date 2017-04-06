from django import forms
from .models import Product, Category, Order, Customer
from django.contrib.auth.hashers import make_password
from django.template.defaultfilters import default
from django.contrib.auth import authenticate
from django.contrib.auth.models import User   
from django.contrib.auth.forms import UserCreationForm

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
    
    
    
class AuthForm(forms.Form):
  
    login = forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)
    
    
    
    def clean(self):
        #metoda dorzuca do cleaned_data instację użytkownika pod kluczem 'user'
        
            cleaned_data = super().clean()          
            #przeniesione z views:
            login = cleaned_data['login']
            password = cleaned_data['password']
            user = authenticate(username=login, password=password)
            if user is None:
                raise forms.ValidationError("Błędny login lub hasło")
  
            cleaned_data['user'] = user
            return cleaned_data
        
        
        
        
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    address = forms.CharField(required = False)
  



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.address = self.cleaned_data['address']


        if commit:
            user.save()

        return user        
        
        




class DeliveryProductForm(forms.Form):
    message = forms.CharField(label='Dodatkowa wiadomość dla sprzedającego', max_length=100)









