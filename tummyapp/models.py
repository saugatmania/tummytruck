
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import related
import random

# Create your models here.
class Tracking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True





DELIVER_CHOICES = (
    ("pending", "PENDING"),
    ("delivered", "DELIVERED"),
    ("return", "RETURN")
)
PACKAGE_CHOICES = (
    ("employee_package", "EMPLOYEE PACKAGE"),
    ("total_veg_package", "TOTAL VEG PACKAGE")
)
WEEK = (
    ("first_week", "FIRST WEEK"),
    ("second_week", "SECOND WEEK"),
    ("third_week", "THIRD WEEK"),
    ("fourth_week", "FOURTH WEEK")
)
DAY = (
    ("sunday", "SUNDAY"),
    ("monday", "MONDAY"),
    ("tuesday", "TUESDAY"),
    ("wednesday", "WEDNESDAY"),
    ("thursday", "THURSDAY"),
    ("friday", "FRIDAY"),
    ("saturday", "SATURDAY")
)
PARENT = (
    ("dairy", "DAIRY"),
    ("beverages", "BEVERAGES"),
    ("hard drinks", "HARD DRINKS"),
    ("soft drinks", "SOFT DRINKS"),
    ("groceries", "GROCERIES"),
    ("kitchen item", "KITCHEN ITEM"),
    ("madi in nepal", "MADE IN NEPAL"),
    ("restaurants", "RESTAURANTS")
)


class Customers(models.Model):
    customer = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return f"{str(self.phone)}--{self.customer}"



class Package_orders(Tracking):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    ordered = models.BooleanField()
    delivered = models.CharField(max_length=50, choices=DELIVER_CHOICES)
    remarks = models.TextField()

    def __str__(self):
        return str(self.id)


class Package_product_purchases(Tracking):
    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES)
    week = models.CharField(max_length=50, choices=WEEK)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    order = models.ForeignKey(Package_orders, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    checkout = models.BooleanField()


class Product_orders(Tracking):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    ordered = models.BooleanField()
    delivered = models.CharField(max_length=50, choices=DELIVER_CHOICES)
    remarks = models.TextField()


class Product_purchases(Tracking):
    product = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    ordered = models.BooleanField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    checkout = models.BooleanField()


class Slider_images(models.Model):
    ACTIVE = (
    ("unknown", "UNKNOWN"),
    ("yes", "YES"),
    ("no", "NO")
)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="tummy_images/", null=True, blank=True)
    is_active = models.CharField(choices=ACTIVE, default='unknown', max_length=100)


class Package_products(Tracking):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    package = models.CharField(max_length=50, choices=PACKAGE_CHOICES)
    week = models.CharField(max_length=50, choices=WEEK)
    day = models.CharField(max_length=50, choices=DAY)
    image = models.ImageField(upload_to="tummy_images/", null=True, blank=True)
    

class Packages(Tracking):
    name = models.CharField(max_length=100)
    description = models.TextField()

    
class Product_categorys(Tracking):
    parent = models.CharField(max_length=50, choices=PARENT)
    name = models.CharField(max_length=100)
    
  
class Product_package_price_historys(Tracking):
    package_product = models.CharField(max_length=50, choices=WEEK)
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    current_price = models.DecimalField(max_digits=15, decimal_places=2)

class Products(Tracking):
    category = models.CharField(max_length=20, choices=PARENT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="tummy_images/", null=True, blank=True)

    def __str__(self):
        return str(self.name)
 
class Product_price_historys(Tracking):
    package_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)



def random_string():
    return str(random.randint(1000, 9999))
    
    


class Blog_posts(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    image = models.ImageField(upload_to="tummy_images/", null=True, blank=True)


class Email_otps(Tracking):
    phone = models.ForeignKey(Customers, on_delete=models.CASCADE)
    otp = models.CharField(default = random_string, max_length=6)
    validated = models.BooleanField(default=True)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    forgot = models.BooleanField()
    forgot_logged = models.BooleanField()


class Profiles(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    lunch_time = models.IntegerField()


class User_notifications(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    message = models.TextField()
    title = models.CharField(max_length=50)


class Users(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.ForeignKey(Customers, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=True)
    is_logistic = models.BooleanField(default=False)
    staff_status = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    superuser_status = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    password_confirmation = models.CharField(max_length=100)
    
