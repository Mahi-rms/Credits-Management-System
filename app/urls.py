from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [    
    path('',views.landing,name="landing"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('logout',views.log_out,name="logout"),
    path('send_otp',views.send_otp,name="send_otp"),    
    path('verify_otp',views.verify_otp,name="verify_otp"),
    path('index',views.index,name="index"),
    path('profile',views.profile,name="profile"),
    path('user_details',views.user_details,name='user_details'),
]