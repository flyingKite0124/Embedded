# -*- coding: utf-8 -*-
from escpos import *
import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()
print "司令大饭店".decode('utf8').encode('GBK')
usb = printer.Usb(0x0485, 0x7541, 0, out_ep=0x03)

#usb.text("司令大饭店".encode('GBK'))
#usb.barcode('1324354657687','EAN13',64,2,'','')
usb.set(align='center')
usb.text("order_id:3\n")
usb.text("desk_id:3\n")
usb.text("fish:3\n")
usb.text("poke:3\n")
usb.text("lettuce:3\n")
#usb.qr("Si Ling Da Fan Dian")
usb.cut()
usb.close()

