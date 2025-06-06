

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
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.util.Locale;
import org.apache.commons.validator.routines.BigIntegerValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BigIntegerValidator_ESTest extends BigIntegerValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = BigInteger.TEN;
      boolean boolean0 = bigIntegerValidator0.maxValue(bigInteger0, 13L);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = BigInteger.TEN;
      boolean boolean0 = bigIntegerValidator0.minValue(bigInteger0, (long) 2);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = BigInteger.ZERO;
      boolean boolean0 = bigIntegerValidator0.isInRange(bigInteger0, 0L, 2192L);
      assertEquals(0, bigIntegerValidator0.getFormatType());
      assertTrue(boolean0);
      assertTrue(bigIntegerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      bigIntegerValidator0.validate3("+", "+", (Locale) null);
      assertTrue(bigIntegerValidator0.isStrict());
      assertEquals(0, bigIntegerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      bigIntegerValidator0.validate3("0", "0", (Locale) null);
      assertTrue(bigIntegerValidator0.isStrict());
      assertEquals(0, bigIntegerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      Locale locale0 = Locale.CHINA;
      BigInteger bigInteger0 = bigIntegerValidator0.validate3("5", (String) null, locale0);
      assertEquals((byte)5, bigInteger0.byteValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = bigIntegerValidator0.validate2("0", (Locale) null);
      assertTrue(bigIntegerValidator0.isStrict());
      assertNotNull(bigInteger0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      Locale locale0 = Locale.ENGLISH;
      BigInteger bigInteger0 = bigIntegerValidator0.validate2("6", locale0);
      assertEquals((short)6, bigInteger0.shortValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      bigIntegerValidator0.validate1("", "");
      assertEquals(0, bigIntegerValidator0.getFormatType());
      assertTrue(bigIntegerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = new BigIntegerValidator(true, 0);
      BigInteger bigInteger0 = bigIntegerValidator0.validate1("cxD0gTp~T@%]V7", "cxD0gTp~T@%]V7");
      assertEquals((byte)0, bigInteger0.byteValue());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = bigIntegerValidator0.validate1("3", "");
      assertNotNull(bigInteger0);
      assertTrue(bigIntegerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = bigIntegerValidator0.validate0("0");
      assertNotNull(bigInteger0);
      assertTrue(bigIntegerValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = new BigIntegerValidator(false, (-2052));
      BigInteger bigInteger0 = bigIntegerValidator0.validate0("8");
      assertEquals((byte)8, bigInteger0.byteValue());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      DecimalFormat decimalFormat0 = (DecimalFormat)bigIntegerValidator0.getFormat1((Locale) null);
      BigInteger bigInteger0 = BigInteger.ZERO;
      bigIntegerValidator0.processParsedValue(bigInteger0, decimalFormat0);
      assertTrue(bigIntegerValidator0.isStrict());
      assertEquals("#,##0.###", decimalFormat0.toLocalizedPattern());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.validate3("org.apache.commons.validator.routines.AbstractFormatValidator", "org.apache.commons.validator.routines.AbstractFormatValidator", (Locale) null);
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
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      DateFormat dateFormat0 = DateFormat.getInstance();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.processParsedValue((Object) null, dateFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigIntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      DateFormat dateFormat0 = DateFormat.getTimeInstance(2);
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.processParsedValue(object0, dateFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.Object cannot be cast to class java.lang.Number (java.lang.Object and java.lang.Number are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.validator.routines.BigIntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.minValue((BigInteger) null, (long) 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigIntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.maxValue((BigInteger) null, (-3278L));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigIntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.isInRange((BigInteger) null, (long) 0, (long) 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigIntegerValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      BigInteger bigInteger0 = BigInteger.TWO;
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      boolean boolean0 = bigIntegerValidator0.maxValue(bigInteger0, 2L);
      assertTrue(boolean0);
      assertTrue(bigIntegerValidator0.isStrict());
      assertEquals(0, bigIntegerValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = BigInteger.TEN;
      boolean boolean0 = bigIntegerValidator0.maxValue(bigInteger0, (long) 2);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = BigInteger.ZERO;
      boolean boolean0 = bigIntegerValidator0.minValue(bigInteger0, 0L);
      assertEquals(0, bigIntegerValidator0.getFormatType());
      assertTrue(bigIntegerValidator0.isStrict());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = BigInteger.ONE;
      boolean boolean0 = bigIntegerValidator0.minValue(bigInteger0, (long) 2);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = BigInteger.ZERO;
      boolean boolean0 = bigIntegerValidator0.isInRange(bigInteger0, (long) 0, (long) 0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = new BigIntegerValidator(true, 1513);
      BigInteger bigInteger0 = BigInteger.ZERO;
      boolean boolean0 = bigIntegerValidator0.isInRange(bigInteger0, 1L, 0L);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = bigIntegerValidator0.validate0("org.apache.commons.validator.routines.AbstractFormatValidator");
      assertNull(bigInteger0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      Locale locale0 = Locale.FRANCE;
      BigInteger bigInteger0 = bigIntegerValidator0.validate2("-FaZuq>?^+529", locale0);
      assertNull(bigInteger0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      BigInteger bigInteger0 = bigIntegerValidator0.validate3("-FaZuq>?^+529", "FaZuq>?^+", (Locale) null);
      assertEquals((short) (-529), bigInteger0.shortValue());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.BigIntegerValidator1();
      BigInteger bigInteger0 = BigInteger.ZERO;
      boolean boolean0 = bigIntegerValidator0.isInRange(bigInteger0, (-1L), (-1L));
      assertTrue(bigIntegerValidator0.isStrict());
      assertEquals(0, bigIntegerValidator0.getFormatType());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      BigIntegerValidator bigIntegerValidator0 = BigIntegerValidator.getInstance();
      // Undeclared exception!
      try { 
        bigIntegerValidator0.validate1("org.apache.commons.validator.routines.BigIntegerValidator", "org.apache.commons.validator.routines.BigIntegerValidator");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.BigIntegerValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }
}
