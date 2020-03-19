from django.shortcuts import render,redirect
from .forms import calform,invform
from django.forms import inlineformset_factory
from .models import *
from django.http import HttpResponse
# Create your views here.
def createin(request):
    form=invform()
    if request.method=='POST':
        form=invform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'home.html',{'form':form})

def show(request):
    data=Invoi.objects.all()
    context={
        'data':data
    }
    return render(request,'show.html',context)

def cal(request,pk):
    tot=0
    OrderFormSet=inlineformset_factory(Invoi,Cal, fields=('a','b'),extra=8)
    key= Invoi.objects.get(id=pk)
    formset=OrderFormSet(instance=key)
    if request.method=='POST':
        formset=OrderFormSet(request.POST,instance=key)
        if formset.is_valid():
            calculation=formset.cleaned_data
            tot=sums(calculation)
            formset.save()

    context={
        'formset':formset,
        'total':tot,
        'inv':pk,
        }
    return render(request,'calculate.html',context)


def sums(calculation):
    item_total=[]
    rates=[]
    qty=[]
    for i in range(len(calculation)):
        for j in calculation[i]:
            if j=='a':
                rates.append((calculation[i][j]))
            elif j=='b':
                qty.append((calculation[i][j]))
    for i in range(len(rates)):
        ad=rates[i]*qty[i]
        item_total.append(ad)

    return(sum(item_total))

def r(request):
    return HttpResponse('LOOK URL')
