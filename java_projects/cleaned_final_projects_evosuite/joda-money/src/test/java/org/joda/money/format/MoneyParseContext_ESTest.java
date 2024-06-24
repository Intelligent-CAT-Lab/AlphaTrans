
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


package org.joda.money.format;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.math.BigDecimal;
import java.nio.CharBuffer;
import java.text.ParsePosition;
import java.util.Locale;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.CurrencyUnit;
import org.joda.money.format.MoneyParseContext;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MoneyParseContext_ESTest extends MoneyParseContext_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(0);
      Locale locale0 = Locale.US;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, (BigDecimal) null, (-3019), currencyUnit0);
      MoneyParseContext moneyParseContext1 = moneyParseContext0.createChild();
      moneyParseContext1.mergeChild(moneyParseContext0);
      assertEquals((-3019), moneyParseContext1.getErrorIndex());
      assertEquals(0, moneyParseContext1.getIndex());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = new BigDecimal(5763);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-2728), "Canada", 10, locale0, bigDecimal0, 222, (CurrencyUnit) null);
      moneyParseContext0.setIndex((-62));
      boolean boolean0 = moneyParseContext0.isFullyParsed();
      assertEquals((-62), moneyParseContext0.getIndex());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isError();
      assertEquals(0, moneyParseContext0.getErrorIndex());
      assertTrue(boolean0);
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      moneyParseContext0.setLocale(locale0);
      assertEquals(0, moneyParseContext0.getErrorIndex());
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      ParsePosition parsePosition0 = moneyParseContext0.toParsePosition();
      assertEquals("java.text.ParsePosition[index=0,errorIndex=0]", parsePosition0.toString());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 22, locale0, (BigDecimal) null, 30, currencyUnit0);
      ParsePosition parsePosition0 = moneyParseContext0.toParsePosition();
      assertEquals("java.text.ParsePosition[index=22,errorIndex=30]", parsePosition0.toString());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CharBuffer charBuffer0 = CharBuffer.allocate(6);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-2447), charBuffer0, 1359, locale0, bigDecimal0, (-2447), (CurrencyUnit) null);
      String string0 = moneyParseContext0.getTextSubstring(0, 6);
      assertEquals(1359, moneyParseContext0.getIndex());
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals("\u0000\u0000\u0000\u0000\u0000\u0000", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      moneyParseContext0.getTextSubstring(0, 0);
      assertEquals(0, moneyParseContext0.getErrorIndex());
      assertTrue(moneyParseContext0.isFullyParsed());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(0);
      Locale locale0 = Locale.CHINESE;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      moneyParseContext0.getTextLength();
      assertEquals(0, moneyParseContext0.getErrorIndex());
      assertTrue(moneyParseContext0.isFullyParsed());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = new BigDecimal(5763);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-2728), "Canada", 10, locale0, bigDecimal0, 222, (CurrencyUnit) null);
      moneyParseContext0.getTextLength();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals(10, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      moneyParseContext0.getText();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals(5763, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Locale locale0 = Locale.CHINESE;
      BigDecimal bigDecimal0 = new BigDecimal(0.0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(810, "", (-1), locale0, bigDecimal0, (-2142), currencyUnit0);
      moneyParseContext0.getText();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals((-1), moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal(0.0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "Taiwan", 1776, locale0, bigDecimal0, 1278, currencyUnit0);
      moneyParseContext0.getText();
      assertEquals(1278, moneyParseContext0.getErrorIndex());
      assertEquals(1776, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(999, "Taiwan", 0, (Locale) null, bigDecimal0, 0, currencyUnit0);
      moneyParseContext0.getLocale();
      assertEquals(0, moneyParseContext0.getIndex());
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(0);
      Locale locale0 = Locale.CHINESE;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      int int0 = moneyParseContext0.getIndex();
      assertEquals(0, moneyParseContext0.getErrorIndex());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Locale locale0 = Locale.UK;
      BigDecimal bigDecimal0 = new BigDecimal(2979);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(2821, "", (-1172), locale0, bigDecimal0, 0, currencyUnit0);
      int int0 = moneyParseContext0.getIndex();
      assertEquals((-1172), int0);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      char[] charArray0 = new char[8];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, (CurrencyUnit) null);
      int int0 = moneyParseContext0.getErrorIndex();
      assertEquals(0, moneyParseContext0.getIndex());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(2591, "Canada", 5763, locale0, bigDecimal0, 772, currencyUnit0);
      int int0 = moneyParseContext0.getErrorIndex();
      assertEquals((-1), int0);
      assertEquals(5763, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      moneyParseContext0.getCurrency();
      assertEquals(5763, moneyParseContext0.getIndex());
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      Locale locale0 = new Locale("RA4h@\"7qvZz#.Kh<", "FCEj*WBRAzmx^");
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 855, currencyUnit0);
      moneyParseContext0.getCurrency();
      assertEquals(855, moneyParseContext0.getErrorIndex());
      assertTrue(moneyParseContext0.isFullyParsed());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-472.55137));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(12, "Taiwan", 1, locale0, bigDecimal0, (-1172), currencyUnit0);
      moneyParseContext0.getAmount();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals(1, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 1);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "Taiwan", 0, locale0, bigDecimal0, 2, currencyUnit0);
      moneyParseContext0.getAmount();
      assertEquals(2, moneyParseContext0.getErrorIndex());
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      moneyParseContext0.getAmount();
      assertEquals(0, moneyParseContext0.getErrorIndex());
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-472.55137));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "Taiwan", 1, locale0, bigDecimal0, (-1172), currencyUnit0);
      moneyParseContext0.getAmount();
      assertEquals((-1172), moneyParseContext0.getErrorIndex());
      assertEquals(1, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      BigDecimal bigDecimal0 = new BigDecimal(0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-990), (CharSequence) null, (-990), locale0, bigDecimal0, 77, currencyUnit0);
      MoneyParseContext moneyParseContext1 = moneyParseContext0.createChild();
      assertEquals((-1), moneyParseContext1.getErrorIndex());
      assertEquals((-990), moneyParseContext1.getIndex());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      MoneyParseContext moneyParseContext1 = moneyParseContext0.createChild();
      assertTrue(moneyParseContext1.isFullyParsed());
      assertEquals(0, moneyParseContext1.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal(0.0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "Taiwan", 1776, locale0, bigDecimal0, 1278, currencyUnit0);
      MoneyParseContext moneyParseContext1 = moneyParseContext0.createChild();
      assertEquals(1776, moneyParseContext1.getIndex());
      assertEquals(1278, moneyParseContext1.getErrorIndex());
      assertTrue(moneyParseContext0.isError());
      assertEquals(1776, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(171, (CharSequence) null, 171, locale0, bigDecimal0, 171, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.setText((CharSequence) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Text must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(2649, (CharSequence) null, 2649, locale0, bigDecimal0, 64, currencyUnit0);
      // Undeclared exception!
      try { 
        moneyParseContext0.mergeChild((MoneyParseContext) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MoneyParseContext", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.isFullyParsed();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MoneyParseContext", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.getTextSubstring(5763, 5763);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MoneyParseContext", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CharBuffer charBuffer0 = CharBuffer.allocate(1686);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(685, charBuffer0, 1686, locale0, bigDecimal0, 1686, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.getTextSubstring(1686, (-1051));
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.HeapCharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      moneyParseContext0.getLocale();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals(5763, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      assertTrue(moneyParseContext0.isFullyParsed());
      
      moneyParseContext0.setText("Taiwan");
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.toBigMoney();
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Cannot convert to BigMoney as no currency found
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      Locale locale0 = new Locale("RA4h@\"7qvZz#.Kh<", "FCEj*WBRAzmx^");
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 855, currencyUnit0);
      moneyParseContext0.toBigMoney();
      assertEquals(855, moneyParseContext0.getErrorIndex());
      assertTrue(moneyParseContext0.isFullyParsed());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 22, locale0, (BigDecimal) null, 30, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isComplete();
      assertFalse(boolean0);
      assertEquals(30, moneyParseContext0.getErrorIndex());
      assertEquals(22, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isComplete();
      assertTrue(boolean0);
      assertTrue(moneyParseContext0.isFullyParsed());
      assertEquals(0, moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-1374.11854808));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(2, "Taiwan", (-3511), locale0, bigDecimal0, 0, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isComplete();
      assertEquals((-3511), moneyParseContext0.getIndex());
      assertFalse(boolean0);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-835), charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isFullyParsed();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 22, locale0, (BigDecimal) null, 30, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isFullyParsed();
      assertEquals(30, moneyParseContext0.getErrorIndex());
      assertFalse(boolean0);
      assertEquals(22, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-1374.11854808));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isError();
      assertEquals(2, moneyParseContext0.getIndex());
      assertEquals(2, moneyParseContext0.getErrorIndex());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, currencyUnit0);
      boolean boolean0 = moneyParseContext0.isError();
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertFalse(boolean0);
      assertEquals(5763, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-1374.11854808));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0);
      moneyParseContext0.setErrorIndex((-3511));
      assertEquals((-3511), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 0, 0);
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, charBuffer0, 22, locale0, (BigDecimal) null, 30, currencyUnit0);
      int int0 = moneyParseContext0.getErrorIndex();
      assertEquals(22, moneyParseContext0.getIndex());
      assertEquals(30, int0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-1374.11854808));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0);
      // Undeclared exception!
      try { 
        moneyParseContext0.getTextSubstring(881, 134);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Locale locale0 = Locale.FRANCE;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-2177), (CharSequence) null, (-2177), locale0, bigDecimal0, (-2177), (CurrencyUnit) null);
      ParsePosition parsePosition0 = moneyParseContext0.toParsePosition();
      assertEquals("java.text.ParsePosition[index=-2177,errorIndex=-1]", parsePosition0.toString());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-1374.11854808));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0);
      moneyParseContext0.getCurrency();
      assertEquals(2, moneyParseContext0.getErrorIndex());
      assertEquals(2, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.getTextLength();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MoneyParseContext", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, (CurrencyUnit) null);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      
      moneyParseContext0.setError();
      assertEquals(5763, moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(2591, "Canada", 5763, locale0, bigDecimal0, 772, currencyUnit0);
      int int0 = moneyParseContext0.getIndex();
      assertEquals(5763, int0);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      Locale locale0 = Locale.ITALIAN;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(670, (CharSequence) null, 670, locale0, bigDecimal0, 670, currencyUnit0);
      moneyParseContext0.setCurrency(currencyUnit0);
      // Undeclared exception!
      try { 
        moneyParseContext0.toBigMoney();
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Cannot convert to BigMoney as no amount found
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      Locale locale0 = Locale.CHINESE;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(956, (CharSequence) null, 956, locale0, bigDecimal0, 956, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.mergeChild(moneyParseContext0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Text must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5763, (CharSequence) null, 5763, locale0, bigDecimal0, 5763, currencyUnit0);
      moneyParseContext0.setAmount(bigDecimal0);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertEquals(5763, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      BigDecimal bigDecimal0 = new BigDecimal((-1374.11854808));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0);
      moneyParseContext0.getAmount();
      assertEquals(2, moneyParseContext0.getIndex());
      assertEquals(2, moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-2177), (CharSequence) null, (-2177), (Locale) null, bigDecimal0, (-2177), (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        moneyParseContext0.setLocale((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }
}
