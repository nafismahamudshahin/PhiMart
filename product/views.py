from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from product.serializers import ProductSerializer , CategorySerializer
from product.models import Product,Category
from rest_framework import status
from django.db.models import Count 
# Create your views here.

@api_view(['GET','POST'])
def view_products(request):
    if request.method == "GET":
        products = Product.objects.select_related("category").all()
        serializer = ProductSerializer(products, many =True , context={'request': request})
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ProductSerializer(data = request.data , context={'request': request})
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


@api_view()
def view_specific_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(product , context={'request': request})
    return Response(serializer.data)

@api_view(['GET','POST'])
def view_categorys(request):
    if request.method == "GET":
        categorys = Category.objects.annotate(product_cnt = Count("products")).all()
        serializer = CategorySerializer(categorys, many = True)

        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("okey")
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category , pk = pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)