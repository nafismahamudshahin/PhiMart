from django.urls import path , include

urlpatterns = [
    path('products/',include('product.products_urls')),
    path('categorys/',include('product.categorys_urls')),
]
