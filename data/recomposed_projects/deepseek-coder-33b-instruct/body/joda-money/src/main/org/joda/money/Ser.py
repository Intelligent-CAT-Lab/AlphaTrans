from __future__ import annotations
import re
import decimal
import io
import typing
from typing import *
import pickle
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class Ser:

    CURRENCY_UNIT: int = 0
    MONEY: int = 0
    BIG_MONEY: int = 0
    __object: typing.Any = None

    __type: int = 0

    def readExternal(self, in_: pickle.Unpickler) -> None:

        self.__type = in_.load()
        if self.__type == self.BIG_MONEY:
            self.__object = self.__readBigMoney(in_)
        elif self.__type == self.MONEY:
            self.__object = Money(0, self.__readBigMoney(in_))
        elif self.__type == self.CURRENCY_UNIT:
            self.__object = self.__readCurrency(in_)
        else:
            raise pickle.UnpicklingError("Serialization input has invalid type")

    def writeExternal(self, out: pickle.Pickler) -> None:
        out.dump(self.__type)
        if self.__type == self.BIG_MONEY:
            obj = typing.cast(BigMoney, self.__object)
            self.__writeBigMoney(out, obj)
        elif self.__type == self.MONEY:
            obj = typing.cast(Money, self.__object)
            self.__writeBigMoney(out, obj.toBigMoney())
        elif self.__type == self.CURRENCY_UNIT:
            obj = typing.cast(CurrencyUnit, self.__object)
            self.__writeCurrency(out, obj)
        else:
            raise pickle.PicklingError("Joda-Money bug: Serialization broken")

    def __init__(self, constructorId: int, object: typing.Any, type: int) -> None:

        if constructorId == 0:
            self.__type = type
            self.__object = object
        else:
            pass

    def __readResolve(self) -> typing.Any:
        return self.__object

    def __readCurrency(self, in_: pickle.Unpickler) -> CurrencyUnit:
        code = in_.load()
        singletonCurrency = CurrencyUnit.of1(code)
        if singletonCurrency.getNumericCode() != in_.load():
            raise pickle.UnpicklingError(
                "Deserialization found a mismatch in the numeric code for currency "
                + code
            )
        if singletonCurrency.getDecimalPlaces() != in_.load():
            raise pickle.UnpicklingError(
                "Deserialization found a mismatch in the decimal places for currency "
                + code
            )
        return singletonCurrency

    def __readBigMoney(self, in_: pickle.Unpickler) -> BigMoney:

        currency = self.__readCurrency(in_)
        bytes_ = in_.load()
        bd = decimal.Decimal(bytes_)
        bigMoney = BigMoney(0, bd, currency)
        return bigMoney

    def __writeCurrency(self, out: pickle.Pickler, obj: CurrencyUnit) -> None:
        out.dump(obj.getCode())
        out.dump(obj.getNumericCode())
        out.dump(obj.getDecimalPlaces())

    def __writeBigMoney(self, out: pickle.Pickler, obj: BigMoney) -> None:
        self.__writeCurrency(out, obj.getCurrencyUnit())
        bytes_ = obj.getAmount().as_tuple().digits
        out.dump(len(bytes_))
        for byte in bytes_:
            out.dump(byte)
        out.dump(obj.getScale())
