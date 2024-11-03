# # listings/forms.py
# from django import forms
# from .models import Car, UserProfile
# from .models import CarForSale, CarForRent
# from django.contrib.auth.models import User

# class CarForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ['title', 'description', 'price', 'year', 'kilometers_driven', 'mileage']


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['phone_number', 'location', 'location_link', 'profile_picture']


# class CarForSaleForm(forms.ModelForm):
#     class Meta:
#         model = CarForSale
#         fields = ['name', 'model_year', 'km_driven', 'brand', 'oil_type', 'accidental_background', 
#                   'description', 'price', 'mileage', 'front_image', 'leftside_img', 'rightside_img',
#                   'back_image', 'registration_number', 'insurance_end_date', 'ownership_type']

# class CarForRentForm(forms.ModelForm):
#     class Meta:
#         model = CarForRent
#         fields = ['name', 'brand', 'oil_type', 'description', 'price_per_day', 'mileage', 'rent_car_image']


from django import forms
from .models import Car, UserProfile, CarForSale, CarForRent
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'description', 'price', 'year', 'kilometers_driven', 'mileage']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','phone_number', 'location', 'location_link', 'profile_picture']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','phone_number', 'location', 'location_link', 'profile_picture']

class CarForSaleForm(forms.ModelForm):
    class Meta:
        model = CarForSale
        fields = [
            'name', 'model_year', 'km_driven', 'brand', 'oil_type', 'accidental_background', 
            'description', 'price', 'mileage', 'front_image', 'leftside_img', 'rightside_img',
            'back_image', 'registration_number', 'insurance_end_date', 'ownership_type'
        ]

class CarForRentForm(forms.ModelForm):
    class Meta:
        model = CarForRent
        fields = ['name', 'brand', 'oil_type', 'description', 'price_per_day', 'mileage', 'rent_car_image']
