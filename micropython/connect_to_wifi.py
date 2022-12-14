import network
import sys
from time import sleep
ap_if =network.WLAN(network.AP_IF)        #Acess Point
ap_if.active(False)                       #Diasable AP

sta_if = network.WLAN(network.STA_IF)     # WirelessLan (WIFI-network)
sta_if.active(True)                       # Enable WIFI-connect to 

wifi_ssid=""
assert wifi_ssid!="",    "Oh no! wifi_ssid not set"
wifi_password=""
assert wifi_password!="", "Oh no! wifi_password not set"
    
print("Connecting to Wifi Network: ",wifi_ssid)
  # Username , Password
sta_if.connect(wifi_ssid , wifi_password ) # Connect to a wifi network
# Wait maximum 30 sec for sucessfull wifi connection (6 sec is normal)
cnt=0
con=sta_if.isconnected()
while( not con):
    sleep(.1)
    cnt=cnt+1
    if(cnt>300):
        break
    con=sta_if.isconnected()

if(con) :
    print("Sucessfull connection to: ", wifi_ssid," after",cnt/10.0, "sec")
else:
    print("Sorry Not able to connection to: ", wifi_ssid)
    print("Breaking the program")
    sys.exit()


