from django.urls import path, include
from product import views as v
urlpatterns =[
    path('',v.view_categorys,name="all-category"),
    path('<int:pk>/',v.view_specific_category,name="view-specific-category")
]