from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.util.Flags import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *


class CreditCardRange:

    lengths: typing.List[int] = None

    maxLen: int = 0

    minLen: int = 0

    high: str = ""

    low: str = ""

    def __init__(
        self,
        constructorId: int,
        low: str,
        high: str,
        minLen: int,
        maxLen: int,
        lengths: typing.List[int],
    ) -> None:

        pass  # LLM could not translate this method


class CreditCardValidator:

    VPAY_VALIDATOR: CodeValidator = CodeValidator.CodeValidator5(
        "^(4)(\\d{12,18})$", LUHN_VALIDATOR
    )
    VISA_VALIDATOR: CodeValidator = CodeValidator5(
        "^(4)(\\d{12}|\\d{15})$", LUHN_VALIDATOR
    )
    MASTERCARD_VALIDATOR_PRE_OCT2016: CodeValidator = CodeValidator5(
        "^(5[1-5]\\d{14})$", LUHN_VALIDATOR
    )
    DINERS_VALIDATOR: CodeValidator = CodeValidator.CodeValidator5(
        "^(30[0-5]\\d{11}|3095\\d{10}|36\\d{12}|3[8-9]\\d{12})$", LUHN_VALIDATOR
    )
    AMEX_VALIDATOR: CodeValidator = CodeValidator.CodeValidator5(
        "^(3[47]\\d{13})$", LUHN_VALIDATOR
    )
    MASTERCARD_PRE_OCT2016: int = 1 << 6
    VPAY: int = 1 << 5
    DINERS: int = 1 << 4
    DISCOVER: int = 1 << 3
    MASTERCARD: int = 1 << 2
    VISA: int = 1 << 1
    AMEX: int = 1 << 0
    NONE: int = 0
    MASTERCARD_REGEX: RegexValidator = RegexValidator.RegexValidator1(
        [
            "^(5[1-5]\\d{14})$",  # 51 - 55 (pre Oct 2016)
            "^(2221\\d{12})$",  # 222100 - 222199
            "^(222[2-9]\\d{12})$",  # 222200 - 222999
            "^(22[3-9]\\d{13})$",  # 223000 - 229999
            "^(2[3-6]\\d{14})$",  # 230000 - 269999
            "^(27[01]\\d{13})$",  # 270000 - 271999
            "^(2720\\d{12})$",  # 272000 - 272099
        ]
    )
    __DISCOVER_REGEX: RegexValidator = RegexValidator.RegexValidator1(
        [
            "^(6011\\d{12,13})$",
            "^(64[4-9]\\d{13})$",
            "^(65\\d{14})$",
            "^(62[2-8]\\d{13})$",
        ]
    )
    __LUHN_VALIDATOR: CheckDigit = LuhnCheckDigit.LUHN_CHECK_DIGIT
    __cardTypes: typing.List[CodeValidator] = []

    __MAX_CC_LENGTH: int = 19
    __MIN_CC_LENGTH: int = 12
    serialVersionUID: int = 5955978921148959496
    MASTERCARD_VALIDATOR: CodeValidator = CodeValidator.CodeValidator2(
        __MASTERCARD_REGEX, __LUHN_VALIDATOR
    )
    DISCOVER_VALIDATOR: CodeValidator = CodeValidator2(
        __DISCOVER_REGEX, __LUHN_VALIDATOR
    )

    @staticmethod
    def createRangeValidator(
        creditCardRanges: typing.List[CreditCardRange], digitCheck: CheckDigit
    ) -> CodeValidator:

        pass  # LLM could not translate this method

    @staticmethod
    def validLength(valueLength: int, range: CreditCardRange) -> bool:
        if range.lengths is not None:
            for length in range.lengths:
                if valueLength == length:
                    return True
            return False
        return valueLength >= range.minLen and valueLength <= range.maxLen

    def validate(self, card: str) -> typing.Any:
        if card is None or len(card) == 0:
            return None
        result = None
        for cardType in self.__cardTypes:
            result = cardType.validate(card)
            if result is not None:
                return result
        return None

    def isValid(self, card: str) -> bool:
        if card is None or len(card) == 0:
            return False
        for cardType in self.__cardTypes:
            if cardType.isValid(card):
                return True
        return False

    @staticmethod
    def genericCreditCardValidator2() -> CreditCardValidator:
        return CreditCardValidator.genericCreditCardValidator0(
            CreditCardValidator.__MIN_CC_LENGTH, CreditCardValidator.__MAX_CC_LENGTH
        )

    @staticmethod
    def genericCreditCardValidator1(length: int) -> CreditCardValidator:
        return CreditCardValidator.genericCreditCardValidator0(length, length)

    @staticmethod
    def genericCreditCardValidator0(minLen: int, maxLen: int) -> CreditCardValidator:
        return CreditCardValidator(
            1,
            0,
            None,
            [CodeValidator(1, LUHN_VALIDATOR, maxLen, None, minLen, "(\\d+)")],
        )

    def __init__(
        self,
        constructorId: int,
        options: int,
        creditCardRanges: typing.List[CreditCardRange],
        creditCardValidators: typing.List[CodeValidator],
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def CreditCardValidator0() -> CreditCardValidator:
        return CreditCardValidator(
            0,
            CreditCardValidator.AMEX
            + CreditCardValidator.VISA
            + CreditCardValidator.MASTERCARD
            + CreditCardValidator.DISCOVER,
            None,
            None,
        )

    def __isOn(self, options: int, flag: int) -> bool:
        return (options & flag) > 0
