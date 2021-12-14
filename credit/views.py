from django.shortcuts import render,redirect
from credit.models import Credit
# Create your views here.
def debits(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    debit=Credit.objects.filter(email=request.user,transaction_type='debit')
    return render(request,'debits.html',{'debit':debit})

def credits(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    credit=Credit.objects.filter(email=request.user,transaction_type='credit')
    return render(request,'credits.html',{'credit':credit})

def transactions(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    transaction=Credit.objects.filter(email=request.user)
    return render(request,'alltransactions.html',{'transaction':transaction})