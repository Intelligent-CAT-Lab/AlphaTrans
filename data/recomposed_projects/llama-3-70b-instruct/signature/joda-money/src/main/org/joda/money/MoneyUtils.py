from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.Money import *


class MoneyUtils:

    @staticmethod
    def subtract1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        if money2 is None:
            return money1
        if money1 is None:
            return money2.negated()
        return money1.minus1(money2)

    @staticmethod
    def add1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        if money1 is None:
            return money2
        if money2 is None:
            return money1
        return money1.plus1(money2)

    @staticmethod
    def min1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        if money1 is None:
            return money2
        if money2 is None:
            return money1
        return money1 if money1.compareTo(money2) < 0 else money2

    @staticmethod
    def max1(money1: BigMoney, money2: BigMoney) -> BigMoney:
        if money1 is None:
            return money2
        if money2 is None:
            return money1
        return money1 if money1.compareTo(money2) > 0 else money2

    @staticmethod
    def subtract0(money1: Money, money2: Money) -> Money:
        if money2 is None:
            return money1
        if money1 is None:
            return money2.negated()
        return money1.minus1(money2)

    @staticmethod
    def add0(money1: Money, money2: Money) -> Money:
        if money1 is None:
            return money2
        if money2 is None:
            return money1
        return money1.plus1(money2)

    @staticmethod
    def min0(money1: Money, money2: Money) -> Money:
        if money1 is None:
            return money2
        if money2 is None:
            return money1
        return money1 if money1.compareTo(money2) < 0 else money2

    @staticmethod
    def max0(money1: Money, money2: Money) -> Money:
        if money1 is None:
            return money2
        if money2 is None:
            return money1
        return money1 if money1.compareTo(money2) > 0 else money2

    @staticmethod
    def isNegativeOrZero(moneyProvider: BigMoneyProvider) -> bool:
        return moneyProvider == None or moneyProvider.toBigMoney().isNegativeOrZero()

    @staticmethod
    def isNegative(moneyProvider: BigMoneyProvider) -> bool:
        return moneyProvider != None and moneyProvider.toBigMoney().isNegative()

    @staticmethod
    def isPositiveOrZero(moneyProvider: BigMoneyProvider) -> bool:
        return moneyProvider == None or moneyProvider.toBigMoney().isPositiveOrZero()

    @staticmethod
    def isPositive(moneyProvider: BigMoneyProvider) -> bool:
        return moneyProvider != None and moneyProvider.toBigMoney().isPositive()

    @staticmethod
    def isZero(moneyProvider: BigMoneyProvider) -> bool:
        return moneyProvider == None or moneyProvider.toBigMoney().isZero()

    @staticmethod
    def checkNotNull(object: typing.Any, message: str) -> None:
        if object is None:
            raise RuntimeError(message)

    def __init__(self) -> None:
        pass
