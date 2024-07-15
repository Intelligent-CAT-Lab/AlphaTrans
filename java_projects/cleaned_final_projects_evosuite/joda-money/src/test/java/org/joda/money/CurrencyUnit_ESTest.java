
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

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Collection;
import java.util.Currency;
import java.util.LinkedList;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.CurrencyUnit;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CurrencyUnit_ESTest extends CurrencyUnit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.of1("XPF");
      boolean boolean0 = currencyUnit0.isPseudoCurrency();
      assertFalse(boolean0);
      assertEquals("XPF", currencyUnit0.getCode());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      int int0 = currencyUnit0.getDecimalPlaces();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode0("Bic");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency '2421'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode0("wYE");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency '7531'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode0("z7");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency '747'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.of1("XPF");
      Currency currency0 = currencyUnit0.toCurrency();
      assertEquals("XPF", currency0.toString());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Currency currency0 = currencyUnit0.toCurrency();
      assertEquals(2, currency0.getDefaultFractionDigits());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.registerCurrency2("SOS", 0, 3, true);
      assertEquals(0, currencyUnit0.getNumericCode());
      assertEquals(3, currencyUnit0.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.registerCurrency2("YER", 3, 3, true);
      assertEquals(3, currencyUnit0.getDecimalPlaces());
      assertEquals(3, currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Set<String> set0 = currencyUnit0.CHF.getCountryCodes();
      LinkedList<Locale.LanguageRange> linkedList0 = new LinkedList<Locale.LanguageRange>();
      List<String> list0 = Locale.filterTags((List<Locale.LanguageRange>) linkedList0, (Collection<String>) set0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.registerCurrency1("YER", 999, 2, list0, true);
      //  // Unstable assertion: assertEquals(2, currencyUnit1.getDecimalPlaces());
      //  // Unstable assertion: assertEquals(0, set0.size());
      //  // Unstable assertion: assertEquals(999, currencyUnit1.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.ofNumericCode1(276);
      assertEquals(276, currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.of1("THB");
      assertEquals(764, currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Locale locale0 = Locale.UK;
      Currency currency0 = Currency.getInstance(locale0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.of0(currency0);
      assertEquals("GBP", currencyUnit0.getCode());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)4376, (short)2049);
      Locale locale0 = Locale.TAIWAN;
      currencyUnit0.getSymbol1(locale0);
      assertEquals(4376, currencyUnit0.getNumericCode());
      assertEquals(2049, currencyUnit0.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      int int0 = currencyUnit0.getNumericCode();
      assertEquals(840, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("THB", (short) (-730), (short) (-730));
      int int0 = currencyUnit0.getNumericCode();
      assertEquals((-730), int0);
      assertEquals(0, currencyUnit0.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Z$91<\u0002UqH", (short)3325, (short)3325);
      Set<String> set0 = currencyUnit0.getCountryCodes();
      assertEquals(3325, currencyUnit0.getNumericCode());
      assertEquals(3325, currencyUnit0.getDecimalPlaces());
      assertTrue(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)138, (short)138);
      currencyUnit0.getCode();
      assertEquals(138, currencyUnit0.getNumericCode());
      assertEquals(138, currencyUnit0.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Locale locale0 = Locale.KOREA;
      CurrencyUnit currencyUnit1 = CurrencyUnit.of2(locale0);
      int int0 = currencyUnit1.compareTo(currencyUnit0);
      //  // Unstable assertion: assertEquals(18, int0);
      //  // Unstable assertion: assertEquals(0, currencyUnit1.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Locale locale0 = Locale.KOREA;
      CurrencyUnit currencyUnit1 = CurrencyUnit.of2(locale0);
      int int0 = currencyUnit0.compareTo(currencyUnit1);
      //  // Unstable assertion: assertEquals((-14), int0);
      //  // Unstable assertion: assertEquals("UZS", currencyUnit1.getCode());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Currency already registered: ", (short)901, (short)901);
      // Undeclared exception!
      try { 
        currencyUnit0.toCurrency();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Currency", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency2((String) null, 126, 126, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      LinkedList<String> linkedList0 = new LinkedList<String>();
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1((String) null, 39, 39, linkedList0, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      List<String> list0 = CurrencyUnit.registeredCountries();
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency0((String) null, 886, 2, list0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCountry((String) null, currencyUnit0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.concurrent.ConcurrentSkipListMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode0((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofCountry((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Country code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.of2((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.of1((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.of0((Currency) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      // Undeclared exception!
      try { 
        currencyUnit0.getSymbol1((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      boolean boolean0 = currencyUnit0.equals(currencyUnit0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode1(11);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency '11'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.of1("XPF");
      CurrencyUnit currencyUnit1 = CurrencyUnit.USD;
      boolean boolean0 = currencyUnit0.equals(currencyUnit1);
      assertFalse(boolean0);
      assertEquals(953, currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      List<String> list0 = List.of("org.joda.money.DefaultCurrencyUnitDataProvider", "@?2=7f-", "@?2=7f-", "RUB", "N3");
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("TOP", 3, 3, list0, false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currency already registered: TOP
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("SOS", 0, (-28), (List<String>) null, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid number of decimal places
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("EUR", 3, 965, (List<String>) null, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid number of decimal places
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Set<String> set0 = currencyUnit0.CHF.getCountryCodes();
      LinkedList<Locale.LanguageRange> linkedList0 = new LinkedList<Locale.LanguageRange>();
      List<String> list0 = Locale.filterTags((List<Locale.LanguageRange>) linkedList0, (Collection<String>) set0);
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("YER", 1002, 2, list0, false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid numeric code
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      LinkedList<String> linkedList0 = new LinkedList<String>();
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("TOP", (-536), 2229, linkedList0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid numeric code
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      List<String> list0 = CurrencyUnit.registeredCountries();
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("+u", (-1503), (-1503), list0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid string code, must be length 3
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      boolean boolean0 = currencyUnit0.isPseudoCurrency();
      //  // Unstable assertion: assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      CurrencyUnit.registerCountry("UZS", currencyUnit0);
      currencyUnit0.getNumeric3Code();
      currencyUnit0.toString();
      currencyUnit0.equals("UZS");
      currencyUnit0.getCountryCodes();
      List<String> list0 = CurrencyUnit.registeredCountries();
      CurrencyUnit currencyUnit1 = CurrencyUnit.registerCurrency1("UZS", (-1), (-1), list0, true);
      currencyUnit1.getCode();
      currencyUnit0.getSymbol0();
      currencyUnit0.isPseudoCurrency();
      // Undeclared exception!
      try { 
        CurrencyUnit.ofCountry("000");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No currency found for country '000'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("THB", (short) (-730), (short) (-730));
      int int0 = currencyUnit0.getDecimalPlaces();
      assertEquals(0, int0);
      assertEquals((-730), currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      int int0 = currencyUnit0.getDecimalPlaces();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Set<String> set0 = currencyUnit0.CHF.getCountryCodes();
      LinkedList<Locale.LanguageRange> linkedList0 = new LinkedList<Locale.LanguageRange>();
      Locale.FilteringMode locale_FilteringMode0 = Locale.FilteringMode.MAP_EXTENDED_RANGES;
      List<String> list0 = Locale.filterTags((List<Locale.LanguageRange>) linkedList0, (Collection<String>) set0, locale_FilteringMode0);
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency1("978", 937, 937, list0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid string code, must be ASCII upper-case letters
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("ERROR: ", (short) (-1), (short) (-1));
      String string0 = currencyUnit0.getNumeric3Code();
      assertTrue(currencyUnit0.isPseudoCurrency());
      assertEquals("", string0);
      assertEquals((-1), currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      String string0 = currencyUnit0.getNumeric3Code();
      assertEquals("036", string0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      CurrencyUnit currencyUnit0 = null;
      try {
        currencyUnit0 = new CurrencyUnit((String) null, (short) (-6359), (short) (-6359));
        fail("Expecting exception: AssertionError");
      
      } catch(AssertionError e) {
         //
         // Joda-Money bug: Currency code must not be null
         //
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.ofCountry("BA");
      assertEquals("BAM", currencyUnit0.getCode());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      // Undeclared exception!
      try { 
        CurrencyUnit.of2(locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No currency found for locale 'fr'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode0("QWoo9^4DM9-Z/");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency 'QWoo9^4DM9-Z/'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.ofNumericCode0("1Y");
      assertEquals("AMD", currencyUnit0.getCode());
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.ofNumericCode0("392");
      assertEquals("JPY", currencyUnit0.getCode());
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.ofNumericCode0("/");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency '-1'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.of1("Data file ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency 'Data file '
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency2("UGX", 999, 30, false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currency already registered: UGX
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      List<String> list0 = CurrencyUnit.registeredCountries();
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency0("TJS", 1060, 1060, list0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid numeric code
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("GV", (short)0, (short)0);
      int int0 = currencyUnit0.getNumericCode();
      assertFalse(currencyUnit0.isPseudoCurrency());
      assertEquals(0, int0);
      assertEquals(0, currencyUnit0.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Locale locale0 = Locale.TAIWAN;
      String string0 = currencyUnit0.getSymbol1(locale0);
      assertEquals("AU$", string0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      LinkedList<Locale.LanguageRange> linkedList0 = new LinkedList<Locale.LanguageRange>();
      Locale.IsoCountryCode locale_IsoCountryCode0 = Locale.IsoCountryCode.PART1_ALPHA3;
      Set<String> set0 = Locale.getISOCountries(locale_IsoCountryCode0);
      List<String> list0 = Locale.filterTags((List<Locale.LanguageRange>) linkedList0, (Collection<String>) set0);
      // Undeclared exception!
      try { 
        CurrencyUnit.registerCurrency0("org.joda.money.IllegalCurrencyException", (short)0, 0, list0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid string code, must be length 3
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      int int0 = currencyUnit0.compareTo(currencyUnit0);
      //  // Unstable assertion: assertEquals(0, int0);
      //  // Unstable assertion: assertEquals(0, currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      List<CurrencyUnit> list0 = CurrencyUnit.registeredCurrencies();
      assertFalse(list0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.registerCurrency2("TOP", (-1), (-1), true);
      assertTrue(currencyUnit0.isPseudoCurrency());
      assertEquals((-1), currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      List<String> list0 = CurrencyUnit.registeredCountries();
      CurrencyUnit currencyUnit0 = CurrencyUnit.registerCurrency1("RSD", 0, 0, list0, true);
      String string0 = currencyUnit0.getNumeric3Code();
      assertEquals(0, currencyUnit0.getDecimalPlaces());
      assertFalse(currencyUnit0.isPseudoCurrency());
      assertEquals("000", string0);
  }  

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)2, (short)2);
      currencyUnit0.getSymbol0();
      assertEquals(2, currencyUnit0.getDecimalPlaces());
      assertEquals(2, currencyUnit0.getNumericCode());
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      currencyUnit0.hashCode();
  }
}
