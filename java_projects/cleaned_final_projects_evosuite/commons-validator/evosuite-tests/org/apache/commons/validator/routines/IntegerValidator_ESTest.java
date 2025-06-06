

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
import java.util.Locale;
import org.apache.commons.validator.routines.IntegerValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockDateFormat;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntegerValidator_ESTest extends IntegerValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      boolean boolean0 = integerValidator0.isInRange1((Integer) 1, 1, (-855));
      assertTrue(integerValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, integerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      Locale locale0 = Locale.TAIWAN;
      Integer integer0 = integerValidator0.validate3("xF0kV4gD7PJX9J", "xF0kV4gD7PJX9J", locale0);
      assertEquals(0, (int)integer0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      Locale locale0 = Locale.US;
      Integer integer0 = integerValidator0.validate3((String) null, (String) null, locale0);
      assertNull(integer0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      Integer integer0 = integerValidator0.validate2("0", locale0);
      assertNotNull(integer0);
      assertTrue(integerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      Locale locale0 = Locale.GERMANY;
      Integer integer0 = integerValidator0.validate2("9", locale0);
      assertNotNull(integer0);
      assertEquals(9, (int)integer0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Locale locale0 = Locale.GERMAN;
      integerValidator0.validate2("jz'YeX0UKq0+,9i9N", locale0);
      assertEquals(0, integerValidator0.getFormatType());
      assertTrue(integerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      Integer integer0 = integerValidator0.validate1("Z0Omz", "Z0Omz");
      assertEquals(0, (int)integer0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(false, (-927));
      Integer integer0 = integerValidator0.validate1("2JQ7|2R m%", "");
      assertNotNull(integer0);
      assertEquals(2, (int)integer0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      integerValidator0.validate1("", "");
      assertEquals(0, integerValidator0.getFormatType());
      assertTrue(integerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Integer integer0 = integerValidator0.validate0("0");
      assertNotNull(integer0);
      assertTrue(integerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      Integer integer0 = integerValidator0.validate0("");
      assertNull(integer0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      boolean boolean0 = integerValidator0.minValue1((Integer) integerValidator0.STANDARD_FORMAT, 0);
      assertTrue(integerValidator0.isStrict());
      assertTrue(boolean0);
      assertEquals(0, integerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      boolean boolean0 = integerValidator0.maxValue1((Integer) integerValidator0.PERCENT_FORMAT, 0);
      assertFalse(boolean0);
      assertTrue(integerValidator0.isStrict());
      assertEquals(0, integerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Locale locale0 = Locale.TAIWAN;
      // Undeclared exception!
      try { 
        integerValidator0.validate3("org.apache.commons.validator.routines.IntegerValidator", "org.apache.commons.validator.routines.IntegerValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.IntegerValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      // Undeclared exception!
      try { 
        integerValidator0.validate1("`WUV*_<,j", "`WUV*_<,j");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"`WUV*_<,j\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      // Undeclared exception!
      try { 
        integerValidator0.minValue1((Integer) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.IntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(false, (-539));
      // Undeclared exception!
      try { 
        integerValidator0.maxValue1((Integer) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.IntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      // Undeclared exception!
      try { 
        integerValidator0.isInRange1((Integer) null, (-3461), (-3461));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.IntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(true, 589);
      boolean boolean0 = integerValidator0.maxValue0(3113, 3113);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(false, (-539));
      boolean boolean0 = integerValidator0.minValue0((-539), 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(false, 0);
      boolean boolean0 = integerValidator0.isInRange0(2, 1, 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(true, 589);
      boolean boolean0 = integerValidator0.isInRange0(0, (-1660), 174);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      DateFormat dateFormat0 = MockDateFormat.getDateInstance(2);
      Object object0 = integerValidator0.processParsedValue(integerValidator0.STANDARD_FORMAT, dateFormat0);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      boolean boolean0 = integerValidator0.maxValue0(0, (-3911));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      boolean boolean0 = integerValidator0.minValue0(0, (-3978));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Integer integer0 = new Integer(0);
      boolean boolean0 = integerValidator0.isInRange1(integer0, 0, 0);
      assertTrue(boolean0);
      assertTrue(integerValidator0.isStrict());
      assertEquals(0, integerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Locale locale0 = Locale.CHINESE;
      Integer integer0 = integerValidator0.validate2("-7", locale0);
      assertEquals((-7), (int)integer0);
      assertTrue(integerValidator0.isStrict());
      assertNotNull(integer0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(true, 589);
      boolean boolean0 = integerValidator0.minValue1((Integer) integerValidator0.PERCENT_FORMAT, 3113);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(false, 1000);
      Integer integer0 = integerValidator0.validate0("4M");
      assertNotNull(integer0);
      assertEquals(4, (int)integer0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(true, (-1148));
      boolean boolean0 = integerValidator0.maxValue1((Integer) integerValidator0.STANDARD_FORMAT, 646);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      IntegerValidator integerValidator0 = new IntegerValidator(false, 1000);
      Locale locale0 = Locale.CANADA_FRENCH;
      Integer integer0 = integerValidator0.validate3("4M", "", locale0);
      assertNotNull(integer0);
      assertEquals(4, (int)integer0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.getInstance();
      boolean boolean0 = integerValidator0.isInRange0((-3978), 201, 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      IntegerValidator integerValidator0 = IntegerValidator.IntegerValidator1();
      Integer integer0 = integerValidator0.validate1("-7", "");
      assertEquals((-7), (int)integer0);
      assertTrue(integerValidator0.isStrict());
      assertNotNull(integer0);
  }
}
