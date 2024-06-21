from __future__ import annotations
import io
import typing
from typing import *
import pickle
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class Ser:

    CURRENCY_UNIT: int = ord("C")

    MONEY: int = ord("M")

    BIG_MONEY: int = ord("B")
    __object: typing.Any = None
    __type: int = None

    def readExternal(self, in_: pickle.Unpickler) -> None:

        self.__type = in_.read(1)[0]

        if self.__type == self.BIG_MONEY:
            self.__object = self.__readBigMoney(in_)
            return
        elif self.__type == self.MONEY:
            self.__object = Money(0, self.__readBigMoney(in_))
            return
        elif self.__type == self.CURRENCY_UNIT:
            self.__object = self.__readCurrency(in_)
            return

        raise EOFError("Serialization input has invalid type")

    def writeExternal(self, out: pickle.Pickler) -> None:

        out.write(self.__type)

        if self.__type == self.BIG_MONEY:
            obj = self.__object
            self.__writeBigMoney(out, obj)
            return

        if self.__type == self.MONEY:
            obj = self.__object.toBigMoney()
            self.__writeBigMoney(out, obj)
            return

        if self.__type == self.CURRENCY_UNIT:
            obj = self.__object
            self.__writeCurrency(out, obj)
            return

        raise InvalidClassException("Joda-Money bug: Serialization broken")

    def __init__(self, constructorId: int, object: typing.Any, type: int) -> None:

        if constructorId == 0:
            self.__type = type
            self.__object = object

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
        bd = Decimal(int.from_bytes(bytes_, byteorder="big")) / (10 ** in_.load())
        bigMoney = BigMoney(0, bd, currency)
        return bigMoney

    def __writeCurrency(self, out: pickle.Pickler, obj: CurrencyUnit) -> None:

        out.writeUTF(obj.getCode())
        out.writeShort(obj.getNumericCode())
        out.writeShort(obj.getDecimalPlaces())

    def __writeBigMoney(self, out: pickle.Pickler, obj: BigMoney) -> None:

        self.__writeCurrency(out, obj.getCurrencyUnit())
        bytes_ = obj.getAmount().unscaledValue().toByteArray()
        out.writeInt(len(bytes_))
        out.write(bytes_)
        out.writeInt(obj.getScale())
