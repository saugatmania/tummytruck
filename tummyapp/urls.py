from django.urls import path
from tummyapp import views


app_name = 'tummyapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    # prurchase
    path('package_orders/', views.package_orders, name='package_orders'),
    path('package_order_form/', views.package_order_form,
         name='package_order_form'),

    path('package_product_purchases/', views.package_product_purchases, name='package_product_purchases'),
    path('package_product_purchases_form/', views.package_product_purchases_form, name='package_product_purchases_form'),
#   
         

    path('product_orders/', views.product_orders, name='product_orders'),
    path('product_orders_form/', views.product_orders_form,
         name='product_orders_form'),

    path('product_purchases/', views.product_purchases, name='product_purchases'),
    path('product_purchases_form/', views.product_purchases_form,
         name='product_purchases_form'),

     path('slider_images/', views.slider_images, name='slider_images'),
     path('slider_images_form/', views.slider_images_form, name='slider_images_form'),
    # -------------------------------------------------------------------------------------------------------------------

    # services
    path('package_products/', views.package_products, name='package_products'),
    path('package_products_form/', views.package_products_form,
         name='package_products_form'),

    path('packages/', views.packages, name='packages'),
    path('packages_form/', views.packages_form, name='packages_form'),

    path('product_categorys/', views.product_categorys, name='product_categorys'),
    path('product_categorys_form/', views.product_categorys_form,
         name='product_categorys_form'),

    path('product_package_price_historys/', views.product_package_price_historys,
         name='product_package_price_historys'),
    path('product_package_price_historys_form/', views.product_package_price_historys_form,
         name='product_package_price_historys_form'),

     path('product_price_historys/', views.product_price_historys,
         name='product_price_historys'),
    path('product_price_historys_form/', views.product_price_historys_form,
         name='product_price_historys_form'),

    path('products/', views.products, name='products'),
    path('products_form/', views.products_form, name='products_form'),
    # --------------------------------------------------------------------------------------------------------------------------
    # useraccount
    path('blog_posts/', views.blog_posts, name='blog_posts'),
    path('blog_posts_form/', views.blog_posts_form, name='blog_posts_form'),

    path('email_otps/', views.email_otps, name='email_otps'),
    path('email_otps_form/', views.email_otps_form, name='email_otps_form'),

    path('profiles/', views.profiles, name='profiles'),
    path('profiles_form/', views.profiles_form, name='profiles_form'),

    path('user_notifications/', views.user_notifications,
         name='user_notifications'),
    path('user_notifications_form/', views.user_notifications_form,
         name='user_notifications_form'),

    path('users/', views.users, name='users'),
    path('users_form/', views.users_form, name='users_form'),

]
