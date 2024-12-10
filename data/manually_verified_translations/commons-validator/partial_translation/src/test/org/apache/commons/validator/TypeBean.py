from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *


class TypeBean:

    __sCreditCard: str = None
    __sDate: str = None
    __sDouble: str = None
    __sFloat: str = None
    __sLong: str = None
    __sInteger: str = None
    __sShort: str = None
    __sByte: str = None

    def setCreditCard(self, sCreditCard: str) -> None:
        self.__sCreditCard = sCreditCard

    def getCreditCard(self) -> str:
        return self.__sCreditCard

    def setDate(self, sDate: str) -> None:
        self.__sDate = sDate

    def getDate(self) -> str:
        return self.__sDate

    def setDouble(self, sDouble: str) -> None:
        self.__sDouble = sDouble

    def getDouble(self) -> str:
        return self.__sDouble

    def setFloat(self, sFloat: str) -> None:
        self.__sFloat = sFloat

    def getFloat(self) -> str:
        return self.__sFloat

    def setLong(self, sLong: str) -> None:
        self.__sLong = sLong

    def getLong(self) -> str:
        return self.__sLong

    def setInteger(self, sInteger: str) -> None:
        self.__sInteger = sInteger

    def getInteger(self) -> str:
        return self.__sInteger

    def setShort(self, sShort: str) -> None:
        self.__sShort = sShort

    def getShort(self) -> str:
        return self.__sShort

    def setByte(self, sByte: str) -> None:
        self.__sByte = sByte

    def getByte(self) -> str:
        return self.__sByte
