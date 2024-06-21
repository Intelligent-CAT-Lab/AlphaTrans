from __future__ import annotations
from io import IOBase
import io
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

        positive_context = context.createChild()
        self.__whenPositive.getPrinterParser().parse(positive_context)

        zero_context = context.createChild()
        self.__whenZero.getPrinterParser().parse(zero_context)

        negative_context = context.createChild()
        self.__whenNegative.getPrinterParser().parse(negative_context)

        best = None

        if not positive_context.isError():
            best = positive_context

        if not zero_context.isError():
            if best is None or zero_context.getIndex() > best.getIndex():
                best = zero_context

        if not negative_context.isError():
            if best is None or negative_context.getIndex() > best.getIndex():
                best = negative_context

        if best is None:
            context.setError()
        else:
            context.mergeChild(best)
            if best == zero_context:
                if (
                    context.getAmount() is None
                    or context.getAmount().compareTo(BigDecimal.ZERO) != 0
                ):
                    context.setAmount(BigDecimal.ZERO)
            elif (
                best == negative_context
                and context.getAmount().compareTo(BigDecimal.ZERO) > 0
            ):
                context.setAmount(context.getAmount().negate())

    def print(
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:

        fmt = (
            self.__whenZero
            if money.isZero()
            else self.__whenPositive if money.isPositive() else self.__whenNegative
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
