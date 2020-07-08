from django.shortcuts import render
from django.http import HttpResponseRedirect
from manneh.models import Manneh
from manneh.forms import MannehForm,RawMannehForm
# Create your views here.
def manneh(request):
    print(request.GET)
    print(request.POST)
    object = Manneh.objects.all()
    context= {
        'name':'john',
        'object': object,
        }
    return render(request,'manneh/index.html',context)

def mannehformview(request):
    if request.method == 'POST':
        m_forms = MannehForm(request.POST)
        if m_forms.is_valid():
            m_forms.save()    
            m_forms = MannehForm() # after saving clear form
    else:
        m_forms = MannehForm()

    context = {
           'form':m_forms
        }
    return render(request,'labeh.html',context)

##########   Getting form input 
def backend(request):

    labeh = request.POST.get('title')
    ls = request.GET.get('title')

    print(labeh)
    print(ls)
    return render(request,'labeh.html',{})

##############  Getting input and passing to DB..
def backend2(request):
    rawform = RawMannehForm()#get method....render by default.. 
    if request.method == 'POST':
        rawform = RawMannehForm(request.POST)
        if rawform.is_valid():
            Manneh.objects.create(**rawform.cleaned_data)
            print(rawform.cleaned_data)
            rawform = RawMannehForm()
    context = {
            'rawform':rawform
     }
   
    return render(request,'labeh.html',context)

############# Validation
def mannehformview2(request):
    if request.method == 'POST':
        m_forms = MannehForm(request.POST)
        if m_forms.is_valid():
            m_forms.save()    
            m_forms = MannehForm() # after saving clear form
    else:
        m_forms = MannehForm()

    context = {
           'form2':m_forms
        }
    return render(request,'labeh.html',context)