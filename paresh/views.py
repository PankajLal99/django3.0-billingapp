from django.shortcuts import render,redirect
from .forms import *
from django.forms import inlineformset_factory
from .models import *
from django.http import HttpResponse
# Create your views here.
def showall(request):
    return render(request,'billing/show.html')

def create(request):
    form=BillingForm()
    if request.method=='POST':
        form=BillingForm(request.POST)
        if form.is_valid():
            invoice=form.cleaned_data.get('invoice')
            form.save()
            return redirect('/paresh/product/'+str(invoice))
    context={
        'form':form
    }
    return render(request,'billing/create.html',context)

def calproduct(request,pk):
    ProductsFormSet=inlineformset_factory(Billing,Products,fields='__all__',extra=5)
    invoice=Billing.objects.get(invoice=pk)
    formset=ProductsFormSet(instance=invoice)
    if request.method=='POST':
        formset=ProductsFormSet(request.POST,instance=invoice)
        print(formset)
        if formset.is_valid():
            print('hey')
            formset.save()
            return redirect('/paresh/calamount/'+str(pk))
           
    context={
        'formset':formset,
        'inv':pk,
    }
    return render(request,'billing/billing.html',context)


 # print("**"*50)
            # cal=formset.cleaned_data
            # print(cal)
            # tot=sums(cal)
            # print(tot)
            # gst=request.POST.get("gst","0.0")
            # dis=request.POST.get("dis","0.0")
            # stotal=request.POST.get("sub","0.0")
            # total=request.POST.get("tot","0.0")
   
def calamount(request,pk):
    total=0
    subtotal=0
    rate=[]
    qty=[]
    data=Products.objects.filter(invoice=pk)
    print('**'*50)
    for i in data:
        print(i.product)
    print('**'*50)
    return HttpResponse("Testing")

    




















# def sums(calculation):
#     item_total=[]
#     rates=[]
#     qty=[]
#     for i in range(len(calculation)):
#         for j in calculation[i]:
#             if j=='rates':
#                 rates.append((calculation[i][j]))
#             elif j=='quantity':
#                 qty.append((calculation[i][j]))
#     for i in range(len(rates)):
#         ad=rates[i]*qty[i]
#         item_total.append(ad)

#     return(sum(item_total))
