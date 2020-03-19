from django.shortcuts import render,redirect
from .forms import *
from django.forms import inlineformset_factory
from .models import *
from django.http import HttpResponse
from num2words import num2words
# Create your views here.
def showall(request):
    return render(request,'billing/show.html')

def create(request):
    form=BillingForm()
    if request.method=='POST':
        form=BillingForm(request.POST)
        if form.is_valid():
            invoice=form.cleaned_data.get('invoice')
            ins=form.save()
            amt=Amount.objects.create(invoice=ins)#create invoiec
            return redirect('/paresh/product/'+str(invoice))
    context={
        'form':form
    }
    return render(request,'billing/create.html',context)

def calproduct(request,pk):
    g=0#gst
    disc=0#discount
    st=0#subtotal
    ft=0#finaltotal
    w=str()
    
    ProductsFormSet=inlineformset_factory(Billing,Products,fields='__all__',extra=3)
    invoice=Billing.objects.get(invoice=pk)
    amtdata=Amount.objects.get(invoice=invoice)
    print('FOUND'*50)
    print(amtdata)
    g=amtdata.gst
    disc=amtdata.discount
    st=amtdata.sub_total
    ft=amtdata.total
    w=amtdata.words
    amtform=AmountForm(instance=invoice)
    formset=ProductsFormSet(instance=invoice)
    if request.method=='POST':
        amtform=AmountForm(request.POST,instance=invoice)
        formset=ProductsFormSet(request.POST,instance=invoice)
        if (formset.is_valid() and amtform.is_valid()):
            print('inside'*50) 
            gst=request.POST.get("gst")
            dis=request.POST.get("dis")
            Amount.objects.update(gst=gst,discount=dis)
            formset.save()
            return redirect('/paresh/calamount/'+str(pk))
    context={
        'formset':formset,
        'amtform':amtform,
        'inv':pk,'g':g,'disc':disc,'st':st,'ft':ft,'w':w,
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
    gst=0
    dis=0
    subtotal=[]
    stot=0
    rate=[]
    qty=[]
    w=str()
    invoice=Billing.objects.get(invoice=pk)
    data=Products.objects.filter(invoice=pk)
    #up=Amount.objects.get(invoice=invoice)
    amtdata=Amount.objects.filter(invoice=pk)
    for i in amtdata:
        gst=i.gst
        dis=i.discount
    print('**'*50)
    for i in data:
        qty.append(i.quantity)
        rate.append(i.rate)
    for i in range(len(data)):
        subtotal.append(rate[i]*qty[i])
    stot=round(sum(subtotal))
    print('subtotal',stot)
    print('gst',gst)
    print('discount',dis)
    total=stot+(gst/100)*stot
    if dis>0:
        total=total-total*(dis/100)
    print('total',total)
    w=str(num2words(total)).title()
    print('words:',w)
    print('**'*50)
    amtdata.update(total=total,sub_total=stot,words=w)
    #return HttpResponse('testing')
    return redirect('/paresh/product/'+str(pk))
    # amtdata=Amount.objects.get(invoice=invoice)
    #         print('**'*50)
    #         g=amtdata.gst
    #         disc=amtdata.discount
    #         st=amtdata.sub_total
    #         ft=amtdata.total
    #         w=amtdata.words
    #         print('**'*50)

    




















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
