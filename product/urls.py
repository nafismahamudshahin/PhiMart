from django.urls import path
from product import views as v

urlpatterns = [
    path('product/',v.view_products,name="products-list")
]
