
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
import java.io.IOException;
import java.io.PipedWriter;
import java.io.StringWriter;
import java.math.BigDecimal;
import java.nio.CharBuffer;
import java.nio.ReadOnlyBufferException;
import java.util.Locale;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFileWriter;
import org.joda.money.BigMoney;
import org.joda.money.BigMoneyProvider;
import org.joda.money.CurrencyUnit;
import org.joda.money.format.LiteralPrinterParser;
import org.joda.money.format.MoneyParseContext;
import org.joda.money.format.MoneyPrintContext;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LiteralPrinterParser_ESTest extends LiteralPrinterParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("qcX");
      Locale locale0 = Locale.ENGLISH;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      StringWriter stringWriter0 = new StringWriter();
      StringBuffer stringBuffer0 = stringWriter0.getBuffer();
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) stringBuffer0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = new BigDecimal((-1.0));
      BigMoney bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 2023);
      // Undeclared exception!
      try { 
        literalPrinterParser0.print(moneyPrintContext0, charBuffer0, bigMoney0);
        fail("Expecting exception: ReadOnlyBufferException");
      
      } catch(ReadOnlyBufferException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.CharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("6u.^/ur.T6TI");
      // Undeclared exception!
      try { 
        literalPrinterParser0.print((MoneyPrintContext) null, (Appendable) null, (BigMoney) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.LiteralPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("oSnvPK\u0000LE,~tEr^;-");
      Locale locale0 = Locale.CANADA_FRENCH;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      PipedWriter pipedWriter0 = new PipedWriter();
      try { 
        literalPrinterParser0.print(moneyPrintContext0, pipedWriter0, (BigMoney) null);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedWriter", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("qQc");
      Locale locale0 = Locale.TAIWAN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-2093064), "qQc", (-2093064), locale0, (BigDecimal) null, (-2093064), currencyUnit0);
      // Undeclared exception!
      try { 
        literalPrinterParser0.parse(moneyParseContext0);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("");
      // Undeclared exception!
      try { 
        literalPrinterParser0.parse((MoneyParseContext) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.format.LiteralPrinterParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      CharBuffer charBuffer0 = CharBuffer.allocate(26);
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(1, charBuffer0, 1, (Locale) null, bigDecimal0, (-121770191), currencyUnit0);
      moneyParseContext0.setIndex((-121770191));
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("nu");
      // Undeclared exception!
      try { 
        literalPrinterParser0.parse(moneyParseContext0);
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
      Locale locale0 = Locale.JAPAN;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(23, "or8.joda.money.format.CiteralPrinterPasr", 23, locale0, bigDecimal0, 23, currencyUnit0);
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("nu");
      literalPrinterParser0.parse(moneyParseContext0);
      assertEquals(23, moneyParseContext0.getErrorIndex());
      assertEquals(23, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("y)aC{f!k~VTS!4 ");
      Locale locale0 = Locale.ROOT;
      BigDecimal bigDecimal0 = new BigDecimal((-1353));
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext((-1), "y)aC{f!k~VTS!4 ", 0, locale0, bigDecimal0, 1336, currencyUnit0);
      literalPrinterParser0.parse(moneyParseContext0);
      assertTrue(moneyParseContext0.isFullyParsed());
      assertEquals(15, moneyParseContext0.getIndex());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("Money '");
      Locale locale0 = Locale.CHINA;
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      MoneyParseContext moneyParseContext0 = new MoneyParseContext(759, "'Money ''", 759, locale0, (BigDecimal) null, 759, currencyUnit0);
      literalPrinterParser0.parse(moneyParseContext0);
      assertFalse(moneyParseContext0.isFullyParsed());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("y)aC{f!k~VTS!4 ");
      Locale locale0 = Locale.ROOT;
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      MockFileWriter mockFileWriter0 = new MockFileWriter("[X[%4k");
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      literalPrinterParser0.print(moneyPrintContext0, mockFileWriter0, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LiteralPrinterParser literalPrinterParser0 = new LiteralPrinterParser("y)aC{f!k~VTS!4 ");
      String string0 = literalPrinterParser0.toString();
      assertEquals("'y)aC{f!k~VTS!4 '", string0);
  }
}
