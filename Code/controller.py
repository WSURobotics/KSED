import serial
import time
from pynput import keyboard

# Make sure: pip install pyserial pynput

# Adjust the COM port (Windows: COM3, Linux/Mac: /dev/ttyUSB0)
ser = serial.Serial('COM3', 115200, timeout=1)  
time.sleep(2)

def on_press(key):
    try:
        if key.char == 'r':  # When 'l' is pressed...
            ser.write(b'r')   # Send 'l' to motor (assuming a Serial 'r' will move motor in the right direction)
        if key.char == 'l':  # When 'l' is pressed...
            ser.write(b'l')   # Send 'l' to motor (assuming a Serial 'l' will move motor in the left direction)
    except AttributeError:
        pass

def on_release(key):
    pass

# Listen for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()