from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import decimal
import typing
from typing import *
import io

# Imports End


class TestMoneyFormatterBuilder:

    # Class Fields Begin
    __GBP: CurrencyUnit = None
    __JPY: CurrencyUnit = None
    __BHD: CurrencyUnit = None
    __GBP_2_34: Money = None
    __GBP_23_45: Money = None
    __GBP_234_56: Money = None
    __GBP_MINUS_234_56: Money = None
    __GBP_2345_67: Money = None
    __GBP_1234567_89: Money = None
    __GBP_1234_56789: BigMoney = None
    __GBP_1234567891234_1234567891: BigMoney = None
    __JPY_2345: Money = None
    __cCachedLocale: typing.Any = None
    __TEST_GB_LOCALE: typing.Any = None
    __TEST_FR_LOCALE: typing.Any = None
    __FR_SYMBOLS: typing.Union[decimal.Decimal, str] = None
    __FR_DECIMAL: str = None
    __FR_GROUP: str = None
    __iBuilder: MoneyFormatterBuilder = None
    # Class Fields End

    # Class Methods Begin
    def test_toFormatter_Locale(self) -> None:
        pass

    def test_toFormatter_defaultLocale(self) -> None:
        pass

    def test_appendSigned_PZN_edgeCases(self) -> None:
        pass

    def test_appendSigned_PZN(self) -> None:
        pass

    def test_appendSigned_PN(self) -> None:
        pass

    def test_append_MoneyFormatter(self) -> None:
        pass

    def test_append_MoneyPrinter_nullMoneyPrinter_nullMoneyParser(self) -> None:
        pass

    def test_append_MoneyPrinterMoneyParser_parser(self) -> None:
        pass

    def test_append_MoneyPrinterMoneyParser_printer(self) -> None:
        pass

    def test_appendAmount_parseExcessGrouping(self) -> None:
        pass

    def test_appendAmount_parseExtendedGroupingSize(
        self, money: BigMoneyProvider, expected: str
    ) -> None:
        pass

    @staticmethod
    def data_appendAmountExtendedGrouping() -> typing.List[typing.List[typing.Any]]:
        pass

    def test_appendAmount_MoneyAmountStyle_JPY_issue49(self) -> None:
        pass

    def test_appendAmount_MoneyAmountStyle_BHD(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:
        pass

    def test_appendAmount_MoneyAmountStyle_JPY(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:
        pass

    def test_appendAmount_MoneyAmountStyle_GBP(
        self, style: MoneyAmountStyle, amount: str, expected: str
    ) -> None:
        pass

    @staticmethod
    def data_appendAmount_MoneyAmountStyle() -> typing.List[typing.List[typing.Any]]:
        pass

    def test_appendAmount_MoneyAmountStyle_null(self) -> None:
        pass

    def test_appendAmountLocalized_JPY_2345(self) -> None:
        pass

    def test_appendAmountLocalized_GBP_1234_56789_US(self) -> None:
        pass

    def test_appendAmountLocalized(
        self, money: BigMoneyProvider, expected: str
    ) -> None:
        pass

    @staticmethod
    def data_appendAmountLocalized() -> typing.List[typing.List[typing.Any]]:
        pass

    def test_appendAmount_3dp_BHD(self) -> None:
        pass

    def test_appendAmount_JPY_2345(self) -> None:
        pass

    def test_appendAmount_GBP_1234_56789_France(self) -> None:
        pass

    def test_appendAmount(self, money: BigMoneyProvider, expected: str) -> None:
        pass

    @staticmethod
    def data_appendAmount() -> typing.List[typing.List[typing.Any]]:
        pass

    def test_appendLiteral_parse_noMatch(self) -> None:
        pass

    def test_appendLiteral_parse_tooShort(self) -> None:
        pass

    def test_appendLiteral_parse_ok(self) -> None:
        pass

    def test_appendLiteral_print_null(self) -> None:
        pass

    def test_appendLiteral_print_empty(self) -> None:
        pass

    def test_appendLiteral_print(self) -> None:
        pass

    def test_appendCurrencySymbolLocalized_parse(self) -> None:
        pass

    def test_appendCurrencySymbolLocalized_print(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_empty(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_badCurrency(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_tooShort(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_ok_notPadded2(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_ok_notPadded1(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_ok_padded(self) -> None:
        pass

    def test_appendCurrencyNumericCode_parse_ok(self) -> None:
        pass

    def test_appendCurrencyNumericCode_print(self) -> None:
        pass

    def test_appendCurrencyNumeric3Code_parse_empty(self) -> None:
        pass

    def test_appendCurrencyNumeric3Code_parse_badCurrency(self) -> None:
        pass

    def test_appendCurrencyNumeric3Code_parse_tooShort(self) -> None:
        pass

    def test_appendCurrencyNumeric3Code_parse_ok(self) -> None:
        pass

    def test_appendCurrencyNumeric3Code_print(self) -> None:
        pass

    def test_appendCurrencyCode_parse_empty(self) -> None:
        pass

    def test_appendCurrencyCode_parse_tooShort(self) -> None:
        pass

    def test_appendCurrencyCode_parse_ok(self) -> None:
        pass

    def test_appendCurrencyCode_print(self) -> None:
        pass

    def test_empty(self) -> None:
        pass

    def afterMethod(self) -> None:
        pass

    def beforeMethod(self) -> None:
        pass

    # Class Methods End
