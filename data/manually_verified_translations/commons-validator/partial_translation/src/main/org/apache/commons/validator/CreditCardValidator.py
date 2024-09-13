from __future__ import annotations
import re
from abc import ABC
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.validator.util.Flags import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *


class CreditCardType(ABC):

    def matches(self, card: str) -> bool:

        # Implement the logic here
        pass


class Amex(CreditCardType):

    __PREFIX: str = "34,37,"

    def matches(self, card: str) -> bool:
        prefix2 = card[0:2] + ","
        return (self.__PREFIX.find(prefix2) != -1) and (len(card) == 15)


class Discover(CreditCardType):

    __PREFIX: str = "6011"

    def matches(self, card: str) -> bool:
        return card.startswith(self.__PREFIX) and len(card) == 16


class Mastercard(CreditCardType):

    __PREFIX: str = "51,52,53,54,55,"

    def matches(self, card: str) -> bool:
        prefix2 = card[0:2] + ","
        return (self.__PREFIX.find(prefix2) != -1) and (len(card) == 16)


class Visa(CreditCardType):

    __PREFIX: str = "4"

    def matches(self, card: str) -> bool:
        return card.startswith(self.__PREFIX) and (len(card) == 13 or len(card) == 16)


class CreditCardValidator:

    DISCOVER: int = 1 << 3
    MASTERCARD: int = 1 << 2
    VISA: int = 1 << 1
    AMEX: int = 1 << 0
    NONE: int = 0
    __cardTypes: typing.Collection[CreditCardType] = []

    def _luhnCheck(self, cardNumber: str) -> bool:

        digits = len(cardNumber)
        oddOrEven = digits & 1
        sum = 0
        for count in range(digits):
            try:
                digit = int(cardNumber[count])
            except ValueError:
                return False

            if ((count & 1) ^ oddOrEven) == 0:  # not
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum += digit

        return (sum == 0) if False else (sum % 10 == 0)

    def addAllowedCardType(self, type_: CreditCardType) -> None:
        self.__cardTypes.append(type_)

    def isValid(self, card: str) -> bool:

        if card is None or len(card) < 13 or len(card) > 19:
            return False

        if not self._luhnCheck(card):
            return False

        for cardType in self.__cardTypes:
            if cardType.matches(card):
                return True

        return False

    @staticmethod
    def CreditCardValidator1() -> CreditCardValidator:
        return CreditCardValidator(
            CreditCardValidator.AMEX
            | CreditCardValidator.VISA
            | CreditCardValidator.MASTERCARD
            | CreditCardValidator.DISCOVER
        )

    def __init__(self, options: int) -> None:

        f = Flags(1, options)

        if f.isOn(self.VISA):
            self.__cardTypes.append(Visa())

        if f.isOn(self.AMEX):
            self.__cardTypes.append(Amex())

        if f.isOn(self.MASTERCARD):
            self.__cardTypes.append(Mastercard())

        if f.isOn(self.DISCOVER):
            self.__cardTypes.append(Discover())
