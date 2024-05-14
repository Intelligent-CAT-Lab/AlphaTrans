# Imports Begin
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import typing

# Imports End


class TestMoneyAmountStyle:

    # Class Fields Begin
    __cCachedLocale: typing.Any = None
    __TEST_GB_LOCALE: typing.Any = None
    __TEST_DE_LOCALE: typing.Any = None
    __TEST_LV_LOCALE: typing.Any = None
    __MONEY: BigMoney = None
    # Class Fields End

    # Class Methods Begin
    def test_toString(self) -> None:
        pass

    def test_equals_notEqual_absValue(self) -> None:
        pass

    def test_equals_equal_absValue_true(self) -> None:
        pass

    def test_equals_equal_absValue_false(self) -> None:
        pass

    def test_equals_notEqual_forcedDecimalPoint(self) -> None:
        pass

    def test_equals_equal_forcedDecimalPoint_true(self) -> None:
        pass

    def test_equals_equal_forcedDecimalPoint_false(self) -> None:
        pass

    def test_equals_notEqual_groupingSize(self) -> None:
        pass

    def test_equals_equal_groupingSize(self) -> None:
        pass

    def test_equals_notEqual_groupingStyle(self) -> None:
        pass

    def test_equals_equal_groupingStyle(self) -> None:
        pass

    def test_equals_notEqual_groupingChar(self) -> None:
        pass

    def test_equals_equal_groupingChar(self) -> None:
        pass

    def test_equals_notEqual_decimalPointChar(self) -> None:
        pass

    def test_equals_equal_decimalPointChar(self) -> None:
        pass

    def test_equals_notEqual_negativeChar(self) -> None:
        pass

    def test_equals_equal_negativeChar(self) -> None:
        pass

    def test_equals_notEqual_positiveChar(self) -> None:
        pass

    def test_equals_equal_positiveChar(self) -> None:
        pass

    def test_equals_notEqual_zeroChar(self) -> None:
        pass

    def test_equals_equal_zeroChar(self) -> None:
        pass

    def test_equals_null(self) -> None:
        pass

    def test_equals_otherType(self) -> None:
        pass

    def test_equals_same(self) -> None:
        pass

    def test_withAbsValue_same(self) -> None:
        pass

    def test_withAbsValue(self) -> None:
        pass

    def test_withForcedDecimalPoint_same(self) -> None:
        pass

    def test_withForcedDecimalPoint(self) -> None:
        pass

    def test_withGroupingSize_negative(self) -> None:
        pass

    def test_withGroupingSize_sameNull(self) -> None:
        pass

    def test_withGroupingSize_same(self) -> None:
        pass

    def test_withGroupingSize(self) -> None:
        pass

    def test_withGroupingStyle_same(self) -> None:
        pass

    def test_withGroupingStyle(self) -> None:
        pass

    def test_withGroupingCharacter_sameNull(self) -> None:
        pass

    def test_withGroupingCharacter_same(self) -> None:
        pass

    def test_withGroupingCharacter(self) -> None:
        pass

    def test_withDecimalPointCharacter_sameNull(self) -> None:
        pass

    def test_withDecimalPointCharacter_same(self) -> None:
        pass

    def test_withDecimalPointCharacter(self) -> None:
        pass

    def test_withNegativeSignCharacter_sameNull(self) -> None:
        pass

    def test_withNegativeSignCharacter_same(self) -> None:
        pass

    def test_withNegativeSignCharacter(self) -> None:
        pass

    def test_withPositiveSignCharacter_sameNull(self) -> None:
        pass

    def test_withPositiveSignCharacter_same(self) -> None:
        pass

    def test_withPositiveSignCharacter(self) -> None:
        pass

    def test_withZeroCharacter_sameNull(self) -> None:
        pass

    def test_withZeroCharacter_same(self) -> None:
        pass

    def test_withZeroCharacter(self) -> None:
        pass

    def test_localize_LV(self) -> None:
        pass

    def test_localize_DE_noGrouping(self) -> None:
        pass

    def test_localize_DE_fixedZeroAndDecimal(self) -> None:
        pass

    def test_localize_DE_fixedGrouping(self) -> None:
        pass

    def test_localize_DE_fixedDecimal(self) -> None:
        pass

    def test_localize_DE_fixedNegative(self) -> None:
        pass

    def test_localize_DE_fixedPositive(self) -> None:
        pass

    def test_localize_DE_fixedZero(self) -> None:
        pass

    def test_localize_DE(self) -> None:
        pass

    def test_localize_GB(self) -> None:
        pass

    def test_of_Locale_DE(self) -> None:
        pass

    def test_of_Locale_GB(self) -> None:
        pass

    def test_print_groupBeforeDecimal(self) -> None:
        pass

    def test_LOCALIZED_NO_GROUPING_print(self) -> None:
        pass

    def test_LOCALIZED_NO_GROUPING(self) -> None:
        pass

    def test_LOCALIZED_GROUPING_print(self) -> None:
        pass

    def test_LOCALIZED_GROUPING(self) -> None:
        pass

    def test_ASCII_DECIMAL_COMMA_NO_GROUPING_print(self) -> None:
        pass

    def test_ASCII_DECIMAL_COMMA_NO_GROUPING(self) -> None:
        pass

    def test_ASCII_DECIMAL_COMMA_GROUP3_SPACE_print(self) -> None:
        pass

    def test_ASCII_DECIMAL_COMMA_GROUP3_SPACE(self) -> None:
        pass

    def test_ASCII_DECIMAL_COMMA_GROUP3_DOT_print(self) -> None:
        pass

    def test_ASCII_ASCII_DECIMAL_COMMA_GROUP3_DOT(self) -> None:
        pass

    def test_ASCII_DECIMAL_POINT_NO_GROUPING_print(self) -> None:
        pass

    def test_ASCII_DECIMAL_POINT_NO_GROUPING(self) -> None:
        pass

    def test_ASCII_ASCII_DECIMAL_POINT_GROUP3_SPACE_print(self) -> None:
        pass

    def test_ASCII_DECIMAL_POINT_GROUP3_SPACE(self) -> None:
        pass

    def test_ASCII_DECIMAL_POINT_GROUP3_COMMA_print(self) -> None:
        pass

    def test_ASCII_DECIMAL_POINT_GROUP3_COMMA(self) -> None:
        pass

    def afterMethod(self) -> None:
        pass

    def beforeMethod(self) -> None:
        pass

    # Class Methods End
