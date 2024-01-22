from django.shortcuts import render 
from django.http import HttpResponse

def ecommerce_index_view(request):
    return HttpResponse('Welcome to 6410742156 Nutchapon Kitkram views!')

def item_view(request, item_id): 
    context_data = {
        "item_id": item_id
        }
    
    return render(request, 'index.html',context= context_data)