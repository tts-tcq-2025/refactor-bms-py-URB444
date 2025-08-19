from compute import (calculate_variance,check_vitals,warning_message,display_alert_message)

vital_range_map = {
  # Vital : [Vital Lower Limit, Vital Upper Limit, Vital Name]
  'temperature': [95,102,'Temperature'],
  'pulse_rate': [60,100,'Pulse Rate'],
  'spo2': [0,90,'Oxygen Saturation']
}

def check_temperature(temperature):
    low_variance,high_variance = calculate_variance(vital_range_map['temperature'][0],
                                                    vital_range_map['temperature'][1])
    warning_message(vital_range_map['temperature'][0],low_variance,temperature,'hypothermia')
    warning_message(high_variance,vital_range_map['temperature'][1],temperature,'hyperthermia')
    status,message = check_vitals(temperature,vital_range_map['temperature'][0],
                 vital_range_map['temperature'][1],vital_range_map['temperature'][2])
    if not status:
        display_alert_message(message)
    return status

def check_pulse_rate(pulse_rate):
    low_variance,high_variance = calculate_variance(vital_range_map['pulse_rate'][0],
                                                    vital_range_map['pulse_rate'][1])
    warning_message(vital_range_map['pulse_rate'][0],low_variance,pulse_rate,'hypothermia')
    warning_message(high_variance,vital_range_map['pulse_rate'][1],pulse_rate,'hyperthermia')
    status,message = check_vitals(pulse_rate,vital_range_map['pulse_rate'][0],
                 vital_range_map['pulse_rate'][1],vital_range_map['pulse_rate'][2])
    if not status:
        display_alert_message(message)
    return status

def check_spo2(spo2):
    low_variance,high_variance = calculate_variance(vital_range_map['spo2'][0],
                                                    vital_range_map['spo2'][1])
    warning_message(vital_range_map['spo2'][0],low_variance,spo2,'hypothermia')
    warning_message(high_variance,vital_range_map['spo2'][1],spo2,'hyperthermia')
    status,message = check_vitals(spo2,vital_range_map['spo2'][0],
                 vital_range_map['spo2'][1],vital_range_map['spo2'][2])
    if not status:
        display_alert_message(message)
    return status

def vitals_ok(temperature,pulse_rate,spo2):
    return check_temperature(temperature) and check_pulse_rate(pulse_rate) and check_spo2(spo2)
