# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.car_list, name='car_list'),
#     path('car/<int:pk>/', views.car_detail, name='car_detail'),

#     # Combined view for Car For Sale and Car For Rent
#     path('cars/', views.car_combined_list, name='car_combined_list'),
#     path('cars/<int:pk>/', views.car_combined_detail, name='car_combined_detail'),
#     path('cars/add/', views.car_combined_create, name='car_combined_create'),
#     path('cars/<int:pk>/edit/', views.car_combined_edit, name='car_combined_edit'),
#     path('cars/<int:pk>/delete/', views.car_combined_delete, name='car_combined_delete'),

#     # Specific URLs for car for sale
#     # path('cars/for-sale/', views.car_for_sale_list, name='car_for_sale_list'),
#     # path('cars/for-rent/', views.car_for_rent_list, name='car_for_rent_list'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_combined_detail, name='car_combined_detail'),
    path('car/new/', views.car_sale_create, name='car_sale_create'),
    path('car/new/rent', views.car_rent_create, name='car_rent_create'),
    path('car/<int:pk>/edit/', views.car_combined_edit, name='car_combined_edit'),
    path('car/<int:pk>/delete/', views.car_combined_delete, name='car_combined_delete'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('rent/', views.rent_car_page, name='rent_car_page'),
    path('rent/details/<int:pk>/', views.rent_car_detail, name='rent_car_detail'),
    path('profile/<int:profile_id>/', views.seller_profile_view, name='seller_profile'),
    path('rental_car/edit/<int:pk>/', views.edit_rental_car, name='edit_rental_car'),
    path('rental_car/delete/<int:pk>/', views.delete_rental_car, name='delete_rental_car'),
]


