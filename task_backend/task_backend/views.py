from django.shortcuts import render
import requests
from django.http import JsonResponse

def get_data_from_swagger(request):
    url = "https://virtserver.swaggerhub.com/IULIAETEODORESCU/project_task/1.0.0/products"  # Example endpoint

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)  # safe=False is needed if the response is a list
        else:
            return JsonResponse({'error': 'Failed to fetch data from SwaggerHub', 'status_code': response.status_code}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    

import requests
from django.http import JsonResponse

def getProducts(request):
    url = "https://virtserver.swaggerhub.com/IULIAETEODORESCU/project_task/1.0.0/products"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch products from API', 'status_code': response.status_code}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


