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

    CURRENCY_UNIT: int = 67
    MONEY: int = 77
    BIG_MONEY: int = 66
    __object: typing.Any = None

    __type: int = 0

    def readExternal(self, in_: pickle.Unpickler) -> None:
        self.__type = in_.read_byte()
        if self.__type == self.BIG_MONEY:
            self.__object = self.__readBigMoney(in_)
            return
        if self.__type == self.MONEY:
            self.__object = Money(0, self.__readBigMoney(in_))
            return
        if self.__type == self.CURRENCY_UNIT:
            self.__object = self.__readCurrency(in_)
            return
        raise StreamCorruptedException("Serialization input has invalid type")

    def writeExternal(self, out: pickle.Pickler) -> None:
        out.write(self.__type)
        if self.__type == self.BIG_MONEY:
            obj = typing.cast(BigMoney, self.__object)
            self.__writeBigMoney(out, obj)
            return
        if self.__type == self.MONEY:
            obj = typing.cast(Money, self.__object)
            self.__writeBigMoney(out, obj.toBigMoney())
            return
        if self.__type == self.CURRENCY_UNIT:
            obj = typing.cast(CurrencyUnit, self.__object)
            self.__writeCurrency(out, obj)
            return
        raise Exception("Joda-Money bug: Serialization broken")

    def __init__(self, constructorId: int, object: typing.Any, type: int) -> None:
        if constructorId == 0:
            self.__type = type
            self.__object = object
        else:
            pass

    def __readResolve(self) -> typing.Any:
        return self.__object

    def __readCurrency(self, in_: pickle.Unpickler) -> CurrencyUnit:
        code: str = in_.read_string()
        singletonCurrency: CurrencyUnit = CurrencyUnit.of1(code)
        if singletonCurrency.getNumericCode() != in_.read_short():
            raise InvalidObjectException(
                "Deserialization found a mismatch in the numeric code for currency "
                + code
            )
        if singletonCurrency.getDecimalPlaces() != in_.read_short():
            raise InvalidObjectException(
                "Deserialization found a mismatch in the decimal places for currency "
                + code
            )
        return singletonCurrency

    def __readBigMoney(self, in_: pickle.Unpickler) -> BigMoney:
        currency: CurrencyUnit = self.__readCurrency(in_)
        bytes: bytes = in_.read_bytes(in_.read_int())
        bd: decimal.Decimal = decimal.Decimal(bytes, in_.read_int())
        bigMoney: BigMoney = BigMoney(0, bd, currency)
        return bigMoney

    def __writeCurrency(self, out: pickle.Pickler, obj: CurrencyUnit) -> None:
        out.write(obj.getCode())
        out.write(obj.getNumericCode())
        out.write(obj.getDecimalPlaces())

    def __writeBigMoney(self, out: pickle.Pickler, obj: BigMoney) -> None:
        self.__writeCurrency(out, obj.getCurrencyUnit())
        bytes = obj.getAmount().unscaledValue().to_bytes()
        out.write(len(bytes))
        out.write(bytes)
        out.write(obj.getScale())
