from django.contrib import admin
from django.urls import path,include
from . import views
app_name='delivery'
urlpatterns = [
#path('register/',views.input,name='input'),
path('',views.main,name='main'),
path('register/',views.input,name='input'),
#path('register/damn/',views.main,name='main'),

#     URLS FOR EVERY RESTAURANT

path('pizzahut/',views.pizza,name='pizza'),
path('boston/',views.boston,name='boston'),
path('gelato/',views.gelato,name='gelato'),
path('pancake/',views.pancake,name='pancake'),
path('fatmans/',views.fatmans,name='fat'),
path('jimis/',views.jimis,name='jimi'),
path('melting/',views.melting,name='melt'),
path('orderplaced/',views.done,name="done"),
path('main/',views.main,name="back"),
#     PENDING!!



path('subway/',views.hotel1,name='subway'),
path('hotel/register/bill/',views.bill,name='bill')
# path('register/damn/hotel/',views.hotel,name='hotel_4'),
# path('register/damn/hotel/',views.hotel,name='hotel_4'),
# path('register/damn/hotel/',views.hotel,name='hotel_4'),
# path('register/damn/hotel/',views.hotel,name='hotel_4'),
# path('register/damn/hotel/',views.hotel,name='hotel_4'),
# path('register/damn/hotel/',views.hotel,name='hotel_4'),
]
