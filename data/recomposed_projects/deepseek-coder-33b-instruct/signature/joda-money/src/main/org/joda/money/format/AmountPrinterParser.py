from __future__ import annotations
import re
import decimal
from io import IOBase
import io
import typing
from typing import *
import os
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *


class AmountPrinterParser(MoneyParser, MoneyPrinter):

    __style: MoneyAmountStyle = None

    __serialVersionUID: int = 1

    def toString(self) -> str:
        return "${amount}"

    def parse(self, context: MoneyParseContext) -> None:

        len_ = context.getTextLength()
        activeStyle = self.style.localize(context.getLocale())
        buf = [""] * (len_ - context.getIndex())
        bufPos = 0
        dpSeen = False
        pos = context.getIndex()
        if pos < len_:
            ch = context.getText()[pos]
            pos += 1
            if ch == activeStyle.getNegativeSignCharacter():
                buf[bufPos] = "-"
                bufPos += 1
            elif ch == activeStyle.getPositiveSignCharacter():
                buf[bufPos] = "+"
                bufPos += 1
            elif (
                activeStyle.getZeroCharacter()
                <= ch
                < activeStyle.getZeroCharacter() + 10
            ):
                buf[bufPos] = chr(ord("0") + ch - activeStyle.getZeroCharacter())
                bufPos += 1
            elif ch == activeStyle.getDecimalPointCharacter():
                buf[bufPos] = "."
                bufPos += 1
                dpSeen = True
            else:
                context.setError()
                return
        lastWasGroup = False
        for _ in range(pos, len_):
            ch = context.getText()[pos]
            if (
                activeStyle.getZeroCharacter()
                <= ch
                < activeStyle.getZeroCharacter() + 10
            ):
                buf[bufPos] = chr(ord("0") + ch - activeStyle.getZeroCharacter())
                bufPos += 1
                lastWasGroup = False
            elif ch == activeStyle.getDecimalPointCharacter() and not dpSeen:
                buf[bufPos] = "."
                bufPos += 1
                dpSeen = True
                lastWasGroup = False
            elif ch == activeStyle.getGroupingCharacter() and not lastWasGroup:
                lastWasGroup = True
            else:
                break
        if lastWasGroup:
            pos -= 1
        try:
            context.setAmount(decimal.Decimal("".join(buf[:bufPos])))
            context.setIndex(pos)
        except decimal.InvalidOperation:
            context.setError()

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:

        activeStyle = self.style.localize(context.getLocale())
        if money.isNegative():
            if not activeStyle.isAbsValue():
                appendable.append(activeStyle.getNegativeSignCharacter())
            str_val = money.negated().getAmount().toPlainString()
        else:
            str_val = money.getAmount().toPlainString()

        zeroChar = activeStyle.getZeroCharacter()
        if zeroChar != "0":
            diff = ord(zeroChar) - ord("0")
            str_val = "".join(
                [
                    chr((ord(ch) + diff) if ch >= "0" and ch <= "9" else ord(ch))
                    for ch in str_val
                ]
            )

        decPoint = str_val.find(".")
        afterDecPoint = decPoint + 1 if decPoint != -1 else len(str_val)
        if activeStyle.getGroupingStyle() == GroupingStyle.NONE:
            if decPoint == -1:
                appendable.append(str_val)
                if activeStyle.isForcedDecimalPoint():
                    appendable.append(activeStyle.getDecimalPointCharacter())
            else:
                appendable.append(str_val[:decPoint])
                appendable.append(activeStyle.getDecimalPointCharacter())
                appendable.append(str_val[afterDecPoint:])
        else:
            groupingSize = activeStyle.getGroupingSize()
            extendedGroupingSize = activeStyle.getExtendedGroupingSize()
            extendedGroupingSize = (
                groupingSize if extendedGroupingSize == 0 else extendedGroupingSize
            )
            groupingChar = activeStyle.getGroupingCharacter()
            pre = len(str_val) if decPoint == -1 else decPoint
            post = len(str_val) - afterDecPoint if decPoint != -1 else 0
            appendable.append(str_val[0])
            for i in range(1, pre):
                if self.__isPreGroupingPoint(
                    pre - i, groupingSize, extendedGroupingSize
                ):
                    appendable.append(groupingChar)
                appendable.append(str_val[i])
            if decPoint != -1 or activeStyle.isForcedDecimalPoint():
                appendable.append(activeStyle.getDecimalPointCharacter())
            if activeStyle.getGroupingStyle() == GroupingStyle.BEFORE_DECIMAL_POINT:
                if decPoint != -1:
                    appendable.append(str_val[afterDecPoint:])
            else:
                for i in range(post):
                    appendable.append(str_val[i + afterDecPoint])
                    if self.__isPostGroupingPoint(
                        i, post, groupingSize, extendedGroupingSize
                    ):
                        appendable.append(groupingChar)

    def __isPostGroupingPoint(
        self, i: int, post: int, groupingSize: int, extendedGroupingSize: int
    ) -> bool:

        atEnd = (i + 1) >= post

        if i > groupingSize:
            return (i - groupingSize) % extendedGroupingSize == (
                extendedGroupingSize - 1
            ) and not atEnd

        return i % groupingSize == (groupingSize - 1) and not atEnd

    def __isPreGroupingPoint(
        self, remaining: int, groupingSize: int, extendedGroupingSize: int
    ) -> bool:

        if remaining >= groupingSize + extendedGroupingSize:
            return (remaining - groupingSize) % extendedGroupingSize == 0
        return remaining % groupingSize == 0

    def __init__(self, style: MoneyAmountStyle) -> None:
        self.__style = style
