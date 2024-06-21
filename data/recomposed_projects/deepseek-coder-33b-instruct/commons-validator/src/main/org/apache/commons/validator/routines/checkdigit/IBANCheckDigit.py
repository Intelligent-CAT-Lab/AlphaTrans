from __future__ import annotations
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class IBANCheckDigit(CheckDigit):

    IBAN_CHECK_DIGIT: CheckDigit = IBANCheckDigit()

    __MODULUS: int = 97

    __MAX: int = 999999999

    __MAX_ALPHANUMERIC_VALUE: int = 35

    __serialVersionUID: int = -3600191725934382801

    __MIN_CODE_LEN: int = 5

    def calculate(self, code: str) -> str:

        if code is None or len(code) < self.__MIN_CODE_LEN:
            raise CheckDigitException.CheckDigitException1(
                "Invalid Code length=" + str(0 if code is None else len(code))
            )

        code = code[:2] + "00" + code[4:]
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
            modulusResult = self.__calculateModulus(code)
            return modulusResult == 1
        except CheckDigitException:
            return False

    def __init__(self) -> None:

        super().__init__(10)

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
