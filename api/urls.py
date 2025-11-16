from django.urls import path , include
# from product.views import ProductViewSet , CagegoryViewSet
from rest_framework_nested import routers
from product import views as v


router = routers.DefaultRouter()
router.register("products",v.ProductViewSet , basename="products")
router.register("category",v.CagegoryViewSet)

product_router = routers.NestedDefaultRouter(router, "products" , lookup = "product")
product_router.register('reviews', v.ReviewViewSet , basename="product-review")

# urlpatterns = router.urls + product_router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls))
]

# urlpatterns = [
#     path('products/',include('product.products_urls')),
#     path('categorys/',include('product.categorys_urls')),
# ]
