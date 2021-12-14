from django.contrib import admin
from django.urls import path
from recharge import views

urlpatterns = [
    path('recharge',views.recharge,name="recharge"),
    path('load_raz',views.load_raz,name="load_raz"),
    path('razcon',views.razcon,name="razcon"),
    path('success',views.success,name="success"),
    path('spend_credits',views.spend_credits,name='spend_credits')
]
