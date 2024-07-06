from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class IBANCheckDigit(CheckDigit):

    IBAN_CHECK_DIGIT: CheckDigit = None
    __MODULUS: int = 97
    __MAX: int = 999999999
    __MAX_ALPHANUMERIC_VALUE: int = 35
    __serialVersionUID: int = -3600191725934382801
    __MIN_CODE_LEN: int = 5

    @staticmethod
    def initialize_fields() -> None:
        IBANCheckDigit.IBAN_CHECK_DIGIT: CheckDigit = IBANCheckDigit()

    def calculate(self, code: str) -> str:
        if code is None or len(code) < self.__MIN_CODE_LEN:
            raise CheckDigitException.CheckDigitException1(
                "Invalid Code length=" + (0 if code is None else len(code))
            )
        code = code[0:2] + "00" + code[4:]
        modulus_result = self.__calculateModulus(code)
        char_value = 98 - modulus_result
        check_digit = str(char_value)
        return check_digit if char_value > 9 else "0" + check_digit

    def isValid(self, code: str) -> bool:
        if code is None or len(code) < self.__MIN_CODE_LEN:
            return False
        check = code[2:4]
        if check == "00" or check == "01" or check == "99":
            return False
        try:
            modulus_result = self.__calculateModulus(code)
            return modulus_result == 1
        except CheckDigitException as ex:
            return False

    def __init__(self) -> None:
        super().__init__("IBAN", 2, False)

    def __calculateModulus(self, code: str) -> int:
        reformattedCode = code[4:] + code[:4]
        total = 0
        for i in range(len(reformattedCode)):
            charValue = ord(reformattedCode[i]) - ord("0")
            if charValue < 0 or charValue > self.__MAX_ALPHANUMERIC_VALUE:
                raise CheckDigitException.CheckDigitException1(
                    "Invalid Character[" + str(i) + "] = '" + str(charValue) + "'"
                )
            total = (charValue > 9 and total * 100 or total * 10) + charValue
            if total > self.__MAX:
                total = total % self.__MODULUS
        return total % self.__MODULUS


IBANCheckDigit.initialize_fields()
