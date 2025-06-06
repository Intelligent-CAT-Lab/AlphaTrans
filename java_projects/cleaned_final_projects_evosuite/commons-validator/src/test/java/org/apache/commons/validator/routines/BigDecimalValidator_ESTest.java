

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
import java.math.BigInteger;
import java.text.DateFormat;
import java.util.Locale;
import org.apache.commons.validator.routines.BigDecimalValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockDateFormat;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BigDecimalValidator_ESTest extends BigDecimalValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = new BigDecimalValidator(false, 0, false);
      BigDecimal bigDecimal0 = new BigDecimal((double) 1);
      boolean boolean0 = bigDecimalValidator0.maxValue(bigDecimal0, (double) 2);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      boolean boolean0 = bigDecimalValidator0.minValue(bigDecimal0, 0.0);
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertTrue(bigDecimalValidator0.isStrict());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(false);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      boolean boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, (-643.0), (double) 2);
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertFalse(bigDecimalValidator0.isStrict());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      boolean boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, (double) 1, (-1640.0));
      assertTrue(bigDecimalValidator0.isStrict());
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertFalse(boolean0);
      assertTrue(bigDecimalValidator0.isAllowFractions());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(true);
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      bigDecimalValidator0.validate3("uerw0SvYKHsnSW9WTj", "uerw0SvYKHsnSW9WTj", locale0);
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertTrue(bigDecimalValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(false);
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate3("7LFLt2LU", "", (Locale) null);
      assertNotNull(bigDecimal0);
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertEquals((byte)7, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      Locale locale0 = Locale.CHINESE;
      bigDecimalValidator0.validate2("haQYd c~P", locale0);
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertTrue(bigDecimalValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      Locale locale0 = Locale.PRC;
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate2("8", locale0);
      assertEquals((short)8, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = new BigDecimalValidator(false, 0, false);
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate1("", "");
      assertNull(bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = new BigDecimalValidator(false, 0, false);
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate1("9wz0bw~*SW.v3v6JN:[", "");
      assertEquals((byte)9, bigDecimal0.byteValue());
      assertNotNull(bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate0("0");
      assertEquals((byte)0, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate0("8");
      assertEquals((short)8, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      Locale locale0 = Locale.GERMANY;
      // Undeclared exception!
      try { 
        bigDecimalValidator0.validate3("qqs;{&.YB%>}yvPc", "qqs;{&.YB%>}yvPc", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unquoted special character ';' in pattern \"qqs;{&.YB%>}yvPc\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      // Undeclared exception!
      try { 
        bigDecimalValidator0.validate1("nHAV}[5!m=r'VmU.", "nHAV}[5!m=r'VmU.");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"nHAV}[5!m=r'VmU.\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      DateFormat dateFormat0 = MockDateFormat.getDateInstance(2);
      // Undeclared exception!
      try { 
        bigDecimalValidator0.processParsedValue(bigDecimalValidator0, dateFormat0);
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // Character array is missing \"e\" notation exponential mark.
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      DateFormat dateFormat0 = MockDateFormat.getDateInstance(2);
      // Undeclared exception!
      try { 
        bigDecimalValidator0.processParsedValue((Object) null, dateFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      // Undeclared exception!
      try { 
        bigDecimalValidator0.minValue((BigDecimal) null, 387.395468228518);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigDecimalValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = new BigDecimalValidator(false, 0, false);
      // Undeclared exception!
      try { 
        bigDecimalValidator0.maxValue((BigDecimal) null, (-1470.8376603958777));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigDecimalValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      // Undeclared exception!
      try { 
        bigDecimalValidator0.isInRange((BigDecimal) null, (-2228.5200035708503), (-2228.5200035708503));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.BigDecimalValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(false);
      // Undeclared exception!
      try { 
        bigDecimalValidator0.validate1(".2G(N)&,w'", (String) null);
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // Character array is missing \"e\" notation exponential mark.
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = new BigDecimalValidator(false, 0, false);
      BigInteger bigInteger0 = BigInteger.ZERO;
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0);
      boolean boolean0 = bigDecimalValidator0.maxValue(bigDecimal0, (double) 0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      boolean boolean0 = bigDecimalValidator0.maxValue(bigDecimal0, (-3036.19));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      boolean boolean0 = bigDecimalValidator0.minValue(bigDecimal0, 0.0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator1(true);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      boolean boolean0 = bigDecimalValidator0.minValue(bigDecimal0, 4370.090111);
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertFalse(boolean0);
      assertTrue(bigDecimalValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      BigDecimal bigDecimal0 = new BigDecimal((long) 0);
      boolean boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, 0.0, 0.0);
      assertEquals(0, bigDecimalValidator0.getFormatType());
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertTrue(boolean0);
      assertTrue(bigDecimalValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = new BigDecimalValidator(false, 0, false);
      BigInteger bigInteger0 = BigInteger.ZERO;
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0);
      boolean boolean0 = bigDecimalValidator0.isInRange(bigDecimal0, (double) 1, (double) 1);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate0((String) null);
      assertNull(bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      Locale locale0 = new Locale("", ")Ur/p&]fO", "");
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate2("0", locale0);
      assertEquals((byte)0, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.getInstance();
      Locale locale0 = new Locale("", ")Ur/p&]fO", "");
      BigDecimal bigDecimal0 = bigDecimalValidator0.validate3((String) null, "", locale0);
      assertNull(bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      BigDecimalValidator bigDecimalValidator0 = BigDecimalValidator.BigDecimalValidator2();
      bigDecimalValidator0.validate1("d%j}/43h0", "d%j}/43h0");
      assertTrue(bigDecimalValidator0.isAllowFractions());
      assertTrue(bigDecimalValidator0.isStrict());
      assertEquals(0, bigDecimalValidator0.getFormatType());
  }
}
