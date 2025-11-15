from django.urls import path , include
from rest_framework.routers import DefaultRouter
# from product.views import ProductViewSet , CagegoryViewSet
from product import views as v
router = DefaultRouter()
router.register("products",v.ProductViewSet)
router.register("category",v.CagegoryViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('products/',include('product.products_urls')),
#     path('categorys/',include('product.categorys_urls')),
# ]
