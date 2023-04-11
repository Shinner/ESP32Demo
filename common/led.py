from machine import Pin
import time

def toggle(p):
    p.value(not p.value())

def callback(p):
    print('pin change', p)

led = Pin(2, Pin.OUT)
led.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
led.on()

while True:
    toggle(led)
    time.sleep_ms(500)