# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import typing

# Imports End


class TestMoney:

    # Class Fields Begin
    __GBP: CurrencyUnit = None
    __EUR: CurrencyUnit = None
    __USD: CurrencyUnit = None
    __JPY: CurrencyUnit = None
    __BIGDEC_2_3: decimal.Decimal = None
    __BIGDEC_2_34: decimal.Decimal = None
    __BIGDEC_2_345: decimal.Decimal = None
    __BIGDEC_M5_78: decimal.Decimal = None
    __GBP_0_00: Money = None
    __GBP_1_23: Money = None
    __GBP_2_33: Money = None
    __GBP_2_34: Money = None
    __GBP_2_35: Money = None
    __GBP_2_36: Money = None
    __GBP_5_78: Money = None
    __GBP_M1_23: Money = None
    __GBP_M5_78: Money = None
    __GBP_INT_MAX_PLUS1: Money = None
    __GBP_INT_MIN_MINUS1: Money = None
    __GBP_INT_MAX_MAJOR_PLUS1: Money = None
    __GBP_INT_MIN_MAJOR_MINUS1: Money = None
    __GBP_LONG_MAX_PLUS1: Money = None
    __GBP_LONG_MIN_MINUS1: Money = None
    __GBP_LONG_MAX_MAJOR_PLUS1: Money = None
    __GBP_LONG_MIN_MAJOR_MINUS1: Money = None
    __JPY_423: Money = None
    __USD_1_23: Money = None
    __USD_2_34: Money = None
    __USD_2_35: Money = None
    # Class Fields End

    # Class Methods Begin
    def test_toString_negative(self) -> None:
        pass

    def test_toString_positive(self) -> None:
        pass

    def test_equals_false(self) -> None:
        pass

    def test_equals_hashCode_positive(self) -> None:
        pass

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:
        pass

    def test_isLessThanOrEqual(self) -> None:
        pass

    def test_isLessThan_currenciesDiffer(self) -> None:
        pass

    def test_isLessThan(self) -> None:
        pass

    def test_isGreaterThanOrEqual_currenciesDiffer(self) -> None:
        pass

    def test_isGreaterThanOrEqual(self) -> None:
        pass

    def test_isGreaterThan_currenciesDiffer(self) -> None:
        pass

    def test_isGreaterThan(self) -> None:
        pass

    def test_isEqual_currenciesDiffer(self) -> None:
        pass

    def test_isEqual_Money(self) -> None:
        pass

    def test_isEqual(self) -> None:
        pass

    def test_compareTo_wrongType(self) -> None:
        pass

    def test_compareTo_currenciesDiffer(self) -> None:
        pass

    def test_compareTo_BigMoney(self) -> None:
        pass

    def test_compareTo_Money(self) -> None:
        pass

    def test_isSameCurrency_Money_nullMoney(self) -> None:
        pass

    def test_isSameCurrency_BigMoney_different(self) -> None:
        pass

    def test_isSameCurrency_BigMoney_same(self) -> None:
        pass

    def test_isSameCurrency_Money_different(self) -> None:
        pass

    def test_isSameCurrency_Money_same(self) -> None:
        pass

    def test_toBigMoney(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_nullCurrency(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_sameCurrency(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_negative(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        pass

    def test_convertedTo_BigDecimalRoundingMode_positive(self) -> None:
        pass

    def test_round_3(self) -> None:
        pass

    def test_round_M1up(self) -> None:
        pass

    def test_round_M1down(self) -> None:
        pass

    def test_round_0up(self) -> None:
        pass

    def test_round_0down(self) -> None:
        pass

    def test_round_1up(self) -> None:
        pass

    def test_round_1down(self) -> None:
        pass

    def test_round_2up(self) -> None:
        pass

    def test_round_2down(self) -> None:
        pass

    def test_abs_negative(self) -> None:
        pass

    def test_abs_positive(self) -> None:
        pass

    def test_negated_negative(self) -> None:
        pass

    def test_negated_positive(self) -> None:
        pass

    def test_dividedBy_long_negative(self) -> None:
        pass

    def test_dividedBy_long_positive_roundUp(self) -> None:
        pass

    def test_dividedBy_long_positive_roundDown(self) -> None:
        pass

    def test_dividedBy_long_positive(self) -> None:
        pass

    def test_dividedBy_long_one(self) -> None:
        pass

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:
        pass

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:
        pass

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:
        pass

    def test_dividedBy_doubleRoundingMode_one(self) -> None:
        pass

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:
        pass

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        pass

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:
        pass

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:
        pass

    def test_multipliedBy_long_negative(self) -> None:
        pass

    def test_multipliedBy_long_positive(self) -> None:
        pass

    def test_multipliedBy_long_one(self) -> None:
        pass

    def test_multipliedBy_doubleRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:
        pass

    def test_multipliedBy_doubleRoundingMode_positive_halfUp(self) -> None:
        pass

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:
        pass

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:
        pass

    def test_multipliedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_multipliedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_multipliedBy_BigDecimalRoundingMode_negative(self) -> None:
        pass

    def test_multipliedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        pass

    def test_multipliedBy_BigDecimalRoundingMode_positive(self) -> None:
        pass

    def test_multipliedBy_BigDecimalRoundingMode_one(self) -> None:
        pass

    def test_minusMinor_negative(self) -> None:
        pass

    def test_minusMinor_positive(self) -> None:
        pass

    def test_minusMinor_zero(self) -> None:
        pass

    def test_minusMajor_negative(self) -> None:
        pass

    def test_minusMajor_positive(self) -> None:
        pass

    def test_minusMajor_zero(self) -> None:
        pass

    def test_minus_doubleRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_minus_doubleRoundingMode_roundUnecessary(self) -> None:
        pass

    def test_minus_doubleRoundingMode_roundDown(self) -> None:
        pass

    def test_minus_doubleRoundingMode_negative(self) -> None:
        pass

    def test_minus_doubleRoundingMode_positive(self) -> None:
        pass

    def test_minus_doubleRoundingMode_zero(self) -> None:
        pass

    def test_minus_double_invalidScale(self) -> None:
        pass

    def test_minus_double_negative(self) -> None:
        pass

    def test_minus_double_positive(self) -> None:
        pass

    def test_minus_double_zero(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_roundDown(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_negative(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_positive(self) -> None:
        pass

    def test_minus_BigDecimalRoundingMode_zero(self) -> None:
        pass

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:
        pass

    def test_minus_BigDecimal_invalidScale(self) -> None:
        pass

    def test_minus_BigDecimal_negative(self) -> None:
        pass

    def test_minus_BigDecimal_positive(self) -> None:
        pass

    def test_minus_BigDecimal_zero(self) -> None:
        pass

    def test_minus_Money_nullMoney(self) -> None:
        pass

    def test_minus_Money_currencyMismatch(self) -> None:
        pass

    def test_minus_Money_negative(self) -> None:
        pass

    def test_minus_Money_positive(self) -> None:
        pass

    def test_minus_Money_zero(self) -> None:
        pass

    def test_minus_Iterable_nullIterable(self) -> None:
        pass

    def test_minus_Iterable_nullEntry(self) -> None:
        pass

    def test_minus_Iterable_currencyMismatch(self) -> None:
        pass

    def test_minus_Iterable_zero(self) -> None:
        pass

    def test_minus_Iterable(self) -> None:
        pass

    def test_plusMinor_negative(self) -> None:
        pass

    def test_plusMinor_positive(self) -> None:
        pass

    def test_plusMinor_zero(self) -> None:
        pass

    def test_plusMajor_negative(self) -> None:
        pass

    def test_plusMajor_positive(self) -> None:
        pass

    def test_plusMajor_zero(self) -> None:
        pass

    def test_plus_doubleRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_plus_doubleRoundingMode_roundUnecessary(self) -> None:
        pass

    def test_plus_doubleRoundingMode_roundDown(self) -> None:
        pass

    def test_plus_doubleRoundingMode_negative(self) -> None:
        pass

    def test_plus_doubleRoundingMode_positive(self) -> None:
        pass

    def test_plus_doubleRoundingMode_zero(self) -> None:
        pass

    def test_plus_double_invalidScale(self) -> None:
        pass

    def test_plus_double_negative(self) -> None:
        pass

    def test_plus_double_positive(self) -> None:
        pass

    def test_plus_double_zero(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_roundDown(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_negative(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_positive(self) -> None:
        pass

    def test_plus_BigDecimalRoundingMode_zero(self) -> None:
        pass

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:
        pass

    def test_plus_BigDecimal_invalidScale(self) -> None:
        pass

    def test_plus_BigDecimal_negative(self) -> None:
        pass

    def test_plus_BigDecimal_positive(self) -> None:
        pass

    def test_plus_BigDecimal_zero(self) -> None:
        pass

    def test_plus_Money_nullMoney(self) -> None:
        pass

    def test_plus_Money_currencyMismatch(self) -> None:
        pass

    def test_plus_Money_negative(self) -> None:
        pass

    def test_plus_Money_positive(self) -> None:
        pass

    def test_plus_Money_zero(self) -> None:
        pass

    def test_plus_Iterable_nullIterable(self) -> None:
        pass

    def test_plus_Iterable_nullEntry(self) -> None:
        pass

    def test_plus_Iterable_currencyMismatch(self) -> None:
        pass

    def test_plus_Iterable_zero(self) -> None:
        pass

    def test_plus_Iterable(self) -> None:
        pass

    def test_withAmount_doubleRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_withAmount_doubleRoundingMode_roundUnecessary(self) -> None:
        pass

    def test_withAmount_doubleRoundingMode_roundDown(self) -> None:
        pass

    def test_withAmount_doubleRoundingMode_same(self) -> None:
        pass

    def test_withAmount_doubleRoundingMode(self) -> None:
        pass

    def test_withAmount_double_invalidScale(self) -> None:
        pass

    def test_withAmount_double_same(self) -> None:
        pass

    def test_withAmount_double(self) -> None:
        pass

    def test_withAmount_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_withAmount_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_withAmount_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        pass

    def test_withAmount_BigDecimalRoundingMode_roundDown(self) -> None:
        pass

    def test_withAmount_BigDecimalRoundingMode_same(self) -> None:
        pass

    def test_withAmount_BigDecimalRoundingMode(self) -> None:
        pass

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:
        pass

    def test_withAmount_BigDecimal_invalidScale(self) -> None:
        pass

    def test_withAmount_BigDecimal_same(self) -> None:
        pass

    def test_withAmount_BigDecimal(self) -> None:
        pass

    def test_isNegativeOrZero(self) -> None:
        pass

    def test_isNegative(self) -> None:
        pass

    def test_isPositiveOrZero(self) -> None:
        pass

    def test_isPositive(self) -> None:
        pass

    def test_isZero(self) -> None:
        pass

    def test_getMinorPart_negative(self) -> None:
        pass

    def test_getMinorPart_positive(self) -> None:
        pass

    def test_getAmountMinorInt_tooBigNegative(self) -> None:
        pass

    def test_getAmountMinorInt_tooBigPositive(self) -> None:
        pass

    def test_getAmountMinorInt_negative(self) -> None:
        pass

    def test_getAmountMinorInt_positive(self) -> None:
        pass

    def test_getAmountMinorLong_tooBigNegative(self) -> None:
        pass

    def test_getAmountMinorLong_tooBigPositive(self) -> None:
        pass

    def test_getAmountMinorLong_negative(self) -> None:
        pass

    def test_getAmountMinorLong_positive(self) -> None:
        pass

    def test_getAmountMinor_negative(self) -> None:
        pass

    def test_getAmountMinor_positive(self) -> None:
        pass

    def test_getAmountMajorInt_tooBigNegative(self) -> None:
        pass

    def test_getAmountMajorInt_tooBigPositive(self) -> None:
        pass

    def test_getAmountMajorInt_negative(self) -> None:
        pass

    def test_getAmountMajorInt_positive(self) -> None:
        pass

    def test_getAmountMajorLong_tooBigNegative(self) -> None:
        pass

    def test_getAmountMajorLong_tooBigPositive(self) -> None:
        pass

    def test_getAmountMajorLong_negative(self) -> None:
        pass

    def test_getAmountMajorLong_positive(self) -> None:
        pass

    def test_getAmountMajor_negative(self) -> None:
        pass

    def test_getAmountMajor_positive(self) -> None:
        pass

    def test_getAmount_negative(self) -> None:
        pass

    def test_getAmount_positive(self) -> None:
        pass

    def test_getScale_JPY(self) -> None:
        pass

    def test_getScale_GBP(self) -> None:
        pass

    def test_withCurrencyUnit_CurrencyRoundingMode_nullCurrency(self) -> None:
        pass

    def test_withCurrencyUnit_CurrencyRoundingMode_UNECESSARY(self) -> None:
        pass

    def test_withCurrencyUnit_CurrencyRoundingMode_same(self) -> None:
        pass

    def test_withCurrencyUnit_CurrencyRoundingMode_UP(self) -> None:
        pass

    def test_withCurrencyUnit_CurrencyRoundingMode_DOWN(self) -> None:
        pass

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:
        pass

    def test_withCurrencyUnit_Currency_scaleProblem(self) -> None:
        pass

    def test_withCurrencyUnit_Currency_same(self) -> None:
        pass

    def test_withCurrencyUnit_Currency(self) -> None:
        pass

    def test_getCurrencyUnit_EUR(self) -> None:
        pass

    def test_getCurrencyUnit_GBP(self) -> None:
        pass

    def test_constructor_scale(self) -> None:
        pass

    def test_constructor_null1(self) -> None:
        pass

    def test_factory_parse_String_nullString(self) -> None:
        pass

    def test_factory_parse_String_badCurrency(self) -> None:
        pass

    def test_factory_parse_String_tooShort(self) -> None:
        pass

    def test_factory_parse(self, str: str, currency: CurrencyUnit, amount: int) -> None:
        pass

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:
        pass

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:
        pass

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:
        pass

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(
        self,
    ) -> None:
        pass

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:
        pass

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:
        pass

    def test_factory_total_CurrencyUnitIterable(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_3(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:
        pass

    def test_factory_total_CurrencyUnitArray_1(self) -> None:
        pass

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:
        pass

    def test_factory_total_Iterable_nullNotFirst(self) -> None:
        pass

    def test_factory_total_Iterable_nullFirst(self) -> None:
        pass

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:
        pass

    def test_factory_total_Iterable_empty(self) -> None:
        pass

    def test_factory_total_Iterable(self) -> None:
        pass

    def test_factory_total_array_nullNotFirst(self) -> None:
        pass

    def test_factory_total_varargs_nullNotFirst(self) -> None:
        pass

    def test_factory_total_array_nullFirst(self) -> None:
        pass

    def test_factory_total_varargs_nullFirst(self) -> None:
        pass

    def test_factory_total_array_currenciesDiffer(self) -> None:
        pass

    def test_factory_total_varargs_currenciesDiffer(self) -> None:
        pass

    def test_factory_total_array_empty(self) -> None:
        pass

    def test_factory_total_varargs_empty(self) -> None:
        pass

    def test_factory_total_array_3(self) -> None:
        pass

    def test_factory_total_varargs_3(self) -> None:
        pass

    def test_factory_total_array_1(self) -> None:
        pass

    def test_factory_total_varargs_1(self) -> None:
        pass

    def test_factory_from_BigMoneyProvider_RoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_factory_from_BigMoneyProvider_RoundingMode_nullBigMoneyProvider(
        self,
    ) -> None:
        pass

    def test_factory_from_BigMoneyProvider_RoundingMode(self) -> None:
        pass

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        pass

    def test_factory_from_BigMoneyProvider_invalidCurrencyScale(self) -> None:
        pass

    def test_factory_from_BigMoneyProvider_fixScale(self) -> None:
        pass

    def test_factory_from_BigMoneyProvider(self) -> None:
        pass

    def test_factory_zero_Currency_nullCurrency(self) -> None:
        pass

    def test_factory_zero_Currency(self) -> None:
        pass

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:
        pass

    def test_factory_ofMinor_Currency_long(self) -> None:
        pass

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:
        pass

    def test_factory_ofMajor_Currency_long(self) -> None:
        pass

    def test_factory_of_Currency_double_RoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_factory_of_Currency_double_RoundingMode_nullCurrency(self) -> None:
        pass

    def test_factory_of_Currency_double_RoundingMode_UNNECESSARY(self) -> None:
        pass

    def test_factory_of_Currency_double_JPY_RoundingMode_UP(self) -> None:
        pass

    def test_factory_of_Currency_double_JPY_RoundingMode_DOWN(self) -> None:
        pass

    def test_factory_of_Currency_double_GBP_RoundingMode_DOWN(self) -> None:
        pass

    def test_factory_of_Currency_double_nullCurrency(self) -> None:
        pass

    def test_factory_of_Currency_double_invalidScaleJPY(self) -> None:
        pass

    def test_factory_of_Currency_double_invalidScaleGBP(self) -> None:
        pass

    def test_factory_of_Currency_double_big(self) -> None:
        pass

    def test_factory_of_Currency_double_medium(self) -> None:
        pass

    def test_factory_of_Currency_double_trailingZero2(self) -> None:
        pass

    def test_factory_of_Currency_double_trailingZero1(self) -> None:
        pass

    def test_factory_of_Currency_double_correctScale(self) -> None:
        pass

    def test_factory_of_Currency_double(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullRoundingMode(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullBigDecimal(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullCurrency(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_RoundingMode_UNNECESSARY(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_JPY_RoundingMode_UP(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_JPY_RoundingMode_DOWN(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_GBP_RoundingMode_DOWN(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_invalidScaleJPY(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_invalidScaleGBP(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal_correctScale(self) -> None:
        pass

    def test_factory_of_Currency_BigDecimal(self) -> None:
        pass

    # Class Methods End
