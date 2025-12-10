from django.db import models
from users.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/images",blank=True , null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE , related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , related_name="cart" )
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE , related_name="item")
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="item")    
    quantity = models.IntegerField()

class Order(models.Model):
    PENDING= "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    STATUS_CHOICES = [
        (PENDING,"Pending"),
        (SHIPPED,"Shipped"),
        (DELIVERED,"Delivered"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name="orders")
    status = models.CharField(choices=STATUS_CHOICES , default=PENDING)
    total_price = models.DecimalField(max_digits=10 ,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name="items")
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity =  models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Review(models.Model):
    product = models.ForeignKey(Product , models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

