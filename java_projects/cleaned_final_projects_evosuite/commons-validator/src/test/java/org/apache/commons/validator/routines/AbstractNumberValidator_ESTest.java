

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
import java.math.BigInteger;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Locale;
import org.apache.commons.validator.routines.BigIntegerValidator;
import org.apache.commons.validator.routines.ByteValidator;
import org.apache.commons.validator.routines.CurrencyValidator;
import org.apache.commons.validator.routines.DoubleValidator;
import org.apache.commons.validator.routines.FloatValidator;
import org.apache.commons.validator.routines.LongValidator;
import org.apache.commons.validator.routines.PercentValidator;
import org.apache.commons.validator.routines.ShortValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AbstractNumberValidator_ESTest extends AbstractNumberValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DecimalFormat decimalFormat0 = (DecimalFormat)NumberFormat.getPercentInstance();
      decimalFormat0.setMultiplier(1083);
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      floatValidator0.determineScale(decimalFormat0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)1;
      BigInteger bigInteger0 = new BigInteger(byteArray0);
      shortValidator0.isInRange(bigInteger0, 0, (byte)1);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      currencyValidator0.maxValue(0, 0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      doubleValidator0.minValue(2, 1);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      Locale locale0 = Locale.GERMANY;
      currencyValidator0.parse("[#", "", locale0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Locale locale0 = Locale.forLanguageTag("R\"p");
      byteValidator0.isValid3("R\"p", "R\"p", locale0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      bigIntegerValidator0.isAllowFractions();
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      floatValidator0.getFormatType();
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, 2);
      floatValidator0.getFormatType();
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      Locale locale0 = Locale.CANADA_FRENCH;
      // Undeclared exception!
      try { 
        percentValidator0.parse("N b,", "N b,", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"N b,\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Locale locale0 = Locale.ITALY;
      // Undeclared exception!
      try { 
        byteValidator0.isValid3("e -#>Q(~<6O7,ugs,h,", "e -#>Q(~<6O7,ugs,h,", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"e -#>Q(~<6O7,ugs,h,\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.FRANCE;
      // Undeclared exception!
      try { 
        shortValidator0.getFormat0("1.b'-X0Oo{+", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"1.b'-X0Oo{+\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      Locale locale0 = Locale.KOREAN;
      // Undeclared exception!
      try { 
        percentValidator0.getFormat("org.apache.commons.validator.routines.AbstractNumberValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractNumberValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      // Undeclared exception!
      try { 
        floatValidator0.determineScale((NumberFormat) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractNumberValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      longValidator0.maxValue(2, 1);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      longValidator0.maxValue(0, 2);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      shortValidator0.minValue(0, 2);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      shortValidator0.minValue(2, 1);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.minValue((Number) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractNumberValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      doubleValidator0.isAllowFractions();
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      shortValidator0.isValid2("z", (Locale) null);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      percentValidator0.validate1("G0", "");
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      currencyValidator0.getFormat1((Locale) null);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CurrencyValidator currencyValidator0 = (CurrencyValidator)CurrencyValidator.getInstance();
      Locale locale0 = new Locale("");
      currencyValidator0.getFormat0("", locale0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DecimalFormat decimalFormat0 = (DecimalFormat)NumberFormat.getPercentInstance();
      decimalFormat0.setMultiplier(1000);
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      floatValidator0.determineScale(decimalFormat0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      NumberFormat numberFormat0 = NumberFormat.getCurrencyInstance();
      floatValidator0.determineScale(numberFormat0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DecimalFormat decimalFormat0 = new DecimalFormat();
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      floatValidator0.determineScale(decimalFormat0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      NumberFormat numberFormat0 = NumberFormat.getIntegerInstance();
      floatValidator0.determineScale(numberFormat0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      bigIntegerValidator0.determineScale((NumberFormat) null);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, 1);
      NumberFormat numberFormat0 = NumberFormat.getPercentInstance();
      longValidator0.determineScale(numberFormat0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      NumberFormat numberFormat0 = NumberFormat.getPercentInstance();
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      floatValidator0.determineScale(numberFormat0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = new BigIntegerValidator(true, 2);
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      bigIntegerValidator0.getFormat0((String) null, locale0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.FRANCE;
      shortValidator0.isValid2("", locale0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      doubleValidator0.validate1((String) null, "");
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      currencyValidator0.maxValue(0, 1);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CurrencyValidator currencyValidator0 = CurrencyValidator.CurrencyValidator1();
      currencyValidator0.maxValue(2, 1);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      // Undeclared exception!
      try { 
        floatValidator0.maxValue((Number) null, (Number) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractNumberValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      doubleValidator0.minValue(0, 1);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      BigInteger bigInteger0 = BigInteger.ZERO;
      floatValidator0.minValue(bigInteger0, bigInteger0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      byte[] byteArray0 = new byte[1];
      BigInteger bigInteger0 = new BigInteger(byteArray0);
      shortValidator0.isInRange(bigInteger0, 0, (byte)1);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      shortValidator0.isInRange(2, 1, 1);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = BigInteger.ZERO;
      // Undeclared exception!
      try { 
        bigIntegerValidator0.isInRange(bigInteger0, bigInteger0, (Number) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractNumberValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte) (-14);
      BigInteger bigInteger0 = new BigInteger(byteArray0);
      shortValidator0.isInRange(bigInteger0, 0, (byte) (-14));
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      floatValidator0.isValid1("m", "m");
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      Locale locale0 = Locale.PRC;
      floatValidator0.isValid3("G0", "G0", locale0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, (short) (-1));
      floatValidator0.getFormatType();
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      Locale locale0 = Locale.PRC;
      DecimalFormat decimalFormat0 = (DecimalFormat)floatValidator0.getFormat("", locale0);
      assertEquals(1, decimalFormat0.getMinimumIntegerDigits());
  }
}
