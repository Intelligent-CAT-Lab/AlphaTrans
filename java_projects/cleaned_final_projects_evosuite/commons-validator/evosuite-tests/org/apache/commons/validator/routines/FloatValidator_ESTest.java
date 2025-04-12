

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
import java.text.DecimalFormat;
import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.routines.FloatValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FloatValidator_ESTest extends FloatValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, 871);
      boolean boolean0 = floatValidator0.isInRange0(871, 871, 4479.0F);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      DecimalFormat decimalFormat0 = new DecimalFormat();
      Object object0 = floatValidator0.processParsedValue(0, decimalFormat0);
      assertTrue(floatValidator0.isStrict());
      assertEquals(0.0F, object0);
      assertNotNull(object0);
      assertEquals(0, floatValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      Locale locale0 = Locale.US;
      Float float0 = floatValidator0.validate3("maOo4 0tqozKRq[", "maOo4 0tqozKRq[", locale0);
      assertEquals(0.0F, (float)float0, 0.01F);
      assertNotNull(float0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, (-100));
      Locale locale0 = Locale.JAPAN;
      Float float0 = floatValidator0.validate2("2", locale0);
      assertEquals(2.0F, (float)float0, 0.01F);
      assertNotNull(float0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, 2);
      Locale locale0 = Locale.ITALY;
      Float float0 = floatValidator0.validate2("-141,900%", locale0);
      assertNotNull(float0);
      assertEquals((-1.419F), (float)float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      Float float0 = floatValidator0.validate1("maOo4 0tqozKRq[", "maOo4 0tqozKRq[");
      assertEquals(0.0F, (float)float0, 0.01F);
      assertNotNull(float0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      Float float0 = floatValidator0.validate1("7", "");
      assertNotNull(float0);
      assertEquals(7.0F, (float)float0, 0.01F);
      assertTrue(floatValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, 0);
      Float float0 = floatValidator0.validate1("", "");
      assertNull(float0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, (-1));
      Float float0 = floatValidator0.validate0(",0L");
      assertNotNull(float0);
      assertEquals(0.0F, (float)float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, 0);
      Float float0 = floatValidator0.validate0("3qjX3d<,g");
      assertNotNull(float0);
      assertEquals(3.0F, (float)float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      floatValidator0.validate0("org.apache.commons.validator.routines.AbstractFormatValidator");
      assertTrue(floatValidator0.isStrict());
      assertEquals(0, floatValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      Float float0 = new Float((float) 0);
      boolean boolean0 = floatValidator0.minValue1(float0, 2324.5425F);
      assertTrue(floatValidator0.isStrict());
      assertEquals(0, floatValidator0.getFormatType());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Float float0 = new Float(0.0F);
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      boolean boolean0 = floatValidator0.isInRange1(float0, 0.0F, 0.0F);
      assertEquals(0, floatValidator0.getFormatType());
      assertTrue(boolean0);
      assertTrue(floatValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Float float0 = new Float(0.0F);
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      boolean boolean0 = floatValidator0.isInRange1(float0, (-978.07104F), (-107.714F));
      assertEquals(0, floatValidator0.getFormatType());
      assertTrue(floatValidator0.isStrict());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      Locale locale0 = Locale.FRANCE;
      // Undeclared exception!
      try { 
        floatValidator0.validate3("F'G.", "F'G.", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"F'G.\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      // Undeclared exception!
      try { 
        floatValidator0.validate1("org.apache.commons.validator.routines.AbstractFormatValidator", "org.apache.commons.validator.routines.AbstractFormatValidator");
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
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      // Undeclared exception!
      try { 
        floatValidator0.processParsedValue((Object) null, (Format) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.FloatValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      DecimalFormat decimalFormat0 = new DecimalFormat();
      // Undeclared exception!
      try { 
        floatValidator0.processParsedValue(decimalFormat0, decimalFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.text.DecimalFormat cannot be cast to class java.lang.Number (java.text.DecimalFormat and java.lang.Number are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.validator.routines.FloatValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      // Undeclared exception!
      try { 
        floatValidator0.maxValue1((Float) null, (-711.0F));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.FloatValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, 1737);
      boolean boolean0 = floatValidator0.maxValue0(0.0F, 653.31464F);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, (-1442));
      boolean boolean0 = floatValidator0.maxValue0(0.0F, (-869.225F));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, 1737);
      boolean boolean0 = floatValidator0.minValue0(0.0F, 0.0F);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, (-2069));
      Float float0 = floatValidator0.validate2("0", (Locale) null);
      assertNotNull(float0);
      assertEquals(0.0F, (float)float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, (-198));
      Locale locale0 = Locale.FRANCE;
      Float float0 = floatValidator0.validate3("4[^\"Z_V=", "", locale0);
      assertNotNull(float0);
      assertEquals(4.0F, (float)float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Float float0 = new Float(430.0439F);
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      boolean boolean0 = floatValidator0.maxValue1(float0, 0.0F);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(true, 1737);
      boolean boolean0 = floatValidator0.minValue0((-3946.0972F), (-1.0F));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      boolean boolean0 = floatValidator0.isInRange0(3248, 0.0F, (-1865.69F));
      assertTrue(floatValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, floatValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      boolean boolean0 = floatValidator0.isInRange0((-646.1517F), 914.7F, (-646.1517F));
      assertTrue(floatValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, floatValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      Float float0 = new Float((float) 0);
      boolean boolean0 = floatValidator0.minValue1(float0, (-2085.01F));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, 2);
      Locale locale0 = Locale.ITALY;
      Float float0 = floatValidator0.validate2("K#u*bjc>|A", locale0);
      assertNull(float0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, 2);
      Float float0 = floatValidator0.validate0("-141,900%");
      assertNotNull(float0);
      assertEquals((-1419.0F), (float)float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      FloatValidator floatValidator0 = new FloatValidator(false, 1551);
      Float float0 = floatValidator0.validate1("-6\"6zi#Y1gvA\f1+", "");
      assertEquals((-6.0F), (float)float0, 0.01F);
      assertNotNull(float0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.FloatValidator1();
      Locale locale0 = Locale.GERMAN;
      Float float0 = floatValidator0.validate3("", "<r=", locale0);
      // Undeclared exception!
      try { 
        floatValidator0.isInRange1(float0, 2, (-3031.87F));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.FloatValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      FloatValidator floatValidator0 = FloatValidator.getInstance();
      Float float0 = new Float((float) 0);
      boolean boolean0 = floatValidator0.maxValue1(float0, 0.0F);
      assertTrue(boolean0);
  }
}
