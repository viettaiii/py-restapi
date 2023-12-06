from django.urls import path
from . import views



## config route products
urlpatterns = [
    path('<int:pk>/' , views.product_detail_view)
]