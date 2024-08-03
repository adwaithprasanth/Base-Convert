def convert_to_decimal(number, base):
    if '.' in number:
        integer_part, fractional_part = number.split('.')
        fractional_part = str(fractional_part)
    else:
        integer_part, fractional_part = number, ''
    
    # Convert integer part
    integer_value = int(integer_part, base)
    
    # Convert fractional part
    fractional_value = 0
    for i, digit in enumerate(fractional_part):
        fractional_value += int(digit, base) / (base ** (i + 1))
    
    return integer_value + fractional_value

def convert_from_decimal(decimal, base):
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    
    # Convert integer part
    if base == 2:
        integer_result = bin(integer_part)[2:]
    elif base == 8:
        integer_result = oct(integer_part)[2:]
    elif base == 10:
        integer_result = str(integer_part)
    elif base == 16:
        integer_result = hex(integer_part)[2:].upper()
    
    # Convert fractional part
    fractional_result = []
    while fractional_part and len(fractional_result) < 10:  # Limit to 10 places
        fractional_part *= base
        digit = int(fractional_part)
        if base == 16:
            fractional_result.append(hex(digit)[2:].upper())
        else:
            fractional_result.append(str(digit))
        fractional_part -= digit

    if fractional_result:
        return f"{integer_result}.{''.join(fractional_result)}"
    else:
        return integer_result

def main():
    number = input("Enter the number to convert: ")
    from_base = int(input("Enter the current base (2, 8, 10, 16): "))
    to_base = int(input("Enter the base to convert to (2, 8, 10, 16): "))

    decimal = convert_to_decimal(number, from_base)
    result = convert_from_decimal(decimal, to_base)

    print(f"The converted number is: {result}")

if __name__ == "__main__":
    main()
