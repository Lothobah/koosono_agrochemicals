from django.shortcuts import render
from django.db.models.fields import files
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import datetime 
from django.db.models import Sum
from django.contrib import admin, messages
from django.urls.conf import path
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from agrochemicals_management_system.forms import AddProductForm,UpdateProductForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.generic import ListView
import json
from agrochemicals_management_system.models import *
from django.core.mail import send_mail 
from django.contrib.auth.models import auth
from django.contrib import admin, messages

#def admin_homepage(request):
    #products = Products.objects.all() 
    #return render(request, "admin_templates/admin_homepage.html",{"products":products})
def add_product(request):
    form = AddProductForm()
    return render(request, "admin_templates/add_product.html",{"form":form})
def add_product_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data["product_name"]
            cost_price = form.cleaned_data["cost_price"]
            

            stock = form.cleaned_data["stock"]

            #product_pic = request.FILES['product_pic']
            #fs = FileSystemStorage()
            #filename = fs.save(product_pic.name, product_pic)
            #product_pic_url = fs.url(filename)
            #try: 
            profit = 0
            total_profit_on_stock_sold = 0
            stock_sold = 0
            add_new_stock = 0
            total_cost_price = 0
            overall_cost_price = 0
            overall_selling_price = 0
            new_stock = 0 
            cost_price = float(request.POST.get("cost_price"))
            selling_price = float(request.POST.get("selling_price"))
            stock = float(request.POST.get("stock"))
            profit = selling_price - cost_price
            new_stock+=stock - stock_sold
            total_stock_sold = 0 
            total_stock_sold+=stock_sold
            amount_of_stock_sold = stock_sold * selling_price
            total_cost_price = cost_price * new_stock
            total_selling_price = stock * selling_price
            total_profit_per_each_stock = new_stock * profit
            total_profit_on_stock_sold = stock_sold * profit
            total_profit_on_stock_sold = "{:,.2f}".format(total_profit_on_stock_sold)
            total_profit_on_overall_sales = total_stock_sold * profit
                
            product_model = Products(product_name=product_name,cost_price=cost_price,
            stock=stock,stock_sold=stock_sold, total_cost_price=total_cost_price,
            new_stock=new_stock,selling_price=selling_price,profit=profit,total_selling_price=total_selling_price,
            total_profit_on_stock_sold=total_profit_on_stock_sold,overall_selling_price=overall_selling_price,
            total_profit_per_each_stock=total_profit_per_each_stock,
            overall_cost_price=overall_cost_price,amount_of_stock_sold=amount_of_stock_sold,
            add_new_stock=add_new_stock, total_stock_sold=total_stock_sold,
            total_profit_on_overall_sales=total_profit_on_overall_sales)
            product_model.save()
                 
            messages.success(
                request, message="Product added successfully.")

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #except:
                #messages.error(request,
                #" Something went wrong!! ")
                #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = AddProductForm(request.POST)
            return render(request, "admin_templates/add_product.html", {"form": form})
def products(request):
    products_unsorted = Products.objects.all()
    products = products_unsorted.order_by("product_name")
    total_amount_of_stock_sold = products.aggregate(
        TOTAL=Sum('amount_of_stock_sold'))['TOTAL']
    overall_cost_price = products.aggregate(TOTAL=Sum('total_cost_price'))['TOTAL']
    overall_selling_price = products.aggregate(
        TOTAL=Sum('total_selling_price'))['TOTAL']
    overall_profit_from_sales = products.aggregate(TOTAL=Sum('total_profit_on_stock_sold'))['TOTAL']
    total_profit_on_overall_sales = products.aggregate(
        TOTAL=Sum('total_profit_on_overall_sales'))['TOTAL']
    try:
        overall_cost_price = "{:,.2f}".format(overall_cost_price)
        overall_selling_price = "{:,.2f}".format(overall_selling_price)
        overall_profit_from_sales = "{:,.2f}".format(overall_profit_from_sales)
        total_amount_of_stock_sold = "{:,.2f}".format(total_amount_of_stock_sold)
        total_profit_on_overall_sales = "{:,.2f}".format(total_profit_on_overall_sales)
        total_profit_on_stock_sold = "{:,.2f}".format(total_profit_on_stock_sold)
    except:
        pass
    return render(request, "admin_templates/admin_homepage.html",{"products":products,
    "overall_cost_price":overall_cost_price,"overall_selling_price":overall_selling_price,
    "overall_profit_from_sales":overall_profit_from_sales,
    "total_amount_of_stock_sold":total_amount_of_stock_sold,
    "total_profit_on_overall_sales":total_profit_on_overall_sales})
def update_product(request, product_id):
    request.session['product_id'] = product_id
    product = Products.objects.get(id=product_id)
    form = UpdateProductForm()
    form.fields['product_name'].initial = product.product_name
    form.fields['cost_price'].initial = product.cost_price
    form.fields['selling_price'].initial = product.selling_price
    form.fields['new_stock'].initial = product.new_stock
    form.fields['total_stock_sold'].initial = product.total_stock_sold
    #form.fields['stock_sold'].initial = product.stock_sold
    #form.fields['stock'].initial = product.stock
    return render(request, "admin_templates/update_product.html",{"form":form,
    "product":product})

def update_product_save(request):
    if request.method != "POST":
            return HttpResponse("<h2>Method not allowed</h2>")
    else:
        product_id = request.session.get("product_id")
        form = UpdateProductForm(request.POST, request.FILES)
        if form.is_valid():
            #try:
            product_name = form.cleaned_data["product_name"]
            cost_price = float(form.cleaned_data["cost_price"])
            selling_price = float(form.cleaned_data["selling_price"])
                
                
            stock = float(form.cleaned_data["stock"])
            stock_sold = float(form.cleaned_data["stock_sold"])
            new_stock = float(form.cleaned_data["new_stock"])
            total_stock_sold = float(form.cleaned_data["total_stock_sold"])
            
            total_stock_sold = total_stock_sold + stock_sold   
                
            #try:
                
            profit = 0
            total_profit_on_stock_sold = 0
            #stock_sold = 0
            total_cost_price = 0
            overall_cost_price = 0
            overall_selling_price = 0
            #new_stock = 0
            add_new_stock = 0 
            #cost_price = float(request.POST.get("cost_price"))
            #selling_price = float(request.POST.get("selling_price"))
            #stock = float(request.POST.get("stock"))
            #new_stock = float(request.POST.get("new_stock")) 
            profit = selling_price - cost_price
            new_stock+=stock - stock_sold
            #stock = new_stock - stock_sold
            amount_of_stock_sold = stock_sold * selling_price
            total_cost_price = cost_price * new_stock
            total_selling_price = new_stock * selling_price
            total_profit_per_each_stock = new_stock * profit
            total_profit_on_stock_sold = stock_sold * profit
            total_profit_on_overall_sales = total_stock_sold * profit
            product = Products.objects.get(id=product_id)    
            product.product_name = product_name
            product.cost_price = cost_price
            product.stock = stock 
            product.add_new_stock = add_new_stock
            product.new_stock = new_stock
            product.stock_sold = stock_sold
            product.selling_price = selling_price
            product.total_stock_sold = total_stock_sold 
            product.total_cost_price = total_cost_price
            product.total_profit_on_stock_sold = total_profit_on_stock_sold
            product.total_profit_per_each_stock = total_profit_per_each_stock
            product.total_selling_price = total_selling_price
            product.overall_cost_price = overall_cost_price
            product.overall_selling_price = overall_selling_price
            product.amount_of_stock_sold = amount_of_stock_sold 
            product.total_profit_on_overall_sales = total_profit_on_overall_sales
            my_date = datetime.date.today()
            updated_at = my_date.strftime("%a. %b %d, %Y")
            product.updated_at = updated_at 
            
            product.save()
            messages.success(request, "Stock updated successfully.")
            return HttpResponseRedirect(reverse("update_product", kwargs={"product_id": product_id}))
            #except:
                #return HttpResponseRedirect(reverse("update_product", kwargs={"product_id":product_id}))
        else:
            #form = UpdateProductForm(request.POST)
            #product = Products.objects.get(id=product_id)
            return render(request, "admin_templates/update_product.html", {"form":form,"id": product_id,
            "total_stock_sold":total_stock_sold})


def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "admin_templates/admin_profile.html", {"user": user})


def edit_admin_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        #username = request.POST.get("username")
        #email = request.POST.get("email")
        #try:
        custom_user = CustomUser.objects.get(id=request.user.id)
        custom_user.first_name = first_name
        custom_user.last_name = last_name
        #custom_user.email = email
        #custom_user.username = username
        if password != None and password != "":
            custom_user.set_password(password)

        custom_user.save()
        messages.success(request, "Your profile has been updated.")
        return HttpResponseRedirect(reverse("admin_profile"))
        #except:
        #messages.error(request, "Error in editing profile")
        #return HttpResponseRedirect(reverse("admin_profile"))
