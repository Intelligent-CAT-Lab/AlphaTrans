from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.util.Flags import *
import typing
from typing import *
import numbers
import io
from abc import ABC

# Imports End


class CreditCardType(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def matches(self, card: str) -> bool:
        pass

    # Class Methods End


class Amex(CreditCardType):

    # Class Fields Begin
    __PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def matches(self, card: str) -> bool:
        pass

    # Class Methods End


class Discover(CreditCardType):

    # Class Fields Begin
    __PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def matches(self, card: str) -> bool:
        pass

    # Class Methods End


class Mastercard(CreditCardType):

    # Class Fields Begin
    __PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def matches(self, card: str) -> bool:
        pass

    # Class Methods End


class Visa(CreditCardType):

    # Class Fields Begin
    __PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def matches(self, card: str) -> bool:
        pass

    # Class Methods End


class CreditCardValidator:

    # Class Fields Begin
    NONE: int = None
    AMEX: int = None
    VISA: int = None
    MASTERCARD: int = None
    DISCOVER: int = None
    __cardTypes: typing.Collection[CreditCardType] = None
    # Class Fields End

    # Class Methods Begin
    def _luhnCheck(self, cardNumber: str) -> bool:
        pass

    def addAllowedCardType(self, type_: CreditCardType) -> None:
        pass

    def isValid(self, card: str) -> bool:
        pass

    @staticmethod
    def CreditCardValidator1() -> CreditCardValidator:
        pass

    def __init__(self, options: int) -> None:
        pass

    # Class Methods End
