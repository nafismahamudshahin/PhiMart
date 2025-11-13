from django.urls import path
from product import views as v

urlpatterns = [
    path('',v.ViewProducts.as_view(),name="products-list"),
    path('<int:pk>',v.ViewSpecificProduct.as_view(),name="specific-product")
]
