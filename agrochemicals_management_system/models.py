from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"),(2, "Staff"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    selling_price = models.DecimalField(max_digits=15, decimal_places=2)
    total_selling_price = models.DecimalField(max_digits=15, decimal_places=2)
    overall_selling_price = models.DecimalField(max_digits=15, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit_per_each_stock = models.DecimalField(max_digits=15, decimal_places=2)
    total_profit_on_stock_sold = models.DecimalField(max_digits=15, decimal_places=2)
    total_profit_on_overall_sales = models.DecimalField(max_digits=17, decimal_places=2)
    total_cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    overall_cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.IntegerField(default=0, blank=True, null=True)
    stock_sold = models.IntegerField(default=0, blank=True, null=True) 
    total_stock_sold = models.IntegerField(blank=True, null=True) 
    add_new_stock = models.IntegerField()
    amount_of_stock_sold = models.DecimalField(max_digits=20, decimal_places=2)
    new_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.CharField(max_length=80)

