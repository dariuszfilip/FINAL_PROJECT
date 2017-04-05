from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Customer, Category, Product, Order
from .forms import BuyProductForm




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
    
    
    
    
class BuyProductView(View):

    def get(self,request):
       
        form = BuyProductForm()
        ctx = {'form':form }
        return render(request,"buy_product.html",ctx)    
     
 
     
    def post(self,request):
        form = BuyProductForm(data=request.POST)
        ctx ={'form':form}
        if form.is_valid():
            title = form.cleaned_data['title']
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
             
            odred = Order.objects.create(
                title = title,
                customer = customer,
                product = product,
                quantity = quantity)
            return HttpResponseRedirect('products')
         
        return render(request,"buy_product.html",ctx)
    
    
#         template_name = 'buy_product.html'
#         form_class = BuyProductForm





class EditProductView(UpdateView):
    
    template_name = 'edit_product.html'
    model = Category
    fields = '__all__'
    
    
class DeleteProductView(DeleteView):
    template_name = 'delete_product.html'
    model = Category
    success_url = reverse_lazy('categories')
        
        
class AddProductView(CreateView):
    template_name = 'add_product.html'
    model = Category
    fields = '__all__'



