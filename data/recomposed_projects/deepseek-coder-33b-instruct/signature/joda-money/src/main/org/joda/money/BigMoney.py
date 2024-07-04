from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
import decimal
import os
import pickle

# from src.main.org.joda.convert.FromString import *
# from src.main.org.joda.convert.ToString import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.Ser import *


class BigMoney:

    __amount: decimal.Decimal = None

    __currency: CurrencyUnit = None

    __PARSE_REGEX: re.Pattern = re.compile("[+-]?[0-9]*[.]?[0-9]*")
    __serialVersionUID: int = 1

    def toString(self) -> str:
        return f"{self.__currency.getCode()} {str(self.__amount)}"

    def hashCode(self) -> int:
        return hash(self.__currency) ^ hash(self.__amount)

    def equals(self, other: typing.Any) -> bool:

        if self is other:
            return True
        if isinstance(other, BigMoney):
            other_money = typing.cast(BigMoney, other)
            return (
                self.__currency.equals(other_money.getCurrencyUnit())
                and self.__amount == other_money.__amount
            )
        return False

    def compareTo(self, other: BigMoneyProvider) -> int:

        otherMoney = BigMoney.of2(other)

        if self.currency.equals(otherMoney.getCurrencyUnit()) == False:
            raise CurrencyMismatchException(
                self.getCurrencyUnit(), otherMoney.getCurrencyUnit()
            )

        return self.amount.compareTo(otherMoney.amount)

    def toBigMoney(self) -> BigMoney:
        return self

    def __init__(
        self, constructorId: int, amount: decimal.Decimal, currency: CurrencyUnit
    ) -> None:

        if constructorId == 0:
            assert currency is not None, "Joda-Money bug: Currency must not be null"
            assert amount is not None, "Joda-Money bug: Amount must not be null"
            self.__currency = currency
            self.__amount = (
                amount
                if amount.as_tuple().exponent >= 0
                else amount.quantize(decimal.Decimal(1))
            )
        else:
            self.__currency = None
            self.__amount = None

    @staticmethod
    def parse(moneyStr: str) -> BigMoney:

        MoneyUtils.checkNotNull(moneyStr, "Money must not be null")
        if len(moneyStr) < 4:
            raise ValueError("Money '" + moneyStr + "' cannot be parsed")
        currStr = moneyStr[0:3]
        amountStart = 3
        while amountStart < len(moneyStr) and moneyStr[amountStart] == " ":
            amountStart += 1
        amountStr = moneyStr[amountStart:]
        if not BigMoney.__PARSE_REGEX.match(amountStr):
            raise ValueError("Money amount '" + moneyStr + "' cannot be parsed")
        return BigMoney.of0(CurrencyUnit.of1(currStr), decimal.Decimal(amountStr))

    def isLessThanOrEqual(self, other: BigMoneyProvider) -> bool:
        return self.compareTo(other) <= 0

    def isLessThan(self, other: BigMoneyProvider) -> bool:
        return self.compareTo(other) < 0

    def isGreaterThanOrEqual(self, other: BigMoneyProvider) -> bool:
        return self.compareTo(other) >= 0

    def isGreaterThan(self, other: BigMoneyProvider) -> bool:
        return self.compareTo(other) > 0

    def isEqual(self, other: BigMoneyProvider) -> bool:
        return self.compareTo(other) == 0

    def isSameCurrency(self, money: BigMoneyProvider) -> bool:
        return self.__currency.equals(BigMoney.of2(money).getCurrencyUnit())

    def toMoney1(self, roundingMode: typing.Any) -> Money:
        return Money.of5(self, roundingMode)

    def toMoney0(self) -> Money:
        return Money.of4(self)

    def convertRetainScale(
        self,
        currency: CurrencyUnit,
        conversionMultipler: decimal.Decimal,
        roundingMode: typing.Any,
    ) -> BigMoney:
        return self.convertedTo(currency, conversionMultipler).withScale1(
            self.getScale(), roundingMode
        )

    def convertedTo(
        self, currency: CurrencyUnit, conversionMultipler: decimal.Decimal
    ) -> BigMoney:

        MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")
        MoneyUtils.checkNotNull(conversionMultipler, "Multiplier must not be null")

        if self.__currency == currency:
            if conversionMultipler == decimal.Decimal(1):
                return self
            raise Exception("Cannot convert to the same currency")

        if conversionMultipler < decimal.Decimal(0):
            raise Exception("Cannot convert using a negative conversion multiplier")

        newAmount = self.__amount * conversionMultipler
        return BigMoney.of0(currency, newAmount)

    def rounded(self, scale: int, roundingMode: typing.Any) -> BigMoney:

        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        if scale >= self.getScale():
            return self

        currentScale = self.__amount.as_tuple().exponent
        newAmount = self.__amount.quantize(
            decimal.Decimal(10) ** -scale, rounding=roundingMode
        )
        newAmount = newAmount.quantize(decimal.Decimal(10) ** -currentScale)

        return BigMoney.of0(self.__currency, newAmount)

    def abs(self) -> BigMoney:
        return self.negated() if self.isNegative() else self

    def negated(self) -> BigMoney:
        if self.isZero():
            return self
        return BigMoney.of0(self.__currency, self.__amount.copy_negate())

    def dividedBy2(self, valueToDivideBy: int, roundingMode: typing.Any) -> BigMoney:

        if valueToDivideBy == 1:
            return self

        newAmount = self.__amount.divide(decimal.Decimal(valueToDivideBy), roundingMode)
        return BigMoney.of0(self.__currency, newAmount)

    def dividedBy1(self, valueToDivideBy: float, roundingMode: typing.Any) -> BigMoney:

        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        if valueToDivideBy == 1:
            return self

        newAmount = self.__amount.divide(decimal.Decimal(valueToDivideBy), roundingMode)

        return BigMoney.of0(self.__currency, newAmount)

    def dividedBy0(
        self, valueToDivideBy: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:

        MoneyUtils.checkNotNull(valueToDivideBy, "Divisor must not be null")
        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        if valueToDivideBy == decimal.Decimal(1):
            return self

        newAmount = self.__amount.quantize(
            decimal.Decimal(1) / valueToDivideBy, rounding=roundingMode
        )

        return BigMoney.of0(self.__currency, newAmount)

    def multiplyRetainScale1(
        self, valueToMultiplyBy: float, roundingMode: typing.Any
    ) -> BigMoney:
        return self.multiplyRetainScale0(
            decimal.Decimal(valueToMultiplyBy), roundingMode
        )

    def multiplyRetainScale0(
        self, valueToMultiplyBy: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:

        MoneyUtils.checkNotNull(valueToMultiplyBy, "Multiplier must not be null")
        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        if valueToMultiplyBy == decimal.Decimal(1):
            return self

        newAmount = self.__amount * valueToMultiplyBy
        newAmount = newAmount.quantize(
            decimal.Decimal(10) ** -self.getScale(), rounding=roundingMode
        )

        return BigMoney.of0(self.__currency, newAmount)

    def multipliedBy2(self, valueToMultiplyBy: int) -> BigMoney:

        if valueToMultiplyBy == 1:
            return self

        newAmount = self.__amount.multiply(decimal.Decimal(valueToMultiplyBy))
        return BigMoney.of0(self.__currency, newAmount)

    def multipliedBy1(self, valueToMultiplyBy: float) -> BigMoney:

        if valueToMultiplyBy == 1:
            return self

        newAmount = self.__amount.multiply(decimal.Decimal(valueToMultiplyBy))
        return BigMoney.of0(self.__currency, newAmount)

    def multipliedBy0(self, valueToMultiplyBy: decimal.Decimal) -> BigMoney:

        MoneyUtils.checkNotNull(valueToMultiplyBy, "Multiplier must not be null")

        if valueToMultiplyBy.compare_to(decimal.Decimal(1)) == 0:
            return self

        newAmount = self.__amount.multiply(valueToMultiplyBy)

        return BigMoney.of0(self.__currency, newAmount)

    def minusRetainScale2(
        self, amountToSubtract: float, roundingMode: typing.Any
    ) -> BigMoney:

        if amountToSubtract == 0:
            return self

        newAmount = self.__amount - decimal.Decimal(amountToSubtract)
        newAmount = newAmount.quantize(
            decimal.Decimal(10) ** -self.getScale(), rounding=roundingMode
        )
        return BigMoney.of0(self.__currency, newAmount)

    def minusRetainScale1(
        self, amountToSubtract: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:

        MoneyUtils.checkNotNull(amountToSubtract, "Amount must not be null")

        if amountToSubtract.compare(decimal.Decimal(0)) == 0:
            return self

        newAmount = self.__amount.subtract(amountToSubtract)
        newAmount = newAmount.setScale(self.getScale(), roundingMode)

        return BigMoney.of0(self.__currency, newAmount)

    def minusRetainScale0(
        self, moneyToSubtract: BigMoneyProvider, roundingMode: typing.Any
    ) -> BigMoney:

        toSubtract = self.__checkCurrencyEqual(moneyToSubtract)
        return self.minusRetainScale1(toSubtract.getAmount(), roundingMode)

    def minusMinor(self, amountToSubtract: int) -> BigMoney:

        if amountToSubtract == 0:
            return self

        newAmount = self.amount - decimal.Decimal(amountToSubtract) / (
            10 ** self.currency.getDecimalPlaces()
        )

        return BigMoney.of0(self.currency, newAmount)

    def minusMajor(self, amountToSubtract: int) -> BigMoney:

        if amountToSubtract == 0:
            return self

        newAmount = self.__amount - decimal.Decimal(amountToSubtract)
        return BigMoney.of0(self.__currency, newAmount)

    def minus3(self, amountToSubtract: float) -> BigMoney:

        if amountToSubtract == 0:
            return self

        newAmount = self.__amount - decimal.Decimal(amountToSubtract)
        return BigMoney.of0(self.__currency, newAmount)

    def minus2(self, amountToSubtract: decimal.Decimal) -> BigMoney:

        MoneyUtils.checkNotNull(amountToSubtract, "Amount must not be null")

        if amountToSubtract.compare_to(decimal.Decimal(0)) == 0:
            return self

        newAmount = self.__amount.subtract(amountToSubtract)

        return BigMoney.of0(self.__currency, newAmount)

    def minus1(self, moneyToSubtract: BigMoneyProvider) -> BigMoney:

        toSubtract = self.__checkCurrencyEqual(moneyToSubtract)
        return self.minus2(toSubtract.getAmount())

    def minus0(self, moniesToSubtract: typing.Iterable[BigMoneyProvider]) -> BigMoney:

        total = self.__amount
        for moneyProvider in moniesToSubtract:
            money = self.__checkCurrencyEqual(moneyProvider)
            total = total - money.__amount
        return self.__with(total)

    def plusRetainScale2(
        self, amountToAdd: float, roundingMode: typing.Any
    ) -> BigMoney:

        if amountToAdd == 0:
            return self

        newAmount = self.__amount + decimal.Decimal(amountToAdd)
        newAmount = newAmount.quantize(
            decimal.Decimal(10) ** -self.getScale(), rounding=roundingMode
        )
        return BigMoney.of0(self.__currency, newAmount)

    def plusRetainScale1(
        self, amountToAdd: decimal.Decimal, roundingMode: typing.Any
    ) -> BigMoney:

        MoneyUtils.checkNotNull(amountToAdd, "Amount must not be null")

        if amountToAdd.compare_to(decimal.Decimal(0)) == 0:
            return self

        newAmount = self.__amount.add(amountToAdd)
        newAmount = newAmount.setScale(self.getScale(), roundingMode)

        return BigMoney.of0(self.__currency, newAmount)

    def plusRetainScale0(
        self, moneyToAdd: BigMoneyProvider, roundingMode: typing.Any
    ) -> BigMoney:

        toAdd = self.__checkCurrencyEqual(moneyToAdd)
        return self.plusRetainScale1(toAdd.getAmount(), roundingMode)

    def plusMinor(self, amountToAdd: int) -> BigMoney:

        if amountToAdd == 0:
            return self

        newAmount = self.amount + decimal.Decimal(amountToAdd) / (
            10 ** self.currency.getDecimalPlaces()
        )

        return BigMoney.of0(self.currency, newAmount)

    def plusMajor(self, amountToAdd: int) -> BigMoney:

        if amountToAdd == 0:
            return self

        newAmount = self.__amount + decimal.Decimal(amountToAdd)
        return BigMoney.of0(self.__currency, newAmount)

    def plus3(self, amountToAdd: float) -> BigMoney:

        if amountToAdd == 0:
            return self

        newAmount = self.__amount + decimal.Decimal(amountToAdd)
        return BigMoney.of0(self.__currency, newAmount)

    def plus2(self, amountToAdd: decimal.Decimal) -> BigMoney:

        MoneyUtils.checkNotNull(amountToAdd, "Amount must not be null")

        if amountToAdd.compare_to(decimal.Decimal(0)) == 0:
            return self

        newAmount = self.__amount.add(amountToAdd)

        return BigMoney.of0(self.__currency, newAmount)

    def plus1(self, moneyToAdd: BigMoneyProvider) -> BigMoney:

        toAdd = self.__checkCurrencyEqual(moneyToAdd)
        return self.plus2(toAdd.getAmount())

    def plus0(self, moniesToAdd: typing.Iterable[BigMoneyProvider]) -> BigMoney:

        total = self.__amount
        for moneyProvider in moniesToAdd:
            money = self.__checkCurrencyEqual(moneyProvider)
            total = total + money.__amount
        return self.__with(total)

    def withAmount1(self, amount: float) -> BigMoney:
        return self.withAmount0(decimal.Decimal(amount))

    def withAmount0(self, amount: decimal.Decimal) -> BigMoney:

        MoneyUtils.checkNotNull(amount, "Amount must not be null")

        if self.__amount == amount:
            return self

        return BigMoney.of0(self.__currency, amount)

    def isNegativeOrZero(self) -> bool:
        return self.__amount <= decimal.Decimal(0)

    def isNegative(self) -> bool:
        return self.__amount < decimal.Decimal(0)

    def isPositiveOrZero(self) -> bool:
        return self.__amount >= decimal.Decimal(0)

    def isPositive(self) -> bool:
        return self.__amount > decimal.Decimal(0)

    def isZero(self) -> bool:
        return self.__amount == decimal.Decimal(0)

    def getMinorPart(self) -> int:

        cdp = self.getCurrencyUnit().getDecimalPlaces()
        return (
            (
                self.__amount.quantize(
                    decimal.Decimal(10) ** -cdp, rounding=decimal.ROUND_DOWN
                )
                % 1
            )
            .scaleb(cdp)
            .normalize()
        )

    def getAmountMinorInt(self) -> int:
        return self.getAmountMinor().to_integral_value(decimal.ROUND_HALF_UP)

    def getAmountMinorLong(self) -> int:
        return int(self.getAmountMinor())

    def getAmountMinor(self) -> decimal.Decimal:
        cdp = self.getCurrencyUnit().getDecimalPlaces()
        return self.__amount.quantize(
            decimal.Decimal(10) ** -cdp, decimal.ROUND_DOWN
        ) * (10**cdp)

    def getAmountMajorInt(self) -> int:
        return self.getAmountMajor().to_integral_value(decimal.ROUND_HALF_EVEN)

    def getAmountMajorLong(self) -> int:
        return self.getAmountMajor().to_integral_value(decimal.ROUND_HALF_UP)

    def getAmountMajor(self) -> decimal.Decimal:
        return self.__amount.quantize(decimal.Decimal("1"), rounding=decimal.ROUND_DOWN)

    def getAmount(self) -> decimal.Decimal:
        return self.__amount

    def withCurrencyScale1(self, roundingMode: typing.Any) -> BigMoney:
        return self.withScale1(self.__currency.getDecimalPlaces(), roundingMode)

    def withCurrencyScale0(self) -> BigMoney:
        return self.withScale1(self.__currency.getDecimalPlaces(), decimal.ROUND_DOWN)

    def withScale1(self, scale: int, roundingMode: typing.Any) -> BigMoney:

        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        if scale == self.__amount.as_tuple().exponent:
            return self

        return BigMoney.of0(
            self.__currency,
            self.__amount.quantize(
                decimal.Decimal(10) ** -scale, rounding=roundingMode
            ),
        )

    def withScale0(self, scale: int) -> BigMoney:
        return self.withScale1(scale, decimal.ROUND_DOWN)

    def isCurrencyScale(self) -> bool:
        return self.__amount.as_tuple().exponent == -self.__currency.getDecimalPlaces()

    def getScale(self) -> int:
        return self.__amount.as_tuple().exponent

    def withCurrencyUnit(self, currency: CurrencyUnit) -> BigMoney:

        MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")

        if self.__currency == currency:
            return self

        return BigMoney(0, self.__amount, currency)

    def getCurrencyUnit(self) -> CurrencyUnit:
        return self.__currency

    @staticmethod
    def total3(
        currency: CurrencyUnit, monies: typing.Iterable[BigMoneyProvider]
    ) -> BigMoney:
        return BigMoney.zero0(currency).plus0(monies)

    @staticmethod
    def total2(
        currency: CurrencyUnit, monies: typing.List[BigMoneyProvider]
    ) -> BigMoney:
        return BigMoney.zero0(currency).plus0(monies)

    @staticmethod
    def total1(monies: typing.Iterable[BigMoneyProvider]) -> BigMoney:

        MoneyUtils.checkNotNull(monies, "Money iterator must not be null")
        it = iter(monies)
        try:
            first = next(it)
        except StopIteration:
            raise ValueError("Money iterator must not be empty")
        total = BigMoney.of2(first)
        MoneyUtils.checkNotNull(total, "Money iterator must not contain null entries")
        for money in it:
            total = total.plus1(money)
        return total

    @staticmethod
    def total0(monies: typing.List[BigMoneyProvider]) -> BigMoney:

        MoneyUtils.checkNotNull(monies, "Money array must not be null")
        if len(monies) == 0:
            raise ValueError("Money array must not be empty")
        total = BigMoney.of2(monies[0])
        MoneyUtils.checkNotNull(total, "Money array must not contain null entries")
        for i in range(1, len(monies)):
            total = total.plus1(BigMoney.of2(monies[i]))
        return total

    @staticmethod
    def of2(moneyProvider: BigMoneyProvider) -> BigMoney:

        MoneyUtils.checkNotNull(moneyProvider, "BigMoneyProvider must not be null")
        money = moneyProvider.toBigMoney()
        MoneyUtils.checkNotNull(money, "BigMoneyProvider must not return null")
        return money

    @staticmethod
    def zero1(currency: CurrencyUnit, scale: int) -> BigMoney:
        return BigMoney.of0(currency, decimal.Decimal(0).scaleb(scale))

    @staticmethod
    def zero0(currency: CurrencyUnit) -> BigMoney:
        return BigMoney.of0(currency, decimal.Decimal(0))

    @staticmethod
    def ofMinor(currency: CurrencyUnit, amountMinor: int) -> BigMoney:

        MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")
        return BigMoney.of0(
            currency,
            decimal.Decimal(amountMinor)
            / decimal.Decimal(10 ** currency.getDecimalPlaces()),
        )

    @staticmethod
    def ofMajor(currency: CurrencyUnit, amountMajor: int) -> BigMoney:
        MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")
        return BigMoney.of0(currency, decimal.Decimal(amountMajor))

    @staticmethod
    def ofScale2(currency: CurrencyUnit, unscaledAmount: int, scale: int) -> BigMoney:
        MoneyUtils.checkNotNull(currency, "Currency must not be null")
        return BigMoney.of0(currency, decimal.Decimal(unscaledAmount) / (10**scale))

    @staticmethod
    def ofScale1(
        currency: CurrencyUnit,
        amount: decimal.Decimal,
        scale: int,
        roundingMode: typing.Any,
    ) -> BigMoney:

        MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null")
        MoneyUtils.checkNotNull(amount, "Amount must not be null")
        MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null")

        scaledAmount = amount.quantize(
            decimal.Decimal(10) ** -scale, rounding=roundingMode
        )

        return BigMoney.of0(currency, scaledAmount)

    @staticmethod
    def ofScale0(
        currency: CurrencyUnit, amount: decimal.Decimal, scale: int
    ) -> BigMoney:
        return BigMoney.ofScale1(currency, amount, scale, decimal.ROUND_UP)

    @staticmethod
    def of1(currency: CurrencyUnit, amount: float) -> BigMoney:

        MoneyUtils.checkNotNull(currency, "Currency must not be null")

        if amount == 0.0:
            return BigMoney.zero0(currency)

        return BigMoney.of0(currency, decimal.Decimal(amount).normalize())

    @staticmethod
    def of0(currency: CurrencyUnit, amount: decimal.Decimal) -> BigMoney:

        MoneyUtils.checkNotNull(currency, "Currency must not be null")
        MoneyUtils.checkNotNull(amount, "Amount must not be null")

        checkedAmount = amount

        if type(amount) != decimal.Decimal:
            value = amount.as_tuple().digits
            if value is None:
                raise ValueError("Illegal Decimal subclass")
            if type(value) != tuple:
                value = tuple(str(value))
            checkedAmount = decimal.Decimal(value)

        return BigMoney(0, checkedAmount, currency)

    def __checkCurrencyEqual(self, moneyProvider: BigMoneyProvider) -> BigMoney:

        money = self.of2(moneyProvider)
        if not self.isSameCurrency(money):
            raise CurrencyMismatchException(
                self.getCurrencyUnit(), money.getCurrencyUnit()
            )
        return money

    def __with(self, newAmount: decimal.Decimal) -> BigMoney:
        if newAmount == self.__amount:
            return self
        return BigMoney(0, newAmount, self.__currency)

    def __writeReplace(self) -> typing.Any:
        return Ser(0, self, Ser.BIG_MONEY)

    def __readObject(self, ois: pickle.Unpickler) -> None:
        raise pickle.UnpicklingError("Serialization delegate required")
