

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
import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.routines.ShortValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockSimpleDateFormat;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ShortValidator_ESTest extends ShortValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      boolean boolean0 = shortValidator0.minValue0((short) (-2609), (short) (-4336));
      assertTrue(boolean0);
      assertEquals(0, shortValidator0.getFormatType());
      assertTrue(shortValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Short short0 = new Short((short) (-2807));
      boolean boolean0 = shortValidator0.isInRange1(short0, (short)1230, (short)2024);
      assertTrue(shortValidator0.isStrict());
      assertEquals(0, shortValidator0.getFormatType());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.KOREA;
      Short short0 = shortValidator0.validate3("0", (String) null, locale0);
      assertEquals((short)0, (short)short0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.FRENCH;
      Short short0 = shortValidator0.validate3("4", "", locale0);
      assertNotNull(short0);
      assertEquals((short)4, (short)short0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.forLanguageTag("");
      Short short0 = shortValidator0.validate3("", "", locale0);
      assertNull(short0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.KOREA;
      Short short0 = shortValidator0.validate2("0", locale0);
      assertEquals((short)0, (short)short0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ShortValidator shortValidator0 = new ShortValidator(false, 1000);
      Short short0 = shortValidator0.validate2("8B8", (Locale) null);
      assertEquals((short)8, (short)short0);
      assertNotNull(short0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.GERMAN;
      Short short0 = shortValidator0.validate2("org.apache.commons.validator.routines.AbstractNumberValidator", locale0);
      assertNull(short0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      shortValidator0.validate1("p}0G", "p}0G");
      assertTrue(shortValidator0.isStrict());
      assertEquals(0, shortValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Short short0 = shortValidator0.validate1("4", "");
      assertEquals((short)4, (short)short0);
      assertNotNull(short0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Short short0 = shortValidator0.validate0("0");
      assertEquals((short)0, (short)short0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Short short0 = shortValidator0.validate0("4");
      assertEquals((short)4, (short)short0);
      assertNotNull(short0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Short short0 = shortValidator0.validate0("5+7k4BP#f|U&C-gu\u0003");
      assertNull(short0);
      assertEquals(0, shortValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Short short0 = new Short((short) (-3876));
      boolean boolean0 = shortValidator0.minValue1(short0, (short) (-1));
      assertFalse(boolean0);
      assertTrue(shortValidator0.isStrict());
      assertEquals(0, shortValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Locale locale0 = Locale.ITALIAN;
      // Undeclared exception!
      try { 
        shortValidator0.validate3("org.apache.commons.validator.routines.AbstractFormatValidator", "org.apache.commons.validator.routines.AbstractFormatValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractFormatValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      // Undeclared exception!
      try { 
        shortValidator0.validate1("org.apache.commons.validator.routines.AbstractFormatValidator", "org.apache.commons.validator.routines.AbstractFormatValidator");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractFormatValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      // Undeclared exception!
      try { 
        shortValidator0.processParsedValue((Object) null, (Format) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ShortValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      // Undeclared exception!
      try { 
        shortValidator0.processParsedValue(mockSimpleDateFormat0, mockSimpleDateFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class org.evosuite.runtime.mock.java.text.MockSimpleDateFormat cannot be cast to class java.lang.Number (org.evosuite.runtime.mock.java.text.MockSimpleDateFormat is in unnamed module of loader 'app'; java.lang.Number is in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.validator.routines.ShortValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      // Undeclared exception!
      try { 
        shortValidator0.maxValue1((Short) null, (short) (-4720));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ShortValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      // Undeclared exception!
      try { 
        shortValidator0.isInRange1((Short) null, (short)28, (short)1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ShortValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      boolean boolean0 = shortValidator0.maxValue0((short) (-1398), (short)4743);
      assertTrue(shortValidator0.isStrict());
      assertTrue(boolean0);
      assertEquals(0, shortValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      boolean boolean0 = shortValidator0.maxValue0((short)113, (short) (-1615));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      boolean boolean0 = shortValidator0.minValue0((short)100, (short)100);
      assertTrue(boolean0);
      assertTrue(shortValidator0.isStrict());
      assertEquals(0, shortValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      boolean boolean0 = shortValidator0.isInRange0((short)0, (short)0, (short)4417);
      assertTrue(boolean0);
      assertEquals(0, shortValidator0.getFormatType());
      assertTrue(shortValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      boolean boolean0 = shortValidator0.isInRange0((short) (-851), (short)0, (short)0);
      assertEquals(0, shortValidator0.getFormatType());
      assertTrue(shortValidator0.isStrict());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Integer integer0 = new Integer(2147416545);
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Object object0 = shortValidator0.processParsedValue(integer0, mockSimpleDateFormat0);
      assertNull(object0);
      assertEquals(0, shortValidator0.getFormatType());
      assertTrue(shortValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Integer integer0 = Integer.valueOf((-2147416048));
      DateFormat dateFormat0 = DateFormat.getDateTimeInstance();
      Object object0 = shortValidator0.processParsedValue(integer0, dateFormat0);
      assertTrue(shortValidator0.isStrict());
      assertNull(object0);
      assertEquals(0, shortValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Short short0 = new Short((short)1359);
      boolean boolean0 = shortValidator0.maxValue1(short0, (short)1359);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      ShortValidator shortValidator0 = new ShortValidator(false, 1497);
      boolean boolean0 = shortValidator0.minValue0((short) (-828), (short)0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      boolean boolean0 = shortValidator0.isInRange0((short)2239, (short)1, (short) (-227));
      assertEquals(0, shortValidator0.getFormatType());
      assertFalse(boolean0);
      assertTrue(shortValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      ShortValidator shortValidator0 = new ShortValidator(false, (-2381));
      DateFormat dateFormat0 = DateFormat.getDateTimeInstance(2, 1);
      Short short0 = (Short)shortValidator0.processParsedValue(0, dateFormat0);
      assertNotNull(short0);
      
      boolean boolean0 = shortValidator0.maxValue1(short0, (short) (-1));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      ShortValidator shortValidator0 = new ShortValidator(false, (-5750));
      Locale locale0 = Locale.FRENCH;
      Short short0 = shortValidator0.validate2("-1", locale0);
      assertNotNull(short0);
      assertEquals((short) (-1), (short)short0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Short short0 = shortValidator0.validate0("-2,322");
      assertNotNull(short0);
      assertEquals((short) (-2322), (short)short0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Short short0 = new Short((short) (-2807));
      boolean boolean0 = shortValidator0.isInRange1(short0, (short) (-2807), (short) (-2807));
      assertEquals(0, shortValidator0.getFormatType());
      assertTrue(boolean0);
      assertTrue(shortValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Short short0 = shortValidator0.validate1("J\"+(w-=w(V>", "");
      assertNull(short0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.ShortValidator1();
      Short short0 = new Short((short) (-3876));
      boolean boolean0 = shortValidator0.minValue1(short0, (short) (-3876));
      assertTrue(shortValidator0.isStrict());
      assertEquals(0, shortValidator0.getFormatType());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      ShortValidator shortValidator0 = ShortValidator.getInstance();
      Locale locale0 = Locale.CHINESE;
      Short short0 = shortValidator0.validate3("-2,308", "", locale0);
      assertEquals((short) (-2308), (short)short0);
      assertNotNull(short0);
  }
}
