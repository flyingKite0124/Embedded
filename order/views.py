from django.shortcuts import render
from django.http import  HttpResponseRedirect
import printer.try_print as printer

# Create your views here.

def index(request):
    return render(request,"home.html")

def submit(requset):
    dish_list=list()
    dishs={
        "value1":["",""],
        "value2":["",""],
        "value3":["",""],
        "value4":["",""],
        "value5":["",""],
    }
    for dish in dishs:
        if dish in requset.GET:
            adish=dict()
            adish["name"]=dishs[dish][0]
            adish["num"]=requset.GET[dish]
            adish["price"]=dishs[dish][1]
            dish_list.append(adish)
    print(dish_list)
    return HttpResponseRedirect("redirect")

def redirect(requset):
    pass
