from django.shortcuts import render

from django.http import HttpResponseForbidden
# Create your views here.
# listings/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, UserProfile,CarForSale, CarForRent, Brand, OilType

from .forms import CarForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserProfileForm,CarForSaleForm,CarForRentForm
from .forms import ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'listings/register.html', {'form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('car_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'listings/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required

def profile_view(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None  # Handle the case where the profile does not exist

    # Get the user's cars for sale and for rent
    cars_for_sale = CarForSale.objects.filter(owner=user, is_for_sale=True)
    cars_for_rent = CarForRent.objects.filter(owner=user, is_for_rent=True)
    # print('*****************')
    # print('*****************')
    # print('*****************')
    # print("User Profile:", user_profile)
    # print("Cars for Sale:", cars_for_sale)
    # print("Cars for Rent:", cars_for_rent)
    # print('*****************')
    # print('*****************')
    # print('*****************')
    return render(request, 'listings/profile.html', {
        'user_profile': user_profile,
        'cars_for_sale': cars_for_sale,
        'cars_for_rent': cars_for_rent,
    })
   

def car_list(request):
    # Get filter values from the request
    name_query = request.GET.get('name', '')
    brand_query = request.GET.get('brand', '')
    year_query = request.GET.get('year', '')
    km_query = request.GET.get('km', '')
    oil_type_query = request.GET.get('oil_type', '')
    price_query = request.GET.get('price', '')

    # Start with all cars for sale
    cars_for_sale = CarForSale.objects.all()

    # Apply filters if values are provided
    if name_query:
        cars_for_sale = cars_for_sale.filter(name__icontains=name_query)
    
    if brand_query:
        cars_for_sale = cars_for_sale.filter(brand__name=brand_query)
    
    if year_query:
        cars_for_sale = cars_for_sale.filter(model_year=year_query)
    
    if km_query:
        try:
            km = int(km_query)
            if km == 200001:
                cars_for_sale = cars_for_sale.filter(km_driven__gt=200000)
            else:
                cars_for_sale = cars_for_sale.filter(km_driven__lte=km)
        except ValueError:
            pass  # Ignore invalid input

    if oil_type_query:
        cars_for_sale = cars_for_sale.filter(oil_type__type=oil_type_query)
    
    if price_query:
        try:
            price = int(price_query)
            if price == 100001:
                cars_for_sale = cars_for_sale.filter(price__gt=100000)
            else:
                cars_for_sale = cars_for_sale.filter(price__lte=price)
        except ValueError:
            pass  # Ignore invalid input

    # Fetch all cars for rent without filtering
    cars_for_rent = CarForRent.objects.all()

    # Fetch choices for dropdown filters
    brands = Brand.objects.all()
    years = CarForSale.objects.values_list('model_year', flat=True).distinct().order_by('-model_year')
    oil_types = OilType.objects.all()
    print('***************')
    print('***************')
    print(brands,years,oil_types)
    print('***************')
    print('***************')
    return render(request, 'listings/car_list.html', {
        'cars_for_sale': cars_for_sale,
        'cars_for_rent': cars_for_rent,
        'brands': brands,
        'years': years,
        'oil_types': oil_types,
    })


def update_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print('************************')
            print('************************')
            
            print('************************')
            print('************************')
            return redirect('profile')  # Adjust this to your profile page URL name
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'listings/update_profile.html', {'form': form})
def seller_profile_view(request, profile_id):
    user_profile = get_object_or_404(UserProfile, id=profile_id)
    return render(request, 'listings/profile.html', {'user_profile': user_profile})

from django.shortcuts import render, get_object_or_404, redirect
from .models import CarForSale, CarForRent
from .forms import CarForSaleForm, CarForRentForm

from django.shortcuts import render
from .models import CarForSale, CarForRent

# def car_list(request):
#     brand_query = request.GET.get('brand', '')
#     price_query = request.GET.get('price', '')

#     # Filter cars for sale based on search criteria
#     cars_for_sale = CarForSale.objects.all()
    
#     if brand_query:
#         # Adjust 'name' based on the field in the Brand model that stores the brand name
#         cars_for_sale = cars_for_sale.filter(brand__name__icontains=brand_query)
    
#     if price_query:
#         try:
#             price = float(price_query)  # Using float to match DecimalField
#             cars_for_sale = cars_for_sale.filter(price__lte=price)
#         except ValueError:
#             pass  # Ignore invalid price input

#     # Fetch all cars for rent without filtering
#     cars_for_rent = CarForRent.objects.all()

#     return render(request, 'listings/car_list.html', {
#         'cars_for_sale': cars_for_sale,
#         'cars_for_rent': cars_for_rent,
#     })
@login_required
def car_combined_detail(request, pk):
    # Try to get the car from CarForSale, and if not found, try CarForRent
    car = get_object_or_404(CarForSale, pk=pk)
    
    # If the car is found in CarForSale, display it
    if car:
        return render(request, 'listings/car_detail.html', {'car': car})
    
    # Otherwise, check in CarForRent
    car = get_object_or_404(CarForRent, pk=pk)
    return render(request, 'listings/car_detail.html', {'car': car})



def car_sale_create(request):
    if request.method == 'POST':
        form = CarForSaleForm(request.POST, request.FILES)
        if form.is_valid():
            car_for_sale = form.save(commit=False)
            car_for_sale.owner = request.user  # Assign the current user as the owner
            car_for_sale.save()
            return redirect('car_list')  # Adjust the redirect URL as needed
    else:
        form = CarForSaleForm()
    return render(request, 'listings/car_form.html', {'form': form})
def car_rent_create(request):
    if request.method == 'POST':
        form = CarForRentForm(request.POST, request.FILES)
        if form.is_valid():
            car_for_rent = form.save(commit=False)
            car_for_rent.owner = request.user  # Assign the current user as the owner
            car_for_rent.save()
            return redirect('car_list')  # Adjust the redirect URL as needed
    else:
        form = CarForRentForm()
    return render(request, 'listings/car_form.html', {'form': form})
@login_required
def rent_car_page(request):
    brand_query = request.GET.get('brand', '')
    price_per_day_query = request.GET.get('price_per_day', '')

    # Filter cars for rent based on search criteria
    cars_for_rent = CarForRent.objects.all()
    
    if brand_query:
        # Adjust 'name' based on the field in the Brand model that stores the brand name
        cars_for_rent = cars_for_rent.filter(brand__name__icontains=brand_query)
    
    if price_per_day_query:
        try:
            price_per_day = float(price_per_day_query)
            cars_for_rent = cars_for_rent.filter(price_per_day__lte=price_per_day)
        except ValueError:
            pass  # Ignore invalid price input

    return render(request, 'listings/rent_car_page.html', {
        'cars_for_rent': cars_for_rent,
    })
def rent_car_detail(request, pk):
    car = get_object_or_404(CarForRent, pk=pk)
    return render(request, 'listings/rent_car_detail.html', {'car': car})
@login_required
def edit_rental_car(request, pk):
    car = get_object_or_404(CarForRent, pk=pk)

    # Check if the logged-in user is the owner of the car
    if car.owner != request.user:
        return HttpResponseForbidden("You are not allowed to edit this car.")

    if request.method == 'POST':
        form = CarForRentForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('rent_car_detail', pk=car.pk)
    else:
        form = CarForRentForm(instance=car)
    
    return render(request, 'listings/edit_rental_car.html', {'form': form, 'car': car})
@login_required
def delete_rental_car(request, pk):
    car = get_object_or_404(CarForRent, pk=pk)

    # Check if the logged-in user is the owner of the car
    if car.owner != request.user:
        return HttpResponseForbidden("You are not allowed to delete this car.")

    if request.method == 'POST':
        car.delete()
        return redirect('rent_car_page')
    
    # Optional: Render a confirmation page (if you want)
    return render(request, 'listings/car_confirm_delete.html', {'car': car})
def car_combined_edit(request, pk):
    car = get_object_or_404(CarForSale, pk=pk)
    if request.method == 'POST':
        form = CarForSaleForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_combined_detail', pk=car.pk)
    else:
        form = CarForSaleForm(instance=car)
    return render(request, 'listings/car_form.html', {'form': form})

def car_combined_delete(request, pk):
    car = get_object_or_404(CarForSale, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'listings/car_confirm_delete.html', {'car': car})
