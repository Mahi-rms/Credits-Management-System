from django.contrib import admin
from django.urls import path
from credit import views

urlpatterns = [
    path('debits',views.debits,name="debits"),
    path('credits',views.credits,name="credits"),
    path('transactions',views.transactions,name="transactions"),
]