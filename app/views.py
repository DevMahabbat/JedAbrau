from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms import MuracietForm
from .models import HomePage, Map, New, Product

# Create your views here.


def index(request):
    data= HomePage.objects.first()
    context = {
        "data": data
    }
    return render(request,'index.html',context)



def contact(request):
    form = MuracietForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,'contact.html')


def news(request):
    news = New.objects.all()
    news1 = New.objects.first()
    context ={
        "news": news,
        "news1" : news1
    }
    print(news1)
    return render(request,"news.html",context)




def newsSingle(request,id):

    news = New.objects.filter(id = id ).first()

    context ={
        "news": news
    }

    return render(request,"newsSingle.html",context)



def products(request):
    products= Product.objects.all()
    context=  {
        "products": products
    }

    return render(request,"products.html",context)
def productSingle(request,id): 
    allproducts = Product.objects.all()
    products= allproducts[2:10]
    currentproduct = allproducts.filter(id= id).first()
    context=  {
        "products": products,
        "currentproduct": currentproduct
    }
  
    return render(request,"productSingle.html",context)

def maps(request):
    maps = Map.objects.all()
    context=  {
        "maps": maps
    }
    return render(request,"maps.html",context)
