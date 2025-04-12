

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
import java.text.NumberFormat;
import java.util.Calendar;
import java.util.Locale;
import java.util.TimeZone;
import org.apache.commons.validator.routines.TimeValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockSimpleDateFormat;
import org.evosuite.runtime.mock.java.util.MockCalendar;
import org.evosuite.runtime.mock.java.util.MockGregorianCalendar;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class TimeValidator_ESTest extends TimeValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      TimeZone timeZone0 = TimeZone.getDefault();
      Locale locale0 = Locale.ROOT;
      timeValidator0.validate7((String) null, "<N\"E", locale0, timeZone0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      Locale locale0 = Locale.US;
      timeValidator0.validate7("^", "^", locale0, (TimeZone) null);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      Locale locale0 = new Locale("315mz9-fwWa");
      timeValidator0.validate6((String) null, "org.apache.commons.validator.routines.AbstractFormatValidator", locale0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      timeValidator0.validate6("1", "1", locale0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.UK;
      TimeZone timeZone0 = TimeZone.getTimeZone("A#&m)");
      Calendar calendar0 = timeValidator0.validate5("A#&m)", locale0, timeZone0);
      assertNull(calendar0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.TAIWAN;
      Calendar calendar0 = timeValidator0.validate4("", locale0);
      assertNull(calendar0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      TimeZone timeZone0 = TimeZone.getDefault();
      timeValidator0.validate3("", "", timeZone0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      timeValidator0.validate3("~", "~", (TimeZone) null);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Calendar calendar0 = timeValidator0.validate2("", "My");
      assertNull(calendar0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      TimeZone timeZone0 = TimeZone.getDefault();
      timeValidator0.validate1("org.apache.commons.validator.routines.TimeValidator", timeZone0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      timeValidator0.validate0("org.apache.commons.validator.routines.AbstractCalendarValidator");
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      MockGregorianCalendar mockGregorianCalendar0 = (MockGregorianCalendar)timeValidator0.processParsedValue((Object) null, mockSimpleDateFormat0);
      assertTrue(mockGregorianCalendar0.isLenient());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Calendar calendar0 = mockSimpleDateFormat0.getCalendar();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, (-5932), 0, 13, 13, 0);
      int int0 = timeValidator0.compareTime(calendar0, mockGregorianCalendar0);
      assertEquals(1, int0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-2722), (-227), (-485), 0, (-485));
      TimeZone timeZone0 = TimeZone.getTimeZone("KSN2O]");
      Calendar calendar0 = MockCalendar.getInstance(timeZone0);
      int int0 = timeValidator0.compareTime(mockGregorianCalendar0, calendar0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(838, 0, 0, 838, 0, 0);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(0, 2, 2, 2, 2);
      int int0 = timeValidator0.compareSeconds(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(13, 13, 13, (-2851), 360);
      Calendar calendar0 = MockCalendar.getInstance();
      int int0 = timeValidator0.compareSeconds(mockGregorianCalendar0, calendar0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.JAPANESE;
      Calendar calendar0 = MockCalendar.getInstance(locale0);
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-92), (-92), (-92));
      int int0 = timeValidator0.compareMinutes(calendar0, mockGregorianCalendar0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 0, 0, 0, 0);
      TimeZone timeZone0 = TimeZone.getTimeZone("");
      Locale locale0 = Locale.GERMANY;
      Calendar calendar0 = MockCalendar.getInstance(timeZone0, locale0);
      int int0 = timeValidator0.compareMinutes(mockGregorianCalendar0, calendar0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2104, (-1594), 3, 0, 1, 1);
      timeValidator0.compareHours(mockGregorianCalendar0, mockGregorianCalendar0);
      assertTrue(timeValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-358), 0, 2104, 0, (-1597), 12);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar();
      int int0 = timeValidator0.compareHours(mockGregorianCalendar0, mockGregorianCalendar1);
      assertTrue(timeValidator0.isStrict());
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Calendar calendar0 = MockCalendar.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, (-533), 2104, (-1597), 14, 13);
      int int0 = timeValidator0.compareHours(mockGregorianCalendar0, calendar0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.CHINESE;
      TimeZone timeZone0 = TimeZone.getTimeZone("{GP;ve");
      // Undeclared exception!
      try { 
        timeValidator0.validate7("{GP;ve", "{GP;ve", locale0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'P'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      // Undeclared exception!
      try { 
        timeValidator0.validate2("org.apache.commons.validator.routines.AbstractCalendarValidator", "org.apache.commons.validator.routines.AbstractCalendarValidator");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'o'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.ITALIAN;
      // Undeclared exception!
      try { 
        timeValidator0.processParsedValue(locale0, (Format) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.TimeValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      NumberFormat numberFormat0 = NumberFormat.getCurrencyInstance();
      // Undeclared exception!
      try { 
        timeValidator0.processParsedValue(locale0, numberFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.text.DecimalFormat cannot be cast to class java.text.DateFormat (java.text.DecimalFormat and java.text.DateFormat are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.validator.routines.TimeValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      // Undeclared exception!
      try { 
        timeValidator0.compareTime((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-961), (-961), (-961), (-961), 3);
      mockGregorianCalendar0.setLenient(false);
      // Undeclared exception!
      try { 
        timeValidator0.compareSeconds(mockGregorianCalendar0, mockGregorianCalendar0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // YEAR
         //
         verifyException("java.util.GregorianCalendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.compareMinutes((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-347), 0, 0, (-347), 0);
      mockGregorianCalendar0.set(0, (-347));
      // Undeclared exception!
      try { 
        timeValidator0.compareMinutes(mockGregorianCalendar0, mockGregorianCalendar0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid era
         //
         verifyException("java.util.GregorianCalendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.validate3("}w84U'QoOKwh", "}w84U'QoOKwh", (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'U'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      // Undeclared exception!
      try { 
        timeValidator0.compareSeconds((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      TimeValidator timeValidator0 = new TimeValidator(false, 818);
      // Undeclared exception!
      try { 
        timeValidator0.validate1("org.apache.commons.validator.routines.AbstractFormatValidator", (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal time style 818
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.JAPANESE;
      Calendar calendar0 = MockCalendar.getInstance(locale0);
      int int0 = timeValidator0.compareMinutes(calendar0, calendar0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Calendar calendar0 = timeValidator0.validate2("/", "/");
      assertEquals(1, calendar0.getMinimalDaysInFirstWeek());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      TimeValidator timeValidator0 = new TimeValidator(true, 1353);
      // Undeclared exception!
      try { 
        timeValidator0.validate4("~uMJ1S_ElQL.%IS", (Locale) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal time style 1353
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-2722), (-227), (-485), 0, (-485));
      int int0 = timeValidator0.compareTime(mockGregorianCalendar0, mockGregorianCalendar0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.US;
      // Undeclared exception!
      try { 
        timeValidator0.validate6("8KqEg)~CrZf2w0$A+#", "8KqEg)~CrZf2w0$A+#", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'q'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-961), (-961), (-961), (-961), 3);
      int int0 = timeValidator0.compareSeconds(mockGregorianCalendar0, mockGregorianCalendar0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      TimeValidator timeValidator0 = new TimeValidator(false, 13);
      Locale locale0 = Locale.ROOT;
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        timeValidator0.validate5("b5M0i3m.Qw=?", locale0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal time style 13
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.compareHours((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      TimeValidator timeValidator0 = new TimeValidator(true, 12);
      // Undeclared exception!
      try { 
        timeValidator0.validate0("org.apache.commons.validator.routines.TimeValidator");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal time style 12
         //
         verifyException("java.text.DateFormat", e);
      }
  }
}
