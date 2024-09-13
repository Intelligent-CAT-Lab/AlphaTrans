from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class IBANCheckDigit(CheckDigit):

    IBAN_CHECK_DIGIT: CheckDigit = None
    __MODULUS: int = 97
    __MAX: int = 999999999
    __MAX_ALPHANUMERIC_VALUE: int = int(ord("Z"))
    __serialVersionUID: int = -3600191725934382801
    __MIN_CODE_LEN: int = 5

    @staticmethod
    def initialize_fields() -> None:
        IBANCheckDigit.IBAN_CHECK_DIGIT: CheckDigit = IBANCheckDigit()

    def calculate(self, code: str) -> str:

        if code is None or len(code) < self.__MIN_CODE_LEN:
            raise CheckDigitException.CheckDigitException1(
                "Invalid Code length=" + str(0 if code is None else len(code))
            )

        code = code[:2] + "00" + code[4:]
        modulusResult = self.__calculateModulus(code)
        charValue = 98 - modulusResult
        checkDigit = str(charValue)
        return checkDigit if charValue > 9 else "0" + checkDigit

    def isValid(self, code: str) -> bool:

        if code is None or len(code) < self.__MIN_CODE_LEN:
            return False
        check = code[2:4]
        if check == "00" or check == "01" or check == "99":
            return False
        try:
            modulusResult = self.__calculateModulus(code)
            return modulusResult == 1
        except CheckDigitException:
            return False

    def __init__(self) -> None:

        # Define the IBAN check digit calculation parameters
        self.check_digit_calculation_parameters = [
            {"start_range": 4, "weight": [2, 1]},
            {"start_range": 2, "weight": [2, 3, 4, 5, 6, 7, 8, 9]},
            {"start_range": 0, "weight": [2, 1]},
        ]

    def calculate(self, code: str) -> int:
        # Check if the code is valid
        if not self.isValid(code):
            raise CheckDigitException("Invalid Code")

        # Calculate the check digit
        check_digit = 0
        for param in self.check_digit_calculation_parameters:
            start_range = param["start_range"]
            weight = param["weight"]
            for i in range(start_range, len(code)):
                check_digit += int(code[i]) * weight[i - start_range]

        # Calculate the check digit
        check_digit = 98 - (check_digit % 97)

        return check_digit

    def isValid(self, code: str) -> bool:
        # Check if the code is valid
        if len(code) != 22:
            return False

        # Check if the code is numeric
        if not code.isdigit():
            return False

        return True

    def __calculateModulus(self, code: str) -> int:

        reformattedCode = code[4:] + code[:4]
        total = 0
        for i in range(len(reformattedCode)):
            charValue = ord(reformattedCode[i])
            if charValue < 0 or charValue > self.__MAX_ALPHANUMERIC_VALUE:
                raise CheckDigitException.CheckDigitException1(
                    "Invalid Character[" + str(i) + "] = '" + str(charValue) + "'"
                )
            total = (total * 100 if charValue > 9 else total * 10) + charValue
            if total > self.__MAX:
                total = total % self.__MODULUS
        return total % self.__MODULUS


IBANCheckDigit.initialize_fields()
