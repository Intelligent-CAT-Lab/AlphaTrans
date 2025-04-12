

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
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import org.apache.commons.validator.routines.ByteValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ByteValidator_ESTest extends ByteValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Byte byte0 = byteValidator0.validate0("127");
      assertNotNull(byte0);
      assertEquals((byte)127, (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      boolean boolean0 = byteValidator0.isInRange0((byte) (-84), (byte) (-84), (byte) (-84));
      assertTrue(byteValidator0.isStrict());
      assertEquals(0, byteValidator0.getFormatType());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Locale locale0 = Locale.CHINA;
      Byte byte0 = byteValidator0.validate3("80?ImsgFZlJ9", "80?ImsgFZlJ9", locale0);
      assertTrue(byteValidator0.isStrict());
      assertNotNull(byte0);
      assertEquals(0, byteValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-1677));
      Locale locale0 = Locale.TAIWAN;
      Byte byte0 = byteValidator0.validate3("1", "", locale0);
      assertNotNull(byte0);
      assertEquals((byte)1, (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-3687));
      Locale locale0 = Locale.CHINA;
      Byte byte0 = byteValidator0.validate3("-1<qtb=o|", "", locale0);
      assertEquals((byte) (-1), (byte)byte0);
      assertNotNull(byte0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Locale locale0 = Locale.ITALY;
      ByteValidator byteValidator0 = new ByteValidator(false, (-2665));
      Byte byte0 = byteValidator0.validate2("0tdXImsg\"Zp", locale0);
      assertEquals((byte)0, (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-1677));
      Locale locale0 = Locale.TAIWAN;
      Byte byte0 = byteValidator0.validate2("1", locale0);
      assertNotNull(byte0);
      assertEquals((byte)1, (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      byteValidator0.validate2("org.apache.commons.validator.routines.ByteValidator", locale0);
      assertEquals(0, byteValidator0.getFormatType());
      assertTrue(byteValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Byte byte0 = byteValidator0.validate1("hXtgcg9W`W0}", "hXtgcg9W`W0}");
      assertEquals(0, byteValidator0.getFormatType());
      assertNotNull(byte0);
      assertTrue(byteValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Byte byte0 = byteValidator0.validate1(" 7", (String) null);
      assertEquals((byte)7, (byte)byte0);
      assertNotNull(byte0);
      assertTrue(byteValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Byte byte0 = byteValidator0.validate1("ylUG[hc |a", "ylUG[hc |a");
      assertNull(byte0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-20));
      Byte byte0 = byteValidator0.validate0("0?f,`I");
      assertEquals((byte)0, (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Byte byte0 = new Byte((byte) (-90));
      boolean boolean0 = byteValidator0.isInRange1(byte0, (byte) (-90), (byte) (-9));
      assertTrue(byteValidator0.isStrict());
      assertEquals(0, byteValidator0.getFormatType());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Byte byte0 = new Byte((byte)104);
      boolean boolean0 = byteValidator0.isInRange1(byte0, (byte)1, (byte)0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      // Undeclared exception!
      try { 
        byteValidator0.validate3("org.apache.commons.validator.routines.AbstractNumberValidator", "org.apache.commons.validator.routines.AbstractNumberValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractNumberValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      // Undeclared exception!
      try { 
        byteValidator0.validate1("hRM ;v/%p;yL", "hRM ;v/%p;yL");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unquoted special character ';' in pattern \"hRM ;v/%p;yL\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      // Undeclared exception!
      try { 
        byteValidator0.minValue1((Byte) null, (byte)29);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ByteValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      // Undeclared exception!
      try { 
        byteValidator0.maxValue1((Byte) null, (byte)27);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ByteValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      boolean boolean0 = byteValidator0.maxValue0((byte) (-65), (byte) (-65));
      assertEquals(0, byteValidator0.getFormatType());
      assertTrue(byteValidator0.isStrict());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      boolean boolean0 = byteValidator0.maxValue0((byte)1, (byte) (-20));
      assertTrue(byteValidator0.isStrict());
      assertEquals(0, byteValidator0.getFormatType());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(true, 3901);
      boolean boolean0 = byteValidator0.minValue0((byte) (-4), (byte) (-4));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      boolean boolean0 = byteValidator0.minValue0((byte)0, (byte)56);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-937));
      Byte byte0 = byteValidator0.validate0("97E9et");
      assertNull(byte0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-957));
      Byte byte0 = byteValidator0.validate0("-150yqtz-!7");
      assertNull(byte0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Locale locale0 = Locale.CHINA;
      DecimalFormatSymbols decimalFormatSymbols0 = new DecimalFormatSymbols(locale0);
      DecimalFormat decimalFormat0 = new DecimalFormat("802IsgFZlJ9", decimalFormatSymbols0);
      Object object0 = byteValidator0.processParsedValue(locale0, decimalFormat0);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Byte byte0 = new Byte((byte) (-1));
      boolean boolean0 = byteValidator0.maxValue1(byte0, (byte)43);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Byte byte0 = new Byte((byte) (-1));
      boolean boolean0 = byteValidator0.minValue1(byte0, (byte)78);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      boolean boolean0 = byteValidator0.isInRange0((byte)1, (byte)1, (byte)0);
      assertTrue(byteValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, byteValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      boolean boolean0 = byteValidator0.isInRange0((byte)0, (byte)1, (byte)0);
      assertTrue(byteValidator0.isStrict());
      assertEquals(0, byteValidator0.getFormatType());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-20));
      Byte byte0 = byteValidator0.validate3("org.apache.commons.validator.routines.AbstractFormatValidator", "i-.", (Locale) null);
      assertNull(byte0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-20));
      Byte byte0 = byteValidator0.validate1("-1<qtb=o|", "");
      assertNotNull(byte0);
      assertEquals((byte) (-1), (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-1677));
      Byte byte0 = new Byte((byte)1);
      boolean boolean0 = byteValidator0.maxValue1(byte0, (byte) (-17));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      // Undeclared exception!
      try { 
        byteValidator0.isInRange1((Byte) null, (byte)0, (byte)0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ByteValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      ByteValidator byteValidator0 = new ByteValidator(false, (-3687));
      Byte byte0 = byteValidator0.validate2("-1<qtb=o|", (Locale) null);
      assertNotNull(byte0);
      assertEquals((byte) (-1), (byte)byte0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.getInstance();
      Byte byte0 = new Byte((byte) (-1));
      boolean boolean0 = byteValidator0.minValue1(byte0, (byte) (-13));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      ByteValidator byteValidator0 = ByteValidator.ByteValidator1();
      Byte byte0 = byteValidator0.validate0("-128");
      assertTrue(byteValidator0.isStrict());
      assertNotNull(byte0);
  }
}
