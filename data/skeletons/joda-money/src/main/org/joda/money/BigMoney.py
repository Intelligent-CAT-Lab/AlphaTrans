from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.Ser import *
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.BigMoneyProvider import *

# from src.main.org.joda.convert.ToString import *
# from src.main.org.joda.convert.FromString import *
import pickle
import os
import decimal
import typing
from typing import *
import io

# Imports End


class BigMoney:

    # Class Fields Begin
    __serialVersionUID: int = None
    __PARSE_REGEX: re.Pattern = None
    __currency: CurrencyUnit = None
    __amount: decimal.Decimal = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, other: typing.Any) -> bool:
        pass

    def compareTo(self, other: BigMoneyProvider) -> int:
        pass

    def toBigMoney(self) -> BigMoney:
        pass

    def __init__(
        self, constructorId: int, amount: decimal.Decimal, currency: CurrencyUnit
    ) -> None:
        pass

    @staticmethod
    def parse(moneyStr: str) -> BigMoney:
        pass

    def isLessThanOrEqual(self, other: BigMoneyProvider) -> bool:
        pass

    def isLessThan(self, other: BigMoneyProvider) -> bool:
        pass

    def isGreaterThanOrEqual(self, other: BigMoneyProvider) -> bool:
        pass

    def isGreaterThan(self, other: BigMoneyProvider) -> bool:
        pass

    def isEqual(self, other: BigMoneyProvider) -> bool:
        pass

    def isSameCurrency(self, money: BigMoneyProvider) -> bool:
        pass

    def toMoney1(self, roundingMode: typing.Any) -> Money:
        pass

    def toMoney0(self) -> Money:
        pass

    def convertRetainScale(
        self,
        currency: CurrencyUnit,
        conversionMultipler: decimal.Decimal,
        roundingMode: typing.Any,
    ) -> BigMoney:
        pass

    def convertedTo(
        self, currency: CurrencyUnit, conversionMultipler: decimal.Decimal
    ) -> BigMoney:
        pass

    def rounded(self, scale: int, roundingMode: typing.Any) -> BigMoney:
        pass

    def abs(self) -> BigMoney:
        pass

    def negated(self) -> BigMoney:
        pass

    def dividedBy2(self, valueToDivideBy: int, roundingMode: typing.Any) -> BigMoney:
        pass

    def dividedBy1(self, valueToDivideBy: float, roundingMode: typing.Any) -> BigMoney:
        pass

    def dividedBy0(
        self, valueToDivideBy: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def multiplyRetainScale1(
        self, valueToMultiplyBy: float, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def multiplyRetainScale0(
        self, valueToMultiplyBy: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def multipliedBy2(self, valueToMultiplyBy: int) -> BigMoney:
        pass

    def multipliedBy1(self, valueToMultiplyBy: float) -> BigMoney:
        pass

    def multipliedBy0(self, valueToMultiplyBy: decimal.Decimal) -> BigMoney:
        pass

    def minusRetainScale2(
        self, amountToSubtract: float, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def minusRetainScale1(
        self, amountToSubtract: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def minusRetainScale0(
        self, moneyToSubtract: BigMoneyProvider, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def minusMinor(self, amountToSubtract: int) -> BigMoney:
        pass

    def minusMajor(self, amountToSubtract: int) -> BigMoney:
        pass

    def minus3(self, amountToSubtract: float) -> BigMoney:
        pass

    def minus2(self, amountToSubtract: decimal.Decimal) -> BigMoney:
        pass

    def minus1(self, moneyToSubtract: BigMoneyProvider) -> BigMoney:
        pass

    def minus0(self, moniesToSubtract: typing.Iterable[BigMoneyProvider]) -> BigMoney:
        pass

    def plusRetainScale2(
        self, amountToAdd: float, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def plusRetainScale1(
        self, amountToAdd: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def plusRetainScale0(
        self, moneyToAdd: BigMoneyProvider, roundingMode: typing.Any
    ) -> BigMoney:
        pass

    def plusMinor(self, amountToAdd: int) -> BigMoney:
        pass

    def plusMajor(self, amountToAdd: int) -> BigMoney:
        pass

    def plus3(self, amountToAdd: float) -> BigMoney:
        pass

    def plus2(self, amountToAdd: decimal.Decimal) -> BigMoney:
        pass

    def plus1(self, moneyToAdd: BigMoneyProvider) -> BigMoney:
        pass

    def plus0(self, moniesToAdd: typing.Iterable[BigMoneyProvider]) -> BigMoney:
        pass

    def withAmount1(self, amount: float) -> BigMoney:
        pass

    def withAmount0(self, amount: decimal.Decimal) -> BigMoney:
        pass

    def isNegativeOrZero(self) -> bool:
        pass

    def isNegative(self) -> bool:
        pass

    def isPositiveOrZero(self) -> bool:
        pass

    def isPositive(self) -> bool:
        pass

    def isZero(self) -> bool:
        pass

    def getMinorPart(self) -> int:
        pass

    def getAmountMinorInt(self) -> int:
        pass

    def getAmountMinorLong(self) -> int:
        pass

    def getAmountMinor(self) -> decimal.Decimal:
        pass

    def getAmountMajorInt(self) -> int:
        pass

    def getAmountMajorLong(self) -> int:
        pass

    def getAmountMajor(self) -> decimal.Decimal:
        pass

    def getAmount(self) -> decimal.Decimal:
        pass

    def withCurrencyScale1(self, roundingMode: typing.Any) -> BigMoney:
        pass

    def withCurrencyScale0(self) -> BigMoney:
        pass

    def withScale1(self, scale: int, roundingMode: typing.Any) -> BigMoney:
        pass

    def withScale0(self, scale: int) -> BigMoney:
        pass

    def isCurrencyScale(self) -> bool:
        pass

    def getScale(self) -> int:
        pass

    def withCurrencyUnit(self, currency: CurrencyUnit) -> BigMoney:
        pass

    def getCurrencyUnit(self) -> CurrencyUnit:
        pass

    @staticmethod
    def total3(
        currency: CurrencyUnit, monies: typing.Iterable[BigMoneyProvider]
    ) -> BigMoney:
        pass

    @staticmethod
    def total2(
        currency: CurrencyUnit, monies: typing.List[BigMoneyProvider]
    ) -> BigMoney:
        pass

    @staticmethod
    def total1(monies: typing.Iterable[BigMoneyProvider]) -> BigMoney:
        pass

    @staticmethod
    def total0(monies: typing.List[BigMoneyProvider]) -> BigMoney:
        pass

    @staticmethod
    def of2(moneyProvider: BigMoneyProvider) -> BigMoney:
        pass

    @staticmethod
    def zero1(currency: CurrencyUnit, scale: int) -> BigMoney:
        pass

    @staticmethod
    def zero0(currency: CurrencyUnit) -> BigMoney:
        pass

    @staticmethod
    def ofMinor(currency: CurrencyUnit, amountMinor: int) -> BigMoney:
        pass

    @staticmethod
    def ofMajor(currency: CurrencyUnit, amountMajor: int) -> BigMoney:
        pass

    @staticmethod
    def ofScale2(currency: CurrencyUnit, unscaledAmount: int, scale: int) -> BigMoney:
        pass

    @staticmethod
    def ofScale1(
        currency: CurrencyUnit,
        amount: decimal.Decimal,
        scale: int,
        roundingMode: typing.Any,
    ) -> BigMoney:
        pass

    @staticmethod
    def ofScale0(
        currency: CurrencyUnit, amount: decimal.Decimal, scale: int
    ) -> BigMoney:
        pass

    @staticmethod
    def of1(currency: CurrencyUnit, amount: float) -> BigMoney:
        pass

    @staticmethod
    def of0(currency: CurrencyUnit, amount: decimal.Decimal) -> BigMoney:
        pass

    def __checkCurrencyEqual(self, moneyProvider: BigMoneyProvider) -> BigMoney:
        pass

    def __with(self, newAmount: decimal.Decimal) -> BigMoney:
        pass

    def __writeReplace(self) -> typing.Any:
        pass

    def __readObject(self, ois: pickle.Unpickler) -> None:
        pass

    # Class Methods End
