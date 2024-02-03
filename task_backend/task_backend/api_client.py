import requests
from django.conf import settings

def get_products():
    try:
        response = requests.get(f"{settings.SWAGGER_API_BASE_URL}/products")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get products: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None

def get_product_categories():
    try:
        response = requests.get(f"{settings.SWAGGER_API_BASE_URL}/productCategories")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get product categories: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None

def get_sales_orders():
    try:
        response = requests.get(f"{settings.SWAGGER_API_BASE_URL}/salesOrders")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get sales orders: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None

def get_sales_order_details(order_id):
    try:
        response = requests.get(f"{settings.SWAGGER_API_BASE_URL}/salesOrderDetails/{order_id}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get sales order details for order {order_id}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None

