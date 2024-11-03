# # Create your models here.

# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)
#     location = models.CharField(max_length=255)
#     location_link = models.URLField(blank=True, null=True)  # Link to Google Maps or location URL
#     profile_picture = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

# class Car(models.Model):
#     owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="cars")
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     year = models.IntegerField()
#     kilometers_driven = models.IntegerField()
#     mileage = models.DecimalField(max_digits=5, decimal_places=2)
#     is_available = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title



# # 1. OilType Model
# class OilType(models.Model):
#     type = models.CharField(max_length=50)  # e.g., petrol, diesel, electric

#     def __str__(self):
#         return self.type

# # 2. Brand Model
# class Brand(models.Model):
#     name = models.CharField(max_length=100)  # e.g., Toyota, Honda, etc.

#     def __str__(self):
#         return self.name

# # 3. CarForSale Model
# class CarForSale(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)  # Car name
#     model_year = models.IntegerField()
#     km_driven = models.IntegerField()
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)
#     accidental_background = models.BooleanField(default=False)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     mileage = models.DecimalField(max_digits=5, decimal_places=2)
#     front_image = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
#     leftside_img = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
#     rightside_img = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
#     back_image = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
#     registration_number = models.CharField(max_length=100)
#     insurance_end_date = models.DateField()
#     ownership_type = models.CharField(max_length=50)  # e.g., 1st, 2nd, 3rd owner
#     created_date = models.DateField(auto_now_add=True)
#     created_time = models.TimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} ({self.model_year}) - {self.brand.name}"

# # 4. CarForRent Model
# class CarForRent(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)  # Car name
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)
#     description = models.TextField()
#     price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
#     mileage = models.DecimalField(max_digits=5, decimal_places=2)
#     rent_car_image = models.ImageField(upload_to='media/cars_for_rent/', blank=True, null=True)
#     created_date = models.DateField(auto_now_add=True)
#     created_time = models.TimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} for rent - {self.brand.name}"


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    location_link = models.URLField(blank=True, null=True)  # Link to Google Maps or location URL
    profile_picture = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)

    def __str__(self):
        print(self.user.username)
        return f"{self.user.username}'s Profile"

from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="cars")
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    kilometers_driven = models.IntegerField()
    mileage = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_for_sale = models.BooleanField(default=False)  # New field to mark as for sale
    is_for_rent = models.BooleanField(default=False)  # New field to mark as for rent
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OilType(models.Model):
    type = models.CharField(max_length=50)  # e.g., petrol, diesel, electric

    def __str__(self):
        return self.type

class Brand(models.Model):
    name = models.CharField(max_length=100)  # e.g., Toyota, Honda, etc.

    def __str__(self):
        return self.name

class CarForSale(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE,related_name='cars_for_sale',null=True, blank=True)
    name = models.CharField(max_length=100)  # Car name
    model_year = models.IntegerField()
    km_driven = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)
    accidental_background = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=5, decimal_places=2)
    front_image = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
    leftside_img = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
    rightside_img = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
    back_image = models.ImageField(upload_to='media/cars_for_sale/', blank=True, null=True)
    registration_number = models.CharField(max_length=100)
    insurance_end_date = models.DateField()
    ownership_type = models.CharField(max_length=50)  # e.g., 1st, 2nd, 3rd owner
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    is_for_sale = models.BooleanField(default=False)  # New field to mark as for sale
    is_for_rent = models.BooleanField(default=False)  # New field to mark as for rent
    def __str__(self):
        return f"{self.name} ({self.model_year}) - {self.brand.name}"

class CarForRent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cars_for_rent',null=True, blank=True)
    name = models.CharField(max_length=100)  # Car name
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    oil_type = models.ForeignKey(OilType, on_delete=models.CASCADE)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=5, decimal_places=2)
    rent_car_image = models.ImageField(upload_to='media/cars_for_rent/', blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    is_for_sale = models.BooleanField(default=False)  # New field to mark as for sale
    is_for_rent = models.BooleanField(default=False)  # New field to mark as for rent
    def __str__(self):
        return f"{self.name} for rent - {self.brand.name}"
