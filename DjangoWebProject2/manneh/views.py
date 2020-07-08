from django.shortcuts import render

# Create your views here.
def manneh(request):
    context= {}
    return render(request,'manneh/index.html',context)