

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
import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.routines.LongValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongValidator_ESTest extends LongValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      boolean boolean0 = longValidator0.maxValue0(0L, 1436L);
      assertTrue(longValidator0.isStrict());
      assertEquals(0, longValidator0.getFormatType());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      boolean boolean0 = longValidator0.minValue0(2113L, 2113L);
      assertTrue(longValidator0.isStrict());
      assertTrue(boolean0);
      assertEquals(0, longValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Long long0 = new Long(2);
      boolean boolean0 = longValidator0.isInRange1(long0, 1L, 3243L);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Locale locale0 = Locale.CHINESE;
      Long long0 = longValidator0.validate3("htrI]FlHmufbZ0R", "htrI]FlHmufbZ0R", locale0);
      assertNotNull(long0);
      assertTrue(longValidator0.isStrict());
      assertEquals(0, longValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Long long0 = longValidator0.validate3("1", "", (Locale) null);
      assertNotNull(long0);
      assertTrue(longValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      longValidator0.validate3("", "", (Locale) null);
      assertEquals(0, longValidator0.getFormatType());
      assertTrue(longValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Locale locale0 = Locale.ROOT;
      Long long0 = longValidator0.validate2("0", locale0);
      assertEquals(0L, (long)long0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Long long0 = longValidator0.validate2("1", (Locale) null);
      assertNotNull(long0);
      assertTrue(longValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      longValidator0.validate2("", (Locale) null);
      assertEquals(0, longValidator0.getFormatType());
      assertTrue(longValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Long long0 = longValidator0.validate1("\"sAVHn[k5}0N", "\"sAVHn[k5}0N");
      assertEquals(0, longValidator0.getFormatType());
      assertTrue(longValidator0.isStrict());
      assertNotNull(long0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, 2210);
      Long long0 = longValidator0.validate1(".", ".");
      assertNull(long0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, (-640));
      Long long0 = longValidator0.validate0("0");
      assertEquals(0L, (long)long0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Long long0 = longValidator0.validate0("8");
      assertNotNull(long0);
      assertTrue(longValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(true, 0);
      Long long0 = new Long(2);
      boolean boolean0 = longValidator0.minValue1(long0, 0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Long long0 = new Long(0);
      boolean boolean0 = longValidator0.isInRange1(long0, 0, 0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      // Undeclared exception!
      try { 
        longValidator0.validate1("org.apache.commons.validator.routines.LongValidator", "org.apache.commons.validator.routines.LongValidator");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.LongValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      // Undeclared exception!
      try { 
        longValidator0.minValue1((Long) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.LongValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      // Undeclared exception!
      try { 
        longValidator0.maxValue1((Long) null, 2210L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.LongValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, 2210);
      boolean boolean0 = longValidator0.maxValue0((-1957L), (-3115L));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      boolean boolean0 = longValidator0.maxValue0(0L, 0L);
      assertTrue(longValidator0.isStrict());
      assertEquals(0, longValidator0.getFormatType());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      boolean boolean0 = longValidator0.minValue0(0L, 1L);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, 2210);
      boolean boolean0 = longValidator0.isInRange0(1821L, (-1957L), (-1544L));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      boolean boolean0 = longValidator0.isInRange0(1L, 2113L, 31L);
      assertFalse(boolean0);
      assertTrue(longValidator0.isStrict());
      assertEquals(0, longValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Locale locale0 = Locale.CANADA;
      Object object0 = longValidator0.processParsedValue(locale0, (Format) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Long long0 = new Long(0L);
      boolean boolean0 = longValidator0.maxValue1(long0, 0L);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Long long0 = new Long(2);
      boolean boolean0 = longValidator0.isInRange1(long0, 0, 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      boolean boolean0 = longValidator0.isInRange0(1899L, 1L, 1899L);
      assertTrue(longValidator0.isStrict());
      assertTrue(boolean0);
      assertEquals(0, longValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, (-1));
      Locale locale0 = Locale.TAIWAN;
      Long long0 = longValidator0.validate2("-2OPxiA(JC1X", locale0);
      assertEquals((-2L), (long)long0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Long long0 = new Long(2);
      boolean boolean0 = longValidator0.minValue1(long0, 1959L);
      assertFalse(boolean0);
      assertEquals(0, longValidator0.getFormatType());
      assertTrue(longValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, (-2697));
      Long long0 = longValidator0.validate0("bez(\"K");
      assertNull(long0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      // Undeclared exception!
      try { 
        longValidator0.isInRange1((Long) null, 1926L, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.LongValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.LongValidator1();
      Locale locale0 = Locale.CANADA_FRENCH;
      // Undeclared exception!
      try { 
        longValidator0.validate3(".CEhuN|Kc?8.]wYfeV", ".CEhuN|Kc?8.]wYfeV", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \".CEhuN|Kc?8.]wYfeV\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      LongValidator longValidator0 = new LongValidator(false, (-2697));
      Long long0 = longValidator0.validate1("1I{}iN5uj", "");
      assertEquals(1L, (long)long0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      LongValidator longValidator0 = LongValidator.getInstance();
      Long long0 = new Long(1);
      boolean boolean0 = longValidator0.maxValue1(long0, (-5388L));
      assertFalse(boolean0);
  }
}
