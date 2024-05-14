# Imports Begin
from src.main.org.joda.money.Ser import *
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import typing

# Imports End


class Money(Serializable, Comparable, BigMoneyProvider):

    # Class Fields Begin
    __serialVersionUID: int = None
    __money: BigMoney = None
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

    def __init__(self, constructorId: int, money: BigMoney) -> None:
        pass

    @staticmethod
    def parse(moneyStr: str) -> "Money":
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

    def isSameCurrency(self, other: BigMoneyProvider) -> bool:
        pass

    def convertedTo(
        self,
        currency: CurrencyUnit,
        conversionMultipler: decimal.Decimal,
        roundingMode: typing.Any,
    ) -> "Money":
        pass

    def rounded(self, scale: int, roundingMode: typing.Any) -> "Money":
        pass

    def abs(self) -> "Money":
        pass

    def negated(self) -> "Money":
        pass

    def dividedBy2(self, valueToDivideBy: int, roundingMode: typing.Any) -> "Money":
        pass

    def dividedBy1(self, valueToDivideBy: float, roundingMode: typing.Any) -> "Money":
        pass

    def dividedBy0(
        self, valueToDivideBy: decimal.Decimal, roundingMode: typing.Any
    ) -> "Money":
        pass

    def multipliedBy2(self, valueToMultiplyBy: int) -> "Money":
        pass

    def multipliedBy1(
        self, valueToMultiplyBy: float, roundingMode: typing.Any
    ) -> "Money":
        pass

    def multipliedBy0(
        self, valueToMultiplyBy: decimal.Decimal, roundingMode: typing.Any
    ) -> "Money":
        pass

    def minusMinor(self, amountToSubtract: int) -> "Money":
        pass

    def minusMajor(self, amountToSubtract: int) -> "Money":
        pass

    def minus5(self, amountToSubtract: float, roundingMode: typing.Any) -> "Money":
        pass

    def minus4(self, amountToSubtract: float) -> "Money":
        pass

    def minus3(
        self, amountToSubtract: decimal.Decimal, roundingMode: typing.Any
    ) -> "Money":
        pass

    def minus2(self, amountToSubtract: decimal.Decimal) -> "Money":
        pass

    def minus1(self, moneyToSubtract: Money) -> "Money":
        pass

    def minus0(self, moniesToSubtract: typing.Iterable[Money]) -> "Money":
        pass

    def plusMinor(self, amountToAdd: int) -> "Money":
        pass

    def plusMajor(self, amountToAdd: int) -> "Money":
        pass

    def plus5(self, amountToAdd: float, roundingMode: typing.Any) -> "Money":
        pass

    def plus4(self, amountToAdd: float) -> "Money":
        pass

    def plus3(self, amountToAdd: decimal.Decimal, roundingMode: typing.Any) -> "Money":
        pass

    def plus2(self, amountToAdd: decimal.Decimal) -> "Money":
        pass

    def plus1(self, moneyToAdd: Money) -> "Money":
        pass

    def plus0(self, moniesToAdd: typing.Iterable[Money]) -> "Money":
        pass

    def withAmount3(self, amount: float, roundingMode: typing.Any) -> "Money":
        pass

    def withAmount2(self, amount: float) -> "Money":
        pass

    def withAmount1(self, amount: decimal.Decimal, roundingMode: typing.Any) -> "Money":
        pass

    def withAmount0(self, amount: decimal.Decimal) -> "Money":
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

    def getScale(self) -> int:
        pass

    def withCurrencyUnit1(
        self, currency: CurrencyUnit, roundingMode: typing.Any
    ) -> "Money":
        pass

    def withCurrencyUnit0(self, currency: CurrencyUnit) -> "Money":
        pass

    def getCurrencyUnit(self) -> CurrencyUnit:
        pass

    @staticmethod
    def total3(currency: CurrencyUnit, monies: typing.Iterable[Money]) -> "Money":
        pass

    @staticmethod
    def total2(currency: CurrencyUnit, monies: typing.List[Money]) -> "Money":
        pass

    @staticmethod
    def total1(monies: typing.Iterable[Money]) -> "Money":
        pass

    @staticmethod
    def total0(monies: typing.List[Money]) -> "Money":
        pass

    @staticmethod
    def of5(moneyProvider: BigMoneyProvider, roundingMode: typing.Any) -> "Money":
        pass

    @staticmethod
    def of4(moneyProvider: BigMoneyProvider) -> "Money":
        pass

    @staticmethod
    def zero(currency: CurrencyUnit) -> "Money":
        pass

    @staticmethod
    def ofMinor(currency: CurrencyUnit, amountMinor: int) -> "Money":
        pass

    @staticmethod
    def ofMajor(currency: CurrencyUnit, amountMajor: int) -> "Money":
        pass

    @staticmethod
    def of3(currency: CurrencyUnit, amount: float, roundingMode: typing.Any) -> "Money":
        pass

    @staticmethod
    def of2(currency: CurrencyUnit, amount: float) -> "Money":
        pass

    @staticmethod
    def of1(
        currency: CurrencyUnit, amount: decimal.Decimal, roundingMode: typing.Any
    ) -> "Money":
        pass

    @staticmethod
    def of0(currency: CurrencyUnit, amount: decimal.Decimal) -> "Money":
        pass

    def __with(self, newInstance: BigMoney) -> "Money":
        pass

    def __writeReplace(self) -> typing.Any:
        pass

    def __readObject(self, ois: pickle.Unpickler) -> None:
        pass

    # Class Methods End
