from django.urls import path, include
from product import views as v
urlpatterns =[
    path('',v.ViewCategorys.as_view(),name="all-category"),
    path('<int:pk>/',v.ViewSpecificCagegory.as_view(),name="view-specific-category")
]