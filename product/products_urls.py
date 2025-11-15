from django.urls import path
from product import views as v

urlpatterns = [
    path('',v.ListCreateView.as_view(),name="products-list"),
    path('<int:id>',v.ViewSpecificProductApi.as_view(),name="specific-product")
]
