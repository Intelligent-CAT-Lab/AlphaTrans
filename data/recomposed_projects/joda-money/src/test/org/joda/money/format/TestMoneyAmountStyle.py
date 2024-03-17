# Imports Begin
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import unittest
import os
import typing
from typing import *

# Imports End


class TestMoneyAmountStyle(unittest.TestCase):

    # Class Fields Begin
    __cCachedLocale: typing.Any = ""  # LLM could not translate field
    __TEST_GB_LOCALE: typing.Any = ""  # LLM could not translate field
    __TEST_DE_LOCALE: typing.Any = ""  # LLM could not translate field
    __TEST_LV_LOCALE: typing.Any = ""  # LLM could not translate field
    __MONEY: BigMoney = BigMoney.of(CurrencyUnit.GBP, BigDecimal("87654321.12345678"))
    # Class Fields End

    # Class Methods Begin
    def test_toString(self) -> None:

        test = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertTrue(test.toString().startswith("MoneyAmountStyle"))

    def test_equals_notEqual_absValue(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_absValue_true(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_absValue_false(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_notEqual_forcedDecimalPoint(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_forcedDecimalPoint_true(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_forcedDecimalPoint_false(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_notEqual_groupingSize(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_groupingSize(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingSize(4)
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingSize(4)
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(b.hashCode(), a.hashCode())

    def test_equals_notEqual_groupingStyle(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_groupingStyle(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_notEqual_groupingChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingCharacter("_")
        self.assertEqual(False, a.equals(b))
        self.assertEqual(False, b.equals(a))

    def test_equals_equal_groupingChar(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_notEqual_decimalPointChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withDecimalPointCharacter("_")
        self.assertEqual(False, a.equals(b))
        self.assertEqual(False, b.equals(a))

    def test_equals_equal_decimalPointChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withDecimalPointCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withDecimalPointCharacter("_")
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(b.hashCode(), a.hashCode())

    def test_equals_notEqual_negativeChar(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_negativeChar(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_notEqual_positiveChar(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_positiveChar(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING.withPositiveSignCharacter("_")
        b = MoneyAmountStyle.LOCALIZED_GROUPING.withPositiveSignCharacter("_")
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(b.hashCode(), a.hashCode())

    def test_equals_notEqual_zeroChar(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_equal_zeroChar(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_null(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(False, a.equals(None))

    def test_equals_otherType(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(False, a.equals(Object()))

    def test_equals_same(self) -> None:

        a = MoneyAmountStyle.LOCALIZED_GROUPING
        self.assertEqual(True, a.equals(a))

    def test_withAbsValue_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withAbsValue(self) -> None:

        pass  # LLM could not translate method body

    def test_withForcedDecimalPoint_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withForcedDecimalPoint(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingSize_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingSize_sameNull(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingSize_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingSize(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingStyle_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingStyle(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingCharacter_sameNull(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingCharacter_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withGroupingCharacter(self) -> None:

        pass  # LLM could not translate method body

    def test_withDecimalPointCharacter_sameNull(self) -> None:

        pass  # LLM could not translate method body

    def test_withDecimalPointCharacter_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withDecimalPointCharacter(self) -> None:

        pass  # LLM could not translate method body

    def test_withNegativeSignCharacter_sameNull(self) -> None:

        pass  # LLM could not translate method body

    def test_withNegativeSignCharacter_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withNegativeSignCharacter(self) -> None:

        pass  # LLM could not translate method body

    def test_withPositiveSignCharacter_sameNull(self) -> None:

        pass  # LLM could not translate method body

    def test_withPositiveSignCharacter_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withPositiveSignCharacter(self) -> None:

        pass  # LLM could not translate method body

    def test_withZeroCharacter_sameNull(self) -> None:

        pass  # LLM could not translate method body

    def test_withZeroCharacter_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withZeroCharacter(self) -> None:

        pass  # LLM could not translate method body

    def test_localize_LV(self) -> None:

        pass  # LLM could not translate method body

    def test_localize_DE_noGrouping(self) -> None:

        pass  # LLM could not translate method body

    def test_localize_DE_fixedZeroAndDecimal(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter(
            "_"
        ).withDecimalPointCharacter("-")
        style = base.localize(TEST_DE_LOCALE)
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

        base = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingCharacter("_")
        style = base.localize(TEST_DE_LOCALE)
        assert style.getZeroCharacter() == "0"
        assert style.getPositiveSignCharacter() == "+"
        assert style.getNegativeSignCharacter() == "-"
        assert style.getDecimalPointCharacter() == ","
        assert style.getGroupingCharacter() == "_"
        assert style.getGroupingStyle() == GroupingStyle.FULL
        assert style.getGroupingSize() == 3
        assert style.getExtendedGroupingSize() == 0
        assert not style.isForcedDecimalPoint()

    def test_localize_DE_fixedDecimal(self) -> None:

        pass  # LLM could not translate method body

    def test_localize_DE_fixedNegative(self) -> None:

        pass  # LLM could not translate method body

    def test_localize_DE_fixedPositive(self) -> None:

        pass  # LLM could not translate method body

    def test_localize_DE_fixedZero(self) -> None:

        base = MoneyAmountStyle.LOCALIZED_GROUPING.withZeroCharacter("_")
        style = base.localize(TEST_DE_LOCALE)
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

        pass  # LLM could not translate method body

    def test_localize_GB(self) -> None:

        pass  # LLM could not translate method body

    def test_of_Locale_DE(self) -> None:

        pass  # LLM could not translate method body

    def test_of_Locale_GB(self) -> None:

        pass  # LLM could not translate method body

    def test_print_groupBeforeDecimal(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_GROUPING.withGroupingStyle(
            GroupingStyle.BEFORE_DECIMAL_POINT
        )
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87,654,321.12345678", test.print0(MONEY))

    def test_LOCALIZED_NO_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_NO_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87654321.12345678", test.print0(MONEY))

    def test_LOCALIZED_NO_GROUPING(self) -> None:

        pass  # LLM could not translate method body

    def test_LOCALIZED_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.LOCALIZED_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87,654,321.123,456,78", test.print0(MONEY))

    def test_LOCALIZED_GROUPING(self) -> None:

        pass  # LLM could not translate method body

    def test_ASCII_DECIMAL_COMMA_NO_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_NO_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87654321,12345678", test.print0(MONEY))

    def test_ASCII_DECIMAL_COMMA_NO_GROUPING(self) -> None:

        pass  # LLM could not translate method body

    def test_ASCII_DECIMAL_COMMA_GROUP3_SPACE_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_SPACE
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87 654 321,123 456 78", test.print0(MONEY))

    def test_ASCII_DECIMAL_COMMA_GROUP3_SPACE(self) -> None:

        pass  # LLM could not translate method body

    def test_ASCII_DECIMAL_COMMA_GROUP3_DOT_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_COMMA_GROUP3_DOT
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87.654.321,123.456.78", test.print0(MONEY))

    def test_ASCII_ASCII_DECIMAL_COMMA_GROUP3_DOT(self) -> None:

        pass  # LLM could not translate method body

    def test_ASCII_DECIMAL_POINT_NO_GROUPING_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_NO_GROUPING
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87654321.12345678", test.print0(MONEY))

    def test_ASCII_DECIMAL_POINT_NO_GROUPING(self) -> None:

        pass  # LLM could not translate method body

    def test_ASCII_ASCII_DECIMAL_POINT_GROUP3_SPACE_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_SPACE
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87 654 321.123 456 78", test.print0(MONEY))

    def test_ASCII_DECIMAL_POINT_GROUP3_SPACE(self) -> None:

        pass  # LLM could not translate method body

    def test_ASCII_DECIMAL_POINT_GROUP3_COMMA_print(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        test = MoneyFormatterBuilder().appendAmount1(style).toFormatter0()
        self.assertEqual("87,654,321.123,456,78", test.print0(MONEY))

    def test_ASCII_DECIMAL_POINT_GROUP3_COMMA(self) -> None:

        pass  # LLM could not translate method body

    def afterMethod(self) -> None:

        Locale.setDefault(self.__cCachedLocale)

    def beforeMethod(self) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_GB")

    # Class Methods End
