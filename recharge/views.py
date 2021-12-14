from django.contrib import messages
from django.shortcuts import render,redirect
from django.conf import settings
import datetime
from django.views.decorators.csrf import csrf_exempt
import razorpay
from app.models import User
from credit.models import Credit
from recharge.models import Recharge


# Create your views here.
def recharge(request):    
    if(not request.user.is_authenticated):
        return redirect('/')
    return render(request,"interface.html")

def load_raz(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    if(request.method=='POST'):
        user=User.objects.get(email=request.user)
        return render(request,"raz_con.html",{'amountp':str(int(request.POST['amount'])*100),'amountr':request.POST['amount'],'name':user.first_name+" "+user.last_name,'email':request.user,'RAZORPAY_ID':settings.RAZORPAY_ID})
    else:
        return render(request,"razorpay.html")

@csrf_exempt
def razcon(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    if(request.method=='POST'):
        DATA = {
        "amount": int(request.POST['amount'])*100,
        "currency": "INR",
        "payment_capture": "1",
        }
        client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_KEY))
        payment=client.order.create(data=DATA)
        user=User.objects.get(email=request.POST['email'])
        user.credits+=int(request.POST['amount'])
        user.save()
        
        order=Recharge()
        order.payment_id=payment['id']
        order.email=request.POST['email']
        order.amount=request.POST['amount']
        order.paid_at=datetime.datetime.now()
        order.save()

        credit=Credit()
        credit.payment_id=payment['id']
        credit.email=request.POST['email']
        credit.amount=request.POST['amount']
        credit.transaction_type='credit'
        credit.paid_at=datetime.datetime.now()
        credit.valid_upto=datetime.datetime.now() + datetime.timedelta(30)
        credit.save()
        return redirect('success')
    else:
        return render(request,"raz_con.html")
def check_credits(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    user=User.objects.get(email=request.user)
    if(user.credits>=int(request.POST['amount'])):
        user.credits-=int(request.POST['amount'])
        user.save()
        return True
    return False
def spend_credits(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    if(check_credits(request)):
        credit=Credit()
        credit.email=request.user
        credit.amount=request.POST['amount']
        credit.transaction_type='debit'
        credit.paid_at=datetime.datetime.now()
        credit.save()
        messages.info(request,"Debit Successful")
    else:
        messages.info(request,"Insufficient Funds..Please Recharge")
    return redirect('index')
def success(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    return render(request,"success.html")