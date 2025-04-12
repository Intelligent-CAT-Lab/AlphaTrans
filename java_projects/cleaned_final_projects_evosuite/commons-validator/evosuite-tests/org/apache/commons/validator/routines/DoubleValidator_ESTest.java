

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
import org.apache.commons.validator.routines.DoubleValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockDateFormat;
import org.evosuite.runtime.mock.java.text.MockSimpleDateFormat;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DoubleValidator_ESTest extends DoubleValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.maxValue0(0.0, 0.0);
      assertEquals(0, doubleValidator0.getFormatType());
      assertTrue(boolean0);
      assertTrue(doubleValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.isInRange0(1, 1, 1);
      assertTrue(boolean0);
      assertEquals(0, doubleValidator0.getFormatType());
      assertTrue(doubleValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DoubleValidator doubleValidator0 = new DoubleValidator(false, 2143154043);
      Locale locale0 = new Locale("-NBXjFQf60;`31{", "-NBXjFQf60;`31{", "-NBXjFQf60;`31{");
      Double double0 = doubleValidator0.validate3("-NBXjFQf60;`31{", "-NBXjFQf60;`31{", locale0);
      assertEquals(0.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Locale locale0 = Locale.ENGLISH;
      Double double0 = doubleValidator0.validate3("8", "", locale0);
      assertEquals(8.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      Locale locale0 = Locale.ITALY;
      Double double0 = doubleValidator0.validate3("-1.073.741.824", "", locale0);
      assertNotNull(double0);
      assertTrue(doubleValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Locale locale0 = Locale.JAPAN;
      Double double0 = doubleValidator0.validate2("5", locale0);
      assertEquals(5.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      doubleValidator0.validate1("MkQ0}", "MkQ0}");
      assertEquals(0, doubleValidator0.getFormatType());
      assertTrue(doubleValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Double double0 = doubleValidator0.validate1("Nu1", "Nu");
      assertEquals(1.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      doubleValidator0.validate1("", "");
      assertTrue(doubleValidator0.isStrict());
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Double double0 = doubleValidator0.validate0("0");
      assertEquals(0.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DoubleValidator doubleValidator0 = new DoubleValidator(true, 2888);
      Double double0 = doubleValidator0.validate0("2");
      assertEquals(2.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      doubleValidator0.validate0("");
      assertEquals(0, doubleValidator0.getFormatType());
      assertTrue(doubleValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DoubleValidator doubleValidator0 = new DoubleValidator(false, 0);
      Double double0 = new Double(2);
      boolean boolean0 = doubleValidator0.minValue1(double0, 0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      Double double0 = new Double((-1521.473492029));
      boolean boolean0 = doubleValidator0.minValue1(double0, 1.0);
      assertTrue(doubleValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      Double double0 = new Double(0.0);
      boolean boolean0 = doubleValidator0.maxValue1(double0, 3324.960294223781);
      assertTrue(boolean0);
      assertTrue(doubleValidator0.isStrict());
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      Double double0 = new Double(2);
      boolean boolean0 = doubleValidator0.maxValue1(double0, 0);
      assertTrue(doubleValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      Locale locale0 = Locale.ENGLISH;
      // Undeclared exception!
      try { 
        doubleValidator0.validate3("org.apache.commons.validator.routines.AbstractNumberValidator", "org.apache.commons.validator.routines.AbstractNumberValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Multiple decimal separators in pattern \"org.apache.commons.validator.routines.AbstractNumberValidator\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      // Undeclared exception!
      try { 
        doubleValidator0.validate1("'~<pJHYE0", "'~<pJHYE0");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Malformed pattern \"'~<pJHYE0\"
         //
         verifyException("java.text.DecimalFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      Locale locale0 = Locale.JAPAN;
      DateFormat dateFormat0 = MockDateFormat.getTimeInstance(2, locale0);
      // Undeclared exception!
      try { 
        doubleValidator0.processParsedValue((Object) null, dateFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DoubleValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      // Undeclared exception!
      try { 
        doubleValidator0.processParsedValue(doubleValidator0, mockSimpleDateFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class org.apache.commons.validator.routines.DoubleValidator cannot be cast to class java.lang.Number (org.apache.commons.validator.routines.DoubleValidator is in unnamed module of loader org.evosuite.instrumentation.InstrumentingClassLoader @13005f4d; java.lang.Number is in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.validator.routines.DoubleValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.isInRange0(864.5, 307.834243566, 0.0);
      assertFalse(boolean0);
      assertTrue(doubleValidator0.isStrict());
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.isInRange0(0.0, 0.0, 213.570476998);
      assertTrue(boolean0);
      assertTrue(doubleValidator0.isStrict());
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      DateFormat dateFormat0 = DateFormat.getInstance();
      Object object0 = doubleValidator0.processParsedValue(doubleValidator0.PERCENT_FORMAT, dateFormat0);
      Object object1 = doubleValidator0.processParsedValue(object0, dateFormat0);
      assertEquals(2.0, object1);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.maxValue0(213.570476998, 0.0);
      assertEquals(0, doubleValidator0.getFormatType());
      assertFalse(boolean0);
      assertTrue(doubleValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      boolean boolean0 = doubleValidator0.minValue0(0.0, 0.0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.minValue0(0, 2);
      assertTrue(doubleValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Double double0 = new Double(1);
      boolean boolean0 = doubleValidator0.isInRange1(double0, 1, 2);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Double double0 = new Double(1991.6069853998);
      boolean boolean0 = doubleValidator0.isInRange1(double0, 882.9135857012346, 2);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.DoubleValidator1();
      boolean boolean0 = doubleValidator0.isInRange0(0.0, 864.5, 0.0);
      assertTrue(doubleValidator0.isStrict());
      assertFalse(boolean0);
      assertEquals(0, doubleValidator0.getFormatType());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Locale locale0 = Locale.PRC;
      Double double0 = doubleValidator0.validate2("d@J}4=M@>*+7^", locale0);
      // Undeclared exception!
      try { 
        doubleValidator0.minValue1(double0, 1403.955);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DoubleValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Double double0 = doubleValidator0.validate1("-6", (String) null);
      assertEquals((-6.0), (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      DoubleValidator doubleValidator0 = new DoubleValidator(false, 0);
      // Undeclared exception!
      try { 
        doubleValidator0.maxValue1((Double) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DoubleValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Locale locale0 = Locale.GERMAN;
      Double double0 = doubleValidator0.validate3("", ".qEt'ma|$:@_&m-F}G", locale0);
      assertNull(double0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Locale locale0 = Locale.KOREA;
      Double double0 = doubleValidator0.validate2("0", locale0);
      assertEquals(0.0, (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      Double double0 = doubleValidator0.validate0("-6");
      assertEquals((-6.0), (double)double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      DoubleValidator doubleValidator0 = DoubleValidator.getInstance();
      // Undeclared exception!
      try { 
        doubleValidator0.isInRange1((Double) null, 500.7975, 2);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DoubleValidator", e);
      }
  }
}
