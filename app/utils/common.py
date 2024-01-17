import pandas as pd

def convert_to_bool(value, true_value='T'):
    return value == true_value

def convert_to_activity(value):
    return value == 'Aktyvus'

def convert_to_date(date_str):
    if date_str == '-':
        return None
    return pd.to_datetime(date_str).date()

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None
