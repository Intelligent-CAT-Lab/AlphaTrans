from __future__ import annotations
import re
import io
import typing
from typing import *
import decimal
import os
import pickle
# from src.main.org.joda.convert.FromString import *
# from src.main.org.joda.convert.ToString import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.Ser import *


class Money(BigMoneyProvider):

    __serialVersionUID: int = 1
    def toString(self) -> str:
         return self.__money.toString()
    def hashCode(self) -> int:
         return self.__money.hashCode() + 3
    def equals(self, other: typing.Any) -> bool:
         if self == other:
             return True
         if isinstance(other, Money):
             otherMoney = other
             return self.money.equals(otherMoney.money)
         return False
    def compareTo(self, other: BigMoneyProvider) -> int:
         return self.__money.compareTo(other)
    def toBigMoney(self) -> BigMoney:
         return self.__money

    def __init__(self, constructorId: int, money: BigMoney) -> None:

         self.__money: BigMoney = None
        pass # LLM could not translate this method


    @staticmethod
    def parse(moneyStr: str) -> Money:
         return Money.of4(BigMoney.parse(moneyStr))
    def isLessThanOrEqual(self, other: BigMoneyProvider) -> bool:
         return self.money.isLessThanOrEqual(other)
    def isLessThan(self, other: BigMoneyProvider) -> bool:
         return self.money.isLessThan(other)
    def isGreaterThanOrEqual(self, other: BigMoneyProvider) -> bool:
         return self.__money.isGreaterThanOrEqual(other)
    def isGreaterThan(self, other: BigMoneyProvider) -> bool:
         return self.money.isGreaterThan(other)
    def isEqual(self, other: BigMoneyProvider) -> bool:
         return self.__money.isEqual(other)
    def isSameCurrency(self, other: BigMoneyProvider) -> bool:
         return self.money.isSameCurrency(other)
    def convertedTo(self, currency: CurrencyUnit, conversionMultipler: decimal.Decimal, roundingMode: typing.Any) -> Money:
         return self.__with(
                self.__money.convertedTo(currency, conversionMultipler).withCurrencyScale1(roundingMode))
    def rounded(self, scale: int, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.rounded(scale, roundingMode))
    def abs(self) -> Money:
         return (self.negated() if self.isNegative() else self)
    def negated(self) -> Money:
         return self.__with(self.__money.negated())
    def dividedBy2(self, valueToDivideBy: int, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.dividedBy2(valueToDivideBy, roundingMode))
    def dividedBy1(self, valueToDivideBy: float, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.dividedBy1(valueToDivideBy, roundingMode))
    def dividedBy0(self, valueToDivideBy: decimal.Decimal, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.dividedBy0(valueToDivideBy, roundingMode))
    def multipliedBy2(self, valueToMultiplyBy: int) -> Money:
         return self.__with(self.__money.multipliedBy2(valueToMultiplyBy))
    def multipliedBy1(self, valueToMultiplyBy: float, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.multiplyRetainScale1(valueToMultiplyBy, roundingMode))
    def multipliedBy0(self, valueToMultiplyBy: decimal.Decimal, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.multiplyRetainScale0(valueToMultiplyBy, roundingMode))
    def minusMinor(self, amountToSubtract: int) -> Money:
         return self.__with(self.__money.minusMinor(amountToSubtract))
    def minusMajor(self, amountToSubtract: int) -> Money:
         return self.__with(self.__money.minusMajor(amountToSubtract))
    def minus5(self, amountToSubtract: float, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.minusRetainScale2(amountToSubtract, roundingMode))
    def minus4(self, amountToSubtract: float) -> Money:
         return self.minus5(amountToSubtract, RoundingMode.UNNECESSARY)
    def minus3(self, amountToSubtract: decimal.Decimal, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.minusRetainScale1(amountToSubtract, roundingMode))
    def minus2(self, amountToSubtract: decimal.Decimal) -> Money:
         return self.minus3(amountToSubtract, RoundingMode.UNNECESSARY)
    def minus1(self, moneyToSubtract: Money) -> Money:
         return self.__with(self.__money.minus1(moneyToSubtract))
    def minus0(self, moniesToSubtract: typing.Iterable[Money]) -> Money:
         return self.__with(self.__money.minus0(moniesToSubtract))
    def plusMinor(self, amountToAdd: int) -> Money:
         return self.__with(self.__money.plusMinor(amountToAdd))
    def plusMajor(self, amountToAdd: int) -> Money:
         return self.__with(self.__money.plusMajor(amountToAdd))
    def plus5(self, amountToAdd: float, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.plusRetainScale2(amountToAdd, roundingMode))
    def plus4(self, amountToAdd: float) -> Money:
         return self.plus5(amountToAdd, RoundingMode.UNNECESSARY)
    def plus3(self, amountToAdd: decimal.Decimal, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.plusRetainScale1(amountToAdd, roundingMode))
    def plus2(self, amountToAdd: decimal.Decimal) -> Money:
         return self.plus3(amountToAdd, RoundingMode.UNNECESSARY)
    def plus1(self, moneyToAdd: Money) -> Money:
         return self.__with(self.__money.plus1(moneyToAdd))
    def plus0(self, moniesToAdd: typing.Iterable[Money]) -> Money:
         return self.__with(self.__money.plus0(moniesToAdd))
    def withAmount3(self, amount: float, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.withAmount1(amount).withCurrencyScale1(roundingMode))
    def withAmount2(self, amount: float) -> Money:
         return self.withAmount3(amount, RoundingMode.UNNECESSARY)
    def withAmount1(self, amount: decimal.Decimal, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.withAmount0(amount).withCurrencyScale1(roundingMode))
    def withAmount0(self, amount: decimal.Decimal) -> Money:
         return self.withAmount1(amount, RoundingMode.UNNECESSARY)
    def isNegativeOrZero(self) -> bool:
         return self.money.isNegativeOrZero()
    def isNegative(self) -> bool:
         return self.__money.isNegative()
    def isPositiveOrZero(self) -> bool:
         return self.__money.isPositiveOrZero()
    def isPositive(self) -> bool:
         return self.__money.isPositive()
    def isZero(self) -> bool:
         return self.__money.isZero()
    def getMinorPart(self) -> int:
         return self.__money.getMinorPart()
    def getAmountMinorInt(self) -> int:
         return self.__money.getAmountMinorInt()
    def getAmountMinorLong(self) -> int:
         return self.__money.getAmountMinorLong()
    def getAmountMinor(self) -> decimal.Decimal:
         return self.__money.getAmountMinor()
    def getAmountMajorInt(self) -> int:
         return self.__money.getAmountMajorInt()
    def getAmountMajorLong(self) -> int:
         return self.__money.getAmountMajorLong()
    def getAmountMajor(self) -> decimal.Decimal:
         return self.__money.getAmountMajor()
    def getAmount(self) -> decimal.Decimal:
         return self.__money.getAmount()
    def getScale(self) -> int:
         return self.__money.getScale()
    def withCurrencyUnit1(self, currency: CurrencyUnit, roundingMode: typing.Any) -> Money:
         return self.__with(self.__money.withCurrencyUnit(currency).withCurrencyScale1(roundingMode))
    def withCurrencyUnit0(self, currency: CurrencyUnit) -> Money:
         return self.withCurrencyUnit1(currency, RoundingMode.UNNECESSARY)
    def getCurrencyUnit(self) -> CurrencyUnit:
         return self.__money.getCurrencyUnit()
    @staticmethod
    def total3(currency: CurrencyUnit, monies: typing.Iterable[Money]) -> Money:
         return Money.zero(currency).plus0(monies)
    @staticmethod
    def total2(currency: CurrencyUnit, monies: typing.List[Money]) -> Money:
         return Money.zero(currency).plus0(monies)
    @staticmethod
    def total1(monies: typing.Iterable[Money]) -> Money:
         MoneyUtils.checkNotNull(monies, "Money iterator must not be null")
         it = monies.iterator()
         if it.hasNext() == False:
             raise ValueError("Money iterator must not be empty")
         total = it.next()
         MoneyUtils.checkNotNull(total, "Money iterator must not contain null entries")
         while it.hasNext():
             total = total.plus1(it.next())
         return total
    @staticmethod
    def total0(monies: typing.List[Money]) -> Money:
         MoneyUtils.checkNotNull(monies, "Money array must not be null")
         if len(monies) == 0:
             raise ValueError("Money array must not be empty")
         total = monies[0]
         MoneyUtils.checkNotNull(total, "Money arary must not contain null entries")
         for i in range(1, len(monies)):
             total = total.plus1(monies[i])
         return total
    @staticmethod
    def of5(moneyProvider: BigMoneyProvider, roundingMode: typing.Any) -> Money:
         MoneyUtils.checkNotNull(moneyProvider, "BigMoneyProvider must not be null")
         MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")
         return Money(0, BigMoney.of2(moneyProvider).withCurrencyScale1(roundingMode))
    @staticmethod
    def of4(moneyProvider: BigMoneyProvider) -> Money:
         return Money.of5(moneyProvider, RoundingMode.UNNECESSARY)
    @staticmethod
    def zero(currency: CurrencyUnit) -> Money:
         MoneyUtils.checkNotNull(currency, "Currency must not be null")
         bd = BigDecimal.valueOf(0, currency.getDecimalPlaces())
         return Money(0, BigMoney.of0(currency, bd))
    @staticmethod
    def ofMinor(currency: CurrencyUnit, amountMinor: int) -> Money:
         return Money(0, BigMoney.ofMinor(currency, amountMinor))
    @staticmethod
    def ofMajor(currency: CurrencyUnit, amountMajor: int) -> Money:
         return Money.of1(currency, decimal.Decimal(amountMajor), RoundingMode.UNNECESSARY)
    @staticmethod
    def of3(currency: CurrencyUnit, amount: float, roundingMode: typing.Any) -> Money:
         return Money.of1(currency, decimal.Decimal(amount), roundingMode)
    @staticmethod
    def of2(currency: CurrencyUnit, amount: float) -> Money:
         return Money.of0(currency, decimal.Decimal(amount))
    @staticmethod
    def of1(currency: CurrencyUnit, amount: decimal.Decimal, roundingMode: typing.Any) -> Money:
         MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")
         MoneyUtils.checkNotNull(amount, "Amount must not be null")
         MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")
         scaledAmount = amount.quantize(decimal.Decimal(10) ** -currency.getDecimalPlaces(), rounding=roundingMode)
         return Money(0, BigMoney.of0(currency, scaledAmount))
    @staticmethod
    def of0(currency: CurrencyUnit, amount: decimal.Decimal) -> Money:
         MoneyUtils.checkNotNull(currency, "Currency must not be null")
         MoneyUtils.checkNotNull(amount, "Amount must not be null")
         if amount.scale() > currency.getDecimalPlaces():
             raise ArithmeticException(
                 "Scale of amount "
                 + amount
                 + " is greater than the scale of the currency "
                 + currency)
         return Money.of1(currency, amount, RoundingMode.UNNECESSARY)
    def __with(self, newInstance: BigMoney) -> Money:
         if self.__money.equals(newInstance):
             return self
         return Money(0, newInstance)
    def __writeReplace(self) -> typing.Any:
         return Ser(0, self, Ser.MONEY)
    def __readObject(self, ois: pickle.Unpickler) -> None:
         raise InvalidObjectException("Serialization delegate required")
