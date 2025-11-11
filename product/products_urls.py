from django.urls import path
from product import views as v

urlpatterns = [
    path('',v.view_products,name="products-list"),
    path('<int:pk>',v.view_specific_product,name="specific-product")
]
