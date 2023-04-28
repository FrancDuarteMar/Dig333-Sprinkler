from machine import UART
import time
from machine import Pin

uart = UART(0,9600,timeout=400)

button1 = Pin(2, Pin.IN,Pin.PULL_UP)
button2 = Pin(3, Pin.IN,Pin.PULL_UP)
button3 = Pin(4, Pin.IN,Pin.PULL_UP)
button4 = Pin(5, Pin.IN,Pin.PULL_UP)

buttonLight1 = Pin(6,Pin.OUT)
buttonLight2 = Pin(7,Pin.OUT)
buttonLight3 = Pin(8,Pin.OUT)
buttonLight4 = Pin(9,Pin.OUT)

prevState1 = button1.value()
prevState2 = button2.value()
prevState3 = button3.value()
prevState4 = button4.value()

while True:


    but1State = button1.value()
    but2State = button2.value()
    but3State = button3.value()
    but4State = button4.value()

    if but1State != prevState1:
        print("Button 1 Pressed!")
        prevState1 = but1State
        uart.write(str("1")+"\n")
        buttonLight1.value(not but1State)
        
    if but2State != prevState2:
        print("Button 2 Pressed!")
        prevState2 = but2State
        uart.write(str("2")+"\n")
        buttonLight2.value(not but2State)

    if but3State != prevState3:
        print("Button 3 Pressed!")
        prevState3 = but3State
        uart.write(str("3")+"\n")
        buttonLight3.value(not but3State)

    if but4State != prevState4:
        print("Button 4 Pressed!")
        prevState4 = but4State
        uart.write(str("4")+"\n")
        buttonLight4.value(not but4State)

        
    time.sleep(0.25)

    

    
    
