# Imports Begin
from src.main.org.joda.money.IllegalCurrencyException import *
from src.main.org.joda.money.CurrencyUnit import *
import typing

# Imports End


class TestCurrencyUnit:

    # Class Fields Begin
    __JDK_GBP: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def test_toString(self) -> None:
        pass

    def test_equals_false(self) -> None:
        pass

    def test_equals_hashCode(self) -> None:
        pass

    def test_compareTo_null(self) -> None:
        pass

    def test_compareTo(self) -> None:
        pass

    def test_toCurrency(self) -> None:
        pass

    def test_getSymbol_TMT_UK(self) -> None:
        pass

    def test_getSymbol_Locale_JPY_Japan(self) -> None:
        pass

    def test_getSymbol_Locale_USD_France(self) -> None:
        pass

    def test_getSymbol_Locale_USD_UK(self) -> None:
        pass

    def test_getSymbol_Locale_GBP_France(self) -> None:
        pass

    def test_getSymbol_Locale_GBP_UK(self) -> None:
        pass

    def test_getSymbol_TMT(self) -> None:
        pass

    def test_getSymbol_JPY(self) -> None:
        pass

    def test_getSymbol_GBP(self) -> None:
        pass

    def test_isPseudoCurrency_XXX(self) -> None:
        pass

    def test_isPseudoCurrency_JPY(self) -> None:
        pass

    def test_isPseudoCurrency_GBP(self) -> None:
        pass

    def test_getDecimalPlaces_XXX(self) -> None:
        pass

    def test_getDecimalPlaces_JPY(self) -> None:
        pass

    def test_getDecimalPlaces_GBP(self) -> None:
        pass

    def test_getCurrencyCodes_GBP(self) -> None:
        pass

    def test_getNumericCode_GBP(self) -> None:
        pass

    def test_getNumeric3Code_XFU(self) -> None:
        pass

    def test_getNumeric3Code_AMD(self) -> None:
        pass

    def test_getNumeric3Code_ALL(self) -> None:
        pass

    def test_getNumeric3Code_GBP(self) -> None:
        pass

    def test_factory_ofCountry_String_unknownCurrency(self) -> None:
        pass

    def test_factory_ofCountry_String_nullString(self) -> None:
        pass

    def test_factory_ofCountry_String(self) -> None:
        pass

    def test_factory_of_Locale_unknownCurrency(self) -> None:
        pass

    def test_factory_of_Locale_nullLocale(self) -> None:
        pass

    def test_factory_of_LocaleUS(self) -> None:
        pass

    def test_factory_of_LocaleUK(self) -> None:
        pass

    def test_factory_ofNumericCode_int_tooLong(self) -> None:
        pass

    def test_factory_ofNumericCode_int_negative(self) -> None:
        pass

    def test_factory_ofNumericCode_int_unknownCurrency(self) -> None:
        pass

    def test_factory_ofNumericCode_int_1char(self) -> None:
        pass

    def test_factory_ofNumericCode_int_2char(self) -> None:
        pass

    def test_factory_ofNumericCode_int(self) -> None:
        pass

    def test_factory_ofNumericCode_String_tooLong(self) -> None:
        pass

    def test_factory_ofNumericCode_String_empty(self) -> None:
        pass

    def test_factory_ofNumericCode_String_negative(self) -> None:
        pass

    def test_factory_ofNumericCode_String_unknownCurrency(self) -> None:
        pass

    def test_factory_ofNumericCode_String_nullString(self) -> None:
        pass

    def test_factory_ofNumericCode_String_1charNoPad(self) -> None:
        pass

    def test_factory_ofNumericCode_String_1char(self) -> None:
        pass

    def test_factory_ofNumericCode_String_2charNoPad(self) -> None:
        pass

    def test_factory_ofNumericCode_String_2char(self) -> None:
        pass

    def test_factory_ofNumericCode_String(self) -> None:
        pass

    def test_factory_of_String_tooLong_unknown(self) -> None:
        pass

    def test_factory_of_String_tooShort_unknown(self) -> None:
        pass

    def test_factory_of_String_empty(self) -> None:
        pass

    def test_factory_of_String_unknownCurrency(self) -> None:
        pass

    def test_factory_of_String_nullString(self) -> None:
        pass

    def test_factory_of_String(self) -> None:
        pass

    def test_factory_of_Currency_nullCurrency(self) -> None:
        pass

    def test_factory_of_Currency(self) -> None:
        pass

    def test_constructor_nullCode(self) -> None:
        pass

    def test_constants(self) -> None:
        pass

    def test_registeredCountries_sorted(self) -> None:
        pass

    def test_registeredCountries(self) -> None:
        pass

    def test_registeredCurrencies_crossCheck(self) -> None:
        pass

    def test_registeredCurrency_alreadyRegisteredCountry(self) -> None:
        pass

    def test_registeredCurrency_alreadyRegisteredNumericCode(self) -> None:
        pass

    def test_registeredCurrency_alreadyRegisteredCode(self) -> None:
        pass

    def test_registeredCurrency_nullCountry(self) -> None:
        pass

    def test_registeredCurrency_validDP_big(self) -> None:
        pass

    def test_registeredCurrency_invalidDP_big(self) -> None:
        pass

    def test_registeredCurrency_invalidDP_small(self) -> None:
        pass

    def test_registeredCurrency_invalidNumericCode_big(self) -> None:
        pass

    def test_registeredCurrency_invalidNumericCode_small(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_dash(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_number(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_lowerCase(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_4letters(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_2letters(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_1letter(self) -> None:
        pass

    def test_registeredCurrency_invalidStringCode_empty(self) -> None:
        pass

    def test_registeredCurrency_nullCode(self) -> None:
        pass

    def test_registeredCurrencies_sorted(self) -> None:
        pass

    def test_registeredCurrencies(self) -> None:
        pass

    # Class Methods End
