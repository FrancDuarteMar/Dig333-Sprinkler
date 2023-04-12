import RPi.GPIO as GPIO  # import gpio
import time      #import time library
import spidev
from lib_nrf24 import NRF24   #import NRF24 library

GPIO.setmode(GPIO.BCM)       # set the gpio mode
  # set the pipe address. this address shoeld be entered on the receiver alo

pipes = [[0xE0, 0xE0, 0xF1, 0xF1, 0xE0], [0xF1, 0xF1, 0xF0, 0xF0, 0xE0]]


radio = NRF24(GPIO, spidev.SpiDev())   # use the gpio pins
radio.begin(0, 25)   # start the radio and set the ce,csn pin ce= GPIO08, csn= GPIO25
radio.setPayloadSize(32)  #set the payload size as 32 bytes
radio.setChannel(0x76) # set the channel as 76 hex
radio.setDataRate(NRF24.BR_1MBPS)    # set radio data rate
radio.setPALevel(NRF24.PA_MIN)  # set PA level
radio.setAutoAck(True)       # set acknowledgement as true 

radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openWritingPipe(pipes[0])     # open the defined pipe for writing
radio.printDetails()      # print basic detals of radio

sendMessage = list("Hi..Arduino UNO")  #the message to be sent
while len(sendMessage) < 32:    
    sendMessage.append(0)
radio.startListening()        # Start listening the radio


c=1
while True:
    akpl_buf = [c,1, 2, 3,4,5,6,7,8,9,0,1, 2, 3,4,5,6,7,8]
    pipe = [0]
    while not radio.available(pipe):
        time.sleep(10000/1000000.0)

    recv_buffer = []
    radio.read(recv_buffer, radio.getDynamicPayloadSize())
    print ("Received:") ,
    print (recv_buffer)
    c = c + 1
    if (c&1) == 0:
        radio.writeAckPayload(1, akpl_buf, len(akpl_buf))
        print ("Loaded payload reply:"),
        print (akpl_buf)
    else:
        print ("(No return payload)")


# while True:
#     start = time.time()      #start the time for checking delivery time
#     # radio.write(sendMessage)   # just write the message to radio
#     # print("Sent the message: {}".format(sendMessage))  # print a message after succesfull send
#     # radio.write()
#     messageRec = []
#     radio.read(messageRec,32)
#     # char receivedMessage[32] = {0} ;   // set incmng message for 32 bytes

#     print("Message Received: ", messageRec)
    
#     while not radio.available(0):
#         time.sleep(1/100)
#         if time.time() - start > 2:
#             print("Timed out.")  # print errror message if radio disconnected or not functioning anymore
#             break
    
    

    
    radio.stopListening()     # close radio
    time.sleep(3)  # give delay of 3 seconds


# >

