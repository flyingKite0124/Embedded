import usb.core
import usb.util
import sys
 
dev =  usb.core.find(idVendor= 0x0485, idProduct= 0x7541)
 
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]
ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
    usb.util.endpoint_direction(e.bEndpointAddress) == \
    usb.util.ENDPOINT_OUT
)
print ep
dev.reset()