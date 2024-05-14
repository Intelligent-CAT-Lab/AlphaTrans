# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import typing

# Imports End


class MoneyUtils:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def subtract1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        pass

    @staticmethod
    def add1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        pass

    @staticmethod
    def min1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        pass

    @staticmethod
    def max1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        pass

    @staticmethod
    def subtract0(money1: Money, money2: Money) -> Money:
        pass

    @staticmethod
    def add0(money1: Money, money2: Money) -> Money:
        pass

    @staticmethod
    def min0(money1: Money, money2: Money) -> Money:
        pass

    @staticmethod
    def max0(money1: Money, money2: Money) -> Money:
        pass

    @staticmethod
    def isNegativeOrZero(moneyProvider: BigMoneyProvider) -> bool:
        pass

    @staticmethod
    def isNegative(moneyProvider: BigMoneyProvider) -> bool:
        pass

    @staticmethod
    def isPositiveOrZero(moneyProvider: BigMoneyProvider) -> bool:
        pass

    @staticmethod
    def isPositive(moneyProvider: BigMoneyProvider) -> bool:
        pass

    @staticmethod
    def isZero(moneyProvider: BigMoneyProvider) -> bool:
        pass

    @staticmethod
    def checkNotNull(object: typing.Any, message: str) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
