from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.template import RequestContext
from .models import Customer
from .forms import Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def pizza(request):
    return render(request,"delivery/pizza.html")

def boston(request):
    return render(request, "delivery/boston.html")

def gelato(request):
    return render(request, "delivery/gelato.html")

def pancake(request):
    return render(request, "delivery/pancake.html")

def fatmans(request):
    return render(request, "delivery/fatmans.html")

def jimis(request):
    return render(request, "delivery/fatmans.html")

def melting(request):
    return render(request, "delivery/meltingpot.html")

def hotel1(request):
    return HttpResponse('<h1>Hello</h1>')


def main(request):
    return render(request,'delivery/main.html')

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def input(request):
    global mylist1,no1
    searchWord = request.GET.get('search')
    print(searchWord)
    mylist = list(request.GET.get("list"))
    mylist = (' ').join(mylist)
    mylist1 = mylist.split(',')

    print(mylist1[4])
    no = list(request.GET.get("no"))
    no=(' ').join(no)

    no1=no.split(',')
    print(no)
    if request.method == "POST":
        form_obj = Order(request.POST)

        #print(form_obj.is_valid(), form_obj.errors, type(form_obj.errors))
        if form_obj.is_valid():
            model_obj = form_obj.save(commit=False)
            model_obj.grand_total=searchWord
            model_obj.save()
            print("Savedddd!!")
            return redirect('/delivery/hotel/register/bill/')
        # else:
        #     #return render(request, 'delivery/indexerror.html')
         #     return HttpResponse("<h2>Hi</h2>")
    else:
        form_obj = Order()

    return render(request,"delivery/form.html",{'form':form_obj,'total':searchWord})

def done(request):
    return render(request,'delivery/indexnewsletter.html' )
def bill(request):
     dict={}
     m=[]
     x=[]
     n=[]
     x=Customer.objects.all()
     y=list(x)
     b=str(mylist1)
     z=y[-1]
     a=str(no1)
     m.append(mylist1[0])
     m.append(mylist1[1])
     m.append(mylist1[2])
     m.append(mylist1[3])
     m.append(mylist1[4])
     n.append(no1[0])
     n.append(no1[1])
     n.append(no1[2])
     n.append(no1[3])
     n.append(no1[4])
     l=0
     for i in m:
        dict[i]=n[l]
        l=l+1


     print(dict)

     return render(request,'delivery/bill.html',{'list':m,'no':n,'z':z,'dict':dict})