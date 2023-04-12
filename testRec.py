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

rx = RFDevice(27)
rx.enable_rx()

# Receiving loop
def rec(rx):

    print("Receiving")

    lastTime = None
    while True:
        currentTime = rx.rx_code_timestamp
        if (currentTime != lastTime and (lastTime is None or currentTime - lastTime > 350000)):
            lastTime = rx.rx_code_timestamp
            try:
                if (rx.rx_code == 13):
                    # Enter/Return Pressed
                    sys.stdout.write('\r\n')
                else:
                    sys.stdout.write(chr(rx.rx_code))
                sys.stdout.flush()
            except:
                pass
        time.sleep(0.01)

# Start receiving thread
t = threading.Thread(target=rec, args=(rx,), daemon=True)
t.start()
