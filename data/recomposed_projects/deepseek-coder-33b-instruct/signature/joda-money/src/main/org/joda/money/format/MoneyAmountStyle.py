from __future__ import annotations
import locale
import re
import numbers
import io
import typing
from typing import *
import decimal
import os
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *


class MoneyAmountStyle:

    LOCALIZED_NO_GROUPING: MoneyAmountStyle = None
    LOCALIZED_GROUPING: MoneyAmountStyle = None
    ASCII_DECIMAL_COMMA_NO_GROUPING: MoneyAmountStyle = None
    ASCII_DECIMAL_COMMA_GROUP3_SPACE: MoneyAmountStyle = None
    ASCII_DECIMAL_COMMA_GROUP3_DOT: MoneyAmountStyle = None
    ASCII_DECIMAL_POINT_NO_GROUPING: MoneyAmountStyle = None
    ASCII_DECIMAL_POINT_GROUP3_SPACE: MoneyAmountStyle = None
    ASCII_DECIMAL_POINT_GROUP3_COMMA: MoneyAmountStyle = None
    __absValue: bool = False

    __forceDecimalPoint: bool = False

    __extendedGroupingSize: int = 0

    __groupingSize: int = 0

    __groupingCharacter: int = 0

    __groupingStyle: GroupingStyle = None

    __decimalPointCharacter: int = 0

    __negativeCharacter: int = 0

    __positiveCharacter: int = 0

    __zeroCharacter: int = 0

    __serialVersionUID: int = 1
    __LOCALIZED_CACHE: typing.Dict[typing.Any, MoneyAmountStyle] = {}

    @staticmethod
    def initialize_fields() -> None:
        MoneyAmountStyle.LOCALIZED_NO_GROUPING: MoneyAmountStyle = MoneyAmountStyle(
            -1, -1, -1, -1, GroupingStyle.NONE, -1, -1, -1, False, False
        )

        MoneyAmountStyle.LOCALIZED_GROUPING: MoneyAmountStyle = MoneyAmountStyle(
            -1, -1, -1, -1, GroupingStyle.FULL, -1, -1, -1, False, False
        )

        MoneyAmountStyle.ASCII_DECIMAL_COMMA_NO_GROUPING: MoneyAmountStyle = (
            MoneyAmountStyle(
                "0", "+", "-", ",", GroupingStyle.NONE, ".", 3, 0, False, False
            )
        )

        MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_SPACE: MoneyAmountStyle = (
            MoneyAmountStyle(
                "0", "+", "-", ",", GroupingStyle.FULL, " ", 3, 0, False, False
            )
        )

        MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_DOT: MoneyAmountStyle = (
            MoneyAmountStyle(
                zeroCharacter=ord("0"),
                positiveCharacter=ord("+"),
                negativeCharacter=ord("-"),
                decimalPointCharacter=ord(","),
                groupingStyle=GroupingStyle.FULL,
                groupingCharacter=ord("."),
                groupingSize=3,
                extendedGroupingSize=0,
                forceDecimalPoint=False,
                absValue=False,
            )
        )

        MoneyAmountStyle.ASCII_DECIMAL_POINT_NO_GROUPING: MoneyAmountStyle = (
            MoneyAmountStyle(
                "0", "+", "-", ".", GroupingStyle.NONE, ",", 3, 0, False, False
            )
        )

        MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_SPACE: MoneyAmountStyle = (
            MoneyAmountStyle(
                "0", "+", "-", ".", GroupingStyle.FULL, " ", 3, 0, False, False
            )
        )

        MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA: MoneyAmountStyle = (
            MoneyAmountStyle(
                "0", "+", "-", ".", GroupingStyle.FULL, ",", 3, 0, False, False
            )
        )

    def toString(self) -> str:
        return (
            "MoneyAmountStyle['"
            + self.getZeroCharacter()
            + "','"
            + self.getPositiveSignCharacter()
            + "','"
            + self.getNegativeSignCharacter()
            + "','"
            + self.getDecimalPointCharacter()
            + "','"
            + str(self.getGroupingStyle())
            + "','"
            + self.getGroupingCharacter()
            + "','"
            + str(self.getGroupingSize())
            + "',"
            + str(self.isForcedDecimalPoint())
            + "',"
            + str(self.isAbsValue())
            + "]"
        )

    def hashCode(self) -> int:

        hash = 13
        hash += self.__zeroCharacter * 17
        hash += self.__positiveCharacter * 17
        hash += self.__negativeCharacter * 17
        hash += self.__decimalPointCharacter * 17
        hash += self.__groupingStyle.hashCode() * 17
        hash += self.__groupingCharacter * 17
        hash += self.__groupingSize * 17
        hash += 2 if self.__forceDecimalPoint else 4
        hash += 3 if self.__absValue else 9
        return hash

    def equals(self, other: typing.Any) -> bool:

        if other == self:
            return True
        if not isinstance(other, MoneyAmountStyle):
            return False
        otherStyle = typing.cast(MoneyAmountStyle, other)
        return (
            (self.__zeroCharacter == otherStyle.__zeroCharacter)
            and (self.__positiveCharacter == otherStyle.__positiveCharacter)
            and (self.__negativeCharacter == otherStyle.__negativeCharacter)
            and (self.__decimalPointCharacter == otherStyle.__decimalPointCharacter)
            and (self.__groupingStyle == otherStyle.__groupingStyle)
            and (self.__groupingCharacter == otherStyle.__groupingCharacter)
            and (self.__groupingSize == otherStyle.__groupingSize)
            and (self.__forceDecimalPoint == otherStyle.__forceDecimalPoint)
            and (self.__absValue == otherStyle.__absValue)
        )

    def withAbsValue(self, absValue: bool) -> MoneyAmountStyle:
        if self.__absValue == absValue:
            return self
        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            absValue,
        )

    def isAbsValue(self) -> bool:
        return self.__absValue

    def withForcedDecimalPoint(self, forceDecimalPoint: bool) -> MoneyAmountStyle:

        if self.__forceDecimalPoint == forceDecimalPoint:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            forceDecimalPoint,
            self.__absValue,
        )

    def isForcedDecimalPoint(self) -> bool:
        return self.__forceDecimalPoint

    def withGroupingStyle(self, groupingStyle: GroupingStyle) -> MoneyAmountStyle:

        MoneyFormatter.checkNotNull(groupingStyle, "groupingStyle")

        if self.__groupingStyle == groupingStyle:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getGroupingStyle(self) -> GroupingStyle:
        return self.__groupingStyle

    def withExtendedGroupingSize(self, extendedGroupingSize: int) -> MoneyAmountStyle:

        sizeVal = extendedGroupingSize if extendedGroupingSize is not None else -1

        if extendedGroupingSize is not None and sizeVal < 0:
            raise ValueError("Extended grouping size must not be negative")

        if sizeVal == self.__extendedGroupingSize:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            sizeVal,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getExtendedGroupingSize(self) -> int:
        return self.__extendedGroupingSize if self.__extendedGroupingSize >= 0 else None

    def withGroupingSize(self, groupingSize: int) -> MoneyAmountStyle:

        sizeVal = groupingSize if groupingSize is not None else -1

        if groupingSize is not None and sizeVal <= 0:
            raise ValueError("Grouping size must be greater than zero")

        if sizeVal == self.__groupingSize:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            sizeVal,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getGroupingSize(self) -> int:
        return self.__groupingSize if self.__groupingSize >= 0 else None

    def withGroupingCharacter(self, groupingCharacter: str) -> MoneyAmountStyle:

        groupingVal = ord(groupingCharacter) if groupingCharacter is not None else -1

        if groupingVal == self.__groupingCharacter:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            groupingVal,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getGroupingCharacter(self) -> str:
        return chr(self.__groupingCharacter) if self.__groupingCharacter >= 0 else None

    def withDecimalPointCharacter(self, decimalPointCharacter: str) -> MoneyAmountStyle:

        dpVal = -1 if decimalPointCharacter is None else ord(decimalPointCharacter)
        if dpVal == self.__decimalPointCharacter:
            return self
        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            self.__negativeCharacter,
            dpVal,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getDecimalPointCharacter(self) -> str:
        return (
            chr(self.__decimalPointCharacter)
            if self.__decimalPointCharacter >= 0
            else None
        )

    def withNegativeSignCharacter(self, negativeCharacter: str) -> MoneyAmountStyle:

        negativeVal = ord(negativeCharacter) if negativeCharacter is not None else -1

        if negativeVal == self.__negativeCharacter:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            self.__positiveCharacter,
            negativeVal,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getNegativeSignCharacter(self) -> str:
        return chr(self.__negativeCharacter) if self.__negativeCharacter >= 0 else None

    def withPositiveSignCharacter(self, positiveCharacter: str) -> MoneyAmountStyle:

        positiveVal = ord(positiveCharacter) if positiveCharacter is not None else -1

        if positiveVal == self.__positiveCharacter:
            return self

        return MoneyAmountStyle(
            self.__zeroCharacter,
            positiveVal,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getPositiveSignCharacter(self) -> str:
        return chr(self.__positiveCharacter) if self.__positiveCharacter >= 0 else None

    def withZeroCharacter(self, zeroCharacter: str) -> MoneyAmountStyle:

        zeroVal = ord(zeroCharacter) if zeroCharacter is not None else -1
        if zeroVal == self.__zeroCharacter:
            return self
        return MoneyAmountStyle(
            zeroVal,
            self.__positiveCharacter,
            self.__negativeCharacter,
            self.__decimalPointCharacter,
            self.__groupingStyle,
            self.__groupingCharacter,
            self.__groupingSize,
            self.__extendedGroupingSize,
            self.__forceDecimalPoint,
            self.__absValue,
        )

    def getZeroCharacter(self) -> str:
        return chr(self.__zeroCharacter) if self.__zeroCharacter >= 0 else None

    def localize(self, locale: typing.Any) -> MoneyAmountStyle:

        MoneyFormatter.checkNotNull(locale, "Locale must not be null")
        result = self
        protoStyle = None
        if self.__zeroCharacter < 0:
            protoStyle = self.__getLocalizedStyle(locale)
            result = result.withZeroCharacter(protoStyle.getZeroCharacter())
        if self.__positiveCharacter < 0:
            protoStyle = (
                protoStyle
                if protoStyle is not None
                else self.__getLocalizedStyle(locale)
            )
            result = result.withPositiveSignCharacter(
                protoStyle.getPositiveSignCharacter()
            )
        if self.__negativeCharacter < 0:
            protoStyle = (
                protoStyle
                if protoStyle is not None
                else self.__getLocalizedStyle(locale)
            )
            result = result.withNegativeSignCharacter(
                protoStyle.getNegativeSignCharacter()
            )
        if self.__decimalPointCharacter < 0:
            protoStyle = (
                protoStyle
                if protoStyle is not None
                else self.__getLocalizedStyle(locale)
            )
            result = result.withDecimalPointCharacter(
                protoStyle.getDecimalPointCharacter()
            )
        if self.__groupingCharacter < 0:
            protoStyle = (
                protoStyle
                if protoStyle is not None
                else self.__getLocalizedStyle(locale)
            )
            result = result.withGroupingCharacter(protoStyle.getGroupingCharacter())
        if self.__groupingSize < 0:
            protoStyle = (
                protoStyle
                if protoStyle is not None
                else self.__getLocalizedStyle(locale)
            )
            result = result.withGroupingSize(protoStyle.getGroupingSize())
        if self.__extendedGroupingSize < 0:
            protoStyle = (
                protoStyle
                if protoStyle is not None
                else self.__getLocalizedStyle(locale)
            )
            result = result.withExtendedGroupingSize(
                protoStyle.getExtendedGroupingSize()
            )
        return result

    @staticmethod
    def of(locale: typing.Any) -> MoneyAmountStyle:
        return MoneyAmountStyle.__getLocalizedStyle(locale)

    @staticmethod
    def __getLocalizedStyle(locale: typing.Any) -> MoneyAmountStyle:

        protoStyle = MoneyAmountStyle.__LOCALIZED_CACHE.get(locale)
        if protoStyle is None:
            symbols = decimal.DecimalFormatSymbols.getInstance(locale)
            format = decimal.NumberFormat.getCurrencyInstance(locale)
            size = (
                format.getGroupingSize()
                if isinstance(format, decimal.DecimalFormat)
                else 3
            )
            size = 3 if size <= 0 else size
            protoStyle = MoneyAmountStyle(
                symbols.getZeroDigit(),
                "+",
                symbols.getMinusSign(),
                symbols.getMonetaryDecimalSeparator(),
                GroupingStyle.FULL,
                symbols.getGroupingSeparator(),
                size,
                0,
                False,
                False,
            )
            MoneyAmountStyle.__LOCALIZED_CACHE.putIfAbsent(locale, protoStyle)
        return protoStyle

    def __init__(
        self,
        zeroCharacter: int,
        positiveCharacter: int,
        negativeCharacter: int,
        decimalPointCharacter: int,
        groupingStyle: GroupingStyle,
        groupingCharacter: int,
        groupingSize: int,
        extendedGroupingSize: int,
        forceDecimalPoint: bool,
        absValue: bool,
    ) -> None:

        self.__zeroCharacter = zeroCharacter
        self.__positiveCharacter = positiveCharacter
        self.__negativeCharacter = negativeCharacter
        self.__decimalPointCharacter = decimalPointCharacter
        self.__groupingStyle = groupingStyle
        self.__groupingCharacter = groupingCharacter
        self.__groupingSize = groupingSize
        self.__extendedGroupingSize = extendedGroupingSize
        self.__forceDecimalPoint = forceDecimalPoint
        self.__absValue = absValue


MoneyAmountStyle.initialize_fields()
