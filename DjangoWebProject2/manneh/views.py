from django.http import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from manneh.models import Manneh
from manneh.forms import MannehForm,RawMannehForm,PassingFormInstance


# Create your views here.
def manneh(request):
    print(request.GET)
    print(request.POST)
    object = Manneh.objects.all()# get list of object
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

#################
#Changing object in the database.. Editing 
def backend3(request):
   initial_data = {
       'surname':'This is my name'
       }
   obj = Manneh.objects.get(id=1)
   rawform = PassingFormInstance(request.POST or None, instance = obj )
   if rawform.is_valid():
       rawform.save()
   context = {
            'rawform':rawform
     }

   return render(request,'labeh.html',context)
##############################
#get data from database through URL id
def dynamic(request,myid):
    try:
        obj = Manneh.objects.get(id=myid)
    except Manneh.DoesNotExist:# handling missing object...
        raise Http404
    context = {
        'obj' : obj,
        'd_id':myid
        }
    return render(request,'labeh.html',context)

######################
#deleting object in database
def deleting(request,d_id):
    try:
        la = Manneh.objects.get(id=d_id)
        if request.method =='POST':
            la.delete()
            return redirect('../')#after del goto home
    except Manneh.DoesNotExist:# handling missing object...
        raise Http404
    context = {
       'la' : la,
       'd_id':d_id
        }
    return render(request,'labeh.html',context)

def labeh_list_view(request):
    query = Manneh.objects.all()
    context = {
        'labeh':query
        }
    return render(request,'manneh/lab.html',context)
