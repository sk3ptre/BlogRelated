import os
import sys
import frida
import time

device = frida.get_usb_device()
pid = device.spawn(["com.ycisplc.hvmoqgrigmdh"])
device.resume(pid)
time.sleep(1)

session = device.attach(pid)
script = session.create_script(open('obfuscated_mal_frida_script.js').read())
script.load()

input()
print "[*] Done"
