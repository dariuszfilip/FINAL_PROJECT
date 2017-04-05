
import datetime
from .models import Order


def current_datetime(request):
    return {
        'current_datetime': datetime.datetime.now()
    }
    
    
# def actual_order(request):
#     return {
#         "actual_order" : 
#         }