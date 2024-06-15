import unittest
from src.main.org.apache.commons.validator.routines.ISINValidator import *

class ISINValidatorTest(unittest.TestCase):

    __VALIDATOR_TRUE = ISINValidator.getInstance(True)
    __VALIDATOR_FALSE = ISINValidator.getInstance(False)

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self.__validFormat = [
            "US0378331005",
            "BMG8571G1096",
            "AU0000XVGZA3",
            "GB0002634946",
            "FR0004026250",
            "DK0009763344",
            "GB00B03MLX29",
            "US7562071065",
            "US56845T3059",
            "LU0327357389",
            "US032511BN64",
            "INE112A01023",
            "EZ0000000003",  # Invented; for use in ISINValidator
            "XS0000000009",
        ]

        self.__invalidFormat = [
            None,
            "",  # empty
            "   ",  # empty
            "US037833100O",  # proper check digit is '5', see above
            "BMG8571G109D",  # proper check digit is '6', see above
            "AU0000XVGZAD",  # proper check digit is '3', see above
            "GB000263494I",  # proper check digit is '6', see above
            "FR000402625C",  # proper check digit is '0', see above
            "DK000976334H",  # proper check digit is '4', see above
            "3133EHHF3",  # see VALIDATOR-422 Valid check-digit, but not valid ISIN
            "AU0000xvgzA3",  # disallow lower case NSIN
            "gb0002634946",  # disallow lower case ISO code
        ]

        self.__invalidFormatTrue = [
            "AA0000000006",  # Invalid country code
        ]

    
    def testIsValidTrue(self) -> None:
        for f in self.__validFormat:
            self.assertTrue(
                ISINValidatorTest.__VALIDATOR_TRUE.isValid(f),
                f
            )

    
    def testInvalidTrue(self) -> None:
        for f in self.__invalidFormat:
            self.assertFalse(
                ISINValidatorTest.__VALIDATOR_TRUE.isValid(f),
                f
            )
        for f in self.__invalidFormatTrue:
            self.assertFalse(
                ISINValidatorTest.__VALIDATOR_TRUE.isValid(f),
                f
            )

    
    def testIsValidFalse(self) -> None:
        for f in self.__validFormat:
            self.assertTrue(
                ISINValidatorTest.__VALIDATOR_FALSE.isValid(f),
                f
            )

    
    def testInvalidFalse(self) -> None:
        for f in self.__invalidFormat:
            self.assertFalse(
                ISINValidatorTest.__VALIDATOR_FALSE.isValid(f),
                f
            )
