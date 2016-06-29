# -*- coding: utf-8 -*-
from escpos import *
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def print_usb(dish_list):
    usb = printer.Usb(0x0485, 0x7541, 0, out_ep=0x03)
    usb.set(align='center')
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    usb.text(now)
    usb.text("order_id:3\n")
    usb.text("desk_id:3\n")
    total=0
    for dish in dish_list:
        dish_num=int(dish.num)
        dish_price=float(dish.price)
        usb.text("%s num:%d price:%f\n"%(dish.name,dish_num,dish_price))
        total+=dish_num*dish_price
    usb.text("total:%f\n"%total)
    usb.cut()
    usb.close()

