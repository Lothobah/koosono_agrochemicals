from django import forms
from django.forms import ChoiceField
#from Student_Management_System.HodViews import Courses
from agrochemicals_management_system.models import *
from django.forms import ModelForm
class ChoiceValidation(ChoiceField):  
    def validate(self, value):
        pass

class DateInput(forms.DateInput):  # class to print date in student form
    input_type = "date"

class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=70, label="Product Name:", required="required", widget=forms.TextInput(
        attrs={"class": "form-control", "autocomplete": "off","placeholder":"Enter product name"}))
    cost_price = forms.DecimalField(max_digits=15,required="required", decimal_places=2, label="Cost Price(GHS):", widget=forms.NumberInput(attrs={
        "class":"form-control","pattern":"[0-9]+","placeholder":"Enter product cost price, eg.20"
    }))
    selling_price = forms.DecimalField(max_digits=15,required="required",decimal_places=2, 
    label="Selling Price(GHS)", widget=forms.NumberInput(attrs={"class":"form-control","pattern":"[0-9]+",
    "placeholder":"Enter product selling price, eg.20"})
    )
    
    stock = forms.IntegerField(label="Product Quantity",required="required", widget=forms.TextInput(
        attrs={"class":"form-control","pattern":"[0-9]+","placeholder":"Enter Product quantity"}
    ))


class UpdateProductForm(forms.Form):
    product_name = forms.CharField(max_length=70, label="Product Name:", required="required", widget=forms.TextInput(
        attrs={"class": "form-control", "autocomplete": "off", "placeholder": "Enter product name"}))
    cost_price = forms.DecimalField(max_digits=15, required="required", decimal_places=2, label="Cost price(GHS):", widget=forms.NumberInput(attrs={
        "class": "form-control", "pattern": "[0-9]+", "placeholder": "Enter cost price, eg.20"
    }))
    selling_price = forms.DecimalField(max_digits=15, required="required", decimal_places=2, label="Selling price(GHS):", widget=forms.NumberInput(attrs={
        "class": "form-control", "pattern": "[0-9]+", "placeholder": "Enter selling price, eg.20"
    }))
    new_stock = forms.IntegerField(label="Stock Quantity:",initial=0,
    widget=forms.TextInput(  
        attrs={"class": "form-control","readonly":"readonly",
               "pattern": "[0-9]+", "placeholder": "Total Stocks" 
              }
    )) 
    total_stock_sold = forms.IntegerField(label="Total Stock Sold:", initial=0,
    widget=forms.TextInput(
        attrs={"class": "form-control", "readonly": "readonly",
                "pattern": "[0-9]+", "placeholder": "Total Stocks"
                }
                                   ))
    stock = forms.IntegerField(label="Enter New Stock:", required=False, 
    initial=0,widget=forms.TextInput(
        attrs={"class": "form-control",
               "pattern": "[0-9]+", "placeholder": "Please enter new stock"}
    ))
    stock_sold = forms.IntegerField(label="Stock sold", required=False,initial=0,   
    widget=forms.TextInput(  
        attrs={"class": "form-control",  
               "pattern": "[0-9]+", "placeholder": "Enter stock sold"}
    ))
