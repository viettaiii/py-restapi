from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

from products.models import Product
from products.serializers import ProductSerializer

# @api_view(['GET'])
# def api_home(request, *args , **kwargs):
#     # model_data = Product.objects.all().order_by('?').first()
#     # data = {}
#     # if model_data:
#     #     data = model_to_dict(model_data , fields=['title','content','price' ,'sale_price'])

#     instance = Product.objects.all().order_by('?').first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
  
#     return Response(data )



@api_view(['POST'])
def api_home(request, *args , **kwargs):
    
    serialize = ProductSerializer(data = request.data)
    if serialize.is_valid(raise_exception=True):
        print(serialize.data)
        return Response(serialize.data)
