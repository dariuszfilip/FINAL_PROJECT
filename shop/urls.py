"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from electronics_shop.views import AddProductView,EditProductView,DeleteProductView, ProductView, ProductsView, CategoriesView, CustomersView, CategoryView, BuyProductView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products', ProductsView.as_view(), name="products"),
    url(r'^categories', CategoriesView.as_view(), name="categories"),
    url(r'^category/(?P<category_id>\d+)', CategoryView.as_view(), name="category"),
    url(r'^customers', CustomersView.as_view(), name="customers"),
    url(r'^product/(?P<product_id>\d+)', ProductView.as_view(), name="product"),
    url(r'^buy', BuyProductView.as_view(), name="buy-product"),
    url(r'^edit-product/(?P<pk>\d+)', EditProductView.as_view(), name="edit-product"),
    url(r'^delete-product/(?P<pk>\d+)', DeleteProductView.as_view(), name="delete-product"),
    url(r'^add-product', AddProductView.as_view(), name="add-product"),
]
