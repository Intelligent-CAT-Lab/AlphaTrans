from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


def get_numeric_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10
    
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 10
    
    return -1

class IBANCheckDigit(CheckDigit):

    IBAN_CHECK_DIGIT: CheckDigit = None
    __MODULUS: int = 97
    __MAX: int = 999999999
    __MAX_ALPHANUMERIC_VALUE: int = get_numeric_value("Z")
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
        modulusResult = self._calculateModulus(code)
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
            modulusResult = self._calculateModulus(code)
            return modulusResult == 1
        except CheckDigitException:
            return False

    def _calculateModulus(self, code: str) -> int:

        reformattedCode = code[4:] + code[:4]
        total = 0
        for i in range(len(reformattedCode)):
            charValue = get_numeric_value(reformattedCode[i])
            if charValue < 0 or charValue > self.__MAX_ALPHANUMERIC_VALUE:
                raise CheckDigitException.CheckDigitException1(
                    "Invalid Character[" + str(i) + "] = '" + str(charValue) + "'"
                )
            total = (total * 100 if charValue > 9 else total * 10) + charValue
            if total > self.__MAX:
                total = total % self.__MODULUS
        return total % self.__MODULUS


IBANCheckDigit.initialize_fields()
