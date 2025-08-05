
from time import sleep
import sys

def check_vitals(temperature, pulseRate, spo2):
    """Pure function: returns (status, message) tuple."""
    if not (95 <= temperature <= 102):
        return False, 'Temperature critical!'
    if not (60 <= pulseRate <= 100):
        return False, 'Pulse Rate is out of range!'
    if spo2 < 90:
        return False, 'Oxygen Saturation out of range!'
    return True, ''

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
    status, message = check_vitals(temperature, pulseRate, spo2)
    if not status:
        print(message)
        blink_alert()
        return False
    return True
