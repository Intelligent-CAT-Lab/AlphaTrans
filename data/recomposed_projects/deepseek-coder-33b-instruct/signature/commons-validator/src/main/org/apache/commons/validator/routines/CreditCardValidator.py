from __future__ import annotations
import copy
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

        self.low = low
        self.high = high

        if constructorId == 0:
            self.minLen = minLen
            self.maxLen = maxLen
            self.lengths = None
        else:
            self.minLen = -1
            self.maxLen = -1
            self.lengths = lengths.copy()


class CreditCardValidator:

    VISA: int = 1 << 1
    MASTERCARD: int = 1 << 2
    DISCOVER: int = 1 << 3
    DINERS: int = 1 << 4
    AMEX: int = 1 << 0
    MASTERCARD_PRE_OCT2016: int = 1 << 6
    VPAY: int = 1 << 5
    NONE: int = 0
    __MASTERCARD_REGEX: RegexValidator = RegexValidator(
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
    __DISCOVER_REGEX: RegexValidator = RegexValidator(
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
    __serialVersionUID: int = 5955978921148959496
    VPAY_VALIDATOR: CodeValidator = None
    MASTERCARD_VALIDATOR_PRE_OCT2016: CodeValidator = None

    @staticmethod
    def initialize_fields() -> None:
        CreditCardValidator.VPAY_VALIDATOR: CodeValidator = (
            CodeValidator.CodeValidator5(
                "^(4)(d{12,18})$", CreditCardValidator.__LUHN_VALIDATOR
            )
        )

        CreditCardValidator.MASTERCARD_VALIDATOR_PRE_OCT2016: CodeValidator = (
            CodeValidator.CodeValidator5(
                "^(5[1-5]d{14})$", CreditCardValidator.__LUHN_VALIDATOR
            )
        )

    @staticmethod
    def createRangeValidator(
        creditCardRanges: typing.List[CreditCardRange], digitCheck: CheckDigit
    ) -> CodeValidator:

        class RangeValidator(RegexValidator):
            __serialVersionUID: int = 1
            ccr: typing.List[CreditCardRange] = creditCardRanges

            def validate(self, value: str) -> str:
                if super().match(value) is not None:
                    length = len(value)
                    for range in self.ccr:
                        if CreditCardValidator.validLength(length, range):
                            if range.high is None:  # single prefix only
                                if value.startswith(range.low):
                                    return value
                            elif range.low <= value <= range.high[: len(value)]:
                                return value
                return None

            def isValid(self, value: str) -> bool:
                return self.validate(value) is not None

            def match(self, value: str) -> typing.List[str]:
                return [self.validate(value)]

        return CodeValidator.CodeValidator2(RangeValidator(["(\\d+)"]), digitCheck)

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
            [
                CodeValidator(
                    1, LuhnCheckDigit.LUHN_CHECK_DIGIT, maxLen, None, minLen, "(\\d+)"
                )
            ],
        )

    def __init__(
        self,
        constructorId: int,
        options: int,
        creditCardRanges: typing.List[CreditCardRange],
        creditCardValidators: typing.List[CodeValidator],
    ) -> None:

        if constructorId == 0:
            if self.__isOn(options, self.VISA):
                self.__cardTypes.append(self.VISA_VALIDATOR)

            if self.__isOn(options, self.VPAY):
                self.__cardTypes.append(self.VPAY_VALIDATOR)

            if self.__isOn(options, self.AMEX):
                self.__cardTypes.append(self.AMEX_VALIDATOR)

            if self.__isOn(options, self.MASTERCARD):
                self.__cardTypes.append(self.MASTERCARD_VALIDATOR)

            if self.__isOn(options, self.MASTERCARD_PRE_OCT2016):
                self.__cardTypes.append(self.MASTERCARD_VALIDATOR_PRE_OCT2016)

            if self.__isOn(options, self.DISCOVER):
                self.__cardTypes.append(self.DISCOVER_VALIDATOR)

            if self.__isOn(options, self.DINERS):
                self.__cardTypes.append(self.DINERS_VALIDATOR)

        elif constructorId == 1:
            if creditCardValidators is None:
                raise ValueError("Card validators are missing")
            self.__cardTypes.extend(creditCardValidators)

        elif constructorId == 2:
            if creditCardRanges is None:
                raise ValueError("Card ranges are missing")
            self.__cardTypes.append(
                self.createRangeValidator(creditCardRanges, self.__LUHN_VALIDATOR)
            )

        elif constructorId == 3:
            if creditCardValidators is None:
                raise ValueError("Card validators are missing")
            if creditCardRanges is None:
                raise ValueError("Card ranges are missing")
            self.__cardTypes.extend(creditCardValidators)
            self.__cardTypes.append(
                self.createRangeValidator(creditCardRanges, self.__LUHN_VALIDATOR)
            )

    @staticmethod
    def CreditCardValidator0() -> CreditCardValidator:
        return CreditCardValidator(
            0,
            CreditCardValidator.AMEX
            | CreditCardValidator.VISA
            | CreditCardValidator.MASTERCARD
            | CreditCardValidator.DISCOVER,
            None,
            None,
        )

    def __isOn(self, options: int, flag: int) -> bool:
        return (options & flag) > 0


CreditCardValidator.initialize_fields()
