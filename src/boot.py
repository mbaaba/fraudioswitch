import network

import esp
esp.osdebug(None)

import gc
gc.collect()

from secret import ssid, password

wl = network.WLAN(network.STA_IF)

wl.active(True)
wl.connect(ssid, password)

while wl.isconnected() == False:
  pass

print('Connection successful')
print(wl.ifconfig())

