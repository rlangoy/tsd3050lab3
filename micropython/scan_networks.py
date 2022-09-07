import network
sta_if = network.WLAN(network.STA_IF)     # Fast WIFI-netverk
sta_if.active(True)                       # Enable radio motak
wifiNets=sta_if.scan()                             # Scan for available access points
for result in sorted(wifiNets):
  ssid, bssid, channel, RSSI, authmode, hidden = result
  print("Station: {}  \t\tStrength: {} ".format(ssid.decode(),RSSI))

