from django.shortcuts import render

# Create your views here.
def showall(request):
    return render(request,'billing/invoice.html')