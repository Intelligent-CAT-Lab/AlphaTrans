from __future__ import annotations
from io import IOBase
import io
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

        len = context.getTextLength()
        activeStyle = self.__style.localize(context.getLocale())
        buf = [""] * (len - context.getIndex())
        bufPos = 0
        dpSeen = False
        pos = context.getIndex()
        if pos < len:
            ch = context.getText().charAt(pos)
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
        for _ in range(pos, len):
            ch = context.getText().charAt(_)
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
            context.setAmount(BigDecimal("".join(buf[:bufPos])))
            context.setIndex(pos)
        except NumberFormatException:
            context.setError()

    def print(
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:

        activeStyle = self.__style.localize(context.getLocale())
        str = ""
        if money.isNegative():
            if not activeStyle.isAbsValue():
                appendable.write(activeStyle.getNegativeSignCharacter())
            str = str(money.negated().getAmount())
        else:
            str = str(money.getAmount())

        zeroChar = activeStyle.getZeroCharacter()
        if zeroChar != "0":
            diff = ord(zeroChar) - ord("0")
            zeroConvert = list(str)
            for i in range(len(str)):
                ch = str[i]
                if ch >= "0" and ch <= "9":
                    zeroConvert[i] = chr(ord(ch) + diff)
            str = "".join(zeroConvert)

        decPoint = str.find(".")
        afterDecPoint = decPoint + 1
        if activeStyle.getGroupingStyle() == GroupingStyle.NONE:
            if decPoint < 0:
                appendable.write(str)
                if activeStyle.isForcedDecimalPoint():
                    appendable.write(activeStyle.getDecimalPointCharacter())
            else:
                appendable.write(str[:decPoint])
                appendable.write(activeStyle.getDecimalPointCharacter())
                appendable.write(str[afterDecPoint:])
        else:
            groupingSize = activeStyle.getGroupingSize()
            extendedGroupingSize = activeStyle.getExtendedGroupingSize()
            extendedGroupingSize = (
                extendedGroupingSize if extendedGroupingSize != 0 else groupingSize
            )
            groupingChar = activeStyle.getGroupingCharacter()
            pre = len(str) if decPoint < 0 else decPoint
            post = len(str) - decPoint - 1 if decPoint >= 0 else 0
            appendable.write(str[0])
            for i in range(1, pre):
                if self.__isPreGroupingPoint(
                    pre - i, groupingSize, extendedGroupingSize
                ):
                    appendable.write(groupingChar)
                appendable.write(str[i])
            if decPoint >= 0 or activeStyle.isForcedDecimalPoint():
                appendable.write(activeStyle.getDecimalPointCharacter())
            if activeStyle.getGroupingStyle() == GroupingStyle.BEFORE_DECIMAL_POINT:
                if decPoint >= 0:
                    appendable.write(str[afterDecPoint:])
            else:
                for i in range(post):
                    appendable.write(str[i + afterDecPoint])
                    if self.__isPostGroupingPoint(
                        i, post, groupingSize, extendedGroupingSize
                    ):
                        appendable.write(groupingChar)

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
