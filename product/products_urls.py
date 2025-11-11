from django.urls import path
from product import views as v

urlpatterns = [
    path('',v.view_products,name="products-list"),
    path('<int:id>',v.view_specific_product,name="specific-product")
]
