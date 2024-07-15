
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
import java.nio.ReadOnlyBufferException;
import java.util.Locale;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockFileWriter;
import org.joda.money.BigMoney;
import org.joda.money.CurrencyUnit;
import org.joda.money.format.AmountPrinterParser;
import org.joda.money.format.LiteralPrinterParser;
import org.joda.money.format.MoneyAmountStyle;
import org.joda.money.format.MoneyFormatter;
import org.joda.money.format.MoneyFormatterBuilder;
import org.joda.money.format.MoneyParseContext;
import org.joda.money.format.MoneyParser;
import org.joda.money.format.MoneyPrintContext;
import org.joda.money.format.MoneyPrinter;
import org.joda.money.format.MultiPrinterParser;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MultiPrinterParser_ESTest extends MultiPrinterParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Locale locale0 = new Locale("7<9]ug;4-LO2Sd(ns");
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      MockFileWriter mockFileWriter0 = new MockFileWriter("7<9]ug;4-LO2Sd(ns");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      multiPrinterParser0.print(moneyPrintContext0, mockFileWriter0, (BigMoney) null);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      MoneyAmountStyle moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA;
      AmountPrinterParser amountPrinterParser0 = new AmountPrinterParser(moneyAmountStyle0);
      moneyPrinterArray0[0] = (MoneyPrinter) amountPrinterParser0;
      moneyPrinterArray0[1] = (MoneyPrinter) amountPrinterParser0;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      boolean boolean0 = multiPrinterParser0.isPrinter();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[3];
      MoneyParser[] moneyParserArray0 = new MoneyParser[9];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      boolean boolean0 = multiPrinterParser0.isPrinter();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("");
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      boolean boolean0 = multiPrinterParser0.isParser();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      MoneyParser[] moneyParserArray0 = new MoneyParser[3];
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[7];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      boolean boolean0 = multiPrinterParser0.isParser();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      // Undeclared exception!
      try { 
        multiPrinterParser0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Bx");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "Money iterator must not contain n~ll entriQs");
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      // Undeclared exception!
      try { 
        multiPrinterParser0.print((MoneyPrintContext) null, charBuffer0, (BigMoney) null);
        fail("Expecting exception: ReadOnlyBufferException");
      
      } catch(ReadOnlyBufferException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.CharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[4];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.US;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      MockFile mockFile0 = new MockFile("^23s*N:l2R.#[,)K%'");
      MockFileWriter mockFileWriter0 = new MockFileWriter(mockFile0, true);
      // Undeclared exception!
      try { 
        multiPrinterParser0.print(moneyPrintContext0, mockFileWriter0, (BigMoney) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MultiPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Bx");
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.GERMAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(8, "tRyAM_&cl9t3j", (-10), locale0, bigDecimal0, (-10), currencyUnit0);
      // Undeclared exception!
      try { 
        multiPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[2];
      MoneyAmountStyle moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA;
      AmountPrinterParser amountPrinterParser0 = new AmountPrinterParser(moneyAmountStyle0);
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      moneyParserArray0[0] = (MoneyParser) amountPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(5, "\u00A3", 2304, (Locale) null, bigDecimal0, 2304, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        multiPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser((MoneyPrinter[]) null, (MoneyParser[]) null);
      // Undeclared exception!
      try { 
        multiPrinterParser0.isPrinter();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      // Undeclared exception!
      try { 
        multiPrinterParser0.isParser();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, (MoneyParser[]) null);
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        multiPrinterParser0.appendTo(moneyFormatterBuilder0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MultiPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[5];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      // Undeclared exception!
      try { 
        multiPrinterParser0.appendTo(moneyFormatterBuilder0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("org.joda.money.format.MultiPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[8];
      MoneyParser[] moneyParserArray0 = new MoneyParser[1];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      String string0 = multiPrinterParser0.toString();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Bx");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      moneyParserArray0[1] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      String string0 = multiPrinterParser0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Bx");
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      moneyParserArray0[1] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      String string0 = multiPrinterParser0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Bx");
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      moneyParserArray0[0] = (MoneyParser) literalPrinterParser0;
      moneyParserArray0[1] = (MoneyParser) literalPrinterParser0;
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.FRENCH;
      MoneyFormatter moneyFormatter0 = new MoneyFormatter((-4158), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001", 1);
      multiPrinterParser0.parse(moneyParseContext0);
      assertEquals(1, moneyParseContext0.getErrorIndex());
      assertTrue(moneyParseContext0.isError());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[0];
      MoneyParser[] moneyParserArray0 = new MoneyParser[0];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.US;
      MoneyParser[] moneyParserArray1 = new MoneyParser[2];
      moneyParserArray1[0] = (MoneyParser) multiPrinterParser0;
      moneyParserArray1[1] = (MoneyParser) multiPrinterParser0;
      MultiPrinterParser multiPrinterParser1 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray1);
      MoneyFormatter moneyFormatter0 = new MoneyFormatter(1, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1);
      MoneyParseContext moneyParseContext0 = moneyFormatter0.parse("V$_G", 1);
      assertFalse(moneyParseContext0.isError());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MoneyFormatterBuilder moneyFormatterBuilder0 = new MoneyFormatterBuilder();
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      multiPrinterParser0.appendTo(moneyFormatterBuilder0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Bx");
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      moneyPrinterArray0[0] = (MoneyPrinter) literalPrinterParser0;
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      String string0 = multiPrinterParser0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      MoneyPrinter[] moneyPrinterArray0 = new MoneyPrinter[1];
      MoneyParser[] moneyParserArray0 = new MoneyParser[2];
      MultiPrinterParser multiPrinterParser0 = new MultiPrinterParser(moneyPrinterArray0, moneyParserArray0);
      Locale locale0 = Locale.GERMAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(8, "tRyAM_&cl9t3j", (-10), locale0, bigDecimal0, (-10), currencyUnit0);
      // Undeclared exception!
      try { 
        multiPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.MultiPrinterParser", e);
      }
  }
}
