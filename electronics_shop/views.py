from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Customer, Category, Product, Order, User
from .forms import  SearchForm, BuyProductForm, AuthForm, MyRegistrationForm, DeliveryProductForm
from django.template.context_processors import request
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
import datetime
from django.contrib import auth  
from django.template.context_processors import csrf

               
 






class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        ctx = {"products": products}
        return render(request, "products.html", ctx)


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        ctx = {"categories": categories}
        return render(request, "categories.html", ctx)


  
class CustomersView(View):
    def get(self, request):
        customers = Customer.objects.all()
        ctx = {"customers": customers}
        return render(request, "customers.html", ctx)
   
    
 
    
class ProductView(View):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        category = product.category
        ctx = {"product": product, "category":category}
        return render(request, "product.html", ctx)
    
    
    
    
class CategoryView(View):

    def get(self,request, category_id):
        category = Category.objects.get(pk=category_id)
        products = Product.objects.filter(category=category)
        ctx = {'category':category,
               'products':products}
        return render(request,"category.html",ctx)
    
    
    
    
# class BuyProductView(View):
# 
#     def get(self,request):
#         form = BuyProductForm()
#         ctx = {'form':form }
#         return render(request,"buy_product.html",ctx)    
    
#     def post(self,request):
#         form = BuyProductForm(data=request.POST)
#         ctx ={'form':form}
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             customer = form.cleaned_data['customer']
#             product = form.cleaned_data['product']
#             quantity = form.cleaned_data['quantity']
#              
#             order= Order.objects.create(
#                 title = title,
#                 customer = customer,
#                 product = product,
#                 quantity = quantity)
#             return HttpResponseRedirect('products')
#          
#         return render(request,"buy_product.html",ctx)

     


class BuyProductView(View):
     def get(self,request, product_id):
         form = BuyProductForm()
         ctx = {'form':form }
         return render(request,"buy_product.html",ctx)
     
  
     def post(self, request, product_id):
         form = BuyProductForm(data=request.POST)
         product = Product.objects.get(pk = product_id)
         customer = request.user
         
         if form.is_valid():
             order = Order.objects.create(
                 title =
                 "Id produktu: " + str(product.id) +
                 " Id klienta: "+ str(customer.id) +
                 " Data zamówienia: " + str(datetime.datetime.now()),
                 customer = customer,
                 product = product,
                 quantity = form.cleaned_data['quantity'],
                 date = datetime.datetime.now(),
                 realised = True   
                 )
#              return HttpResponseRedirect('categories')
         
         
         ctx = {'product':product, 'customer': customer, 'order':order}
         return render(request,"order.html",ctx)          
    




class DeliveryProductView(View):
     def get(self,request):
         form = DeliveryProductForm()
         ctx = {'form':form }
         return render(request,"delivery.html",ctx)
      
   
     def post(self, request):
        form = DeliveryProductForm(data=request.POST)
#         product = Product.objects.get(pk = product_id)
#         customer_address = request.user.email
        
        user = User.objects.get(username='Jan')
        customer_address = user.customer.address
        
          
        if form.is_valid():
            message = form.cleaned_data['message'],
            address = customer_address
                
                
                
#              return HttpResponseRedirect('categories')
          
          
        ctx = {'message':message, 'address': address}
        return render(request,"delivery.html",ctx) 
        





class EditProductView(UpdateView):
    
    template_name = 'edit_product.html'
    model = Product
    fields = '__all__'
    
    
class DeleteProductView(DeleteView):
    template_name = 'delete_product.html'
    model = Product
    success_url = reverse_lazy('categories')
        
        
class AddProductView(CreateView):
    template_name = 'add_product.html'
    model = Product
    fields = '__all__'
    
    
    
    
class ProductSearchView(View):
       
    
    def get(self, request):
        ctx = {'form': SearchForm()}
        return render(request, 'product_search.html', ctx)
    
    def post(self, request):
        form = SearchForm(data=request.POST)
        ctx = {"form": form}
        if form.is_valid():
            name = form.cleaned_data['product']
            products = Product.objects.filter(name=name)
            ctx['results'] = products  
            
        return render(request, 'product_results.html', ctx)
    
    
    
class LoginView(View):   
    def get(self, request):
        form = AuthForm()
        ctx = {'form': form}
        return render(request, 'login.html', ctx)
            
    def post(self, request):
        form = AuthForm(data=request.POST)
        ctx ={'form': form}
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return HttpResponseRedirect(reverse('categories'))      
        else:
            return render(request, 'login.html', ctx)
    
    
    
    
class LogoutView(LoginRequiredMixin, View):   
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    
    
    
    
    
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
#             return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print (args)
    return render(request, 'register.html', args)
    
    
    
    
    
    




