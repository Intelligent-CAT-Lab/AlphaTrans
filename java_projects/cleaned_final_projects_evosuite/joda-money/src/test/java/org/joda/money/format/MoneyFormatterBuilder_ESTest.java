
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
import java.nio.CharBuffer;
import java.util.Locale;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.format.LiteralPrinterParser;
import org.joda.money.format.MoneyAmountStyle;
import org.joda.money.format.MoneyFormatter;
import org.joda.money.format.MoneyFormatterBuilder;
import org.joda.money.format.MoneyParser;
import org.joda.money.format.MoneyPrinter;
import org.joda.money.format.MultiPrinterParser;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MoneyFormatterBuilder_ESTest extends MoneyFormatterBuilder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.PRC;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(2303, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyFormatter moneyFormatter1 = moneyFormatter0.withLocale(locale0);
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendSigned1(moneyFormatter0, moneyFormatter1, moneyFormatter1);
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      Locale locale0 = Locale.KOREAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(3, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyFormatter moneyFormatter1 = moneyFormatter0.withLocale(locale0);
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendSigned0(moneyFormatter1, moneyFormatter0);
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      Locale locale0 = new Locale("N; y", "");
      MoneyFormatter moneyFormatter0 = moneyFormatterBuilder0.toFormatter1(locale0);
      assertNotNull(moneyFormatter0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyAmountStyle moneyAmountStyle0 = MoneyAmountStyle.LOCALIZED_NO_GROUPING;
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendAmount1(moneyAmountStyle0);
      assertSame(moneyFormatterBuilder1, moneyFormatterBuilder0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.appendSigned0((MoneyFormatter) null, (MoneyFormatter) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // MoneyFormatter whenPositive must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      char[] charArray0 = new char[5];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      CharBuffer charBuffer1 = CharBuffer.wrap((CharSequence) charBuffer0);
      charBuffer0.compact();
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.appendLiteral(charBuffer1);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.HeapCharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      Locale locale0 = Locale.ROOT;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1550), locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.append0(moneyFormatter0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MultiPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      Locale locale0 = new Locale("");
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-3822), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.append0(moneyFormatter0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("org.joda.money.format.MultiPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.appendSigned1((MoneyFormatter) null, (MoneyFormatter) null, (MoneyFormatter) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // MoneyFormatter whenPositive must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("org.joda.money.format.SignedPrinterParser");
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.append1(literalPrinterParser0, literalPrinterParser0);
      assertSame(moneyFormatterBuilder1, moneyFormatterBuilder0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.toFormatter1((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      char[] charArray0 = new char[1];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendLiteral(charBuffer0);
      assertSame(moneyFormatterBuilder1, moneyFormatterBuilder0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      char[] charArray0 = new char[0];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendLiteral(charBuffer0);
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendLiteral((CharSequence) null);
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      Locale locale0 = Locale.ROOT;
      MoneyParser[] moneyParserArray0 = new MoneyParser[6];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(690, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.append0(moneyFormatter0);
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.appendAmount1((MoneyAmountStyle) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // MoneyAmountStyle must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencyNumeric3Code();
      assertSame(moneyFormatterBuilder1, moneyFormatterBuilder0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencySymbolLocalized();
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencyNumericCode();
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendAmount0();
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        moneyFormatterBuilder0.append0((MoneyFormatter) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // MoneyFormatter must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencyCode();
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatter moneyFormatter0 = moneyFormatterBuilder0.toFormatter0();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendSigned0(moneyFormatter0, moneyFormatter0);
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyFormatterBuilder moneyFormatterBuilder1 = moneyFormatterBuilder0.appendAmountLocalized();
      assertSame(moneyFormatterBuilder0, moneyFormatterBuilder1);
  }
}
