# -*- coding: utf-8 -*-
from escpos import *
import datetime
import serial
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def print_usb(dish_list):
    usb = printer.Usb(0x0485, 0x7541, 0, out_ep=0x03)
    usb.set(align='center')
    now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S\n")
    usb.text(now)
    usb.text("desk_id:3\n")
    usb.set(align='left')
    total=0
    for dish in dish_list:
        dish_num=int(dish["num"])
        dish_price=float(dish["price"])
        usb.text("\t%s\tnum:%d\tprice:%.2f$\n"%(dish["name"],dish_num,dish_price))
        total+=dish_num*dish_price
    usb.set(align='right')
    usb.text("total:%.2f$\n"%total)
    usb.cut()
    usb.close()


def print_stm():
    ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.4)
    ser.write("h")

if __name__ == '__main__':
    print_stm()
