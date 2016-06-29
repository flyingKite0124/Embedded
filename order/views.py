from django.shortcuts import render
from django.http import  HttpResponseRedirect
import printer.try_print as printer

# Create your views here.

def index(request):
    return render(request,"home.html")

def submit(requset):
    dish_list=list()
    dishs={
        "value1":["Cake","20"],
        "value2":["Salmon","17"],
        "value3":["Bread","8"],
        "value4":["Fish","13"],
        "value5":["Bacon","22"],
    }
    for dish in dishs:
        if dish in requset.GET and int(requset.GET[dish]):
            adish=dict()
            adish["name"]=dishs[dish][0]
            adish["num"]=requset.GET[dish]
            adish["price"]=dishs[dish][1]
            dish_list.append(adish)
    printer.print_usb(dish_list)
    printer.print_stm()
    return HttpResponseRedirect("redirect")


def redirect(requset):
    return render(requset,"Myredirect.html")
