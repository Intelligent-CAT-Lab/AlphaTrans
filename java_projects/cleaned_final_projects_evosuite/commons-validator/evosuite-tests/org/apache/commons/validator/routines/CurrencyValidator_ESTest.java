

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



package org.apache.commons.validator.routines;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.MessageFormat;
import java.text.NumberFormat;
import java.text.SimpleDateFormat;
import java.util.Locale;
import org.apache.commons.validator.routines.BigDecimalValidator;
import org.apache.commons.validator.routines.CurrencyValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockDateFormat;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CurrencyValidator_ESTest extends CurrencyValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      Locale locale0 = Locale.GERMAN;
      currencyValidator0.validate3("UBw 5\"oCwhV8K3-JW\b", (String) null, locale0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      MessageFormat messageFormat0 = new MessageFormat("3CHw9");
      // Undeclared exception!
      try { 
        currencyValidator0.parse("3CHw9", messageFormat0);
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // Character array is missing \"e\" notation exponential mark.
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      CurrencyValidator currencyValidator0 = new CurrencyValidator(false, true);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      CurrencyValidator currencyValidator0 = (CurrencyValidator)CurrencyValidator.getInstance();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      DecimalFormat decimalFormat0 = (DecimalFormat)currencyValidator0.getFormat((String) null, locale0);
      currencyValidator0.parse("", decimalFormat0);
      assertEquals("#,##0.00", decimalFormat0.toPattern());
      assertEquals("-", decimalFormat0.getNegativePrefix());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      CurrencyValidator currencyValidator0 = (CurrencyValidator)CurrencyValidator.getInstance();
      SimpleDateFormat simpleDateFormat0 = (SimpleDateFormat)MockDateFormat.getTimeInstance(0);
      Object object0 = currencyValidator0.parse("yY+YG#PF8*Bv", simpleDateFormat0);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = CurrencyValidator.getInstance();
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate1("org.apache.commons.validator.routines.AbstractFormatValidator", "V<6&!V:T6v_pX]BTv@");
      assertNull(bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      CurrencyValidator currencyValidator0 = (CurrencyValidator)CurrencyValidator.getInstance();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      DecimalFormat decimalFormat0 = (DecimalFormat)NumberFormat.getIntegerInstance(locale0);
      BigDecimal bigDecimal0 = (BigDecimal)currencyValidator0.parse("1", decimalFormat0);
      assertEquals((short)1, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      NumberFormat numberFormat0 = NumberFormat.getIntegerInstance();
      // Undeclared exception!
      try { 
        currencyValidator0.parse((String) null, numberFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }
}
