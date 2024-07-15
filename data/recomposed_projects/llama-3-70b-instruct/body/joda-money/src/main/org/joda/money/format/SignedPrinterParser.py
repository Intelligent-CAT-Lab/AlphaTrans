from __future__ import annotations
import re
from io import IOBase
import io
import typing
from typing import *
import os
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *


class SignedPrinterParser(MoneyParser, MoneyPrinter):

    __whenNegative: MoneyFormatter = None

    __whenZero: MoneyFormatter = None

    __whenPositive: MoneyFormatter = None

    __serialVersionUID: int = 1

    def toString(self) -> str:
        return (
            "PositiveZeroNegative("
            + self.__whenPositive
            + ","
            + self.__whenZero
            + ","
            + self.__whenNegative
            + ")"
        )

    def parse(self, context: MoneyParseContext) -> None:
        positiveContext = context.createChild()
        self.__whenPositive.getPrinterParser().parse(positiveContext)
        zeroContext = context.createChild()
        self.__whenZero.getPrinterParser().parse(zeroContext)
        negativeContext = context.createChild()
        self.__whenNegative.getPrinterParser().parse(negativeContext)
        best = None
        if not positiveContext.isError():
            best = positiveContext
        if not zeroContext.isError():
            if best is None or zeroContext.getIndex() > best.getIndex():
                best = zeroContext
        if not negativeContext.isError():
            if best is None or negativeContext.getIndex() > best.getIndex():
                best = negativeContext
        if best is None:
            context.setError()
        else:
            context.mergeChild(best)
            if best == zeroContext:
                if (
                    context.getAmount() is None
                    or context.getAmount().compareTo(BigDecimal.ZERO) != 0
                ):
                    context.setAmount(BigDecimal.ZERO)
            elif (
                best == negativeContext
                and context.getAmount().compareTo(BigDecimal.ZERO) > 0
            ):
                context.setAmount(context.getAmount().negate())

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:
        fmt = (
            money.isZero()
            and self.__whenZero
            or money.isPositive()
            and self.__whenPositive
            or self.__whenNegative
        )
        fmt.getPrinterParser().print(context, appendable, money)

    def __init__(
        self,
        whenPositive: MoneyFormatter,
        whenZero: MoneyFormatter,
        whenNegative: MoneyFormatter,
    ) -> None:
        self.__whenPositive = whenPositive
        self.__whenZero = whenZero
        self.__whenNegative = whenNegative
