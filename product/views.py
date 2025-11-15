# import from django:
from django.shortcuts import render , get_object_or_404
from django.db.models import Count 
from django.http import HttpResponse

# import from mine app:
from product.serializers import ProductSerializer , CategorySerializer
from product.models import Product,Category

# import from rest framework:
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# Create your views here.

class ListCreateView(ListCreateAPIView):
    # queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.select_related("category").all()

class ViewSpecificProductApi(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def delete(self, request, id):
        product = get_object_or_404(Product,pk=id)
        if product.stock==0:
            product.delete()
            return Response({'message':'delete success'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message':'product could not delete'})


class ViewProducts(APIView):
    def get(self,request):
        products = Product.objects.select_related("category").all()
        serializer = ProductSerializer(products, many =True , context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data = request.data , context={'request': request})
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data)

# view all products


class ViewSpecificProduct(APIView):
    def get(self,request , pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product , context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        product = get_object_or_404(Product,pk=pk)
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class ViewCategorysApi(ListCreateAPIView):
    queryset = Category.objects.annotate(product_cnt = Count('products'))
    serializer_class = CategorySerializer

class ViewCategorys(APIView):
    def get(self, request):
        categorys = Category.objects.annotate(product_cnt = Count("products"))
        serializer = CategorySerializer(categorys, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status = status.HTTP_201_CREATED)

class ViewSpecificCategoryApi(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ViewSpecificCagegory(APIView):
    def get(self, request , pk):
        category = get_object_or_404(Category , pk = pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self,request,pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status= status.HTTP_426_UPGRADE_REQUIRED)
    
    def delete(self , request ,pk):
        category = get_object_or_404(Category , pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)