from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'title':'Blog',
        'home':'Welcome To Our Home page'
        }
    return render(request,'index.html',context)

def about(request):
    context={
        'title':'Blog',
        'about':'Welcome To Our About page'
        }
    return render(request,'about.html',context)