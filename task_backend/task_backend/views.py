from django.shortcuts import render

from django.http import JsonResponse
from .api_client import get_sales_order_details

def sales_order_details_view(request):
    sales_order_details = get_sales_order_details()
    return JsonResponse(sales_order_details, safe=False)

