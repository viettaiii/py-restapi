from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json

from products.models import Product

def api_home(request, *args , **kwargs):
    model_data = Product.objects.all()
    data = {}
    if model_data:
        data = serialize('json' , model_data)
  
    return JsonResponse(data , safe=False)
