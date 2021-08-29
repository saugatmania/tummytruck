from django import forms
from django.db.models import fields
from tummyapp import models
from tummyapp.models import Customers,  Package_orders, Package_product_purchases, Product_orders, Product_purchases, Package_products, Packages, Product_categorys, Product_package_price_historys, Products, Blog_posts, Email_otps, Profiles, User_notifications, Users, Slider_images, Product_price_historys


class Package_ordersForm(forms.ModelForm):
    class Meta:
        model = Package_orders
        fields = "__all__"


class Package_product_purchasesForm(forms.ModelForm):
    class Meta:
        model = Package_product_purchases
        fields = '__all__'


class Product_ordersForm(forms.ModelForm):
    class Meta:
        model = Product_orders
        fields = '__all__'


class Product_purchasesForm(forms.ModelForm):
    class Meta:
        model = Product_purchases
        fields = '__all__'

class Slider_imagesForm(forms.ModelForm):
    class Meta:
        model = Slider_images
        fields = '__all__'


# -----------------------------------------------------------------------------------------------------------


class Package_productsForm(forms.ModelForm):
    class Meta:
        model = Package_products
        fields = '__all__'


class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = '__all__'


class Product_categorysForm(forms.ModelForm):
    class Meta:
        model = Product_categorys
        fields = '__all__'


class Product_package_price_historysForm(forms.ModelForm):
    class Meta:
        model = Product_package_price_historys
        fields = '__all__'

class Product_price_historysForm(forms.ModelForm):
    class Meta:
        model = Product_price_historys
        fields = '__all__'


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

# ---------------------------------------------------------------------------------------------------------------------------


class Blog_postsForm(forms.ModelForm):
    class Meta:
        model = Blog_posts
        fields = '__all__'


class Email_optsForm(forms.ModelForm):
    class Meta:
        model = Email_otps
        fields = '__all__'


class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'


class User_notificationsForm(forms.ModelForm):
    class Meta:
        model = User_notifications
        fields = '__all__'


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"
