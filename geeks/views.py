from django.shortcuts import (render,HttpResponseRedirect,get_object_or_404)
from .forms import GeeksForm
from .models import GeeksModel
from .forms import ContactsForm
from .models import ContactsModel
from .models import LoginModel
##from .models import PaymentsForm
from .models import PaymentsModel1

def dummy(request):
    return render(request,'dummy.html')

def index(request):
    context={}
    form=GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,'index.html',context)
def login(request):
    return render(request,'login.html')
    

def update_view(request,id):
    context={}
    obj=get_object_or_404(GeeksModel, id = id)
    form=GeeksForm(request.POST or None,instance=obj )
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/geeks/"+id)
    context["form"]=form
    return render(request,"update_view.html",context)

def delete_view(request,id):
    context={}
    obj=get_object_or_404(GeeksModel, id = id)
    form=GeeksForm(request.POST or None,instance=obj )
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/geeks/list")
    return render(request,"delete_view.html",context)



def detail_view(request,id):
    context={}
    context["data"]=GeeksModel.objects.get(id = id)
    return render(request,"detail_view.html",context)

def contacts_create_view(request):
    context={}
    form=ContactsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,"contacts_create_view.html",context)

##def payment(request):
##    context={}
##    form=paymentsForm(request.POST or None)
##    if form.is_valid():
##        form.save()
##    context['form']=form
##    return render(request,"payment.html",context)

def payment(request):
    ##//write code from image
    if request.method=="POST":
        fullname=request.POST.get('fullname'),
        email=request.POST.get('email'),
        address=request.POST.get('address'),
        city=request.POST.get('city'),
        state=request.POST.get('state'),
        zipcode=request.POST.get('zipcode'),
        nameoncard=request.POST.get('nameoncard'),
        expmonth=request.POST.get('expmonth'),
        expyear=request.POST.get('expyear'),
        cvv=request.POST.get('cvv'),

        ob=payment(fullname=fullname,email=email,address=address,
                   city=city,state=state,zipcode=zipcode,nameoncar=nameoncard,
                   expmonth=expmonth,expyear=expyear,cvv=cvv)
        ob.save()
        print('data saved')
    return render(request,"payment.html")

def create_view(request):
    context={}
    form=GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,"create_view.html",context)
    
def list_view(request):
    context={}
    context["dataset"]=GeeksModel.objects.all()
    return render(request,"list_view.html",context)
