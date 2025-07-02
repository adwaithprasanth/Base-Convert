# In NumberConverterApp/convert.py
def convert_to_decimal(number_str, from_base):
    try:
        # This handles common errors like invalid digits for the given base
        # e.g., '2' in binary, '9' in octal, 'G' in hexadecimal
        return int(number_str, from_base)
    except ValueError:
        return None # Indicate conversion failure

def convert_from_decimal(decimal_val, to_base):
    if decimal_val is None:
        return "Invalid Input"

    if to_base == 2:
        return bin(decimal_val)[2:]
    elif to_base == 8:
        return oct(decimal_val)[2:]
    elif to_base == 10:
        return str(decimal_val)
    elif to_base == 16:
        return hex(decimal_val)[2:].upper()
    else:
        return "Unsupported Target Base" # Should not happen with current UI

def perform_conversion(number_str, from_base, to_base):
    decimal_val = convert_to_decimal(number_str, from_base)
    if decimal_val is None:
        return "Invalid Input for Base " + str(from_base)

    return convert_from_decimal(decimal_val, to_base)