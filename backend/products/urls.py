from django.urls import path
from . import views



## config route products
## /api/products/
urlpatterns = [
     path('' , views.product_create_view),
    path('<int:pk>/' , views.product_detail_view)
]