from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField
class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Customer(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    phone = PhoneNumberField()
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=100)
    username = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.first_name + self. last_name
    
class Product(models.Model):
    name = models.CharField( max_length=100)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name=(""), on_delete=models.CASCADE)
    description = models.CharField( max_length=250, default="",blank=True, null=True)
    image = models.ImageField(upload_to="uploads/product/")
    #Sale
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField( max_length=100 , default='', blank=True)
    phone = PhoneNumberField(blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product