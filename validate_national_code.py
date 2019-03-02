"""
Validate national code method for Iranian national ID Codes
"""
# Standard library imports
import re

def validate(national_code):    
    if national_code is None:
        return False
    if type(national_code) != str:
        return False
    national_code = national_code.replace('_','').replace('-','').replace(' ','')    
    valid_national_code_pattern = "[0-9]{10}"
    invalid_codes = ( "0000000000", "1111111111", "2222222222", "3333333333", "4444444444", "5555555555", "6666666666", "7777777777", "8888888888", "9999999999")
    
    if national_code in invalid_codes:
        return False
    
    if len(national_code) != 10:
        return False    
    
    if re.search(valid_national_code_pattern,national_code) is None:
        return False
    
    checksum_digit = national_code[9]
    main_digits = national_code[:9]

    i = 10
    sum = 0
    for n in main_digits:
        sum = sum + (int(n)  * i)
        i -= 1
    remainder = sum % 11

    if not((remainder < 2 and remainder == checksum_digit) or (remainder >= 2 and ((11 - remainder) == int(checksum_digit)))):
        return False    
    
    return True

if __name__ == '__main__':
    remainder = 14 % 4
    print(remainder)