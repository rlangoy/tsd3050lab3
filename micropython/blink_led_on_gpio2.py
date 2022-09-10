from time import sleep
from machine import Pin

LED_GPIO_2 = Pin(2, Pin.OUT)    # create output pin on LED_GPIO_2
while(True):
    LED_GPIO_2.off()            
    sleep(.2)
    LED_GPIO_2.on()
    sleep(.2)
