from __future__ import annotations
import io
import typing
from typing import *
import decimal
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


class TestMoneyFormatterBuilder:

    __iBuilder: MoneyFormatterBuilder = None

    __FR_GROUP: str = decimal.Decimal(1000).to_eng_string().replace(",", "")[1]

    __FR_DECIMAL: str = FR_SYMBOLS.getMonetaryDecimalSeparator()

    __FR_SYMBOLS = decimal.Decimal(Locale.FRANCE)

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

    GBP_2_34: Money = Money.parse("GBP 2.34")

    __BHD: CurrencyUnit = CurrencyUnit.of("BHD")

    __JPY: CurrencyUnit = CurrencyUnit.of("JPY")

    __GBP: CurrencyUnit = CurrencyUnit.GBP

    def test_toFormatter_Locale(self) -> None:

        test = self.__iBuilder.toFormatter1(self.__TEST_FR_LOCALE)
        self.assertEqual(self.__TEST_FR_LOCALE, test.getLocale())

    def test_toFormatter_defaultLocale(self) -> None:

        test = self.__iBuilder.toFormatter0()
        assert self.__TEST_GB_LOCALE == test.getLocale()

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

        self.assertEqual("GBP 234.56", f.print0(self.__GBP_234_56))
        self.assertEqual(
            "GBP 0.00 (zero)", f.print0(BigMoney.zero0(self.__GBP).withScale0(2))
        )
        self.assertEqual("GBP (234.56)", f.print0(self.__GBP_MINUS_234_56))
        self.assertEqual(self.__GBP_234_56.toBigMoney(), f.parseBigMoney("GBP 234.56"))
        self.assertEqual(
            BigMoney.zero0(self.__GBP).withScale0(2), f.parseBigMoney("GBP 0.00 (zero)")
        )
        self.assertEqual(BigMoney.zero0(self.__GBP), f.parseBigMoney("GBP 1.23 (zero)"))
        self.assertEqual(
            self.__GBP_MINUS_234_56.toBigMoney(), f.parseBigMoney("GBP (234.56)")
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

        assert f.print0(self.__GBP_234_56) == "GBP 234.56"
        assert f.print0(Money.zero(self.__GBP)) == "GBP -"
        assert f.print0(self.__GBP_MINUS_234_56) == "(GBP 234.56)"
        assert f.parseMoney("GBP 234.56") == self.__GBP_234_56
        assert f.parseMoney("GBP -234.56") == self.__GBP_MINUS_234_56
        assert f.parseMoney("GBP -") == Money.zero(self.__GBP)
        assert f.parseMoney("(GBP 234.56)") == self.__GBP_MINUS_234_56
        assert f.parseMoney("(GBP -234.56)") == self.__GBP_MINUS_234_56

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

        assert (
            f.toString()
            == "PositiveZeroNegative(${code}' '${amount},${code}' '${amount},'('${code}' '${amount}')')"
        )
        assert f.print0(self.__GBP_234_56) == "GBP 234.56"
        assert f.print0(Money.zero(self.__GBP)) == "GBP 0.00"
        assert f.print0(self.__GBP_MINUS_234_56) == "(GBP 234.56)"
        assert f.parseMoney("GBP 234.56") == self.__GBP_234_56
        assert f.parseMoney("GBP 0") == Money.zero(self.__GBP)
        assert f.parseMoney("(GBP 234.56)") == self.__GBP_MINUS_234_56
        context = f.parse("X", 0)
        assert context.getIndex() == 0
        assert context.getErrorIndex() == 0

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
        assert test.isPrinter() == False
        assert test.isParser() == False
        assert test.toString() == ""

    def test_append_MoneyPrinterMoneyParser_parser(self) -> None:

        parser = MoneyParser()
        parser.parse = lambda context: (
            context.setAmount(self.__JPY_2345.getAmount()),
            context.setCurrency(self.__JPY_2345.getCurrencyUnit()),
        )

        self.__iBuilder.append1(None, parser)
        test = self.__iBuilder.toFormatter0()

        assert test.isPrinter() == False
        assert test.isParser() == True
        assert test.parseMoney("") == self.__JPY_2345
        assert test.toString().startswith(
            "org.joda.money.format.TestMoneyFormatterBuilder$"
        )

    def test_append_MoneyPrinterMoneyParser_printer(self) -> None:

        class MoneyPrinterImpl(MoneyPrinter):
            def print(
                self,
                context: MoneyPrintContext,
                appendable: Appendable,
                money: BigMoney,
            ) -> None:
                appendable.append("HELLO")

        printer = MoneyPrinterImpl()
        self.__iBuilder.append1(printer, None)
        test = self.__iBuilder.toFormatter0()
        assert test.isPrinter()
        assert not test.isParser()
        assert test.print0(self.__JPY_2345) == "HELLO"
        assert test.toString().startswith(
            "org.joda.money.format.TestMoneyFormatterBuilder$"
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
        assert expected == money

    def test_appendAmount_parseExtendedGroupingSize(
        self, money: BigMoneyProvider, expected: str
    ) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.appendAmount1(
            MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA.withExtendedGroupingSize(
                2
            )
        ).toFormatter0()
        assert expected == test.print0(money)
        assert "${amount}" == test.toString()

    @staticmethod
    def data_appendAmountExtendedGrouping() -> typing.List[typing.List[typing.Any]]:

        GBP_2_34 = Money.of(TestMoneyFormatterBuilder.__GBP, decimal.Decimal("2.34"))
        GBP_23_45 = Money.of(TestMoneyFormatterBuilder.__GBP, decimal.Decimal("23.45"))
        GBP_234_56 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("234.56")
        )
        GBP_2345_67 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("2345.67")
        )
        GBP_1234567_89 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("1234567.89")
        )
        GBP_1234_56789 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("1234.56789")
        )
        GBP_1234567891234_1234567891 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("1234567891234.1234567891")
        )
        GBP_MINUS_234_56 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("-234.56")
        )

        return [
            [GBP_2_34, "2.34"],
            [GBP_23_45, "23.45"],
            [GBP_234_56, "234.56"],
            [GBP_2345_67, "2,345.67"],
            [GBP_1234567_89, "12,34,567.89"],
            [GBP_1234_56789, "1,234.567,89"],
            [GBP_1234567891234_1234567891, "12,34,56,78,91,234.123,45,67,89,1"],
            [GBP_MINUS_234_56, "-234.56"],
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
        assert expected == test.print0(money)
        if not style.isAbsValue():
            assert money.getAmount() == test.parse(expected, 0).getAmount()
        else:
            assert money.getAmount().copy_abs() == test.parse(expected, 0).getAmount()

    def test_appendAmount_MoneyAmountStyle_JPY(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:

        self.__iBuilder.appendAmount1(style)
        test = self.__iBuilder.toFormatter0()
        money = BigMoney.of0(self.__JPY, decimal.Decimal(amount))
        assert expected == test.print0(money)
        if not style.isAbsValue():
            assert money.getAmount() == test.parse(expected, 0).getAmount()
        else:
            assert money.getAmount().copy_abs() == test.parse(expected, 0).getAmount()

    def test_appendAmount_MoneyAmountStyle_GBP(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:

        self.__iBuilder.appendAmount1(style)
        test = self.__iBuilder.toFormatter0()
        money = BigMoney.of0(self.__GBP, decimal.Decimal(amount))
        assert expected == test.print0(money)
        if not style.isAbsValue():
            assert money.getAmount() == test.parse(expected, 0).getAmount()
        else:
            assert money.getAmount().copy_abs() == test.parse(expected, 0).getAmount()

    @staticmethod
    def data_appendAmount_MoneyAmountStyle() -> typing.List[typing.List[typing.Any]]:

        pass  # LLM could not translate this method

    def test_appendAmount_MoneyAmountStyle_null(self) -> None:

        # Assuming that the method appendAmount1 is a method of the class MoneyFormatterBuilder
        # and it takes a MoneyAmountStyle object as an argument.
        # Since null is not a valid argument in Python, we can pass None as an argument.
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
        assert expected == test.print0(money)
        assert "${amount}" == test.toString()

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
        money = Money.of2(self.__BHD, 6345345.735)
        assert test.print0(money) == "6,345,345.735"

    def test_appendAmount_JPY_2345(self) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter0()
        assert "2,345" == test.print0(self.__JPY_2345)
        assert "${amount}" == test.toString()

    def test_appendAmount_GBP_1234_56789_France(self) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter1(Locale.FRANCE)
        self.assertEqual("1,234.567,89", test.print0(self.__GBP_1234_56789))
        self.assertEqual("${amount}", test.toString())

    def test_appendAmount(self, money: BigMoneyProvider, expected: str) -> None:

        self.__iBuilder.appendAmount0()
        test = self.__iBuilder.toFormatter0()
        assert expected == test.print0(money)
        assert "${amount}" == test.toString()

    @staticmethod
    def data_appendAmount() -> typing.List[typing.List[typing.Any]]:

        GBP_2_34 = Money.of(TestMoneyFormatterBuilder.__GBP, decimal.Decimal("2.34"))
        GBP_23_45 = Money.of(TestMoneyFormatterBuilder.__GBP, decimal.Decimal("23.45"))
        GBP_234_56 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("234.56")
        )
        GBP_2345_67 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("2345.67")
        )
        GBP_1234567_89 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("1234567.89")
        )
        GBP_1234_56789 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("1234.56789")
        )
        GBP_1234567891234_1234567891 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("1234567891234.1234567891")
        )
        GBP_MINUS_234_56 = Money.of(
            TestMoneyFormatterBuilder.__GBP, decimal.Decimal("-234.56")
        )

        return [
            [GBP_2_34, "2.34"],
            [GBP_23_45, "23.45"],
            [GBP_234_56, "234.56"],
            [GBP_2345_67, "2,345.67"],
            [GBP_1234567_89, "1,234,567.89"],
            [GBP_1234_56789, "1,234.567,89"],
            [GBP_1234567891234_1234567891, "1,234,567,891,234.123,456,789,1"],
            [GBP_MINUS_234_56, "-234.56"],
        ]

    def test_appendLiteral_parse_noMatch(self) -> None:

        self.__iBuilder.appendLiteral("Hello")
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("Helol", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendLiteral_parse_tooShort(self) -> None:

        self.__iBuilder.appendLiteral("Hello")
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("Hell", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendLiteral_parse_ok(self) -> None:

        self.__iBuilder.appendLiteral("Hello")
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("HelloWorld", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 5
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendLiteral_print_null(self) -> None:

        self.__iBuilder.appendLiteral(None)
        test = self.__iBuilder.toFormatter0()
        assert test.print0(self.__GBP_2_34) == ""
        assert test.toString() == ""

    def test_appendLiteral_print_empty(self) -> None:

        self.__iBuilder.appendLiteral("")
        test = self.__iBuilder.toFormatter0()
        assert test.print0(self.__GBP_2_34) == ""
        assert test.toString() == ""

    def test_appendLiteral_print(self) -> None:

        self.__iBuilder.appendLiteral("Hello")
        test = self.__iBuilder.toFormatter0()
        self.assertEqual("Hello", test.print0(self.__GBP_2_34))
        self.assertEqual("'Hello'", test.toString())

    def test_appendCurrencySymbolLocalized_parse(self) -> None:

        self.__iBuilder.appendCurrencySymbolLocalized()
        test = self.__iBuilder.toFormatter0()
        assert test.isParser() == False

    def test_appendCurrencySymbolLocalized_print(self) -> None:

        self.__iBuilder.appendCurrencySymbolLocalized()
        test = self.__iBuilder.toFormatter0()
        assert "\u00a3" == test.print0(self.__GBP_2_34)
        assert "${symbolLocalized}" == test.toString()

    def test_appendCurrencyNumericCode_parse_empty(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyNumericCode_parse_badCurrency(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("991A", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyNumericCode_parse_tooShort(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyNumericCode_parse_ok_notPadded2(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("51 ", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 2
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency().getCode() == "AMD"

    def test_appendCurrencyNumericCode_parse_ok_notPadded1(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("8A", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 1
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency().getCode() == "ALL"

    def test_appendCurrencyNumericCode_parse_ok_padded(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("008A", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 3
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency().getCode() == "ALL"

    def test_appendCurrencyNumericCode_parse_ok(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("826A", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 3
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == self.__GBP

    def test_appendCurrencyNumericCode_print(self) -> None:

        self.__iBuilder.appendCurrencyNumericCode()
        test = self.__iBuilder.toFormatter0()
        assert "826" == test.print0(self.__GBP_2_34)
        assert "${numericCode}" == test.toString()

    def test_appendCurrencyNumeric3Code_parse_empty(self) -> None:

        self.__iBuilder.appendCurrencyNumeric3Code()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyNumeric3Code_parse_badCurrency(self) -> None:

        self.__iBuilder.appendCurrencyNumeric3Code()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("991A", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyNumeric3Code_parse_tooShort(self) -> None:

        self.__iBuilder.appendCurrencyNumeric3Code()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("82", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyNumeric3Code_parse_ok(self) -> None:

        self.__iBuilder.appendCurrencyNumeric3Code()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("826A", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 3
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == self.__GBP

    def test_appendCurrencyNumeric3Code_print(self) -> None:

        self.__iBuilder.appendCurrencyNumeric3Code()
        test = self.__iBuilder.toFormatter0()
        assert "826" == test.print0(self.__GBP_2_34)
        assert "${numeric3Code}" == test.toString()

    def test_appendCurrencyCode_parse_empty(self) -> None:

        self.__iBuilder.appendCurrencyCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyCode_parse_tooShort(self) -> None:

        self.__iBuilder.appendCurrencyCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("GB", 0)
        assert parsed.isError() == True
        assert parsed.getIndex() == 0
        assert parsed.getErrorIndex() == 0
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == None

    def test_appendCurrencyCode_parse_ok(self) -> None:

        self.__iBuilder.appendCurrencyCode()
        test = self.__iBuilder.toFormatter0()
        parsed = test.parse("GBP", 0)
        assert parsed.isError() == False
        assert parsed.getIndex() == 3
        assert parsed.getErrorIndex() == -1
        assert parsed.getAmount() == None
        assert parsed.getCurrency() == self.__GBP

    def test_appendCurrencyCode_print(self) -> None:

        self.__iBuilder.appendCurrencyCode()
        test = self.__iBuilder.toFormatter0()
        assert "GBP" == test.print0(self.__GBP_2_34)
        assert "${code}" == test.toString()

    def test_empty(self) -> None:

        test: MoneyFormatter = self.__iBuilder.toFormatter0()
        assert test.print0(self.__GBP_2_34) == ""
        assert test.toString() == ""

    def afterMethod(self) -> None:

        # Locale.setDefault(cCachedLocale)
        # This is not possible in Python, as Python does not have a direct equivalent to Java's Locale.setDefault() method.
        # However, you can set the locale for the entire program using the locale module.
        # import locale
        # locale.setlocale(locale.LC_ALL, '<locale>')

        # iBuilder = null
        self.__iBuilder = None

    def beforeMethod(self) -> None:

        # Set the default locale to TEST_GB_LOCALE
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")

        # Create a new instance of MoneyFormatterBuilder
        self.__iBuilder = MoneyFormatterBuilder()
