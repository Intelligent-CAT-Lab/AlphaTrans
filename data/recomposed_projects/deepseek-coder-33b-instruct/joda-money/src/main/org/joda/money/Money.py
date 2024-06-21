from __future__ import annotations
import io
import typing
from typing import *
import decimal
import os
import pickle
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.MoneyUtils import *

# src.main.org.joda.money.Ser


class Money(BigMoneyProvider):

    __money: BigMoney = None

    __serialVersionUID: int = 1

    def toString(self) -> str:

        if self.__money is not None:
            return self.__money.toString()
        else:
            return ""

    def hashCode(self) -> int:

        if self.__money is not None:
            return self.__money.hashCode() + 3
        else:
            return 3

    def equals(self, other: typing.Any) -> bool:

        if self == other:
            return True
        if isinstance(other, Money):
            other_money = typing.cast(Money, other)
            return self.__money.equals(other_money.__money)
        return False

    def compareTo(self, other: BigMoneyProvider) -> int:

        if isinstance(other, BigMoney):
            return self.__money.compareTo(other)
        else:
            raise TypeError("other must be an instance of BigMoney")

    def toBigMoney(self) -> BigMoney:

        return self.__money

    def __init__(self, constructorId: int, money: BigMoney) -> None:

        if constructorId == 0:
            assert money is not None, "Joda-Money bug: BigMoney must not be null"
            assert (
                money.isCurrencyScale()
            ), "Joda-Money bug: Only currency scale is valid for Money"
            self.__money = money
        else:
            self.__money = None

    @staticmethod
    def parse(moneyStr: str) -> Money:

        return Money.of4(BigMoney.parse(moneyStr))

    def isLessThanOrEqual(self, other: BigMoneyProvider) -> bool:

        return self.__money.isLessThanOrEqual(other)

    def isLessThan(self, other: BigMoneyProvider) -> bool:

        return self.__money.isLessThan(other)

    def isGreaterThanOrEqual(self, other: BigMoneyProvider) -> bool:

        if isinstance(other, BigMoney):
            return self.__money.isGreaterThanOrEqual(other)
        else:
            raise TypeError("other must be an instance of BigMoney")

    def isGreaterThan(self, other: BigMoneyProvider) -> bool:

        if isinstance(other, BigMoney):
            return self.__money.isGreaterThan(other)
        else:
            raise TypeError("other must be an instance of BigMoney")

    def isEqual(self, other: BigMoneyProvider) -> bool:

        return self.__money.isEqual(other)

    def isSameCurrency(self, other: BigMoneyProvider) -> bool:

        # Assuming BigMoneyProvider has a method called getCurrencyUnit()
        # which returns the currency unit of the BigMoneyProvider
        return self.__money.getCurrencyUnit() == other.getCurrencyUnit()

    def convertedTo(
        self,
        currency: CurrencyUnit,
        conversionMultipler: decimal.Decimal,
        roundingMode: typing.Any,
    ) -> Money:

        newInstance = self.__money.convertedTo(currency, conversionMultipler)
        newInstance = newInstance.withCurrencyScale1(roundingMode)
        return self.__with(newInstance)

    def rounded(self, scale: int, roundingMode: typing.Any) -> Money:

        # Assuming BigMoney has a method called 'rounded'
        newInstance = self.__money.rounded(scale, roundingMode)

        return self.__with(newInstance)

    def abs(self) -> Money:

        return self.negated() if self.isNegative() else self

    def negated(self) -> Money:

        return self.__with(self.__money.negated())

    def dividedBy2(self, valueToDivideBy: int, roundingMode: typing.Any) -> Money:

        # Assuming BigMoney has a method dividedBy2
        newInstance = self.__money.dividedBy2(valueToDivideBy, roundingMode)

        return self.__with(newInstance)

    def dividedBy1(self, valueToDivideBy: float, roundingMode: typing.Any) -> Money:

        # Assuming BigMoney has a method dividedBy1
        newInstance = self.__money.dividedBy1(valueToDivideBy, roundingMode)

        return self.__with(newInstance)

    def dividedBy0(
        self, valueToDivideBy: decimal.Decimal, roundingMode: typing.Any
    ) -> Money:

        # Assuming BigMoney has a method called 'dividedBy0'
        newInstance = self.__money.dividedBy0(valueToDivideBy, roundingMode)

        return self.__with(newInstance)

    def multipliedBy2(self, valueToMultiplyBy: int) -> Money:

        # Assuming BigMoney has a method called multipliedBy2
        newInstance = self.__money.multipliedBy2(valueToMultiplyBy)

        return self.__with(newInstance)

    def multipliedBy1(
        self, valueToMultiplyBy: float, roundingMode: typing.Any
    ) -> Money:

        newInstance = self.__money.multiplyRetainScale1(valueToMultiplyBy, roundingMode)
        return self.__with(newInstance)

    def multipliedBy0(
        self, valueToMultiplyBy: decimal.Decimal, roundingMode: typing.Any
    ) -> Money:

        newInstance = self.__money.multiplyRetainScale0(valueToMultiplyBy, roundingMode)
        return self.__with(newInstance)

    def minusMinor(self, amountToSubtract: int) -> Money:

        # Assuming BigMoney has a method minusMinor
        new_money = self.__money.minusMinor(amountToSubtract)

        return self.__with(new_money)

    def minusMajor(self, amountToSubtract: int) -> Money:

        newInstance = self.__money.minusMajor(amountToSubtract)
        return self.__with(newInstance)

    def minus5(self, amountToSubtract: float, roundingMode: typing.Any) -> Money:

        # Assuming BigMoney has a method minusRetainScale2
        newInstance = self.__money.minusRetainScale2(
            decimal.Decimal(amountToSubtract), roundingMode
        )
        return self.__with(newInstance)

    def minus4(self, amountToSubtract: float) -> Money:

        return self.minus5(amountToSubtract, decimal.ROUND_DOWN)

    def minus3(
        self, amountToSubtract: decimal.Decimal, roundingMode: typing.Any
    ) -> Money:

        newInstance = BigMoney.minusRetainScale1(amountToSubtract, roundingMode)
        return self.__with(newInstance)

    def minus2(self, amountToSubtract: decimal.Decimal) -> Money:

        return self.minus3(amountToSubtract, decimal.ROUND_DOWN)

    def minus1(self, moneyToSubtract: Money) -> Money:

        # Assuming BigMoney has a method minus1
        new_money = self.__money.minus1(moneyToSubtract.__money)

        return self.__with(new_money)

    def minus0(self, moniesToSubtract: typing.Iterable[Money]) -> Money:

        # Convert the Iterable of Money objects to a list of BigMoney objects
        big_money_list = [money.__money for money in moniesToSubtract]

        # Call the minus0 method on the BigMoney object
        result_big_money = self.__money.minus0(big_money_list)

        # Create a new Money object with the result
        result_money = Money()
        result_money.__money = result_big_money

        return result_money

    def plusMinor(self, amountToAdd: int) -> Money:

        newInstance = self.__money.plusMinor(amountToAdd)
        return self.__with(newInstance)

    def plusMajor(self, amountToAdd: int) -> Money:

        # Assuming that the BigMoney class has a method called plusMajor
        # that takes an integer and returns a BigMoney object.
        new_money = self.__money.plusMajor(amountToAdd)

        # Assuming that the __with method is a private method that takes a BigMoney object
        # and returns a new Money object.
        return self.__with(new_money)

    def plus5(self, amountToAdd: float, roundingMode: typing.Any) -> Money:

        newInstance = BigMoney.plusRetainScale2(amountToAdd, roundingMode)
        return self.__with(newInstance)

    def plus4(self, amountToAdd: float) -> Money:

        return self.plus5(amountToAdd, RoundingMode.UNNECESSARY)

    def plus3(self, amountToAdd: decimal.Decimal, roundingMode: typing.Any) -> Money:

        newInstance = self.__money.plusRetainScale1(amountToAdd, roundingMode)
        return self.__with(newInstance)

    def plus2(self, amountToAdd: decimal.Decimal) -> Money:

        return self.plus3(amountToAdd, decimal.ROUND_UP)

    def plus1(self, moneyToAdd: Money) -> Money:

        # Call the plus1 method from BigMoney class
        newInstance = BigMoney.plus1(self.__money, moneyToAdd.__money)

        # Call the __with method from Money class
        return self.__with(newInstance)

    def plus0(self, moniesToAdd: typing.Iterable[Money]) -> Money:

        # Convert Iterable[Money] to List[BigMoney]
        big_monies_to_add = [money.__money for money in moniesToAdd]

        # Call BigMoney's plus0 method
        new_instance = self.__money.plus0(big_monies_to_add)

        # Call __with method
        return self.__with(new_instance)

    def withAmount3(self, amount: float, roundingMode: typing.Any) -> Money:

        new_instance = self.__with(
            self.__money.withAmount1(amount).withCurrencyScale1(roundingMode)
        )
        return new_instance

    def withAmount2(self, amount: float) -> Money:

        return self.withAmount3(amount, decimal.ROUND_DOWN)

    def withAmount1(self, amount: decimal.Decimal, roundingMode: typing.Any) -> Money:

        newInstance = self.__with(
            self.__money.withAmount0(amount).withCurrencyScale1(roundingMode)
        )
        return newInstance

    def withAmount0(self, amount: decimal.Decimal) -> Money:

        return self.withAmount1(amount, decimal.ROUND_DOWN)

    def isNegativeOrZero(self) -> bool:

        return self.__money.isNegativeOrZero()

    def isNegative(self) -> bool:

        return self.__money.isNegative()

    def isPositiveOrZero(self) -> bool:

        # Assuming BigMoney class has a method isPositiveOrZero
        return self.__money.isPositiveOrZero()

    def isPositive(self) -> bool:

        return self.__money.isPositive()

    def isZero(self) -> bool:

        return self.__money.isZero()

    def getMinorPart(self) -> int:

        return self.__money.getMinorPart()

    def getAmountMinorInt(self) -> int:

        if self.__money is None:
            return 0
        else:
            return self.__money.getAmountMinorInt()

    def getAmountMinorLong(self) -> int:

        if self.__money is None:
            return 0
        else:
            return self.__money.getAmountMinorLong()

    def getAmountMinor(self) -> decimal.Decimal:

        if self.__money is None:
            raise ValueError("Money object is not initialized")

        return self.__money.getAmountMinor()

    def getAmountMajorInt(self) -> int:

        if self.__money is None:
            return 0
        else:
            return self.__money.getAmountMajorInt()

    def getAmountMajorLong(self) -> int:

        if self.__money is None:
            return 0

        return self.__money.getAmountMajorLong()

    def getAmountMajor(self) -> decimal.Decimal:

        if self.__money is None:
            raise ValueError("Money object is not initialized")

        return self.__money.getAmountMajor()

    def getAmount(self) -> decimal.Decimal:

        if self.__money is None:
            return None
        else:
            return self.__money.getAmount()

    def getScale(self) -> int:

        if self.__money is None:
            raise ValueError("Money object is not initialized")

        return self.__money.getScale()

    def withCurrencyUnit1(
        self, currency: CurrencyUnit, roundingMode: typing.Any
    ) -> Money:

        new_money = self.__money.withCurrencyUnit(currency).withCurrencyScale1(
            roundingMode
        )
        return self.__with(new_money)

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

        if monies is None:
            raise ValueError("Money iterator must not be null")

        it = iter(monies)

        try:
            total = next(it)
        except StopIteration:
            raise ValueError("Money iterator must not be empty")

        if total is None:
            raise ValueError("Money iterator must not contain null entries")

        for money in it:
            total = total.plus1(money)

        return total

    @staticmethod
    def total0(monies: typing.List[Money]) -> Money:

        if monies is None:
            raise ValueError("Money array must not be null")
        if len(monies) == 0:
            raise ValueError("Money array must not be empty")
        total = monies[0]
        if total is None:
            raise ValueError("Money array must not contain null entries")
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
        bd = decimal.Decimal(0).scaleb(currency.getDecimalPlaces())
        return Money(0, BigMoney.of0(currency, bd))

    @staticmethod
    def ofMinor(currency: CurrencyUnit, amountMinor: int) -> Money:

        return Money(0, BigMoney.ofMinor(currency, amountMinor))

    @staticmethod
    def ofMajor(currency: CurrencyUnit, amountMajor: int) -> Money:

        return Money.of1(currency, decimal.Decimal(amountMajor), decimal.ROUND_DOWN)

    @staticmethod
    def of3(currency: CurrencyUnit, amount: float, roundingMode: typing.Any) -> Money:

        return Money.of1(currency, decimal.Decimal(amount), roundingMode)

    @staticmethod
    def of2(currency: CurrencyUnit, amount: float) -> Money:

        return Money.of0(currency, decimal.Decimal(amount))

    @staticmethod
    def of1(
        currency: CurrencyUnit, amount: decimal.Decimal, roundingMode: typing.Any
    ) -> Money:

        MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")
        MoneyUtils.checkNotNull(amount, "Amount must not be null")
        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        scaledAmount = amount.quantize(
            decimal.Decimal(10) ** -currency.getDecimalPlaces(), rounding=roundingMode
        )

        return Money(0, BigMoney.of0(currency, scaledAmount))

    @staticmethod
    def of0(currency: CurrencyUnit, amount: decimal.Decimal) -> Money:

        MoneyUtils.checkNotNull(currency, "Currency must not be null")
        MoneyUtils.checkNotNull(amount, "Amount must not be null")
        if amount.as_tuple().exponent > currency.getDecimalPlaces():
            raise ArithmeticError(
                "Scale of amount "
                + str(amount)
                + " is greater than the scale of the currency "
                + str(currency)
            )
        return Money.of1(currency, amount, decimal.ROUND_DOWN)

    def __with(self, newInstance: BigMoney) -> Money:

        if self.__money.equals(newInstance):
            return self
        return Money(0, newInstance)

    def __writeReplace(self) -> typing.Any:

        return Ser(0, self, Ser.MONEY)

    def __readObject(self, ois: pickle.Unpickler) -> None:

        raise InvalidObjectException("Serialization delegate required")
