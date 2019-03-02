'''
Testings for validate_national_code methods

'''
# Standard library imports
import unittest

# Local application imports
import validate_national_code



class TestValidateNationalCodeMethod(unittest.TestCase):

    # Invalid inputs that must return False
    def test_validate_national_code_None_or_empty(self):
        self.assertFalse(validate_national_code.validate(None))
        self.assertFalse(validate_national_code.validate(''))

    def test_validate_national_code_not_string(self):
        self.assertFalse(validate_national_code.validate(123))
    
    def test_validate_national_code_repeated_numbers(self):        
        invalid_codes = ( '0000000000', '1111111111', '2222222222', '3333333333', '4444444444', '5555555555', '6666666666', '7777777777', '8888888888', '9999999999')
        for invalid_code in invalid_codes:
            self.assertFalse(validate_national_code.validate(invalid_code))
    
    # Vaild inputs that must return True
        


if __name__ == '__main__':
    unittest.main()

