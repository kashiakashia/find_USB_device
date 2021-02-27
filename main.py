# this script is for WindowsOS
# ---- !!!!!!! ------
import win32com.client
import time
import usb.core
import usb.util
import usb.backend.libusb1

# ----------------DEFINES-----------------
VID = 0x0781
PID = 0x5597


# list all USB devices connected to your PC
def print_USB_dev():
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("Win32_USBHub"):
        print(usb.DeviceID)


def find_my_dev(vid, pid):
    dev = usb.core.find(idVendor=vid, idProduct=pid)
    if not dev:
        print("Couldn't find the device")
        exit(1)
    print("\nWhat you have been looking for is found!")
    exit(0)


print_USB_dev()
find_my_dev(VID, PID)
