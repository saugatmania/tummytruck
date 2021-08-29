from tummyapp.models import Blog_posts, Email_otps, Package_orders, Package_product_purchases, Product_categorys, Product_orders, Product_package_price_historys, Product_purchases, Package_products, Products, Packages, Profiles, User_notifications, Users, Slider_images, Product_price_historys
from django.shortcuts import render, reverse, get_object_or_404
from tummyapp.forms import CustomersForm, Package_ordersForm, Package_product_purchasesForm, Product_ordersForm, Product_purchasesForm, Package_productsForm, PackagesForm, Product_categorysForm, Product_package_price_historysForm, ProductsForm, Blog_postsForm, Email_optsForm, ProfilesForm, User_notificationsForm, UsersForm, Slider_imagesForm, Product_price_historysForm
from django.http.response import HttpResponseRedirect


def home(request):
    form = CustomersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("tummyapp:home"))
    return render(request, 'home.html', {'form': form})


# def purchase(request):
    # package_orders = Package_orders.objects.all()
    # package_product_purchases = Package_product_purchases.objects.all()
    # product_orders = Product_orders.objects.all()
    # product_purchases = Product_purchases.objects.all()

    # context = {"package_orders": package_orders, 'package_product_purchases': package_product_purchases,
    #            'product_order': product_orders, 'product_purchases': product_purchases}

    # return render(request, 'purchase.html', context)


def package_orders(request):
    package_orders = Package_orders.objects.all()

    context = {'package_orders': package_orders}
    return render(request, 'package_orders.html', context)


def package_order_form(request):
    package_order_form = Package_ordersForm(request.POST or None)
    if package_order_form.is_valid():
        package_order_form.save()
        return HttpResponseRedirect(reverse("tummyapp:package_orders"))
    return render(request, 'package_order_form.html', {'form': package_order_form})


def package_product_purchases(request):
    package_product_purchases = Package_product_purchases.objects.all()

    context = {'package_product_purchases': package_product_purchases}
    return render(request, 'package_product_purchases.html', context)


def package_product_purchases_form(request):
    package_product_purchases_form = Package_product_purchasesForm(
        request.POST or None)
    if package_product_purchases_form.is_valid():
        package_product_purchases_form.save()
        return HttpResponseRedirect(reverse("tummyapp:package_product_purchases"))
    return render(request, 'package_product_purchases_form.html', {'form': package_product_purchases_form})


# def package_product_purchases_form_add(request):
#     package_product_purchases_form_add = Package_product_purchasesForm(request.POST or None)
#     if package_product_purchases_form_add.is_valid():
#         package_product_purchases_form_add.save()
#         return HttpResponseRedirect(reverse("tummyapp:package_product_purchases"))
#     context = {"package_product_purchases_form_add": package_product_purchases_form_add}
#     return render(request, "package_product_purchases_form.html", context)


# def package_product_purchases_form_delete(request, id):
#     tummyapp = get_object_or_404(Package_product_purchases, id=id)  
#     tummyapp.delete()
#     return HttpResponseRedirect(reverse("tummyapp:package_product_purchases"))




def product_orders(request):
    product_orders = Product_orders.objects.all()

    context = {'product_order': product_orders}
    return render(request, 'product_orders.html', context)


def product_orders_form(request):
    product_orders_form = Product_ordersForm(
        request.POST or None)
    if product_orders_form.is_valid():
        product_orders_form.save()
        return HttpResponseRedirect(reverse("tummyapp:product_orders"))
    return render(request, 'product_orders_form.html', {'form': product_orders_form})


def product_purchases(request):
    product_purchases = Product_purchases.objects.all()

    context = {'product_purchases': product_purchases}
    return render(request, 'product_purchases.html', context)


def product_purchases_form(request):
    product_purchases_form = Product_purchasesForm(
        request.POST or None)
    if product_purchases_form.is_valid():
        product_purchases_form.save()
        return HttpResponseRedirect(reverse("tummyapp:product_purchases"))
    return render(request, 'product_purchases_form.html', {'form': product_purchases_form})


def slider_images(request):
    slider_images = Slider_images.objects.all()

    context = {'slider_images': slider_images}
    return render(request, 'slider_images.html', context)

def slider_images_form(request):
    slider_images_form = Slider_imagesForm(
        request.POST or None, request.FILES)
    if slider_images_form.is_valid():
        slider_images_form.save()
        return HttpResponseRedirect(reverse("tummyapp:slider_images"))
    return render(request, 'slider_images_form.html', {'form': slider_images_form})





# def services(request):
    # package_products = Package_products.objects.all()
    # packages = Packages.objects.all()
    # product_categorys = Product_categorys.objects.all()
    # product_package_price_historys = Product_package_price_historys.objects.all()
    # products = Products.objects.all()

    # context = {'package_products': package_products, 'packages': packages, 'product_categorys': product_categorys,
    #            'product_package_price_historys': product_package_price_historys, 'products': products}
    # return render(request, 'service.html', context)


def package_products(request):
    package_products = Package_products.objects.all()

    context = {'package_products': package_products}
    return render(request, 'package_products.html', context)


def package_products_form(request):
    package_products_form = Package_productsForm(request.POST or None, request.FILES or None)
  
    
    if package_products_form.is_valid():
        package_products_form.save()
        return HttpResponseRedirect(reverse("tummyapp:package_products"))
    return render(request, 'package_products_form.html', {'form': package_products_form})


def packages(request):
    packages = Packages.objects.all()

    context = {'packages': packages}
    return render(request, 'packages.html', context)


def packages_form(request):
    packages_form = PackagesForm(request.POST or None)
    if packages_form.is_valid():
        packages_form.save()
        return HttpResponseRedirect(reverse("tummyapp:packages"))
    return render(request, 'packages_form.html', {'form': packages_form})


def product_categorys(request):
    product_categorys = Product_categorys.objects.all()

    context = {'product_categorys': product_categorys}
    return render(request, 'product_categorys.html', context)


def product_categorys_form(request):
    product_categorys_form = Product_categorysForm(request.POST or None)
    if product_categorys_form.is_valid():
        product_categorys_form.save()
        return HttpResponseRedirect(reverse("tummyapp:product_categorys"))
    return render(request, 'product_categorys_form.html', {'form': product_categorys_form})


def product_package_price_historys(request):
    product_package_price_historys = Product_package_price_historys.objects.all()

    context = {'product_package_price_historys': product_package_price_historys}
    return render(request, 'product_package_price_historys.html', context)


def product_package_price_historys_form(request):
    product_package_price_historys_form = Product_package_price_historysForm(
        request.POST or None)
    if product_package_price_historys_form.is_valid():
        product_package_price_historys_form.save()
        return HttpResponseRedirect(reverse("tummyapp:product_package_price_historys"))
    return render(request, 'product_package_price_historys_form.html', {'form': product_package_price_historys_form})


def product_price_historys(request):
    product_price_historys = Product_price_historys.objects.all()

    context = {'product_price_historys': product_price_historys}
    return render(request, 'product_price_historys.html', context)



def product_price_historys_form(request):
    product_price_historys_form = Product_price_historysForm(
        request.POST or None, request.FILES or None)
    if product_price_historys_form.is_valid():
        product_price_historys_form.save()
        return HttpResponseRedirect(reverse("tummyapp:product_price_historys"))
    return render(request, 'product_price_historys_form.html', {'form': product_price_historys_form})


def products(request):
    products = Products.objects.all()

    context = {'products': products}
    return render(request, 'products.html', context)


def products_form(request):
    products_form = ProductsForm(request.POST or None, request.FILES)
    if products_form.is_valid():
        products_form.save()
        return HttpResponseRedirect(reverse("tummyapp:products"))
    return render(request, 'package_order_form.html', {'form': products_form})


# def useraccount(request):
#     blog_posts = Blog_posts.objects.all()
#     email_otps = Email_otps.objects.all()
#     profiles = Profiles.objects.all()
#     user_notifications = User_notifications.objects.all()
#     users = Users.objects.all()

#     context = {'blog_posts': blog_posts, 'email_otps': email_otps,
#                'profiles': profiles, 'user_notifications': user_notifications, 'users': users}
#     return render(request, 'useraccount.html', context)


def blog_posts(request):
    blog_posts = Blog_posts.objects.all()

    context = {'blog_posts': blog_posts}
    return render(request, 'blog_posts.html', context)


def blog_posts_form(request):
    blog_posts_form = Blog_postsForm(request.POST or None, request.FILES)
    if blog_posts_form.is_valid():
        blog_posts_form.save()
        return HttpResponseRedirect(reverse("tummyapp:blog_posts"))
    return render(request, 'package_order_form.html', {'form': blog_posts_form})


def email_otps(request):
    email_otps = Email_otps.objects.all()

    context = {'email_otps': email_otps}
    return render(request, 'email_otps.html', context)


def email_otps_form(request):
    email_otps_form = Email_optsForm(request.POST or None)
    if email_otps_form.is_valid():
        email_otps_form.save()
        return HttpResponseRedirect(reverse("tummyapp:email_otps"))
    return render(request, 'package_order_form.html', {'form': email_otps_form})


def profiles(request):
    profiles = Profiles.objects.all()

    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


def profiles_form(request):
    profiles_form = ProfilesForm(request.POST or None)
    if profiles_form.is_valid():
        profiles_form.save()
        return HttpResponseRedirect(reverse("tummyapp:profiles"))
    return render(request, 'package_order_form.html', {'form': profiles_form})


def user_notifications(request):
    user_notifications = User_notifications.objects.all()

    context = {'user_notifications': user_notifications}
    return render(request, 'user_notifications.html', context)


def user_notifications_form(request):
    user_notifications_form = User_notificationsForm(request.POST or None)
    if user_notifications_form.is_valid():
        user_notifications_form.save()
        return HttpResponseRedirect(reverse("tummyapp:user_notifications"))
    return render(request, 'package_order_form.html', {'form': user_notifications_form})


def users(request):
    users = Users.objects.all()

    context = {'users': users}
    return render(request, 'users.html', context)


def users_form(request):
    users_form = UsersForm(request.POST or None)
    if users_form.is_valid():
        users_form.save()
        return HttpResponseRedirect(reverse("tummyapp:users"))
    return render(request, 'package_order_form.html', {'form': users_form})
