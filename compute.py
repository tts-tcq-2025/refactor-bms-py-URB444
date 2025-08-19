import sys
from time import sleep

def calculate_variance(vital_low_limit,vital_high_limit):
    variance_factor = vital_high_limit*0.015  # Warning Tolerance of 1.5%
    low_variance = variance_factor + vital_low_limit
    high_variance = vital_high_limit - variance_factor
    return low_variance,high_variance

def check_vitals(value, low, high, name):
    if value < low or value > high:
        return False,f'{name} is out of range!'
    return True,''

def warning_message(low_limit,high_limit,value,warning):
    # Check for warning and display message
    if value >= low_limit and value <= high_limit:
        display_alert_message(f'Warning: Approaching {warning}')

def display_alert_message(message):
    print(message)
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
