from django.contrib import admin
from tummyapp.models import Customers, Package_orders, Product_orders, Packages, Products, Users, Package_product_purchases, Product_purchases, Package_products, Product_categorys, Product_package_price_historys, Blog_posts, Email_otps, Profiles, User_notifications, Slider_images, Product_price_historys


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer', 'phone']



@admin.register(Package_orders)
class Package_ordersAdmin(admin.ModelAdmin):
    list_display = ['customer', 'shipping_address',
                    'ordered', 'delivered', 'created', 'modified', 'remarks']


@admin.register(Package_product_purchases)
class Package_product_purchasesAdmin(admin.ModelAdmin):
    list_display = ['package', 'week', 'unit_price', 'quantity',
                    'total_price', 'created', 'modified', 'checkout', 'customer']


@admin.register(Product_orders)
class Product_ordersAdmin(admin.ModelAdmin):
    list_display = ['customer', 'shipping_address', 'ordered',
                    'delivered', 'created', 'modified', 'remarks']


@admin.register(Product_purchases)
class Product_purchasesAdmin(admin.ModelAdmin):
    list_display = ['product', 'unit_price', 'ordered',
                    'total_price', 'customer', 'quantity', 'checkout']

@admin.register(Slider_images)
class Slider_imagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'is_active']


@admin.register(Package_products)
class Package_productsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description',
                    'package', 'week', 'day', 'image', 'created', 'modified']


@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'modified']


@admin.register(Product_categorys)
class Product_categorysAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'created', 'modified']


@admin.register(Product_package_price_historys)
class Product_package_price_historysAdmin(admin.ModelAdmin):
    list_display = ['package_product', 'old_price',
                    'current_price', 'created', 'modified']

@admin.register(Product_price_historys)
class Product_price_historysAdmin(admin.ModelAdmin):
    list_display = ['package_product', 'old_price',
                    'current_price', 'created', 'modified']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image',
                    'category', 'created', 'modified']


@admin.register(Blog_posts)
class Blog_postsAdmin(admin.ModelAdmin):
    list_display = ['description', 'title', 'subtitle', 'image']


@admin.register(Email_otps)
class Email_otpsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'otp', 'validated',
                    'count', 'date', 'time', 'forgot', 'forgot_logged']


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'occupation',
                    'location', 'phone', 'lunch_time']


@admin.register(User_notifications)
class User_notificationsAdmin(admin.ModelAdmin):
    list_display = ['user','message', 'title']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_customer', 'is_logistic', 'staff_status', 'active', 'superuser_status', 'password', 'password_confirmation']
