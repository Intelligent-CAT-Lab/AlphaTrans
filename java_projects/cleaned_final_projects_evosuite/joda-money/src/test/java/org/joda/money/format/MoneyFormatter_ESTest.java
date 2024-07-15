
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
import java.io.CharArrayWriter;
import java.io.PipedWriter;
import java.io.Writer;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.CharBuffer;
import java.util.Locale;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.evosuite.runtime.mock.java.io.MockPrintWriter;
import org.joda.money.BigMoney;
import org.joda.money.BigMoneyProvider;
import org.joda.money.CurrencyUnit;
import org.joda.money.Money;
import org.joda.money.format.AmountPrinterParser;
import org.joda.money.format.LiteralPrinterParser;
import org.joda.money.format.MoneyAmountStyle;
import org.joda.money.format.MoneyFormatter;
import org.joda.money.format.MoneyParseContext;
import org.joda.money.format.MoneyParser;
import org.joda.money.format.MoneyPrinter;
import org.joda.money.format.MultiPrinterParser;
import org.joda.money.format.SignedPrinterParser;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MoneyFormatter_ESTest extends MoneyFormatter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[8];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(345, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CharBuffer charBuffer0 = CharBuffer.allocate(64);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney(charBuffer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Unparsed text found at index 0: \u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Locale locale0 = Locale.ROOT;
      MoneyParser[] moneyParserArray0 = new MoneyParser[7];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[6];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = null;
      try {
        moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Printers and parsers must match
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Parsing did not find both currency and amount: ");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[1] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[2] = (MoneyPrinter) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, (-3667));
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("Money amount '");
      moneyFormatter0.printIO(mockPrintWriter0, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Locale locale0 = Locale.JAPANESE;
      MoneyParser[] moneyParserArray0 = new MoneyParser[7];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Parsing did not find both currency and amount: ");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[1] = (MoneyPrinter) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(30, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      Writer writer0 = Writer.nullWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(writer0, true);
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      moneyFormatter0.print1(mockPrintWriter0, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      MoneyFormatter.checkNotNull("00", "00");
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser(")");
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[7];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1585), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      String string0 = moneyFormatter0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Parsing did not find both currency and amount: ");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[1] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[2] = (MoneyPrinter) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, (-3667));
      String string0 = moneyFormatter0.print0(bigMoney0);
      assertEquals("Parsing did not find both currency and amount: Parsing did not find both currency and amount: Parsing did not find both currency and amount: ", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Locale locale0 = Locale.KOREAN;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(2041, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.ofMinor(currencyUnit0, (-795L));
      String string0 = moneyFormatter0.print0(money0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Locale locale0 = Locale.CHINA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Cannot convert using a negative conversion multiplier");
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[9];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(3531, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001:org.joda.money.format.LiteralPrinterParser@0000000001", 0);
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Parsing did not find both currency and amount: ");
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      moneyParserArray0[1] = (MoneyParser) literalPrinterParser0;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      moneyParserArray0[2] = (MoneyParser) multiPrinterParser0;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("Parsing did not find both currency and amount: ", 0);
      assertEquals(47, moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Locale locale0 = Locale.JAPANESE;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      AmountPrinterParser amountPrinterParser0 = new AmountPrinterParser((MoneyAmountStyle) null);
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      moneyPrinterArray0[0] = (MoneyPrinter) amountPrinterParser0;
      moneyPrinterArray0[1] = (MoneyPrinter) amountPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(274, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      boolean boolean0 = moneyFormatter0.isPrinter();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Locale locale0 = Locale.PRC;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(535, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      boolean boolean0 = moneyFormatter0.isParser();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Locale locale0 = Locale.PRC;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MoneyParser[] moneyParserArray0 = new MoneyParser[10];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(535, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      boolean boolean0 = moneyFormatter0.isParser();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1805, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = moneyFormatter0.getPrinterParser();
      assertSame(multiPrinterParser0, multiPrinterParser1);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-3557), locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.withLocale((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, (MoneyParser[]) null);
      Locale locale0 = Locale.ROOT;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(525, locale0, (MoneyParser[]) null, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(3282, locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      MockPrintStream mockPrintStream0 = new MockPrintStream("/N:#WZU4w,}}ag");
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-1L));
      // Undeclared exception!
      try { 
        moneyFormatter0.printIO(mockPrintStream0, bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[7];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CharBuffer charBuffer0 = CharBuffer.allocate(360);
      // Undeclared exception!
      try { 
        moneyFormatter0.printIO(charBuffer0, (BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Parsing did not find both currency and amount: ");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[1] = (MoneyPrinter) literalPrinterParser0;
      moneyPrinterArray0[2] = (MoneyPrinter) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      PipedWriter pipedWriter0 = new PipedWriter();
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 0, roundingMode0);
      // Undeclared exception!
      try { 
        moneyFormatter0.print1(pipedWriter0, bigMoney0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Pipe not connected
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(347, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      char[] charArray0 = new char[0];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      // Undeclared exception!
      try { 
        moneyFormatter0.print1(charBuffer0, (BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      moneyPrinterArray0[0] = (MoneyPrinter) multiPrinterParser0;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1585), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      moneyPrinterArray0[1] = (MoneyPrinter) signedPrinterParser0;
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      // Undeclared exception!
      try { 
        moneyFormatter0.print0(bigMoney0);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[8];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(67, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      moneyPrinterArray0[0] = (MoneyPrinter) signedPrinterParser0;
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 67, 3696);
      // Undeclared exception!
      try { 
        moneyFormatter0.print0(bigMoney0);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Locale locale0 = Locale.CANADA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[5];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1510), locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.ofMinor(currencyUnit0, (-1510));
      // Undeclared exception!
      try { 
        moneyFormatter0.print0(money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Locale locale0 = Locale.US;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1545), locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.print0((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Locale locale0 = Locale.CHINESE;
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(44, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      moneyParserArray0[0] = (MoneyParser) signedPrinterParser0;
      MoneyAmountStyle moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_SPACE;
      AmountPrinterParser amountPrinterParser0 = new AmountPrinterParser(moneyAmountStyle0);
      moneyParserArray0[1] = (MoneyParser) amountPrinterParser0;
      // Undeclared exception!
      try { 
        moneyFormatter0.parseMoney("0Z0");
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(15, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseMoney("^tB>YZKnrW_8bt+}=P");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Locale locale0 = Locale.CHINA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[9];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-491), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseMoney((CharSequence) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Text must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney("");
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // MoneyFomatter has not been configured to be able to parse
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Locale locale0 = Locale.GERMAN;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, (MoneyParser[]) null);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(45, locale0, (MoneyParser[]) null, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney("MoneyFormatter whenNegative must not be null");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Locale locale0 = Locale.ENGLISH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(362, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney((CharSequence) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Text must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1585), locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.isPrinter();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      // Undeclared exception!
      try { 
        MoneyFormatter.checkNotNull((Object) null, "00");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // 00
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Locale locale0 = Locale.US;
      MoneyFormatter moneyFormatter0 = null;
      try {
        moneyFormatter0 = new MoneyFormatter((-248), locale0, (MoneyParser[]) null, (MoneyPrinter[]) null, (MultiPrinterParser) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // PrinterParser must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.KOREAN;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((byte)0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("", (byte)0);
      assertFalse(moneyParseContext0.isError());
      assertEquals(0, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parse("Parsing did not find both currency and amount: ", 0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // MoneyFomatter has not been configured to be able to parse
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Locale locale0 = new Locale("Mt0K");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-701), locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parse("Mt0K", 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Locale locale0 = Locale.JAPAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Parsing did not find both currency and amount: ");
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      moneyParserArray0[1] = (MoneyParser) literalPrinterParser0;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      moneyParserArray0[2] = (MoneyParser) multiPrinterParser0;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney("Parsing did not find both currency and amount: ");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Text could not be parsed at index 47: Parsing did not find both currency and amount: 
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      Locale locale0 = Locale.ENGLISH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney("");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Parsing did not find both currency and amount: 
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[9];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      Writer writer0 = Writer.nullWriter();
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, 988);
      // Undeclared exception!
      try { 
        moneyFormatter0.printIO(writer0, bigMoney0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // MoneyFomatter has not been configured to be able to print
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(64, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.isParser();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[8];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(345, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CharArrayWriter charArrayWriter0 = new CharArrayWriter();
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 345);
      // Undeclared exception!
      try { 
        moneyFormatter0.print1(charArrayWriter0, bigMoney0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // MoneyFomatter has not been configured to be able to print
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Locale locale0 = Locale.ENGLISH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[9];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(347, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseMoney("");
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // MoneyFomatter has not been configured to be able to parse
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[8];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(345, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parse("i!o&%?P-X>ow", 345);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
         //
         // Invalid start index: 345
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1), locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parse("T8", (-1));
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
         //
         // Invalid start index: -1
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[7];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      CharBuffer charBuffer0 = CharBuffer.allocate(360);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney(charBuffer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Unparsed text found at index 0: \u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000...
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser(")");
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[7];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-1585), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parseMoney("org.joda.money.format.LiteralPrinterParser@0000000001");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Text could not be parsed at index 0: org.joda.money.format.LiteralPrinterParser@0000000001
         //
         verifyException("org.joda.money.format.MoneyFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = null;
      try {
        moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Printers and parsers must match
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[18];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      // Undeclared exception!
      try { 
        moneyFormatter0.parse((CharSequence) null, (-2593));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Text must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.JAPANESE;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      String string0 = moneyFormatter0.toString();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[9];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      Locale locale1 = moneyFormatter0.getLocale();
      assertEquals("deu", locale1.getISO3Language());
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyFormatter moneyFormatter1 = moneyFormatter0.withLocale(locale0);
      assertNotSame(moneyFormatter1, moneyFormatter0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[7];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.CANADA;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 360);
      // Undeclared exception!
      try { 
        moneyFormatter0.print0(bigMoney0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // MoneyFomatter has not been configured to be able to print
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[6];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      boolean boolean0 = moneyFormatter0.isPrinter();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      Locale locale0 = Locale.FRENCH;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      moneyParserArray0[0] = (MoneyParser) signedPrinterParser0;
      // Undeclared exception!
      try { 
        moneyFormatter0.parseBigMoney("T8");
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }
}
