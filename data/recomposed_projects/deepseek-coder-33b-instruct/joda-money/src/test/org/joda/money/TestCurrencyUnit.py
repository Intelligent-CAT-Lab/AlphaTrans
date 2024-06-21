from __future__ import annotations
import io
import typing
from typing import *
import os
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.IllegalCurrencyException import *


class TestCurrencyUnit:

    __JDK_GBP: CurrencyUnit = CurrencyUnit.of("GBP")

    def test_toString(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert "GBP" == test.toString()

    def test_equals_false(self) -> None:

        a = CurrencyUnit.of1("GBP")
        assert not a.equals(None)
        obj = "String"  # avoid warning in Eclipse
        assert not a.equals(obj)
        assert not a.equals(object())

    def test_equals_hashCode(self) -> None:

        a = CurrencyUnit.of1("GBP")
        b = CurrencyUnit.of1("GBP")
        c = CurrencyUnit.of1("EUR")

        assert a.equals(a)
        assert b.equals(b)
        assert c.equals(c)

        assert a.equals(b)
        assert b.equals(a)
        assert a.hashCode() == b.hashCode()

        assert not a.equals(c)
        assert not b.equals(c)

    def test_compareTo_null(self) -> None:

        try:
            CurrencyUnit.of1("EUR").compareTo(None)
        except IllegalCurrencyException as e:
            print(e)

    def test_compareTo(self) -> None:

        a = CurrencyUnit.of1("EUR")
        b = CurrencyUnit.of1("GBP")
        c = CurrencyUnit.of1("JPY")

        assert a.compareTo(a) == 0
        assert b.compareTo(b) == 0
        assert c.compareTo(c) == 0

        assert a.compareTo(b) < 0
        assert b.compareTo(a) > 0

        assert a.compareTo(c) < 0
        assert c.compareTo(a) > 0

        assert b.compareTo(c) < 0
        assert c.compareTo(b) > 0

    def test_toCurrency(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert TestCurrencyUnit.__JDK_GBP == test.toCurrency()

    def test_getSymbol_TMT_UK(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("TMT")
            assert "TMT" == test.getSymbol1(locale.getlocale())
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_JPY_Japan(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_US.utf8")
            test = CurrencyUnit.of1("JPY")
            assert test.getSymbol1(locale.normalize("ja_JP.utf8")) == "\uFFE5"
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_USD_France(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
            test = CurrencyUnit.of1("USD")
            assert "US" in test.getSymbol1(locale.FRANCE)
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_USD_UK(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("USD")
            assert test.getSymbol1(locale.currency(grouping=True)) == "$"
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_GBP_France(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
            test = CurrencyUnit.of1("GBP")
            assert "GB" in test.getSymbol1(locale.FRANCE)
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_GBP_UK(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("GBP")
            assert test.getSymbol1(locale.getlocale()) == "\u00A3"
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_TMT(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("TMT")
            assert "TMT" == test.getSymbol0()
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_JPY(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("JPY")
            assert "JP" in test.getSymbol0()
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_GBP(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("GBP")
            assert test.getSymbol0() == "\u00A3"
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_isPseudoCurrency_XXX(self) -> None:

        test = CurrencyUnit.of1("XXX")
        assert test.isPseudoCurrency()

    def test_isPseudoCurrency_JPY(self) -> None:

        test = CurrencyUnit.of1("JPY")
        assert not test.isPseudoCurrency()

    def test_isPseudoCurrency_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert not test.isPseudoCurrency()

    def test_getDecimalPlaces_XXX(self) -> None:

        test = CurrencyUnit.of1("XXX")
        assert test.getDecimalPlaces() == 0

    def test_getDecimalPlaces_JPY(self) -> None:

        test = CurrencyUnit.of1("JPY")
        assert test.getDecimalPlaces() == 0

    def test_getDecimalPlaces_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert test.getDecimalPlaces() == 2

    def test_getCurrencyCodes_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP").getCountryCodes()
        assert "GB" in test
        assert "IM" in test
        assert "JE" in test
        assert "GG" in test

    def test_getNumericCode_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert test.getNumericCode() == 826

    def test_getNumeric3Code_XFU(self) -> None:

        test = CurrencyUnit.of1("XFU")
        assert test.getNumeric3Code() == ""

    def test_getNumeric3Code_AMD(self) -> None:

        test = CurrencyUnit.of1("AMD")
        assert "051" == test.getNumeric3Code()

    def test_getNumeric3Code_ALL(self) -> None:

        test = CurrencyUnit.of1("ALL")
        assert test.getNumeric3Code() == "008"

    def test_getNumeric3Code_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert test.getNumeric3Code() == "826"

    def test_factory_ofCountry_String_unknownCurrency(self) -> None:

        try:
            CurrencyUnit.ofCountry("gb")
        except IllegalCurrencyException as ex:
            assert ex.getMessage() == "No currency found for country 'gb'"
            raise ex

    def test_factory_ofCountry_String_nullString(self) -> None:

        try:
            CurrencyUnit.ofCountry(None)
        except IllegalCurrencyException as e:
            print(f"Caught IllegalCurrencyException: {e}")

    def test_factory_ofCountry_String(self) -> None:

        # Call the static method ofCountry from the CurrencyUnit class
        test = CurrencyUnit.ofCountry("GB")

        # Call the getCode method from the CurrencyUnit class
        code = test.getCode()

        # Assert that the code is equal to "GBP"
        assert code == "GBP"

    def test_factory_of_Locale_unknownCurrency(self) -> None:

        try:
            CurrencyUnit.of2(Locale("en", "XY"))
        except IllegalCurrencyException as ex:
            self.assertEqual("No currency found for locale 'en_XY'", ex.getMessage())
            raise ex

    def test_factory_of_Locale_nullLocale(self) -> None:

        # Calling the method of2 from CurrencyUnit class
        CurrencyUnit.of2(None)

    def test_factory_of_LocaleUS(self) -> None:

        test = CurrencyUnit.of2(Locale.US)
        assert test.getCode() == "USD"

    def test_factory_of_LocaleUK(self) -> None:

        test = CurrencyUnit.of2(Locale.UK)
        assert test.getCode() == "GBP"

    def test_factory_ofNumericCode_int_tooLong(self) -> None:

        try:
            CurrencyUnit.ofNumericCode1(1234)
        except IllegalCurrencyException as ex:
            assert (
                ex.getMessage() == "Unknown currency '1234'"
            ), "Error message does not match"
            raise ex

    def test_factory_ofNumericCode_int_negative(self) -> None:

        try:
            CurrencyUnit.ofNumericCode1(-1)
        except IllegalCurrencyException as ex:
            assert (
                ex.getMessage() == "Unknown currency '-1'"
            ), "Error message does not match"
            raise ex

    def test_factory_ofNumericCode_int_unknownCurrency(self) -> None:

        try:
            CurrencyUnit.ofNumericCode1(111)
        except IllegalCurrencyException as ex:
            assert (
                ex.getMessage() == "Unknown currency '111'"
            ), "Error message does not match"
            raise ex

    def test_factory_ofNumericCode_int_1char(self) -> None:

        test = CurrencyUnit.ofNumericCode1(8)
        assert test.getCode() == "ALL"

    def test_factory_ofNumericCode_int_2char(self) -> None:

        # Calling the static method ofNumericCode1 of CurrencyUnit class
        test = CurrencyUnit.ofNumericCode1(51)

        # Calling the instance method getCode of CurrencyUnit class
        result = test.getCode()

        # Asserting the result
        assert result == "AMD"

    def test_factory_ofNumericCode_int(self) -> None:

        test = CurrencyUnit.ofNumericCode1(826)
        assert test.getCode() == "GBP"

    def test_factory_ofNumericCode_String_tooLong(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("1234")
        except IllegalCurrencyException as ex:
            assert (
                ex.getMessage() == "Unknown currency '1234'"
            ), "Error message does not match"
            raise ex

    def test_factory_ofNumericCode_String_empty(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("")
        except IllegalCurrencyException as ex:
            assert ex.getMessage() == "Unknown currency ''"
            raise ex

    def test_factory_ofNumericCode_String_negative(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("-1")
        except IllegalCurrencyException as e:
            print(f"Caught expected exception: {e}")
        else:
            raise AssertionError("Expected IllegalCurrencyException was not raised")

    def test_factory_ofNumericCode_String_unknownCurrency(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("111")
        except IllegalCurrencyException as ex:
            assert ex.getMessage() == "Unknown currency '111'"
            raise ex

    def test_factory_ofNumericCode_String_nullString(self) -> None:

        # Call the method ofNumericCode0 from CurrencyUnit class
        CurrencyUnit.ofNumericCode0(None)

    def test_factory_ofNumericCode_String_1charNoPad(self) -> None:

        # Call the static method ofNumericCode0 of the CurrencyUnit class
        test = CurrencyUnit.ofNumericCode0("8")

        # Call the instance method getCode of the CurrencyUnit class
        result = test.getCode()

        # Assert that the result is equal to "ALL"
        assert result == "ALL"

    def test_factory_ofNumericCode_String_1char(self) -> None:

        # Call the static method ofNumericCode0 of the CurrencyUnit class
        test = CurrencyUnit.ofNumericCode0("008")

        # Call the instance method getCode of the CurrencyUnit class
        code = test.getCode()

        # Assert that the code is equal to "ALL"
        assert code == "ALL"

    def test_factory_ofNumericCode_String_2charNoPad(self) -> None:

        test = CurrencyUnit.ofNumericCode0("51")
        assert test.getCode() == "AMD"

    def test_factory_ofNumericCode_String_2char(self) -> None:

        # Calling the static method ofNumericCode0 of class CurrencyUnit
        test = CurrencyUnit.ofNumericCode0("051")

        # Calling the method getCode of class CurrencyUnit
        result = test.getCode()

        # Asserting the result
        assert result == "AMD"

    def test_factory_ofNumericCode_String(self) -> None:

        # Call the static method ofNumericCode0 of the CurrencyUnit class
        test = CurrencyUnit.ofNumericCode0("826")

        # Call the method getCode of the CurrencyUnit class
        code = test.getCode()

        # Assert that the code is equal to "GBP"
        assert code == "GBP"

    def test_factory_of_String_tooLong_unknown(self) -> None:

        try:
            CurrencyUnit.of1("ABCD")
        except IllegalCurrencyException as e:
            print(e)

    def test_factory_of_String_tooShort_unknown(self) -> None:

        try:
            CurrencyUnit.of1("AB")
        except IllegalCurrencyException as e:
            print(e)

    def test_factory_of_String_empty(self) -> None:

        try:
            CurrencyUnit.of1("")
        except IllegalCurrencyException as e:
            print(e)

    def test_factory_of_String_unknownCurrency(self) -> None:

        try:
            CurrencyUnit.of1("ABC")
        except IllegalCurrencyException as ex:
            self.assertEqual("Unknown currency 'ABC'", ex.getMessage())
            raise ex

    def test_factory_of_String_nullString(self) -> None:

        # Calling the method of1 from CurrencyUnit class
        CurrencyUnit.of1(None)

    def test_factory_of_String(self) -> None:

        test = CurrencyUnit.of1("GBP")
        assert "GBP" == test.getCode()

    def test_factory_of_Currency_nullCurrency(self) -> None:

        try:
            CurrencyUnit.of0(None)
        except IllegalCurrencyException as e:
            print(e)

    def test_factory_of_Currency(self) -> None:

        test = CurrencyUnit.of0(self.__JDK_GBP)
        assert "GBP" == test.getCode()

    def test_constructor_nullCode(self) -> None:

        try:
            CurrencyUnit(None, 1, 2)
        except IllegalCurrencyException as e:
            print(f"Caught exception: {e}")

    def test_constants(self) -> None:

        self.assertEqual(CurrencyUnit.of1("USD"), CurrencyUnit.USD)
        self.assertEqual(CurrencyUnit.of1("EUR"), CurrencyUnit.EUR)
        self.assertEqual(CurrencyUnit.of1("JPY"), CurrencyUnit.JPY)
        self.assertEqual(CurrencyUnit.of1("GBP"), CurrencyUnit.GBP)
        self.assertEqual(CurrencyUnit.of1("CHF"), CurrencyUnit.CHF)
        self.assertEqual(CurrencyUnit.of1("AUD"), CurrencyUnit.AUD)
        self.assertEqual(CurrencyUnit.of1("CAD"), CurrencyUnit.CAD)

    def test_registeredCountries_sorted(self) -> None:

        curList1 = CurrencyUnit.registeredCountries()
        curList2 = CurrencyUnit.registeredCountries()
        curList2.sort()
        assert curList2 == curList1
        random.shuffle(curList2)
        curList2.sort()
        assert curList2 == curList1

    def test_registeredCountries(self) -> None:

        countryList = CurrencyUnit.registeredCountries()
        assert "GB" in countryList
        assert "EU" in countryList
        assert "US" in countryList

    def test_registeredCurrencies_crossCheck(self) -> None:

        curList = CurrencyUnit.registeredCurrencies()
        for currencyUnit in curList:
            try:
                curr = Currency.getInstance(currencyUnit.getCode())
                dp = (
                    curr.getDefaultFractionDigits()
                    if curr.getDefaultFractionDigits() >= 0
                    else 0
                )
                assert curr.getCurrencyCode() == dp == currencyUnit.getDecimalPlaces()
            except ValueError:
                pass

    def test_registeredCurrency_alreadyRegisteredCountry(self) -> None:

        CurrencyUnit.registerCurrency0("GBX", 991, 2, ["GB"])

    def test_registeredCurrency_alreadyRegisteredNumericCode(self) -> None:

        CurrencyUnit.registerCurrency0("TST", 826, 2, ["TS"])

    def test_registeredCurrency_alreadyRegisteredCode(self) -> None:

        CurrencyUnit.registerCurrency0("GBP", 991, 2, ["GB"])

    def test_registeredCurrency_nullCountry(self) -> None:

        CurrencyUnit.registerCurrency0("TST", 991, 2, [None])

    def test_registeredCurrency_validDP_big(self) -> None:

        CurrencyUnit.registerCurrency0("XLG", -1, 30, [])

        currency = CurrencyUnit.of1("XLG")
        assert currency.getDecimalPlaces() == 30

    def test_registeredCurrency_invalidDP_big(self) -> None:

        CurrencyUnit.registerCurrency0("TST", 991, 31, ["TS"])

    def test_registeredCurrency_invalidDP_small(self) -> None:

        CurrencyUnit.registerCurrency0("TST", 991, -2, ["TS"])

    def test_registeredCurrency_invalidNumericCode_big(self) -> None:

        CurrencyUnit.registerCurrency0("TST", 1000, 2, ["TS"])

    def test_registeredCurrency_invalidNumericCode_small(self) -> None:

        CurrencyUnit.registerCurrency0("TST", -2, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_dash(self) -> None:

        CurrencyUnit.registerCurrency0("A-", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_number(self) -> None:

        CurrencyUnit.registerCurrency0("123", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_lowerCase(self) -> None:

        CurrencyUnit.registerCurrency0("xxA", 991, 2, ["xx"])

    def test_registeredCurrency_invalidStringCode_4letters(self) -> None:

        CurrencyUnit.registerCurrency0("ABCD", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_2letters(self) -> None:

        CurrencyUnit.registerCurrency0("AB", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_1letter(self) -> None:

        CurrencyUnit.registerCurrency0("A", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_empty(self) -> None:

        CurrencyUnit.registerCurrency0("", 991, 2, ["TS"])

    def test_registeredCurrency_nullCode(self) -> None:

        try:
            CurrencyUnit.registerCurrency0(None, 991, 2, ["TS"])
        except IllegalCurrencyException as e:
            print(f"Caught an exception: {e}")

    def test_registeredCurrencies_sorted(self) -> None:

        curList1 = CurrencyUnit.registeredCurrencies()
        curList2 = CurrencyUnit.registeredCurrencies()
        curList2.sort()
        assert curList2 == curList1
        random.shuffle(curList2)
        curList2.sort()
        assert curList2 == curList1

    def test_registeredCurrencies(self) -> None:

        curList = CurrencyUnit.registeredCurrencies()
        found = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "GBP":
                found = True
                break
        assert found
