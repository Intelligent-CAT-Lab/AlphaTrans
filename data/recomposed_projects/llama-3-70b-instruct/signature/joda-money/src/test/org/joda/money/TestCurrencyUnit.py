from __future__ import annotations
import re
import random
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

    __JDK_GBP: typing.Any = CurrencyUnit.of("GBP")

    def test_toString(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertEqual("GBP", test.toString())

    def test_equals_false(self) -> None:
        a: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertFalse(a.equals(None))
        obj: Object = "String"  # avoid warning in Eclipse
        self.assertFalse(a.equals(obj))
        self.assertFalse(a.equals(Object()))

    def test_equals_hashCode(self) -> None:
        a: CurrencyUnit = CurrencyUnit.of1("GBP")
        b: CurrencyUnit = CurrencyUnit.of1("GBP")
        c: CurrencyUnit = CurrencyUnit.of1("EUR")
        self.assertTrue(a.equals(a))
        self.assertTrue(b.equals(b))
        self.assertTrue(c.equals(c))

        self.assertTrue(a.equals(b))
        self.assertTrue(b.equals(a))
        self.assertTrue(a.hashCode() == b.hashCode())

        self.assertFalse(a.equals(c))
        self.assertFalse(b.equals(c))

    def test_compareTo_null(self) -> None:
        with pytest.raises(NullPointerException):
            CurrencyUnit.of1("EUR").compareTo(None)

    def test_compareTo(self) -> None:
        a: CurrencyUnit = CurrencyUnit.of1("EUR")
        b: CurrencyUnit = CurrencyUnit.of1("GBP")
        c: CurrencyUnit = CurrencyUnit.of1("JPY")
        self.assertEqual(0, a.compareTo(a))
        self.assertEqual(0, b.compareTo(b))
        self.assertEqual(0, c.compareTo(c))

        self.assertTrue(a.compareTo(b) < 0)
        self.assertTrue(b.compareTo(a) > 0)

        self.assertTrue(a.compareTo(c) < 0)
        self.assertTrue(c.compareTo(a) > 0)

        self.assertTrue(b.compareTo(c) < 0)
        self.assertTrue(c.compareTo(b) > 0)

    def test_toCurrency(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertEqual(self.__JDK_GBP, test.toCurrency())

    def test_getSymbol_TMT_UK(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("TMT")
            self.assertEqual("TMT", test.getSymbol1(Locale.UK))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_Locale_JPY_Japan(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("JPY")
            self.assertEqual("\uFFE5", test.getSymbol1(Locale.JAPAN))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_Locale_USD_France(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("USD")
            assertTrue(test.getSymbol1(Locale.FRANCE).contains("US"))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_Locale_USD_UK(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("USD")
            self.assertEqual("$", test.getSymbol1(Locale.US))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_Locale_GBP_France(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("GBP")
            assertTrue(test.getSymbol1(Locale.FRANCE).contains("GB"))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_Locale_GBP_UK(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("GBP")
            self.assertEqual("\u00A3", test.getSymbol1(Locale.UK))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_TMT(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("TMT")
            self.assertEqual("TMT", test.getSymbol0())
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_JPY(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("JPY")
            assertTrue(test.getSymbol0().contains("JP"))
        finally:
            Locale.setDefault(loc)

    def test_getSymbol_GBP(self) -> None:
        loc = Locale.getDefault()
        try:
            Locale.setDefault(Locale.UK)
            test = CurrencyUnit.of1("GBP")
            self.assertEqual("\u00A3", test.getSymbol0())
        finally:
            Locale.setDefault(loc)

    def test_isPseudoCurrency_XXX(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("XXX")
        self.assertTrue(test.isPseudoCurrency())

    def test_isPseudoCurrency_JPY(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("JPY")
        self.assertFalse(test.isPseudoCurrency())

    def test_isPseudoCurrency_GBP(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertFalse(test.isPseudoCurrency())

    def test_getDecimalPlaces_XXX(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("XXX")
        self.assertEqual(0, test.getDecimalPlaces())

    def test_getDecimalPlaces_JPY(self) -> None:
        test = CurrencyUnit.of1("JPY")
        self.assertEqual(0, test.getDecimalPlaces())

    def test_getDecimalPlaces_GBP(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertEqual(2, test.getDecimalPlaces())

    def test_getCurrencyCodes_GBP(self) -> None:
        test = CurrencyUnit.of1("GBP").getCountryCodes()
        self.assertTrue(test.contains("GB"))
        self.assertTrue(test.contains("IM"))
        self.assertTrue(test.contains("JE"))
        self.assertTrue(test.contains("GG"))

    def test_getNumericCode_GBP(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertEqual(826, test.getNumericCode())

    def test_getNumeric3Code_XFU(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("XFU")
        self.assertEqual("", test.getNumeric3Code())

    def test_getNumeric3Code_AMD(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("AMD")
        self.assertEqual("051", test.getNumeric3Code())

    def test_getNumeric3Code_ALL(self) -> None:
        test = CurrencyUnit.of1("ALL")
        self.assertEqual("008", test.getNumeric3Code())

    def test_getNumeric3Code_GBP(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of1("GBP")
        self.assertEqual("826", test.getNumeric3Code())

    def test_factory_ofCountry_String_unknownCurrency(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_ofCountry_String_nullString(self) -> None:
        with self.assertRaises(NullPointerException):
            CurrencyUnit.ofCountry(None)

    def test_factory_ofCountry_String(self) -> None:
        test = CurrencyUnit.ofCountry("GB")
        self.assertEqual("GBP", test.getCode())

    def test_factory_of_Locale_unknownCurrency(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Locale_nullLocale(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_LocaleUS(self) -> None:
        test = CurrencyUnit.of2(Locale.US)
        self.assertEqual("USD", test.getCode())

    def test_factory_of_LocaleUK(self) -> None:
        test = CurrencyUnit.of2(Locale.UK)
        self.assertEqual("GBP", test.getCode())

    def test_factory_ofNumericCode_int_tooLong(self) -> None:
        with self.assertRaises(IllegalCurrencyException) as cm:
            CurrencyUnit.ofNumericCode1(1234)
        self.assertEqual("Unknown currency '1234'", str(cm.exception))

    def test_factory_ofNumericCode_int_negative(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_ofNumericCode_int_unknownCurrency(self) -> None:
        with self.assertRaises(IllegalCurrencyException) as cm:
            CurrencyUnit.ofNumericCode1(111)
        self.assertEqual("Unknown currency '111'", str(cm.exception))

    def test_factory_ofNumericCode_int_1char(self) -> None:
        test: CurrencyUnit = CurrencyUnit.ofNumericCode1(8)
        self.assertEqual("ALL", test.getCode())

    def test_factory_ofNumericCode_int_2char(self) -> None:
        test: CurrencyUnit = CurrencyUnit.ofNumericCode1(51)
        self.assertEqual("AMD", test.getCode())

    def test_factory_ofNumericCode_int(self) -> None:
        test = CurrencyUnit.ofNumericCode1(826)
        self.assertEqual("GBP", test.getCode())

    def test_factory_ofNumericCode_String_tooLong(self) -> None:
        with self.assertRaises(IllegalCurrencyException) as cm:
            CurrencyUnit.ofNumericCode0("1234")
        self.assertEqual("Unknown currency '1234'", str(cm.exception))

    def test_factory_ofNumericCode_String_empty(self) -> None:
        with self.assertRaises(IllegalCurrencyException) as cm:
            CurrencyUnit.ofNumericCode0("")
        self.assertEqual("Unknown currency ''", str(cm.exception))

    def test_factory_ofNumericCode_String_negative(self) -> None:
        with self.assertRaises(IllegalCurrencyException):
            CurrencyUnit.ofNumericCode0("-1")

    def test_factory_ofNumericCode_String_unknownCurrency(self) -> None:
        with self.assertRaises(IllegalCurrencyException) as cm:
            CurrencyUnit.ofNumericCode0("111")
        self.assertEqual("Unknown currency '111'", str(cm.exception))

    def test_factory_ofNumericCode_String_nullString(self) -> None:
        with pytest.raises(NullPointerException):
            CurrencyUnit.ofNumericCode0(None)

    def test_factory_ofNumericCode_String_1charNoPad(self) -> None:
        test: CurrencyUnit = CurrencyUnit.ofNumericCode0("8")
        self.assertEqual("ALL", test.getCode())

    def test_factory_ofNumericCode_String_1char(self) -> None:
        test: CurrencyUnit = CurrencyUnit.ofNumericCode0("008")
        self.assertEqual("ALL", test.getCode())

    def test_factory_ofNumericCode_String_2charNoPad(self) -> None:
        test: CurrencyUnit = CurrencyUnit.ofNumericCode0("51")
        self.assertEqual("AMD", test.getCode())

    def test_factory_ofNumericCode_String_2char(self) -> None:
        test: CurrencyUnit = CurrencyUnit.ofNumericCode0("051")
        self.assertEqual("AMD", test.getCode())

    def test_factory_ofNumericCode_String(self) -> None:
        test = CurrencyUnit.ofNumericCode0("826")
        self.assertEqual("GBP", test.getCode())

    def test_factory_of_String_tooLong_unknown(self) -> None:
        with self.assertRaises(IllegalCurrencyException):
            CurrencyUnit.of1("ABCD")

    def test_factory_of_String_tooShort_unknown(self) -> None:
        with self.assertRaises(IllegalCurrencyException):
            CurrencyUnit.of1("AB")

    def test_factory_of_String_empty(self) -> None:
        with self.assertRaises(IllegalCurrencyException):
            CurrencyUnit.of1("")

    def test_factory_of_String_unknownCurrency(self) -> None:
        with self.assertRaises(IllegalCurrencyException) as cm:
            CurrencyUnit.of1("ABC")
        self.assertEqual("Unknown currency 'ABC'", str(cm.exception))

    def test_factory_of_String_nullString(self) -> None:
        with pytest.raises(NullPointerException):
            CurrencyUnit.of1(None)

    def test_factory_of_String(self) -> None:
        test = CurrencyUnit.of1("GBP")
        self.assertEqual("GBP", test.getCode())

    def test_factory_of_Currency_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            CurrencyUnit.of0(None)

    def test_factory_of_Currency(self) -> None:
        test: CurrencyUnit = CurrencyUnit.of0(self.__JDK_GBP)
        self.assertEqual("GBP", test.getCode())

    def test_constructor_nullCode(self) -> None:
        with self.assertRaises(AssertionError):
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
        curList1: List[str] = CurrencyUnit.registeredCountries()
        curList2: List[str] = CurrencyUnit.registeredCountries()
        curList2.sort()
        self.assertEqual(curList2, curList1)
        random.shuffle(curList2)
        curList2.sort()
        self.assertEqual(curList2, curList1)

    def test_registeredCountries(self) -> None:
        countryList = CurrencyUnit.registeredCountries()
        self.assertTrue(countryList.contains("GB"))
        self.assertTrue(countryList.contains("EU"))
        self.assertTrue(countryList.contains("US"))

    def test_registeredCurrencies_crossCheck(self) -> None:

        pass  # LLM could not translate this method

    def test_registeredCurrency_alreadyRegisteredCountry(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("GBX", 991, 2, ["GB"])

    def test_registeredCurrency_alreadyRegisteredNumericCode(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("TST", 826, 2, ["TS"])

    def test_registeredCurrency_alreadyRegisteredCode(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("GBP", 991, 2, ["GB"])

    def test_registeredCurrency_nullCountry(self) -> None:
        with self.assertRaises(NullPointerException):
            CurrencyUnit.registerCurrency0("TST", 991, 2, [None])

    def test_registeredCurrency_validDP_big(self) -> None:
        CurrencyUnit.registerCurrency0("XLG", -1, 30, [])
        currency: CurrencyUnit = CurrencyUnit.of1("XLG")
        self.assertEqual(30, currency.getDecimalPlaces())

    def test_registeredCurrency_invalidDP_big(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("TST", 991, 31, ["TS"])

    def test_registeredCurrency_invalidDP_small(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("TST", 991, -2, ["TS"])

    def test_registeredCurrency_invalidNumericCode_big(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("TST", 1000, 2, ["TS"])

    def test_registeredCurrency_invalidNumericCode_small(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("TST", -2, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_dash(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("A-", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_number(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("123", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_lowerCase(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("xxA", 991, 2, ["xx"])

    def test_registeredCurrency_invalidStringCode_4letters(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("ABCD", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_2letters(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("AB", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_1letter(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("A", 991, 2, ["TS"])

    def test_registeredCurrency_invalidStringCode_empty(self) -> None:
        with self.assertRaises(ValueError):
            CurrencyUnit.registerCurrency0("", 991, 2, ["TS"])

    def test_registeredCurrency_nullCode(self) -> None:
        with self.assertRaises(NullPointerException):
            CurrencyUnit.registerCurrency0(None, 991, 2, ["TS"])

    def test_registeredCurrencies_sorted(self) -> None:
        curList1: List[CurrencyUnit] = CurrencyUnit.registeredCurrencies()
        curList2: List[CurrencyUnit] = CurrencyUnit.registeredCurrencies()
        curList2.sort()
        self.assertEqual(curList2, curList1)
        random.shuffle(curList2)
        curList2.sort()
        self.assertEqual(curList2, curList1)

    def test_registeredCurrencies(self) -> None:
        curList: typing.List[CurrencyUnit] = CurrencyUnit.registeredCurrencies()
        found: bool = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "GBP":
                found = True
                break
        self.assertTrue(found)
