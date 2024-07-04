from __future__ import annotations
import locale
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import decimal
import unittest
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *


class TestMoneyFormatterBuilder(unittest.TestCase):

    __iBuilder: MoneyFormatterBuilder = None

    __FR_GROUP: str = FR_SYMBOLS.get_grouping_separator()
    __FR_DECIMAL: str = FR_SYMBOLS.getMonetaryDecimalSeparator()
    __FR_SYMBOLS: decimal.Decimal = decimal.Decimal(locale="fr_FR")
    __TEST_FR_LOCALE: typing.Any = Locale("fr", "FR", "TEST")
    __TEST_GB_LOCALE: typing.Any = Locale("en", "GB", "TEST")
    __cCachedLocale: typing.Any = Locale.getDefault()
    __JPY_2345: Money = Money.parse("JPY 2345")
    __GBP_1234567891234_1234567891: BigMoney = BigMoney.parse(
        "GBP 1234567891234.1234567891"
    )
    __GBP_1234_56789: BigMoney = BigMoney.parse("GBP 1234.56789")
    __GBP_1234567_89: Money = Money.parse("GBP 1234567.89")
    __GBP_2345_67: Money = Money.parse("GBP 2345.67")
    __GBP_MINUS_234_56: Money = Money.parse("GBP -234.56")
    __GBP_234_56: Money = Money.parse("GBP 234.56")
    __GBP_23_45: Money = Money.parse("GBP 23.45")
    __GBP_2_34: Money = Money.parse("GBP 2.34")
    __BHD: CurrencyUnit = CurrencyUnit.of("BHD")
    __JPY: CurrencyUnit = CurrencyUnit.of("JPY")
    __GBP: CurrencyUnit = CurrencyUnit.GBP

    def test_toFormatter_Locale(self) -> None:

        test = self.__iBuilder.toFormatter1(self.__TEST_FR_LOCALE)
        self.assertEqual(self.__TEST_FR_LOCALE, test.getLocale())

    def test_toFormatter_defaultLocale(self) -> None:

        test = self.__iBuilder.toFormatter0()
        self.assertEqual(self.__TEST_GB_LOCALE, test.getLocale())

    def test_appendSigned_PZN_edgeCases(self) -> None:

        pos = MoneyFormatterBuilder().appendAmount0().toFormatter0()
        zro = (
            MoneyFormatterBuilder()
            .appendAmount0()
            .appendLiteral(" (zero)")
            .toFormatter0()
        )
        neg = (
            MoneyFormatterBuilder()
            .appendLiteral("(")
            .appendAmount1(
                MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA.withAbsValue(True)
            )
            .appendLiteral(")")
            .toFormatter0()
        )
        f = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendSigned1(pos, zro, neg)
            .toFormatter0()
        )

        self.assertEqual("GBP 234.56", f.print0(TestMoneyFormatterBuilder.__GBP_234_56))
        self.assertEqual(
            "GBP 0.00 (zero)",
            f.print0(BigMoney.zero0(TestMoneyFormatterBuilder.__GBP).withScale0(2)),
        )
        self.assertEqual(
            "GBP (234.56)", f.print0(TestMoneyFormatterBuilder.__GBP_MINUS_234_56)
        )
        self.assertEqual(
            TestMoneyFormatterBuilder.__GBP_234_56.toBigMoney(),
            f.parseBigMoney("GBP 234.56"),
        )
        self.assertEqual(
            BigMoney.zero0(TestMoneyFormatterBuilder.__GBP).withScale0(2),
            f.parseBigMoney("GBP 0.00 (zero)"),
        )
        self.assertEqual(
            BigMoney.zero0(TestMoneyFormatterBuilder.__GBP),
            f.parseBigMoney("GBP 1.23 (zero)"),
        )
        self.assertEqual(
            TestMoneyFormatterBuilder.__GBP_MINUS_234_56.toBigMoney(),
            f.parseBigMoney("GBP (234.56)"),
        )

    def test_appendSigned_PZN(self) -> None:

        pos = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendAmount0()
            .toFormatter0()
        )
        zro = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" -")
            .toFormatter0()
        )
        neg = (
            MoneyFormatterBuilder()
            .appendLiteral("(")
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendAmount1(
                MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA.withAbsValue(True)
            )
            .appendLiteral(")")
            .toFormatter0()
        )
        f = MoneyFormatterBuilder().appendSigned1(pos, zro, neg).toFormatter0()

        self.assertEqual("GBP 234.56", f.print0(self.__GBP_234_56))
        self.assertEqual("GBP -", f.print0(Money.zero(self.__GBP)))
        self.assertEqual("(GBP 234.56)", f.print0(self.__GBP_MINUS_234_56))
        self.assertEqual(self.__GBP_234_56, f.parseMoney("GBP 234.56"))
        self.assertEqual(self.__GBP_MINUS_234_56, f.parseMoney("GBP -234.56"))
        self.assertEqual(Money.zero(self.__GBP), f.parseMoney("GBP -"))
        self.assertEqual(self.__GBP_MINUS_234_56, f.parseMoney("(GBP 234.56)"))
        self.assertEqual(self.__GBP_MINUS_234_56, f.parseMoney("(GBP -234.56)"))

    def test_appendSigned_PN(self) -> None:

        pos = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendAmount0()
            .toFormatter0()
        )

        neg = (
            MoneyFormatterBuilder()
            .appendLiteral("(")
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendAmount1(
                MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA.withAbsValue(True)
            )
            .appendLiteral(")")
            .toFormatter0()
        )

        f = MoneyFormatterBuilder().appendSigned0(pos, neg).toFormatter0()

        self.assertEqual(
            "PositiveZeroNegative(${code}' '${amount},${code}' '${amount},'('${code}'"
            + " '${amount}')')",
            f.toString(),
        )

        self.assertEqual("GBP 234.56", f.print0(self.__GBP_234_56))
        self.assertEqual("GBP 0.00", f.print0(Money.zero(self.__GBP)))
        self.assertEqual("(GBP 234.56)", f.print0(self.__GBP_MINUS_234_56))
        self.assertEqual(self.__GBP_234_56, f.parseMoney("GBP 234.56"))
        self.assertEqual(Money.zero(self.__GBP), f.parseMoney("GBP 0"))
        self.assertEqual(self.__GBP_MINUS_234_56, f.parseMoney("(GBP 234.56)"))

        context = f.parse("X", 0)
        self.assertEqual(0, context.getIndex())
        self.assertEqual(0, context.getErrorIndex())

    def test_append_MoneyFormatter(self) -> None:

        f1 = MoneyFormatterBuilder().appendAmount0().toFormatter0()
        f2 = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" ")
            .append0(f1)
            .toFormatter0()
        )

        self.assertEqual("GBP 2,345.67", f2.print0(self.__GBP_2345_67))

    def test_append_MoneyPrinter_nullMoneyPrinter_nullMoneyParser(self) -> None:

        self.__iBuilder.append1(None, None)
        test = self.__iBuilder.toFormatter0()
        self.assertEqual(False, test.isPrinter())
        self.assertEqual(False, test.isParser())
        self.assertEqual("", test.toString())

    def test_append_MoneyPrinterMoneyParser_parser(self) -> None:

        parser = MoneyParser()
        parser.parse = lambda context: (
            context.setAmount(self.__JPY_2345.getAmount()),
            context.setCurrency(self.__JPY_2345.getCurrencyUnit()),
        )

        self.__iBuilder.append1(None, parser)
        test = self.__iBuilder.toFormatter0()

        self.assertEqual(False, test.isPrinter())
        self.assertEqual(True, test.isParser())
        self.assertEqual(self.__JPY_2345, test.parseMoney(""))
        self.assertEqual(
            True,
            test.toString().startswith(
                "org.joda.money.format.TestMoneyFormatterBuilder$"
            ),
        )

    def test_append_MoneyPrinterMoneyParser_printer(self) -> None:

        printer = MoneyPrinter()
        printer.print = lambda context, appendable, money: appendable.write("HELLO")

        self.__iBuilder.append1(printer, None)
        test = self.__iBuilder.toFormatter0()
        self.assertEqual(True, test.isPrinter())
        self.assertEqual(False, test.isParser())
        self.assertEqual("HELLO", test.print0(self.__JPY_2345))
        self.assertTrue(
            test.toString().startswith(
                "org.joda.money.format.TestMoneyFormatterBuilder$"
            )
        )

    def test_appendAmount_parseExcessGrouping(self) -> None:

        expected = BigMoney.parse("GBP 12123.4567")
        f = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendAmount1(MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA)
            .toFormatter0()
        )
        money = f.parseBigMoney("GBP 12,1,2,3,.,45,6,7")
        self.assertEqual(expected, money)

    def test_appendAmount_parseExtendedGroupingSize(
        self, money: BigMoneyProvider, expected: str
    ) -> None:

        self.iBuilder.appendAmount0()
        test = (
            MoneyFormatterBuilder()
            .appendAmount1(
                MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA.withExtendedGroupingSize(
                    2
                )
            )
            .toFormatter0()
        )
        self.assertEqual(expected, test.print0(money))
        self.assertEqual("${amount}", test.toString())

    @staticmethod
    def data_appendAmountExtendedGrouping() -> typing.List[typing.List[typing.Any]]:
        return [
            [TestMoneyFormatterBuilder.__GBP_2_34, "2.34"],
            [TestMoneyFormatterBuilder.__GBP_23_45, "23.45"],
            [TestMoneyFormatterBuilder.__GBP_234_56, "234.56"],
            [TestMoneyFormatterBuilder.__GBP_2345_67, "2,345.67"],
            [TestMoneyFormatterBuilder.__GBP_1234567_89, "12,34,567.89"],
            [TestMoneyFormatterBuilder.__GBP_1234_56789, "1,234.567,89"],
            [
                TestMoneyFormatterBuilder.__GBP_1234567891234_1234567891,
                "12,34,56,78,91,234.123,45,67,89,1",
            ],
            [TestMoneyFormatterBuilder.__GBP_MINUS_234_56, "-234.56"],
        ]

    def test_appendAmount_MoneyAmountStyle_JPY_issue49(self) -> None:

        money = Money.parse("JPY 12")
        style = MoneyAmountStyle.LOCALIZED_GROUPING
        formatter = (
            MoneyFormatterBuilder()
            .appendAmount1(style)
            .toFormatter0()
            .withLocale(Locale.JAPAN)
        )
        self.assertEqual("12", formatter.print0(money))

    def test_appendAmount_MoneyAmountStyle_BHD(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:

        self.__iBuilder.appendAmount1(style)
        test = self.__iBuilder.toFormatter0()
        money = BigMoney.of0(self.__BHD, decimal.Decimal(amount))
        self.assertEqual(expected, test.print0(money))
        if not style.isAbsValue():
            self.assertEqual(money.getAmount(), test.parse(expected, 0).getAmount())
        else:
            self.assertEqual(
                abs(money.getAmount()), test.parse(expected, 0).getAmount()
            )

    def test_appendAmount_MoneyAmountStyle_JPY(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:

        self.__iBuilder.appendAmount1(style)
        test = self.__iBuilder.toFormatter0()
        money = BigMoney.of0(self.__JPY, decimal.Decimal(amount))
        self.assertEqual(expected, test.print0(money))
        if not style.isAbsValue():
            self.assertEqual(money.getAmount(), test.parse(expected, 0).getAmount())
        else:
            self.assertEqual(
                abs(money.getAmount()), test.parse(expected, 0).getAmount()
            )

    def test_appendAmount_MoneyAmountStyle_GBP(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:

        self.__iBuilder.appendAmount1(style)
        test = self.__iBuilder.toFormatter0()
        money = BigMoney.of0(self.__GBP, decimal.Decimal(amount))
        self.assertEqual(expected, test.print0(money))
        if not style.isAbsValue():
            self.assertEqual(money.getAmount(), test.parse(expected, 0).getAmount())
        else:
            self.assertEqual(
                abs(money.getAmount()), test.parse(expected, 0).getAmount()
            )

    @staticmethod
    def data_appendAmount_MoneyAmountStyle() -> typing.List[typing.List[typing.Any]]:

        pass  # LLM could not translate this method

    def test_appendAmount_MoneyAmountStyle_null(self) -> None:
        with pytest.raises(TypeError):
            self.__iBuilder.appendAmount1(None)

    def test_appendAmountLocalized_JPY_2345(self) -> None:

        self.__iBuilder.appendAmountLocalized()
        test = self.__iBuilder.toFormatter1(Locale.FRANCE)
        self.assertEqual("2" + self.__FR_GROUP + "345", test.print0(self.__JPY_2345))
        self.assertEqual("${amount}", test.toString())

    def test_appendAmountLocalized_GBP_1234_56789_US(self) -> None:

        self.__iBuilder.appendAmountLocalized()
        test = self.__iBuilder.toFormatter1(Locale.US)
        self.assertEqual("1,234.567,89", test.print0(self.__GBP_1234_56789))
        self.assertEqual("${amount}", test.toString())

    def test_appendAmountLocalized(
        self, money: BigMoneyProvider, expected: str
    ) -> None:

        self.__iBuilder.appendAmountLocalized()
        test = self.__iBuilder.toFormatter1(Locale.FRANCE)
        self.assertEqual(expected, test.print0(money))
        self.assertEqual("${amount}", test.toString())

    @staticmethod
    def data_appendAmountLocalized() -> typing.List[typing.List[typing.Any]]:

        return [
            [
                TestMoneyFormatterBuilder.__GBP_2_34,
                "2" + TestMoneyFormatterBuilder.__FR_DECIMAL + "34",
            ],
            [
                TestMoneyFormatterBuilder.__GBP_23_45,
                "23" + TestMoneyFormatterBuilder.__FR_DECIMAL + "45",
            ],
            [
                TestMoneyFormatterBuilder.__GBP_234_56,
                "234" + TestMoneyFormatterBuilder.__FR_DECIMAL + "56",
            ],
            [
                TestMoneyFormatterBuilder.__GBP_2345_67,
                "2"
                + TestMoneyFormatterBuilder.__FR_GROUP
                + "345"
                + TestMoneyFormatterBuilder.__FR_DECIMAL
                + "67",
            ],
            [
                TestMoneyFormatterBuilder.__GBP_1234567_89,
                "1"
                + TestMoneyFormatterBuilder.__FR_GROUP
                + "234"
                + TestMoneyFormatterBuilder.__FR_GROUP
                + "567"
                + TestMoneyFormatterBuilder.__FR_DECIMAL
                + "89",
            ],
            [
                TestMoneyFormatterBuilder.__GBP_1234_56789,
                "1"
                + TestMoneyFormatterBuilder.__FR_GROUP
                + "234"
                + TestMoneyFormatterBuilder.__FR_DECIMAL
                + "567"
                + TestMoneyFormatterBuilder.__FR_GROUP
                + "89",
            ],
            [
                TestMoneyFormatterBuilder.__GBP_MINUS_234_56,
                "-234" + TestMoneyFormatterBuilder.__FR_DECIMAL + "56",
            ],
        ]

    def test_appendAmount_3dp_BHD(self) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter0()
        money = Money.of2(CurrencyUnit.of1("BHD"), 6345345.735)
        self.assertEqual("6,345,345.735", test.print0(money))

    def test_appendAmount_JPY_2345(self) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("2,345", test.print0(self.__JPY_2345))
        self.assertEqual("${amount}", test.toString())

    def test_appendAmount_GBP_1234_56789_France(self) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter1(Locale.FRANCE)
        self.assertEqual("1,234.567,89", test.print0(self.__GBP_1234_56789))
        self.assertEqual("${amount}", test.toString())

    def test_appendAmount(self, money: BigMoneyProvider, expected: str) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual(expected, test.print0(money))
        self.assertEqual("${amount}", test.toString())

    @staticmethod
    def data_appendAmount() -> typing.List[typing.List[typing.Any]]:
        return [
            [TestMoneyFormatterBuilder.__GBP_2_34, "2.34"],
            [TestMoneyFormatterBuilder.__GBP_23_45, "23.45"],
            [TestMoneyFormatterBuilder.__GBP_234_56, "234.56"],
            [TestMoneyFormatterBuilder.__GBP_2345_67, "2,345.67"],
            [TestMoneyFormatterBuilder.__GBP_1234567_89, "1,234,567.89"],
            [TestMoneyFormatterBuilder.__GBP_1234_56789, "1,234.567,89"],
            [
                TestMoneyFormatterBuilder.__GBP_1234567891234_1234567891,
                "1,234,567,891,234.123,456,789,1",
            ],
            [TestMoneyFormatterBuilder.__GBP_MINUS_234_56, "-234.56"],
        ]

    def test_appendLiteral_parse_noMatch(self) -> None:

        self.iBuilder.appendLiteral("Hello")
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("Helol", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendLiteral_parse_tooShort(self) -> None:

        self.iBuilder.appendLiteral("Hello")
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("Hell", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendLiteral_parse_ok(self) -> None:

        self.iBuilder.appendLiteral("Hello")
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("HelloWorld", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(5, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendLiteral_print_null(self) -> None:

        self.__iBuilder.appendLiteral(None)
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("", test.print0(self.__GBP_2_34))
        self.assertEqual("", test.toString())

    def test_appendLiteral_print_empty(self) -> None:

        self.__iBuilder.appendLiteral("")
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("", test.print0(self.__GBP_2_34))
        self.assertEqual("", test.toString())

    def test_appendLiteral_print(self) -> None:

        self.__iBuilder.appendLiteral("Hello")
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("Hello", test.print0(self.__GBP_2_34))
        self.assertEqual("'Hello'", test.toString())

    def test_appendCurrencySymbolLocalized_parse(self) -> None:

        self.__iBuilder.appendCurrencySymbolLocalized()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual(False, test.isParser())

    def test_appendCurrencySymbolLocalized_print(self) -> None:

        self.__iBuilder.appendCurrencySymbolLocalized()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("\u00a3", test.print0(self.__GBP_2_34))
        self.assertEqual("${symbolLocalized}", test.toString())

    def test_appendCurrencyNumericCode_parse_empty(self) -> None:

        self.iBuilder.appendCurrencyNumericCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyNumericCode_parse_badCurrency(self) -> None:

        self.iBuilder.appendCurrencyNumericCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("991A", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyNumericCode_parse_tooShort(self) -> None:

        self.iBuilder.appendCurrencyNumericCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyNumericCode_parse_ok_notPadded2(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("51 ", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(2, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual("AMD", parsed.getCurrency().getCode())

    def test_appendCurrencyNumericCode_parse_ok_notPadded1(self) -> None:

        self.iBuilder.appendCurrencyNumericCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("8A", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(1, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual("ALL", parsed.getCurrency().getCode())

    def test_appendCurrencyNumericCode_parse_ok_padded(self) -> None:

        self.iBuilder.appendCurrencyNumericCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("008A", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(3, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual("ALL", parsed.getCurrency().getCode())

    def test_appendCurrencyNumericCode_parse_ok(self) -> None:

        self.iBuilder.appendCurrencyNumericCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("826A", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(3, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(CurrencyUnit.GBP, parsed.getCurrency())

    def test_appendCurrencyNumericCode_print(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("826", test.print0(self.__GBP_2_34))
        self.assertEqual("${numericCode}", test.toString())

    def test_appendCurrencyNumeric3Code_parse_empty(self) -> None:

        self.iBuilder.appendCurrencyNumeric3Code()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyNumeric3Code_parse_badCurrency(self) -> None:

        self.iBuilder.appendCurrencyNumeric3Code()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("991A", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyNumeric3Code_parse_tooShort(self) -> None:

        self.iBuilder.appendCurrencyNumeric3Code()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("82", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyNumeric3Code_parse_ok(self) -> None:

        self.iBuilder.appendCurrencyNumeric3Code()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("826A", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(3, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(CurrencyUnit.GBP, parsed.getCurrency())

    def test_appendCurrencyNumeric3Code_print(self) -> None:

        self.__iBuilder.appendCurrencyNumeric3Code()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("826", test.print0(self.__GBP_2_34))
        self.assertEqual("${numeric3Code}", test.toString())

    def test_appendCurrencyCode_parse_empty(self) -> None:

        self.iBuilder.appendCurrencyCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyCode_parse_tooShort(self) -> None:

        self.iBuilder.appendCurrencyCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("GB", 0)
        self.assertEqual(True, parsed.isError())
        self.assertEqual(0, parsed.getIndex())
        self.assertEqual(0, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(None, parsed.getCurrency())

    def test_appendCurrencyCode_parse_ok(self) -> None:

        self.iBuilder.appendCurrencyCode()
        test = self.iBuilder.toFormatter0()
        parsed = test.parse("GBP", 0)
        self.assertEqual(False, parsed.isError())
        self.assertEqual(3, parsed.getIndex())
        self.assertEqual(-1, parsed.getErrorIndex())
        self.assertEqual(None, parsed.getAmount())
        self.assertEqual(CurrencyUnit.GBP, parsed.getCurrency())

    def test_appendCurrencyCode_print(self) -> None:

        self.__iBuilder.appendCurrencyCode()
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("GBP", test.print0(self.__GBP_2_34))
        self.assertEqual("${code}", test.toString())

    def test_empty(self) -> None:

        test = self.__iBuilder.toFormatter0()
        self.assertEqual("", test.print0(self.__GBP_2_34))
        self.assertEqual("", test.toString())

    def afterMethod(self) -> None:
        Locale.setDefault(self.__cCachedLocale)
        self.__iBuilder = None

    def beforeMethod(self) -> None:

        # Set the default locale to TEST_GB_LOCALE
        Locale.setDefault(self.__TEST_GB_LOCALE)

        # Initialize the MoneyFormatterBuilder
        self.__iBuilder = MoneyFormatterBuilder()
