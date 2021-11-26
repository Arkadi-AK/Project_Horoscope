from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('types/', views.get_info_types, name='horoscope-types'),
    path('types/<str:zodiac_types>/', views.get_info_zodiac_types),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('', views.index, name='horoscope-main'),

]
