from __future__ import annotations
import io
import typing
from typing import *
import decimal
import os
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *


class TestMoneyAmountStyle:

    __MONEY: BigMoney = BigMoney.of(
        CurrencyUnit.GBP, decimal.Decimal("87654321.12345678")
    )

    __TEST_LV_LOCALE: typing.Any = Locale("lv", "LV", "TEST")

    __TEST_DE_LOCALE: typing.Any = Locale("de", "DE", "TEST")

    __TEST_GB_LOCALE: typing.Any = Locale("en", "GB", "TEST")

    __cCachedLocale: typing.Any = Locale.getDefault()

    def test_toString(self) -> None:

        test = MoneyAmountStyle.LOCALIZED_GROUPING
        assert test.toString().startswith("MoneyAmountStyle")

    def test_equals_notEqual_absValue(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withAbsValue(True)

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_absValue_true(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withAbsValue(True)
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withAbsValue(True)

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_equal_absValue_false(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withAbsValue(True).withAbsValue(False)
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withAbsValue(True).withAbsValue(False)

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_forcedDecimalPoint(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withForcedDecimalPoint(True)

        assert not a.equals(b)
        assert not b.equals(a)

    def test_equals_equal_forcedDecimalPoint_true(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withForcedDecimalPoint(True)
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withForcedDecimalPoint(True)

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_equal_forcedDecimalPoint_false(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withForcedDecimalPoint(
            True
        ).withForcedDecimalPoint(False)
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withForcedDecimalPoint(
            True
        ).withForcedDecimalPoint(False)

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_groupingSize(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingSize(4)

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_groupingSize(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingSize(4)
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingSize(4)

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_groupingStyle(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingStyle(
            GroupingStyle.BEFORE_DECIMAL_POINT
        )
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingStyle(GroupingStyle.NONE)

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_groupingStyle(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingStyle(
            GroupingStyle.BEFORE_DECIMAL_POINT
        )
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingStyle(
            GroupingStyle.BEFORE_DECIMAL_POINT
        )

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_groupingChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingCharacter("_")

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_groupingChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingCharacter("_")

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_decimalPointChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withDecimalPointCharacter("_")

        assert not a.equals(b)
        assert not b.equals(a)

    def test_equals_equal_decimalPointChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withDecimalPointCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withDecimalPointCharacter("_")

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_negativeChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withNegativeSignCharacter("_")

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_negativeChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withNegativeSignCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withNegativeSignCharacter("_")

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_positiveChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withPositiveSignCharacter("_")

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_positiveChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withPositiveSignCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withPositiveSignCharacter("_")

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_notEqual_zeroChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter("_")

        assert a.equals(b) == False
        assert b.equals(a) == False

    def test_equals_equal_zeroChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter("_")

        assert a.equals(b)
        assert b.equals(a)
        assert b.hashCode() == a.hashCode()

    def test_equals_null(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        assert a.equals(None) == False

    def test_equals_otherType(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(False, a.equals(object()))

    def test_equals_same(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(True, a.equals(a))

    def test_withAbsValue_same(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        assert base.isAbsValue() == False
        test = base.withAbsValue(False)
        assert test is base

    def test_withAbsValue(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        assert base.isAbsValue() == False
        test = base.withAbsValue(True)
        assert base.isAbsValue() == False
        assert test.isAbsValue() == True

    def test_withForcedDecimalPoint_same(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        assert base.isForcedDecimalPoint() == False
        test = base.withForcedDecimalPoint(False)
        assert test is base

    def test_withForcedDecimalPoint(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        assert False == base.isForcedDecimalPoint()
        test = base.withForcedDecimalPoint(True)
        assert False == base.isForcedDecimalPoint()
        assert True == test.isForcedDecimalPoint()

    def test_withGroupingSize_negative(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        base.withGroupingSize(-1)

    def test_withGroupingSize_sameNull(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getGroupingSize())
        test = base.withGroupingSize(None)
        self.assertIs(base, test)

    def test_withGroupingSize_same(self) -> None:

        base = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        self.assertEqual(3, base.getGroupingSize())
        test = base.withGroupingSize(3)
        self.assertIs(base, test)

    def test_withGroupingSize(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getGroupingSize())
        test = base.withGroupingSize(6)
        self.assertEqual(None, base.getGroupingSize())
        self.assertEqual(6, test.getGroupingSize())

    def test_withGroupingStyle_same(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        assert GroupingStyle.FULL == base.getGroupingStyle()
        test = base.withGroupingStyle(GroupingStyle.FULL)
        assert base is test

    def test_withGroupingStyle(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        assert GroupingStyle.FULL == base.getGroupingStyle()
        test = base.withGroupingStyle(GroupingStyle.BEFORE_DECIMAL_POINT)
        assert GroupingStyle.FULL == base.getGroupingStyle()
        assert GroupingStyle.BEFORE_DECIMAL_POINT == test.getGroupingStyle()

    def test_withGroupingCharacter_sameNull(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getGroupingCharacter())
        test = base.withGroupingCharacter(None)
        self.assertIs(base, test)

    def test_withGroupingCharacter_same(self) -> None:

        base = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        self.assertEqual(",", base.getGroupingCharacter())
        test = base.withGroupingCharacter(",")
        self.assertIs(base, test)

    def test_withGroupingCharacter(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getGroupingCharacter())
        test = base.withGroupingCharacter("_")
        self.assertEqual(None, base.getGroupingCharacter())
        self.assertEqual("_", test.getGroupingCharacter())

    def test_withDecimalPointCharacter_sameNull(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getDecimalPointCharacter())
        test = base.withDecimalPointCharacter(None)
        self.assertIs(base, test)

    def test_withDecimalPointCharacter_same(self) -> None:

        base = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        self.assertEqual(".", base.getDecimalPointCharacter())
        test = base.withDecimalPointCharacter(".")
        self.assertIs(base, test)

    def test_withDecimalPointCharacter(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getDecimalPointCharacter())
        test = base.withDecimalPointCharacter("_")
        self.assertEqual(None, base.getDecimalPointCharacter())
        self.assertEqual("_", test.getDecimalPointCharacter())

    def test_withNegativeSignCharacter_sameNull(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getNegativeSignCharacter())
        test = base.withNegativeSignCharacter(None)
        self.assertIs(base, test)

    def test_withNegativeSignCharacter_same(self) -> None:

        base = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        self.assertEqual("-", base.getNegativeSignCharacter())
        test = base.withNegativeSignCharacter("-")
        self.assertIs(base, test)

    def test_withNegativeSignCharacter(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getNegativeSignCharacter())
        test = base.withNegativeSignCharacter("_")
        self.assertEqual(None, base.getNegativeSignCharacter())
        self.assertEqual("_", test.getNegativeSignCharacter())

    def test_withPositiveSignCharacter_sameNull(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getPositiveSignCharacter())
        test = base.withPositiveSignCharacter(None)
        self.assertIs(base, test)

    def test_withPositiveSignCharacter_same(self) -> None:

        base = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        assert "+" == base.getPositiveSignCharacter()
        test = base.withPositiveSignCharacter("+")
        assert base == test

    def test_withPositiveSignCharacter(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getPositiveSignCharacter())
        test = base.withPositiveSignCharacter("_")
        self.assertEqual(None, base.getPositiveSignCharacter())
        self.assertEqual("_", test.getPositiveSignCharacter())

    def test_withZeroCharacter_sameNull(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getZeroCharacter())
        test = base.withZeroCharacter(None)
        self.assertIs(base, test)

    def test_withZeroCharacter_same(self) -> None:

        base = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        self.assertEqual("0", base.getZeroCharacter())
        test = base.withZeroCharacter("0")
        self.assertIs(base, test)

    def test_withZeroCharacter(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(None, base.getZeroCharacter())
        test = base.withZeroCharacter("_")
        self.assertEqual(None, base.getZeroCharacter())
        self.assertEqual("_", test.getZeroCharacter())

    def test_localize_LV(self) -> None:

        pass  # LLM could not translate this method

    def test_localize_DE_noGrouping(self) -> None:

        pass  # LLM could not translate this method

    def test_localize_DE_fixedZeroAndDecimal(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter(
            "_"
        ).withDecimalPointCharacter("-")
        style = base.localize(self.__TEST_DE_LOCALE)

        assert style.getZeroCharacter() == "_"
        assert style.getPositiveSignCharacter() == "+"
        assert style.getNegativeSignCharacter() == "-"
        assert style.getDecimalPointCharacter() == "-"
        assert style.getGroupingCharacter() == "."
        assert style.getGroupingStyle() == GroupingStyle.FULL
        assert style.getGroupingSize() == 3
        assert style.getExtendedGroupingSize() == 0
        assert style.isForcedDecimalPoint() == False

    def test_localize_DE_fixedGrouping(self) -> None:

        pass  # LLM could not translate this method

    def test_localize_DE_fixedDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_localize_DE_fixedNegative(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING.withNegativeSignCharacter("_")
        style = base.localize(self.__TEST_DE_LOCALE)

        assert style.getZeroCharacter() == "0"
        assert style.getPositiveSignCharacter() == "+"
        assert style.getNegativeSignCharacter() == "_"
        assert style.getDecimalPointCharacter() == ","
        assert style.getGroupingCharacter() == "."
        assert style.getGroupingStyle() == GroupingStyle.FULL
        assert style.getGroupingSize() == 3
        assert style.getExtendedGroupingSize() == 0
        assert style.isForcedDecimalPoint() == False

    def test_localize_DE_fixedPositive(self) -> None:

        pass  # LLM could not translate this method

    def test_localize_DE_fixedZero(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter("_")
        style = base.localize(self.__TEST_DE_LOCALE)

        assert style.getZeroCharacter() == "_"
        assert style.getPositiveSignCharacter() == "+"
        assert style.getNegativeSignCharacter() == "-"
        assert style.getDecimalPointCharacter() == ","
        assert style.getGroupingCharacter() == "."
        assert style.getGroupingStyle() == GroupingStyle.FULL
        assert style.getGroupingSize() == 3
        assert style.getExtendedGroupingSize() == 0
        assert style.isForcedDecimalPoint() == False

    def test_localize_DE(self) -> None:

        pass  # LLM could not translate this method

    def test_localize_GB(self) -> None:

        pass  # LLM could not translate this method

    def test_of_Locale_DE(self) -> None:

        style = MoneyAmountStyle.of(self.__TEST_DE_LOCALE)

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "," == style.getDecimalPointCharacter()
        assert "." == style.getGroupingCharacter()
        assert GroupingStyle.FULL == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def test_of_Locale_GB(self) -> None:

        pass  # LLM could not translate this method

    def test_print_groupBeforeDecimal(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingStyle(
            GroupingStyle.BEFORE_DECIMAL_POINT
        )
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87,654,321.12345678", test.print0(self.__MONEY))

    def test_LOCALIZED_NO_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_NO_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        assert test.print0(self.__MONEY) == "87654321.12345678"

    def test_LOCALIZED_NO_GROUPING(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_NO_GROUPING

        assert style.getZeroCharacter() is None
        assert style.getPositiveSignCharacter() is None
        assert style.getNegativeSignCharacter() is None
        assert style.getDecimalPointCharacter() is None
        assert style.getGroupingCharacter() is None
        assert style.getGroupingStyle() == GroupingStyle.NONE
        assert style.getGroupingSize() is None
        assert style.getExtendedGroupingSize() is None
        assert style.isForcedDecimalPoint() == False

    def test_LOCALIZED_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        assert test.print0(self.__MONEY) == "87,654,321.123,456,78"

    def test_LOCALIZED_GROUPING(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_GROUPING

        assert style.getZeroCharacter() is None
        assert style.getPositiveSignCharacter() is None
        assert style.getNegativeSignCharacter() is None
        assert style.getDecimalPointCharacter() is None
        assert style.getGroupingCharacter() is None
        assert style.getGroupingStyle() == GroupingStyle.FULL
        assert style.getGroupingSize() is None
        assert style.getExtendedGroupingSize() is None
        assert style.isForcedDecimalPoint() == False

    def test_ASCII_DECIMAL_COMMA_NO_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_NO_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87654321,12345678", test.print0(self.__MONEY))

    def test_ASCII_DECIMAL_COMMA_NO_GROUPING(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_NO_GROUPING

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "," == style.getDecimalPointCharacter()
        assert "." == style.getGroupingCharacter()
        assert GroupingStyle.NONE == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def test_ASCII_DECIMAL_COMMA_GROUP3_SPACE_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_SPACE
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87 654 321,123 456 78", test.print0(self.__MONEY))

    def test_ASCII_DECIMAL_COMMA_GROUP3_SPACE(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_SPACE

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "," == style.getDecimalPointCharacter()
        assert " " == style.getGroupingCharacter()
        assert GroupingStyle.FULL == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def test_ASCII_DECIMAL_COMMA_GROUP3_DOT_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_DOT
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        result = test.print0(self.__MONEY)

        self.assertEqual("87.654.321,123.456.78", result)

    def test_ASCII_ASCII_DECIMAL_COMMA_GROUP3_DOT(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_DOT

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "," == style.getDecimalPointCharacter()
        assert "." == style.getGroupingCharacter()
        assert GroupingStyle.FULL == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def test_ASCII_DECIMAL_POINT_NO_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_NO_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        result = test.print0(self.__MONEY)

        assert result == "87654321.12345678"

    def test_ASCII_DECIMAL_POINT_NO_GROUPING(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_NO_GROUPING

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "." == style.getDecimalPointCharacter()
        assert "," == style.getGroupingCharacter()
        assert GroupingStyle.NONE == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def test_ASCII_ASCII_DECIMAL_POINT_GROUP3_SPACE_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_SPACE
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        result = test.print0(self.__MONEY)

        self.assertEqual("87 654 321.123 456 78", result)

    def test_ASCII_DECIMAL_POINT_GROUP3_SPACE(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_SPACE

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "." == style.getDecimalPointCharacter()
        assert " " == style.getGroupingCharacter()
        assert GroupingStyle.FULL == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def test_ASCII_DECIMAL_POINT_GROUP3_COMMA_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        result = test.print0(self.__MONEY)

        self.assertEqual("87,654,321.123,456,78", result)

    def test_ASCII_DECIMAL_POINT_GROUP3_COMMA(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA

        assert "0" == style.getZeroCharacter()
        assert "+" == style.getPositiveSignCharacter()
        assert "-" == style.getNegativeSignCharacter()
        assert "." == style.getDecimalPointCharacter()
        assert "," == style.getGroupingCharacter()
        assert GroupingStyle.FULL == style.getGroupingStyle()
        assert 3 == style.getGroupingSize()
        assert 0 == style.getExtendedGroupingSize()
        assert False == style.isForcedDecimalPoint()

    def afterMethod(self) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "")

    def beforeMethod(self) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_GB.utf8")
