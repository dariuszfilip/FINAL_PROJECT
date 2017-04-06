
import datetime
from electronics_shop.models import Product, Customer, Order


def current_datetime(request):
    return {
        'current_datetime': datetime.datetime.now()
    }
    
#     
# def actual_order(request):
#     return {
#         "actual_order" : Order.obejct.get(pk=1)
#         }