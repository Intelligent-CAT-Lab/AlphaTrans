

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
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.Format;
import java.text.NumberFormat;
import java.util.Locale;
import org.apache.commons.validator.routines.BigDecimalValidator;
import org.apache.commons.validator.routines.PercentValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PercentValidator_ESTest extends PercentValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      NumberFormat numberFormat0 = NumberFormat.getInstance();
      // Undeclared exception!
      try { 
        percentValidator0.parse("0.01", numberFormat0);
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // Character array is missing \"e\" notation exponential mark.
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      // Undeclared exception!
      try { 
        percentValidator0.parse("c+@4i%ard^t|[b^E`", (Format) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractFormatValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      PercentValidator percentValidator0 = new PercentValidator(true);
      DecimalFormat decimalFormat0 = (DecimalFormat)NumberFormat.getPercentInstance();
      percentValidator0.parse("0", decimalFormat0);
      assertEquals(1, decimalFormat0.getMultiplier());
      assertEquals("#,##0", decimalFormat0.toPattern());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      Locale locale0 = Locale.GERMAN;
      NumberFormat numberFormat0 = NumberFormat.getIntegerInstance(locale0);
      percentValidator0.parse("", numberFormat0);
      assertTrue(percentValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      DateFormat dateFormat0 = DateFormat.getTimeInstance();
      percentValidator0.parse("*nbPg@/Af7", dateFormat0);
      assertTrue(percentValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      percentValidator0.validate3("(k9w,_vk/}-OK*8XX+j", "%z#~wbJQp*eO\"|1", (Locale) null);
      assertTrue(percentValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      PercentValidator percentValidator0 = PercentValidator.PercentValidator1();
      Locale locale0 = Locale.GERMAN;
      NumberFormat numberFormat0 = NumberFormat.getIntegerInstance(locale0);
      percentValidator0.parse("0.01", numberFormat0);
      assertTrue(percentValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = PercentValidator.getInstance();
      assertTrue(bigDecimalValidator0.isAllowFractions());
  }
}
