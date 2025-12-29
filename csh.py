#!/usr/bin/env python3
from evdev import InputDevice, ecodes, list_devices
import subprocess
import time

# find the device by name
device_name = "Nintendo.Co.Ltd. Pro Controller"  
dev = None

while True:
    if dev is None:
        devices = [InputDevice(path) for path in list_devices()]

        for d in devices:
            if device_name in d.name:
                dev = d
                print(f"Using device: {dev.path}")
                break
        if dev is None:
            #raise Exception("Controller not found")
            print("Controller not found, retrying in 2 seconds")
            time.sleep(2)
            continue
    try:
        for event in dev.read_loop():
            # only look at key events
            if event.type == ecodes.EV_KEY:
                # trigger on button press (key_down = 1)
                if event.value == 1:  
                    if event.code == 309:  # your middle button
                        subprocess.run(["/home/iwasmateo/Documents/grim.sh"])
                        print("screenshot taken")
    except OSError:
        print("Controller disconnected, looking again in 2 seconds")
        dev = None
        time.sleep(2)
