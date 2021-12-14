from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from datetime import datetime
# Create your models here.
class CustomUserManager(BaseUserManager):
    '''def create_superuser(self,email,password,first_name,last_name,mobile,**extra):
        user=_create_user(email,password,first_name,last_name,mobile,**extra)
        return user

    def create_user(self,email,password,first_name,last_name,mobile,**extra):
        return _create_user(email,password,first_name,last_name,mobile,**extra)'''

    def create_user(self,email,password,first_name,last_name,mobile,**extra):
        if(not email):
            return ValueError("Email not Provided")
        if(not password):
            return ValueError("Password not Provided")

        extra.setdefault('is_staff',False)
        extra.setdefault('is_active',True)
        extra.setdefault('is_superuser',False)
        user=self.model(email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,first_name,last_name,mobile,**extra):
        if(not email):
            return ValueError("Email not Provided")
        if(not password):
            return ValueError("Password not Provided")
        extra.setdefault('is_staff',True)
        extra.setdefault('is_active',True)
        extra.setdefault('is_superuser',True)
        user=self.model(email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(primary_key=True,db_index=True,max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=12)
    credits=models.IntegerField(default=0)
    last_login=models.DateTimeField(auto_now=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['first_name','last_name','mobile']

    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"

'''class Authentication(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(db_index=True,max_length=255,unique=True)
    ph_number=models.CharField(max_length=12)
    password=models.CharField(max_length=255,default="12345")
    created_at=models.DateTimeField(blank=True)
    last_login=models.DateTimeField(auto_now=True)    
    loggedin_at=models.DateTimeField(default=datetime.now,blank=True)
    objects=models.Manager()
    '''