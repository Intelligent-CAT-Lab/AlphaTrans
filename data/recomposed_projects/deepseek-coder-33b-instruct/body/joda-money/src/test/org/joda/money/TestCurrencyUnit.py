from __future__ import annotations
import locale
import re
import random
import mock
from abc import ABC
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.IllegalCurrencyException import *


class TestCurrencyUnit(unittest.TestCase):

    __JDK_GBP: CurrencyUnit = CurrencyUnit.of("GBP")

    def test_toString(self) -> None:
        test = CurrencyUnit.of1("GBP")
        self.assertEqual("GBP", test.toString())

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
        self.assertTrue(a.equals(a))
        self.assertTrue(b.equals(b))
        self.assertTrue(c.equals(c))

        self.assertTrue(a.equals(b))
        self.assertTrue(b.equals(a))
        self.assertEqual(a.hashCode(), b.hashCode())

        self.assertFalse(a.equals(c))
        self.assertFalse(b.equals(c))

    def test_compareTo_null(self) -> None:
        with pytest.raises(RuntimeError):
            CurrencyUnit.of1("EUR").compareTo(None)

    def test_compareTo(self) -> None:

        a = CurrencyUnit.of1("EUR")
        b = CurrencyUnit.of1("GBP")
        c = CurrencyUnit.of1("JPY")

        self.assertEqual(a.compareTo(a), 0)
        self.assertEqual(b.compareTo(b), 0)
        self.assertEqual(c.compareTo(c), 0)

        self.assertTrue(a.compareTo(b) < 0)
        self.assertTrue(b.compareTo(a) > 0)

        self.assertTrue(a.compareTo(c) < 0)
        self.assertTrue(c.compareTo(a) > 0)

        self.assertTrue(b.compareTo(c) < 0)
        self.assertTrue(c.compareTo(b) > 0)

    def test_toCurrency(self) -> None:

        test = CurrencyUnit.of1("GBP")
        self.assertEqual(self.__JDK_GBP, test.toCurrency())

    def test_getSymbol_TMT_UK(self) -> None:

        loc = locale.getlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("TMT")
            self.assertEqual("TMT", test.getSymbol1(locale.UK))
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_JPY_Japan(self) -> None:

        # Save the current default locale
        loc = locale.getdefaultlocale()

        try:
            # Set the default locale to UK
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")

            # Get the currency unit for JPY
            test = CurrencyUnit.of1("JPY")

            # Assert that the symbol for JPY in Japan is '¥'
            self.assertEqual("\u00A5", test.getSymbol1(locale.getlocale()))
        finally:
            # Reset the default locale
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_USD_France(self) -> None:

        loc = locale.getlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
            test = CurrencyUnit.of1("USD")
            self.assertTrue("US" in test.getSymbol1(locale.FRANCE))
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_USD_UK(self) -> None:

        # Save the current default locale
        loc = locale.getlocale()

        try:
            # Set the default locale to UK
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")

            # Get the CurrencyUnit for USD
            test = CurrencyUnit.of1("USD")

            # Assert that the symbol for USD in the US locale is '$'
            self.assertEqual("$", test.getSymbol1(locale.LC_US))
        finally:
            # Reset the default locale
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_GBP_France(self) -> None:

        loc = locale.getlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
            test = CurrencyUnit.of1("GBP")
            self.assertTrue("GB" in test.getSymbol1(locale.FRANCE))
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_Locale_GBP_UK(self) -> None:

        # Save the current locale
        loc = locale.getlocale()

        try:
            # Set the locale to UK
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")

            # Get the currency unit for GBP
            test = CurrencyUnit.of1("GBP")

            # Assert that the symbol for GBP in UK locale is '£'
            self.assertEqual("\u00A3", test.getSymbol1(locale.getlocale()))
        finally:
            # Reset the locale to the original value
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_TMT(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("TMT")
            self.assertEqual("TMT", test.getSymbol0())
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_JPY(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
            test = CurrencyUnit.of1("JPY")
            self.assertTrue("JP" in test.getSymbol0())
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_getSymbol_GBP(self) -> None:

        loc = locale.getdefaultlocale()
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.utf8")
            test = CurrencyUnit.of1("GBP")
            self.assertEqual("\u00A3", test.getSymbol0())
        finally:
            locale.setlocale(locale.LC_ALL, loc)

    def test_isPseudoCurrency_XXX(self) -> None:
        test = CurrencyUnit.of1("XXX")
        self.assertTrue(test.isPseudoCurrency())

    def test_isPseudoCurrency_JPY(self) -> None:
        test = CurrencyUnit.of1("JPY")
        self.assertFalse(test.isPseudoCurrency())

    def test_isPseudoCurrency_GBP(self) -> None:
        test = CurrencyUnit.of1("GBP")
        self.assertFalse(test.isPseudoCurrency())

    def test_getDecimalPlaces_XXX(self) -> None:
        test = CurrencyUnit.of1("XXX")
        self.assertEqual(0, test.getDecimalPlaces())

    def test_getDecimalPlaces_JPY(self) -> None:
        test = CurrencyUnit.of1("JPY")
        self.assertEqual(0, test.getDecimalPlaces())

    def test_getDecimalPlaces_GBP(self) -> None:
        test = CurrencyUnit.of1("GBP")
        self.assertEqual(2, test.getDecimalPlaces())

    def test_getCurrencyCodes_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP").getCountryCodes()
        self.assertTrue("GB" in test)
        self.assertTrue("IM" in test)
        self.assertTrue("JE" in test)
        self.assertTrue("GG" in test)

    def test_getNumericCode_GBP(self) -> None:
        test = CurrencyUnit.of1("GBP")
        self.assertEqual(826, test.getNumericCode())

    def test_getNumeric3Code_XFU(self) -> None:

        test = CurrencyUnit.of1("XFU")
        self.assertEqual("", test.getNumeric3Code())

    def test_getNumeric3Code_AMD(self) -> None:

        test = CurrencyUnit.of1("AMD")
        self.assertEqual("051", test.getNumeric3Code())

    def test_getNumeric3Code_ALL(self) -> None:

        test = CurrencyUnit.of1("ALL")
        self.assertEqual("008", test.getNumeric3Code())

    def test_getNumeric3Code_GBP(self) -> None:

        test = CurrencyUnit.of1("GBP")
        self.assertEqual("826", test.getNumeric3Code())

    def test_factory_ofCountry_String_unknownCurrency(self) -> None:
        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofCountry("gb")
        assert str(ex.value) == "No currency found for country 'gb'"

    def test_factory_ofCountry_String_nullString(self) -> None:
        with pytest.raises(RuntimeError):
            CurrencyUnit.ofCountry(None)

    def test_factory_ofCountry_String(self) -> None:
        test = CurrencyUnit.ofCountry("GB")
        self.assertEqual("GBP", test.getCode())

    def test_factory_of_Locale_unknownCurrency(self) -> None:
        try:
            CurrencyUnit.of2(Locale("en", "XY"))
        except IllegalCurrencyException as ex:
            self.assertEqual("No currency found for locale 'en_XY'", str(ex))
            raise ex

    def test_factory_of_Locale_nullLocale(self) -> None:
        with pytest.raises(RuntimeError):
            CurrencyUnit.of2(None)

    def test_factory_of_LocaleUS(self) -> None:

        # Create a mock Locale object
        class MockLocale:
            def getCountry(self):
                return "US"

        test = CurrencyUnit.of2(MockLocale())
        self.assertEqual("USD", test.getCode())

    def test_factory_of_LocaleUK(self) -> None:

        # Create a mock Locale object
        class MockLocale:
            def getCountry(self):
                return "UK"

        test = CurrencyUnit.of2(MockLocale())
        self.assertEqual("GBP", test.getCode())

    def test_factory_ofNumericCode_int_tooLong(self) -> None:

        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofNumericCode1(1234)
        assert str(ex.value) == "Unknown currency '1234'"

    def test_factory_ofNumericCode_int_negative(self) -> None:

        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofNumericCode1(-1)
        assert str(ex.value) == "Unknown currency '-1'"

    def test_factory_ofNumericCode_int_unknownCurrency(self) -> None:

        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofNumericCode1(111)
        assert str(ex.value) == "Unknown currency '111'"

    def test_factory_ofNumericCode_int_1char(self) -> None:

        test = CurrencyUnit.ofNumericCode1(8)
        self.assertEqual("ALL", test.getCode())

    def test_factory_ofNumericCode_int_2char(self) -> None:

        test = CurrencyUnit.ofNumericCode1(51)
        self.assertEqual("AMD", test.getCode())

    def test_factory_ofNumericCode_int(self) -> None:

        test = CurrencyUnit.ofNumericCode1(826)
        self.assertEqual("GBP", test.getCode())

    def test_factory_ofNumericCode_String_tooLong(self) -> None:

        numericCurrencyCode = "1234"

        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofNumericCode0(numericCurrencyCode)

        assert str(ex.value) == "Unknown currency '1234'"

    def test_factory_ofNumericCode_String_empty(self) -> None:

        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofNumericCode0("")

        assert str(ex.value) == "Unknown currency ''"

    def test_factory_ofNumericCode_String_negative(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.ofNumericCode0("-1")

    def test_factory_ofNumericCode_String_unknownCurrency(self) -> None:

        numericCurrencyCode = "111"

        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.ofNumericCode0(numericCurrencyCode)

        assert str(ex.value) == "Unknown currency '111'"

    def test_factory_ofNumericCode_String_nullString(self) -> None:

        with pytest.raises(RuntimeError):
            CurrencyUnit.ofNumericCode0(None)

    def test_factory_ofNumericCode_String_1charNoPad(self) -> None:

        test = CurrencyUnit.ofNumericCode0("8")
        self.assertEqual("ALL", test.getCode())

    def test_factory_ofNumericCode_String_1char(self) -> None:

        test = CurrencyUnit.ofNumericCode0("008")
        self.assertEqual("ALL", test.getCode())

    def test_factory_ofNumericCode_String_2charNoPad(self) -> None:

        test = CurrencyUnit.ofNumericCode0("51")
        self.assertEqual("AMD", test.getCode())

    def test_factory_ofNumericCode_String_2char(self) -> None:

        test = CurrencyUnit.ofNumericCode0("051")
        self.assertEqual("AMD", test.getCode())

    def test_factory_ofNumericCode_String(self) -> None:

        test = CurrencyUnit.ofNumericCode0("826")
        self.assertEqual("GBP", test.getCode())

    def test_factory_of_String_tooLong_unknown(self) -> None:
        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.of1("ABCD")

    def test_factory_of_String_tooShort_unknown(self) -> None:
        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.of1("AB")

    def test_factory_of_String_empty(self) -> None:
        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.of1("")

    def test_factory_of_String_unknownCurrency(self) -> None:
        with pytest.raises(IllegalCurrencyException) as ex:
            CurrencyUnit.of1("ABC")
        assert str(ex.value) == "Unknown currency 'ABC'"

    def test_factory_of_String_nullString(self) -> None:
        with pytest.raises(RuntimeError):
            CurrencyUnit.of1(None)

    def test_factory_of_String(self) -> None:
        test = CurrencyUnit.of1("GBP")
        self.assertEqual("GBP", test.getCode())

    def test_factory_of_Currency_nullCurrency(self) -> None:
        with pytest.raises(RuntimeError):
            CurrencyUnit.of0(None)

    def test_factory_of_Currency(self) -> None:
        test = CurrencyUnit.of0(TestCurrencyUnit.__JDK_GBP)
        self.assertEqual("GBP", test.getCode())

    def test_constructor_nullCode(self) -> None:

        with pytest.raises(AssertionError):
            CurrencyUnit(None, 1, 2)

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
        self.assertEqual(curList2, curList1)
        random.shuffle(curList2)
        curList2.sort()
        self.assertEqual(curList2, curList1)

    def test_registeredCountries(self) -> None:

        countryList = CurrencyUnit.registeredCountries()
        self.assertTrue("GB" in countryList)
        self.assertTrue("EU" in countryList)
        self.assertTrue("US" in countryList)

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
                self.assertEqual(
                    curr.getCurrencyCode(), dp, currencyUnit.getDecimalPlaces()
                )
            except ValueError:
                pass

    def test_registeredCurrency_alreadyRegisteredCountry(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("GBX", 991, 2, ["GB"])

    def test_registeredCurrency_alreadyRegisteredNumericCode(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("TST", 826, 2, ["TS"])

    def test_registeredCurrency_alreadyRegisteredCode(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("GBP", 991, 2, ["GB"])

    def test_registeredCurrency_nullCountry(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("TST", 991, 2, [None])

    def test_registeredCurrency_validDP_big(self) -> None:

        CurrencyUnit.registerCurrency0("XLG", -1, 30, [])

        currency = CurrencyUnit.of1("XLG")
        self.assertEqual(30, currency.getDecimalPlaces())

    def test_registeredCurrency_invalidDP_big(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("TST", 991, 31, ["TS"])

    def test_registeredCurrency_invalidDP_small(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("TST", 991, -2, ["TS"])

    def test_registeredCurrency_invalidNumericCode_big(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("TST", 1000, 2, ["TS"])

    def test_registeredCurrency_invalidNumericCode_small(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("TST", -2, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_dash(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("A-", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_number(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("123", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_lowerCase(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("xxa", 991, 2, ["xx"])

    def test_registeredCurrency_invalidStringCode_4letters(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("ABCD", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_2letters(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("AB", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_1letter(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("A", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_empty(self) -> None:

        with pytest.raises(IllegalCurrencyException):
            CurrencyUnit.registerCurrency0("", 991, 2, ["TS"])

    def test_registeredCurrency_nullCode(self) -> None:

        with pytest.raises(RuntimeError):
            CurrencyUnit.registerCurrency0(None, 991, 2, ["TS"])

    def test_registeredCurrencies_sorted(self) -> None:

        curList1 = CurrencyUnit.registeredCurrencies()
        curList2 = CurrencyUnit.registeredCurrencies()
        curList2.sort()
        self.assertEqual(curList2, curList1)
        random.shuffle(curList2)
        curList2.sort()
        self.assertEqual(curList2, curList1)

    def test_registeredCurrencies(self) -> None:
        curList = CurrencyUnit.registeredCurrencies()
        found = any(currencyUnit.getCode() == "GBP" for currencyUnit in curList)
        self.assertTrue(found)
