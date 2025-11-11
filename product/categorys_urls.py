from django.urls import path, include
from product import views as v
urlpatterns =[
    path('',v.view_categorys,name="all-category")
]