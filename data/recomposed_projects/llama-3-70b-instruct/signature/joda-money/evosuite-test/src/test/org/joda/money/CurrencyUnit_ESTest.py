from __future__ import annotations
import time
import locale
import re
import os
import typing
from typing import *
import decimal
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.CurrencyUnit import *

# from src.test.org.joda.money.CurrencyUnit_ESTest_scaffolding import *


class CurrencyUnit_ESTest(unittest.TestCase):

    def test66(self) -> None:
        currencyUnit0 = CurrencyUnit.GBP
        currencyUnit0.hashCode()

    def test65(self) -> None:

        currencyUnit0 = CurrencyUnit("", 2, 2)
        currencyUnit0.getSymbol0()
        self.assertEqual(2, currencyUnit0.getDecimalPlaces())
        self.assertEqual(2, currencyUnit0.getNumericCode())

    def test63(self) -> None:

        list0 = CurrencyUnit.registeredCountries()
        currencyUnit0 = CurrencyUnit.registerCurrency1("RSD", 0, 0, list0, True)
        string0 = currencyUnit0.getNumeric3Code()
        self.assertEqual(0, currencyUnit0.getDecimalPlaces())
        self.assertFalse(currencyUnit0.isPseudoCurrency())
        self.assertEqual("000", string0)

    def test62(self) -> None:

        currencyUnit0 = CurrencyUnit.registerCurrency2("TOP", -1, -1, True)
        self.assertTrue(currencyUnit0.isPseudoCurrency())
        self.assertEqual(-1, currencyUnit0.getNumericCode())

    def test61(self) -> None:
        list0 = CurrencyUnit.registeredCurrencies()
        assert not list0, "List is not empty"

    def test60(self) -> None:

        locale0 = Locale.TAIWAN
        currencyUnit0 = CurrencyUnit.of2(locale0)
        int0 = currencyUnit0.compareTo(currencyUnit0)
        # Unstable assertion: self.assertEqual(0, int0)
        # Unstable assertion: self.assertEqual(0, currencyUnit0.getNumericCode())

    def test59(self) -> None:

        linkedList0 = []
        locale_IsoCountryCode0 = Locale.IsoCountryCode.PART1_ALPHA3
        set0 = Locale.getISOCountries(locale_IsoCountryCode0)
        list0 = Locale.filterTags(linkedList0, set0)

        try:
            CurrencyUnit.registerCurrency0(
                "org.joda.money.IllegalCurrencyException", 0, 0, list0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.CurrencyUnit", e)

    def test58(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        locale0 = Locale.TAIWAN
        string0 = currencyUnit0.getSymbol1(locale0)
        self.assertEqual("AU$", string0)

    def test57(self) -> None:

        currencyUnit0 = CurrencyUnit("GV", 0, 0)
        int0 = currencyUnit0.getNumericCode()
        self.assertFalse(currencyUnit0.isPseudoCurrency())
        self.assertEqual(0, int0)
        self.assertEqual(0, currencyUnit0.getDecimalPlaces())

    def test56(self) -> None:

        list0 = CurrencyUnit.registeredCountries()

        try:
            CurrencyUnit.registerCurrency0("TJS", 1060, 1060, list0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.CurrencyUnit", e)

    def test55(self) -> None:

        try:
            CurrencyUnit.registerCurrency2("UGX", 999, 30, False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Currency already registered: UGX
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test54(self) -> None:

        try:
            CurrencyUnit.of1("Data file ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test53(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("/")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.CurrencyUnit", e)

    def test52(self) -> None:

        currencyUnit0 = CurrencyUnit.ofNumericCode0("392")
        self.assertEqual("JPY", currencyUnit0.getCode())

    def test51(self) -> None:

        currencyUnit0 = CurrencyUnit.ofNumericCode0("1Y")
        self.assertEqual("AMD", currencyUnit0.getCode())

    def test50(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("QWoo9^4DM9-Z/")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.CurrencyUnit", e)

    def test49(self) -> None:

        locale0 = Locale.FRENCH
        try:
            CurrencyUnit.of2(locale0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test48(self) -> None:
        currencyUnit0 = CurrencyUnit.ofCountry("BA")
        self.assertEqual("BAM", currencyUnit0.getCode())

    def test47(self) -> None:

        currencyUnit0 = None
        try:
            currencyUnit0 = CurrencyUnit(None, -6359, -6359)
            self.fail("Expecting exception: AssertionError")

        except AssertionError:
            # Joda-Money bug: Currency code must not be null
            pass

    def test46(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        string0 = currencyUnit0.getNumeric3Code()
        self.assertEqual("036", string0)

    def test45(self) -> None:

        currencyUnit0 = CurrencyUnit("ERROR: ", -1, -1)
        string0 = currencyUnit0.getNumeric3Code()
        self.assertTrue(currencyUnit0.isPseudoCurrency())
        self.assertEqual("", string0)
        self.assertEqual(-1, currencyUnit0.getNumericCode())

    def test44(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        set0 = currencyUnit0.CHF.getCountryCodes()
        linkedList0 = LinkedList[Locale.LanguageRange]()
        locale_FilteringMode0 = Locale.FilteringMode.MAP_EXTENDED_RANGES
        list0 = Locale.filterTags(linkedList0, set0, locale_FilteringMode0)

        # Undeclared exception in Java, so we'll use a try-except block
        try:
            CurrencyUnit.registerCurrency1("978", 937, 937, list0, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid string code, must be ASCII upper-case letters
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test43(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        int0 = currencyUnit0.getDecimalPlaces()
        self.assertEqual(2, int0)

    def test42(self) -> None:

        currencyUnit0 = CurrencyUnit("THB", -730, -730)
        int0 = currencyUnit0.getDecimalPlaces()
        self.assertEqual(0, int0)
        self.assertEqual(-730, currencyUnit0.getNumericCode())

    def test41(self) -> None:

        locale0 = Locale.TAIWAN
        currencyUnit0 = CurrencyUnit.of2(locale0)
        CurrencyUnit.registerCountry("UZS", currencyUnit0)
        currencyUnit0.getNumeric3Code()
        currencyUnit0.toString()
        currencyUnit0.equals("UZS")
        currencyUnit0.getCountryCodes()
        list0 = CurrencyUnit.registeredCountries()
        currencyUnit1 = CurrencyUnit.registerCurrency1("UZS", (-1), (-1), list0, True)
        currencyUnit1.getCode()
        currencyUnit0.getSymbol0()
        currencyUnit0.isPseudoCurrency()
        # Undeclared exception in Java code
        try:
            CurrencyUnit.ofCountry("000")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # No currency found for country '000'
            #
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test40(self) -> None:
        locale0 = Locale.TAIWAN
        currencyUnit0 = CurrencyUnit.of2(locale0)
        boolean0 = currencyUnit0.isPseudoCurrency()
        #  // Unstable assertion: assertTrue(boolean0);

    def test39(self) -> None:

        list0 = CurrencyUnit.registeredCountries()
        # Undeclared exception in Java code
        try:
            CurrencyUnit.registerCurrency1("+u", (-1503), (-1503), list0, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid string code, must be length 3
            #
            self.assertEqual(str(e), "Invalid string code, must be length 3")

    def test38(self) -> None:

        linkedList0 = []
        try:
            CurrencyUnit.registerCurrency1("TOP", -536, 2229, linkedList0, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Invalid numeric code
            #
            self.assertEqual(str(e), "Invalid numeric code")

    def test37(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        set0 = currencyUnit0.CHF.getCountryCodes()
        linkedList0 = LinkedList[Locale.LanguageRange]()
        list0 = Locale.filterTags(linkedList0, set0)

        try:
            CurrencyUnit.registerCurrency1("YER", 1002, 2, list0, False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.CurrencyUnit", e)

    def test36(self) -> None:

        try:
            CurrencyUnit.registerCurrency1("EUR", 3, 965, None, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid number of decimal places
            self.assertTrue("Invalid number of decimal places" in str(e))

    def test35(self) -> None:

        try:
            CurrencyUnit.registerCurrency1("SOS", 0, -28, None, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid number of decimal places
            self.assertTrue("Invalid number of decimal places" in str(e))

    def test34(self) -> None:

        list0 = [
            "org.joda.money.DefaultCurrencyUnitDataProvider",
            "@?2=7f-",
            "@?2=7f-",
            "RUB",
            "N3",
        ]
        try:
            CurrencyUnit.registerCurrency1("TOP", 3, 3, list0, False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.CurrencyUnit", e)

    def test33(self) -> None:

        currencyUnit0 = CurrencyUnit.of1("XPF")
        currencyUnit1 = CurrencyUnit.USD
        boolean0 = currencyUnit0.equals(currencyUnit1)
        self.assertFalse(boolean0)
        self.assertEqual(953, currencyUnit0.getNumericCode())

    def test32(self) -> None:

        try:
            CurrencyUnit.ofNumericCode1(11)
            self.fail("Expecting exception: ValueError")

        except IllegalCurrencyException as e:
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test31(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        boolean0 = currencyUnit0.equals(currencyUnit0)
        self.assertTrue(boolean0)

    def test30(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        try:
            currencyUnit0.getSymbol1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test29(self) -> None:

        try:
            CurrencyUnit.of0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Currency must not be null
            verifyException("org.joda.money.MoneyUtils", e)

    def test28(self) -> None:

        try:
            CurrencyUnit.of1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test27(self) -> None:

        with pytest.raises(RuntimeError):
            CurrencyUnit.of2(None)

    def test26(self) -> None:
        with pytest.raises(RuntimeError):
            CurrencyUnit.ofCountry(None)
        verifyException("org.joda.money.MoneyUtils", RuntimeError)

    def test25(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test24(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        try:
            CurrencyUnit.registerCountry(None, currencyUnit0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.concurrent.ConcurrentSkipListMap", e)

    def test23(self) -> None:

        list0 = CurrencyUnit.registeredCountries()

        with self.assertRaises(RuntimeError):
            CurrencyUnit.registerCurrency0(None, 886, 2, list0)

        # Currency code must not be null
        # verifyException("org.joda.money.MoneyUtils", e)
        # This line is commented out in the original Java code, so I'm not sure what it's supposed to do.
        # If it's a method call, it's not available in the provided partial Python translation.

    def test22(self) -> None:

        linkedList0 = []
        try:
            CurrencyUnit.registerCurrency1(None, 39, 39, linkedList0, False)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "Currency code must not be null")

    def test21(self) -> None:

        # Undeclared exception
        try:
            CurrencyUnit.registerCurrency2(None, 126, 126, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Currency code must not be null
            self.assertIsInstance(e, RuntimeError)

    def test20(self) -> None:

        currencyUnit0 = CurrencyUnit("Currency already registered: ", 901, 901)

        with pytest.raises(ValueError) as e:
            currencyUnit0.toCurrency()

        assert str(e.value) == "Expecting exception: ValueError"

    def test19(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        locale0 = Locale.KOREA
        currencyUnit1 = CurrencyUnit.of2(locale0)
        int0 = currencyUnit0.compareTo(currencyUnit1)
        #  // Unstable assertion: self.assertEqual((-14), int0)
        #  // Unstable assertion: self.assertEqual("UZS", currencyUnit1.getCode())

    def test18(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        locale0 = Locale.KOREA
        currencyUnit1 = CurrencyUnit.of2(locale0)
        int0 = currencyUnit1.compareTo(currencyUnit0)
        #  // Unstable assertion: self.assertEqual(18, int0)
        #  // Unstable assertion: self.assertEqual(0, currencyUnit1.getDecimalPlaces())

    def test17(self) -> None:

        currencyUnit0 = CurrencyUnit("", 138, 138)
        currencyUnit0.getCode()
        self.assertEqual(138, currencyUnit0.getNumericCode())
        self.assertEqual(138, currencyUnit0.getDecimalPlaces())

    def test16(self) -> None:

        currencyUnit0 = CurrencyUnit("Z$91<\u0002UqH", 3325, 3325)
        set0 = currencyUnit0.getCountryCodes()
        self.assertEqual(currencyUnit0.getNumericCode(), 3325)
        self.assertEqual(currencyUnit0.getDecimalPlaces(), 3325)
        self.assertTrue(not set0)

    def test15(self) -> None:

        currencyUnit0 = CurrencyUnit("THB", -730, -730)
        int0 = currencyUnit0.getNumericCode()
        self.assertEqual(-730, int0)
        self.assertEqual(0, currencyUnit0.getDecimalPlaces())

    def test14(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        int0 = currencyUnit0.getNumericCode()
        self.assertEqual(840, int0)

    def test13(self) -> None:

        currencyUnit0 = CurrencyUnit("", 4376, 2049)
        locale0 = Locale.TAIWAN
        currencyUnit0.getSymbol1(locale0)
        self.assertEqual(4376, currencyUnit0.getNumericCode())
        self.assertEqual(2049, currencyUnit0.getDecimalPlaces())

    def test12(self) -> None:
        locale0 = Locale.UK
        currency0 = Currency.getInstance(locale0)
        currencyUnit0 = CurrencyUnit.of0(currency0)
        self.assertEqual("GBP", currencyUnit0.getCode())

    def test11(self) -> None:
        currencyUnit0 = CurrencyUnit.of1("THB")
        self.assertEqual(764, currencyUnit0.getNumericCode())

    def test10(self) -> None:

        currencyUnit0 = CurrencyUnit.ofNumericCode1(276)
        self.assertEqual(276, currencyUnit0.getNumericCode())

    def test09(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        set0 = currencyUnit0.CHF.getCountryCodes()
        linkedList0 = LinkedList[Locale.LanguageRange]()
        list0 = Locale.filterTags(linkedList0, set0)
        currencyUnit1 = CurrencyUnit.registerCurrency1("YER", 999, 2, list0, True)
        #  // Unstable assertion: self.assertEqual(2, currencyUnit1.getDecimalPlaces())
        #  // Unstable assertion: self.assertEqual(0, len(set0))
        #  // Unstable assertion: self.assertEqual(999, currencyUnit1.getNumericCode())

    def test08(self) -> None:

        currencyUnit0 = CurrencyUnit.registerCurrency2("YER", 3, 3, True)
        self.assertEqual(3, currencyUnit0.getDecimalPlaces())
        self.assertEqual(3, currencyUnit0.getNumericCode())

    def test07(self) -> None:

        currencyUnit0 = CurrencyUnit.registerCurrency2("SOS", 0, 3, True)
        self.assertEqual(0, currencyUnit0.getNumericCode())
        self.assertEqual(3, currencyUnit0.getDecimalPlaces())

    def test06(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        currency0 = currencyUnit0.toCurrency()

        # Python's built-in unittest module does not have a direct equivalent to Java's org.evosuite.runtime.EvoAssertions.assertEquals.
        # However, you can use the unittest.TestCase.assertEqual method to assert that two values are equal.
        # Here is an example:

        self.assertEqual(
            2, len(currency0.split(".")[1])
        )  # Get the number of fraction digits

        # Note: This is a simplified example and may not work as expected for all currencies.
        # For a more accurate translation, you would need to use a library that provides a direct equivalent to Java's org.evosuite.runtime.EvoAssertions.assertEquals.

    def test05(self) -> None:

        currencyUnit0 = CurrencyUnit.of1("XPF")
        currency0 = currencyUnit0.toCurrency()
        self.assertEqual("XPF", currency0)

    def test04(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("z7")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test03(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("wYE")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test02(self) -> None:

        try:
            CurrencyUnit.ofNumericCode0("Bic")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test01(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        int0 = currencyUnit0.getDecimalPlaces()
        self.assertEqual(0, int0)

    def test00(self) -> None:

        currencyUnit0 = CurrencyUnit.of1("XPF")
        boolean0 = currencyUnit0.isPseudoCurrency()
        self.assertFalse(boolean0)
        self.assertEqual("XPF", currencyUnit0.getCode())
