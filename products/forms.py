from django import forms
from .models import Review, Order



class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review']




class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ['user', 'items', 'being_delivered', 'received', 'slug']
		widgets = {
		'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}),
		'company_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Company Name'}),
		'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
		'postal_code' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Zip/Postal Code'}),
		'country' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Country'}),
		'state' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'State'}),
		'phone_number' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
		'shipping_address' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Shipping Address'}),
		'billing_address' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Billing Address'}),
		'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Note about your Order'}),
		}


