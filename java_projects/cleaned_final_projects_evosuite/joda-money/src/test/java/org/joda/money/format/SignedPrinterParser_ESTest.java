
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
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.Locale;
import java.util.PriorityQueue;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.BigMoney;
import org.joda.money.BigMoneyProvider;
import org.joda.money.CurrencyUnit;
import org.joda.money.format.AmountPrinterParser;
import org.joda.money.format.LiteralPrinterParser;
import org.joda.money.format.MoneyAmountStyle;
import org.joda.money.format.MoneyFormatter;
import org.joda.money.format.MoneyParseContext;
import org.joda.money.format.MoneyParser;
import org.joda.money.format.MoneyPrintContext;
import org.joda.money.format.MoneyPrinter;
import org.joda.money.format.MultiPrinterParser;
import org.joda.money.format.SignedPrinterParser;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SignedPrinterParser_ESTest extends SignedPrinterParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Locale locale0 = Locale.KOREAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[14];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tH&-pPq)pA6s");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1743, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter(11, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter0, moneyFormatter1);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("tH&-pPq)pA6s", 11);
      byte[] byteArray0 = new byte[6];
      byteArray0[0] = (byte) (-1);
      BigInteger bigInteger0 = new BigInteger(byteArray0);
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0);
      moneyParseContext0.setAmount(bigDecimal0);
      signedPrinterParser0.parse(moneyParseContext0);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertFalse(moneyParseContext0.isError());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tH&'pPq)pA6s");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter((-2321), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("h&5'pP)A6s", 2);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter0, moneyFormatter0);
      signedPrinterParser0.parse(moneyParseContext0);
      assertFalse(moneyParseContext0.isError());
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Locale locale0 = Locale.CANADA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[6];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(10, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, (-417));
      signedPrinterParser0.print(moneyPrintContext0, (Appendable) null, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Locale locale0 = Locale.TAIWAN;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(999, locale0, moneyParserArray0, (MoneyPrinter[]) null, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      // Undeclared exception!
      try { 
        signedPrinterParser0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tH&'pPq)pA6s");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1720, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter(2, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter0, moneyFormatter1);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("tH&'pPq)pA6s", 2);
      moneyParseContext0.setIndex((-4962));
      // Undeclared exception!
      try { 
        signedPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Locale locale0 = Locale.GERMANY;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(3, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      MathContext mathContext0 = MathContext.DECIMAL64;
      BigDecimal bigDecimal0 = new BigDecimal((long) (-2042), mathContext0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(3, (CharSequence) null, (-2042), locale0, bigDecimal0, 88, currencyUnit0);
      // Undeclared exception!
      try { 
        signedPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Text must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Locale locale0 = Locale.CANADA_FRENCH;
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      MoneyAmountStyle moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_NO_GROUPING;
      AmountPrinterParser amountPrinterParser0 = new AmountPrinterParser(moneyAmountStyle0);
      moneyParserArray0[0] = (MoneyParser) amountPrinterParser0;
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[6];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(88, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(88, "org.joda.money.format.MoneyPrintContext", 88, locale0, bigDecimal0, (-1081), currencyUnit0);
      // Undeclared exception!
      try { 
        signedPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -49
         //
         verifyException("org.joda.money.format.AmountPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tOH&['pPq)pAhs");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter((-1696), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter1, moneyFormatter0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("eF^~)9H3THVdSR", 2);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      moneyParseContext0.setAmount(bigDecimal0);
      signedPrinterParser0.parse(moneyParseContext0);
      signedPrinterParser0.parse(moneyParseContext0);
      assertEquals((-1), moneyParseContext0.getErrorIndex());
      assertFalse(moneyParseContext0.isError());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tH&'pPq)pA6s");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter((-2321), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter0, moneyFormatter1);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("h&5'pP)A6s", 2);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      moneyParseContext0.setAmount(bigDecimal0);
      signedPrinterParser0.parse(moneyParseContext0);
      assertFalse(moneyParseContext0.isError());
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Locale locale0 = Locale.CANADA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[6];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Money array must not contain null entries");
      MoneyAmountStyle moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_COMMA_NO_GROUPING;
      AmountPrinterParser amountPrinterParser0 = new AmountPrinterParser(moneyAmountStyle0);
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[7];
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      moneyParserArray1[1] = (MoneyParser) literalPrinterParser0;
      moneyParserArray1[2] = (MoneyParser) literalPrinterParser0;
      moneyParserArray1[3] = (MoneyParser) amountPrinterParser0;
      moneyParserArray1[4] = (MoneyParser) literalPrinterParser0;
      moneyParserArray1[5] = (MoneyParser) amountPrinterParser0;
      moneyParserArray1[6] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(10, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("jrtc?4Wx']L{T4", 10);
      signedPrinterParser0.parse(moneyParseContext0);
      assertFalse(moneyParseContext0.isFullyParsed());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tOH&['pPq)pAhs");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter((-1696), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter1, moneyFormatter0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("eF^~)9H3THVdSR", 2);
      // Undeclared exception!
      try { 
        signedPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.SignedPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Locale locale0 = Locale.US;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[8];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("B&OcG@", 1);
      signedPrinterParser0.parse(moneyParseContext0);
      assertFalse(moneyParseContext0.isComplete());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("tH&'pPq)pA6s");
      moneyParserArray1[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter1 = new MoneyFormatter((-2321), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter1, moneyFormatter0, moneyFormatter1);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("h&5'pP)A6s", 2);
      signedPrinterParser0.parse(moneyParseContext0);
      signedPrinterParser0.parse(moneyParseContext0);
      assertFalse(moneyParseContext0.isError());
      assertEquals((-1), moneyParseContext0.getErrorIndex());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Locale locale0 = Locale.US;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[8];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(13, locale0, (MoneyParser[]) null, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      CharArrayWriter charArrayWriter0 = new CharArrayWriter(0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      PriorityQueue<BigMoneyProvider> priorityQueue0 = new PriorityQueue<BigMoneyProvider>();
      BigMoney bigMoney0 = BigMoney.total3(currencyUnit0, priorityQueue0);
      BigMoney bigMoney1 = bigMoney0.plus3((-336L));
      // Undeclared exception!
      try { 
        signedPrinterParser0.print(moneyPrintContext0, charArrayWriter0, bigMoney1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Locale locale0 = Locale.KOREA;
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray1 = new MoneyParser[5];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0);
      SignedPrinterParser signedPrinterParser0 = new SignedPrinterParser(moneyFormatter0, moneyFormatter0, moneyFormatter0);
      String string0 = signedPrinterParser0.toString();
      assertEquals("PositiveZeroNegative(,,)", string0);
  }
}
