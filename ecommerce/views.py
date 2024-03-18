from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def ecommerce_index_view(request):
    return HttpResponse('Welcome to 6410742156 Nutchapon Kitkram views!')

def item_view(request, item_id): 
    context_data = {
        "item_id": item_id
        }
    
    return render(request, 'index.html',context= context_data)

def ecommerce_home_view(request):
    return render(request, 'home.html')

def ecommerce_category_view(request):
    return render(request, 'category.html')

def ecommerce_contact_view(request):
    return render(request, 'contact.html')

def ecommerce_product_view(request):
    return render(request, 'product.html')

def ecommerce_checkout_view(request):
    return render(request, 'checkout.html')

@csrf_exempt
def basic_request(request):
    if request.method == 'GET':
        return JsonResponse({"status": "GET Passed"}, safe=False)
    elif request.method == 'POST':
        return JsonResponse({"status": "POST Passed"}, safe=False)
    else:
        return JsonResponse({"message": "Invalid Request"}, status=400)
# End of file

@csrf_exempt
def tokenize(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error": "Input not found"}, safe=False ,status=500)
        url = "https://api.aiforthai.in.th/tlexplus"
        data = {'text': sentence}
        headers = {'Apikey': "Y8NI2FLfPemnvAKJShCVNSn3FdErX110"}
        response = requests.post(url, data=data, headers=headers)
        response_json = response.json()
        return JsonResponse({"student":"6410742156", "tokenized": response_json}, safe=False)
    return JsonResponse({"error": "Invalid method"}, status=403, safe=False)