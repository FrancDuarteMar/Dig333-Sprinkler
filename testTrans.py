import sys
import tty
import termios
import threading
import time
from rpi_rf import RFDevice

# Elegant shutdown
def exithandler():
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    try:
        rx.cleanup()
        tx.cleanup()
    except:
        pass
    sys.exit(0)
    
    
# Activate our transmitter and received
tx = RFDevice(17)
tx.enable_tx()


# Remember how the shell was set up so we can reset on exit
old_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)

while True:

    # Wait for a keypress
    char = sys.stdin.read(1)

    # If CTRL-C, shutdown
    if ord(char) == 3:
        exithandler()
    else:
        # Transmit character
        tx.tx_code(ord(char))

    time.sleep(0.01)
