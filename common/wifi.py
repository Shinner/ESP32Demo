wlan = None
def do_connect(ssid,key):
    import network
    global wlan
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.disconnect()
        wlan.connect(ssid,key)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())