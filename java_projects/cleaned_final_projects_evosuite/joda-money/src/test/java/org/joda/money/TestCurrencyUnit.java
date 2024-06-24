
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */

package org.joda.money;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Currency;
import java.util.List;
import java.util.Locale;
import java.util.Set;

/** Test CurrencyUnit. */
public class TestCurrencyUnit {

    private static final Currency JDK_GBP = Currency.getInstance("GBP");

    @Test
    public void test_registeredCurrencies() {
        List<CurrencyUnit> curList = CurrencyUnit.registeredCurrencies();
        boolean found = false;
        for (CurrencyUnit currencyUnit : curList) {
            if (currencyUnit.getCode().equals("GBP")) {
                found = true;
                break;
            }
        }
        assertTrue(found);
    }

    @Test
    public void test_registeredCurrencies_sorted() {
        List<CurrencyUnit> curList1 = CurrencyUnit.registeredCurrencies();
        List<CurrencyUnit> curList2 = CurrencyUnit.registeredCurrencies();
        Collections.sort(curList2);
        assertEquals(curList2, curList1);
        Collections.shuffle(curList2);
        Collections.sort(curList2);
        assertEquals(curList2, curList1);
    }

    @Test(expected = NullPointerException.class)
    public void test_registeredCurrency_nullCode() {
        CurrencyUnit.registerCurrency0(null, 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_empty() {
        CurrencyUnit.registerCurrency0("", 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_1letter() {
        CurrencyUnit.registerCurrency0("A", 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_2letters() {
        CurrencyUnit.registerCurrency0("AB", 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_4letters() {
        CurrencyUnit.registerCurrency0("ABCD", 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_lowerCase() {
        CurrencyUnit.registerCurrency0("xxA", 991, 2, Arrays.asList("xx"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_number() {
        CurrencyUnit.registerCurrency0("123", 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidStringCode_dash() {
        CurrencyUnit.registerCurrency0("A-", 991, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidNumericCode_small() {
        CurrencyUnit.registerCurrency0("TST", -2, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidNumericCode_big() {
        CurrencyUnit.registerCurrency0("TST", 1000, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidDP_small() {
        CurrencyUnit.registerCurrency0("TST", 991, -2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_invalidDP_big() {
        CurrencyUnit.registerCurrency0("TST", 991, 31, Arrays.asList("TS"));
    }

    @Test
    public void test_registeredCurrency_validDP_big() {
        CurrencyUnit.registerCurrency0("XLG", -1, 30, new ArrayList<String>());

        CurrencyUnit currency = CurrencyUnit.of1("XLG");
        assertEquals(30, currency.getDecimalPlaces());
    }

    @Test(expected = NullPointerException.class)
    public void test_registeredCurrency_nullCountry() {
        CurrencyUnit.registerCurrency0("TST", 991, 2, Arrays.asList((String) null));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_alreadyRegisteredCode() {
        CurrencyUnit.registerCurrency0("GBP", 991, 2, Arrays.asList("GB"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_alreadyRegisteredNumericCode() {
        CurrencyUnit.registerCurrency0("TST", 826, 2, Arrays.asList("TS"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_registeredCurrency_alreadyRegisteredCountry() {
        CurrencyUnit.registerCurrency0("GBX", 991, 2, Arrays.asList("GB"));
    }

    @Test
    public void test_registeredCurrencies_crossCheck() {
        List<CurrencyUnit> curList = CurrencyUnit.registeredCurrencies();
        for (CurrencyUnit currencyUnit : curList) {
            try {
                Currency curr = Currency.getInstance(currencyUnit.getCode());
                int dp = curr.getDefaultFractionDigits() < 0 ? 0 : curr.getDefaultFractionDigits();
                assertEquals(curr.getCurrencyCode(), dp, currencyUnit.getDecimalPlaces());
            } catch (IllegalArgumentException ignored) {
            }
        }
    }

    @Test
    public void test_registeredCountries() {
        List<String> countryList = CurrencyUnit.registeredCountries();
        assertTrue(countryList.contains("GB"));
        assertTrue(countryList.contains("EU"));
        assertTrue(countryList.contains("US"));
    }

    @Test
    public void test_registeredCountries_sorted() {
        List<String> curList1 = CurrencyUnit.registeredCountries();
        List<String> curList2 = CurrencyUnit.registeredCountries();
        Collections.sort(curList2);
        assertEquals(curList2, curList1);
        Collections.shuffle(curList2);
        Collections.sort(curList2);
        assertEquals(curList2, curList1);
    }

    @Test
    public void test_constants() {
        assertEquals(CurrencyUnit.of1("USD"), CurrencyUnit.USD);
        assertEquals(CurrencyUnit.of1("EUR"), CurrencyUnit.EUR);
        assertEquals(CurrencyUnit.of1("JPY"), CurrencyUnit.JPY);
        assertEquals(CurrencyUnit.of1("GBP"), CurrencyUnit.GBP);
        assertEquals(CurrencyUnit.of1("CHF"), CurrencyUnit.CHF);
        assertEquals(CurrencyUnit.of1("AUD"), CurrencyUnit.AUD);
        assertEquals(CurrencyUnit.of1("CAD"), CurrencyUnit.CAD);
    }

    @Test(expected = AssertionError.class)
    public void test_constructor_nullCode() {
        new CurrencyUnit(null, (short) 1, (short) 2);
    }

    @Test
    public void test_factory_of_Currency() {
        CurrencyUnit test = CurrencyUnit.of0(JDK_GBP);
        assertEquals("GBP", test.getCode());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_nullCurrency() {
        CurrencyUnit.of0((Currency) null);
    }

    @Test
    public void test_factory_of_String() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertEquals("GBP", test.getCode());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_String_nullString() {
        CurrencyUnit.of1((String) null);
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_of_String_unknownCurrency() {
        try {
            CurrencyUnit.of1("ABC");
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency 'ABC'", ex.getMessage());
            throw ex;
        }
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_of_String_empty() {
        CurrencyUnit.of1("");
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_of_String_tooShort_unknown() {
        CurrencyUnit.of1("AB");
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_of_String_tooLong_unknown() {
        CurrencyUnit.of1("ABCD");
    }

    @Test
    public void test_factory_ofNumericCode_String() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode0("826");
        assertEquals("GBP", test.getCode());
    }

    @Test
    public void test_factory_ofNumericCode_String_2char() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode0("051");
        assertEquals("AMD", test.getCode());
    }

    @Test
    public void test_factory_ofNumericCode_String_2charNoPad() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode0("51");
        assertEquals("AMD", test.getCode());
    }

    @Test
    public void test_factory_ofNumericCode_String_1char() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode0("008");
        assertEquals("ALL", test.getCode());
    }

    @Test
    public void test_factory_ofNumericCode_String_1charNoPad() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode0("8");
        assertEquals("ALL", test.getCode());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_ofNumericCode_String_nullString() {
        CurrencyUnit.ofNumericCode0((String) null);
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_String_unknownCurrency() {
        try {
            CurrencyUnit.ofNumericCode0("111");
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency '111'", ex.getMessage());
            throw ex;
        }
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_String_negative() {
        CurrencyUnit.ofNumericCode0("-1");
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_String_empty() {
        try {
            CurrencyUnit.ofNumericCode0("");
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency ''", ex.getMessage());
            throw ex;
        }
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_String_tooLong() {
        try {
            CurrencyUnit.ofNumericCode0("1234");
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency '1234'", ex.getMessage());
            throw ex;
        }
    }

    @Test
    public void test_factory_ofNumericCode_int() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode1(826);
        assertEquals("GBP", test.getCode());
    }

    @Test
    public void test_factory_ofNumericCode_int_2char() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode1(51);
        assertEquals("AMD", test.getCode());
    }

    @Test
    public void test_factory_ofNumericCode_int_1char() {
        CurrencyUnit test = CurrencyUnit.ofNumericCode1(8);
        assertEquals("ALL", test.getCode());
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_int_unknownCurrency() {
        try {
            CurrencyUnit.ofNumericCode1(111);
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency '111'", ex.getMessage());
            throw ex;
        }
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_int_negative() {
        try {
            CurrencyUnit.ofNumericCode1(-1);
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency '-1'", ex.getMessage());
            throw ex;
        }
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofNumericCode_int_tooLong() {
        try {
            CurrencyUnit.ofNumericCode1(1234);
        } catch (IllegalCurrencyException ex) {
            assertEquals("Unknown currency '1234'", ex.getMessage());
            throw ex;
        }
    }

    @Test
    public void test_factory_of_LocaleUK() {
        CurrencyUnit test = CurrencyUnit.of2(Locale.UK);
        assertEquals("GBP", test.getCode());
    }

    @Test
    public void test_factory_of_LocaleUS() {
        CurrencyUnit test = CurrencyUnit.of2(Locale.US);
        assertEquals("USD", test.getCode());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Locale_nullLocale() {
        CurrencyUnit.of2((Locale) null);
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_of_Locale_unknownCurrency() {
        try {
            CurrencyUnit.of2(new Locale("en", "XY"));
        } catch (IllegalCurrencyException ex) {
            assertEquals("No currency found for locale 'en_XY'", ex.getMessage());
            throw ex;
        }
    }

    @Test
    public void test_factory_ofCountry_String() {
        CurrencyUnit test = CurrencyUnit.ofCountry("GB");
        assertEquals("GBP", test.getCode());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_ofCountry_String_nullString() {
        CurrencyUnit.ofCountry((String) null);
    }

    @Test(expected = IllegalCurrencyException.class)
    public void test_factory_ofCountry_String_unknownCurrency() {
        try {
            CurrencyUnit.ofCountry("gb");
        } catch (IllegalCurrencyException ex) {
            assertEquals("No currency found for country 'gb'", ex.getMessage());
            throw ex;
        }
    }

    @Test
    public void test_getNumeric3Code_GBP() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertEquals("826", test.getNumeric3Code());
    }

    @Test
    public void test_getNumeric3Code_ALL() {
        CurrencyUnit test = CurrencyUnit.of1("ALL");
        assertEquals("008", test.getNumeric3Code());
    }

    @Test
    public void test_getNumeric3Code_AMD() {
        CurrencyUnit test = CurrencyUnit.of1("AMD");
        assertEquals("051", test.getNumeric3Code());
    }

    @Test
    public void test_getNumeric3Code_XFU() {
        CurrencyUnit test = CurrencyUnit.of1("XFU");
        assertEquals("", test.getNumeric3Code());
    }

    @Test
    public void test_getNumericCode_GBP() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertEquals(826, test.getNumericCode());
    }

    @Test
    public void test_getCurrencyCodes_GBP() {
        Set<String> test = CurrencyUnit.of1("GBP").getCountryCodes();
        assertTrue(test.contains("GB"));
        assertTrue(test.contains("IM"));
        assertTrue(test.contains("JE"));
        assertTrue(test.contains("GG"));
    }

    @Test
    public void test_getDecimalPlaces_GBP() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertEquals(2, test.getDecimalPlaces());
    }

    @Test
    public void test_getDecimalPlaces_JPY() {
        CurrencyUnit test = CurrencyUnit.of1("JPY");
        assertEquals(0, test.getDecimalPlaces());
    }

    @Test
    public void test_getDecimalPlaces_XXX() {
        CurrencyUnit test = CurrencyUnit.of1("XXX");
        assertEquals(0, test.getDecimalPlaces());
    }

    @Test
    public void test_isPseudoCurrency_GBP() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertFalse(test.isPseudoCurrency());
    }

    @Test
    public void test_isPseudoCurrency_JPY() {
        CurrencyUnit test = CurrencyUnit.of1("JPY");
        assertFalse(test.isPseudoCurrency());
    }

    @Test
    public void test_isPseudoCurrency_XXX() {
        CurrencyUnit test = CurrencyUnit.of1("XXX");
        assertTrue(test.isPseudoCurrency());
    }

    @Test
    public void test_getSymbol_GBP() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("GBP");
            assertEquals("\u00A3", test.getSymbol0());
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_JPY() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("JPY");
            assertTrue(test.getSymbol0().contains("JP"));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_TMT() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("TMT");
            assertEquals("TMT", test.getSymbol0());
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_Locale_GBP_UK() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("GBP");
            assertEquals("\u00A3", test.getSymbol1(Locale.UK));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_Locale_GBP_France() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("GBP");
            assertTrue(test.getSymbol1(Locale.FRANCE).contains("GB"));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_Locale_USD_UK() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("USD");
            assertEquals("$", test.getSymbol1(Locale.US));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_Locale_USD_France() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("USD");
            assertTrue(test.getSymbol1(Locale.FRANCE).contains("US"));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_Locale_JPY_Japan() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("JPY");
            assertEquals("\uFFE5", test.getSymbol1(Locale.JAPAN));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_getSymbol_TMT_UK() {
        Locale loc = Locale.getDefault();
        try {
            Locale.setDefault(Locale.UK);
            CurrencyUnit test = CurrencyUnit.of1("TMT");
            assertEquals("TMT", test.getSymbol1(Locale.UK));
        } finally {
            Locale.setDefault(loc);
        }
    }

    @Test
    public void test_toCurrency() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertEquals(JDK_GBP, test.toCurrency());
    }

    @Test
    public void test_compareTo() {
        CurrencyUnit a = CurrencyUnit.of1("EUR");
        CurrencyUnit b = CurrencyUnit.of1("GBP");
        CurrencyUnit c = CurrencyUnit.of1("JPY");
        assertEquals(0, a.compareTo(a));
        assertEquals(0, b.compareTo(b));
        assertEquals(0, c.compareTo(c));

        assertTrue(a.compareTo(b) < 0);
        assertTrue(b.compareTo(a) > 0);

        assertTrue(a.compareTo(c) < 0);
        assertTrue(c.compareTo(a) > 0);

        assertTrue(b.compareTo(c) < 0);
        assertTrue(c.compareTo(b) > 0);
    }

    @Test(expected = NullPointerException.class)
    public void test_compareTo_null() {
        CurrencyUnit.of1("EUR").compareTo(null);
    }

    @Test
    public void test_equals_hashCode() {
        CurrencyUnit a = CurrencyUnit.of1("GBP");
        CurrencyUnit b = CurrencyUnit.of1("GBP");
        CurrencyUnit c = CurrencyUnit.of1("EUR");
        assertTrue(a.equals(a));
        assertTrue(b.equals(b));
        assertTrue(c.equals(c));

        assertTrue(a.equals(b));
        assertTrue(b.equals(a));
        assertTrue(a.hashCode() == b.hashCode());

        assertFalse(a.equals(c));
        assertFalse(b.equals(c));
    }

    @Test
    public void test_equals_false() {
        CurrencyUnit a = CurrencyUnit.of1("GBP");
        assertFalse(a.equals(null));
        Object obj = "String"; // avoid warning in Eclipse
        assertFalse(a.equals(obj));
        assertFalse(a.equals(new Object()));
    }

    @Test
    public void test_toString() {
        CurrencyUnit test = CurrencyUnit.of1("GBP");
        assertEquals("GBP", test.toString());
    }
}
