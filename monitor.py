
from time import sleep
import sys

def check_vitals(value, low, high, name):
    if value < low or value > high:
        return False,f'{name} is out of range!'
    return True,''

def blink_alert(times=6, delay=1):
    """Handles the blinking alert animation."""
    for _ in range(times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)
    print()  # Move to next line after blinking

def vitals_ok(temperature, pulseRate, spo2):
    for value, low, high, name in [
        (temperature,95, 102, 'Temperature'),
        (pulseRate, 60, 100, 'Pulse Rate'),
        (spo2, 0, 90, 'Oxygen Saturation')
    ]:
        result = check_vitals(value, low, high, name)
        print_status(result[0],result[1])

def print_status(status,message):
    if not status:
        print(message)
        blink_alert()
        return False
    return True
