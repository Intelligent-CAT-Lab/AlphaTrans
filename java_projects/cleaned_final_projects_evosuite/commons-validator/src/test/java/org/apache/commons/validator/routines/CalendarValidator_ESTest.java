

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
import java.text.DateFormatSymbols;
import java.text.Format;
import java.text.NumberFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Locale;
import java.util.SimpleTimeZone;
import java.util.TimeZone;
import org.apache.commons.validator.routines.CalendarValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockSimpleDateFormat;
import org.evosuite.runtime.mock.java.util.MockCalendar;
import org.evosuite.runtime.mock.java.util.MockGregorianCalendar;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CalendarValidator_ESTest extends CalendarValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.GERMAN;
      DateFormatSymbols dateFormatSymbols0 = DateFormatSymbols.getInstance(locale0);
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat("", dateFormatSymbols0);
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      calendarValidator0.validate7("", "|P9xdTEk,+sJA/c6YA", locale0, timeZone0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.TRADITIONAL_CHINESE;
      Calendar calendar0 = calendarValidator0.validate7("}", "}", locale0, (TimeZone) null);
      assertEquals("org.evosuite.runtime.mock.java.util.MockGregorianCalendar[time=?,areFieldsSet=false,areAllFieldsSet=false,lenient=false,zone=sun.util.calendar.ZoneInfo[id=\"GMT\",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=?,YEAR=?,MONTH=?,WEEK_OF_YEAR=?,WEEK_OF_MONTH=?,DAY_OF_MONTH=?,DAY_OF_YEAR=?,DAY_OF_WEEK=?,DAY_OF_WEEK_IN_MONTH=?,AM_PM=?,HOUR=?,HOUR_OF_DAY=?,MINUTE=?,SECOND=?,MILLISECOND=?,ZONE_OFFSET=?,DST_OFFSET=?]", calendar0.toString());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      calendarValidator0.validate6("PS9c#WE( zPpK A", "", locale0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Calendar calendar0 = calendarValidator0.validate5("i<[*sO{ mQ\"-3eN`", (Locale) null, (TimeZone) null);
      assertNull(calendar0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.JAPAN;
      calendarValidator0.validate4("Q`", locale0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      TimeZone timeZone0 = TimeZone.getTimeZone("");
      calendarValidator0.validate3("org.apache.commons.validator.routines.AbstractCalendarValidator", "", timeZone0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(true, 0);
      Calendar calendar0 = calendarValidator0.validate2("", "W>Y=2w#|*A@L{C2aq");
      assertNull(calendar0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Calendar calendar0 = calendarValidator0.validate1("", (TimeZone) null);
      assertNull(calendar0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-2998), (-2998), (-1163));
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone((-96), "");
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(simpleTimeZone0);
      int int0 = calendarValidator0.compareYears(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Calendar calendar0 = MockCalendar.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 0, 0, 0, 4661, 0);
      int int0 = calendarValidator0.compareYears(mockGregorianCalendar0, calendar0);
      assertTrue(calendarValidator0.isStrict());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-1115), (-1115), 0);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(1, 1, 1, 853, (-1115), 1);
      int int0 = calendarValidator0.compareWeeks(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 1, (-605));
      Calendar calendar0 = MockCalendar.getInstance();
      int int0 = calendarValidator0.compareWeeks(mockGregorianCalendar0, calendar0);
      assertEquals((-1), int0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2864, 1, 1, 856, 856);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(1, (-56), 0);
      int int0 = calendarValidator0.compareQuarters1(mockGregorianCalendar0, mockGregorianCalendar1, 1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(2437, 2465, (-1));
      int int0 = calendarValidator0.compareQuarters1(mockGregorianCalendar0, mockGregorianCalendar1, (-1));
      assertTrue(calendarValidator0.isStrict());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2932, 2932, 2932, 2932, (-1085), 4);
      Locale locale0 = Locale.US;
      Calendar calendar0 = MockCalendar.getInstance(locale0);
      int int0 = calendarValidator0.compareQuarters0(mockGregorianCalendar0, calendar0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-1491), (-1491), 5, 5, 5);
      Calendar calendar0 = MockCalendar.getInstance();
      int int0 = calendarValidator0.compareQuarters0(mockGregorianCalendar0, calendar0);
      assertEquals((-1), int0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      calendarValidator0.compareMonths(mockGregorianCalendar0, mockGregorianCalendar0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(1, (-1548), 0, 3, 3, 3);
      Locale locale0 = Locale.JAPAN;
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(locale0);
      int int0 = calendarValidator0.compareMonths(mockGregorianCalendar1, mockGregorianCalendar0);
      assertEquals(1, int0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(629, 629, 0, 5, (-2039), (-2615));
      Locale locale0 = Locale.CANADA_FRENCH;
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(locale0);
      int int0 = calendarValidator0.compareMonths(mockGregorianCalendar0, mockGregorianCalendar1);
      assertTrue(calendarValidator0.isStrict());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.KOREA;
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(locale0);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(1, 2, (-2369), 1, 2851, 747);
      int int0 = calendarValidator0.compareDates(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals(1, int0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone((-251), "");
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(simpleTimeZone0);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar((-3558), 1, 1599, 1, 3);
      int int0 = calendarValidator0.compareDates(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals((-1), int0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.US;
      // Undeclared exception!
      try { 
        calendarValidator0.validate6("k", "DMId<wL~9(hzt7V!", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'I'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.validate3("Invalid field: ", "Invalid field: ", (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'I'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.validate2("po", "po");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'p'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(true, 1074);
      // Undeclared exception!
      try { 
        calendarValidator0.validate0("2l<e<l} 6");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 1074
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.processParsedValue(calendarValidator0, (Format) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.CalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      NumberFormat numberFormat0 = NumberFormat.getNumberInstance();
      // Undeclared exception!
      try { 
        calendarValidator0.processParsedValue((Object) null, numberFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.text.DecimalFormat cannot be cast to class java.text.DateFormat (java.text.DecimalFormat and java.text.DateFormat are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.validator.routines.CalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      // Undeclared exception!
      try { 
        calendarValidator0.compareYears((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      // Undeclared exception!
      try { 
        calendarValidator0.compareWeeks((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.compareQuarters1((Calendar) null, (Calendar) null, (-80));
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
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(1292, 10, 1147);
      mockGregorianCalendar0.set(0, 1292);
      // Undeclared exception!
      try { 
        calendarValidator0.compareQuarters1(mockGregorianCalendar0, mockGregorianCalendar0, 1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid era
         //
         verifyException("java.util.GregorianCalendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.GERMAN;
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(locale0);
      CalendarValidator.adjustToTimeZone(mockGregorianCalendar0, (TimeZone) null);
      // Undeclared exception!
      try { 
        calendarValidator0.compareQuarters0(mockGregorianCalendar0, mockGregorianCalendar0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.GregorianCalendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(629, 629, 0, 5, (-2039), 0);
      mockGregorianCalendar0.set(0, 5);
      // Undeclared exception!
      try { 
        calendarValidator0.compareMonths(mockGregorianCalendar0, mockGregorianCalendar0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid era
         //
         verifyException("java.util.GregorianCalendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.compareDates((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      // Undeclared exception!
      try { 
        CalendarValidator.adjustToTimeZone((Calendar) null, timeZone0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.CalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeZone timeZone0 = TimeZone.getTimeZone("2_X9wB");
      CalendarValidator.adjustToTimeZone(mockGregorianCalendar0, timeZone0);
      assertEquals("org.evosuite.runtime.mock.java.util.MockGregorianCalendar[time=1392409281320,areFieldsSet=false,areAllFieldsSet=false,lenient=true,zone=sun.util.calendar.ZoneInfo[id=\"GMT\",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2014,MONTH=1,WEEK_OF_YEAR=7,WEEK_OF_MONTH=3,DAY_OF_MONTH=14,DAY_OF_YEAR=45,DAY_OF_WEEK=6,DAY_OF_WEEK_IN_MONTH=2,AM_PM=1,HOUR=8,HOUR_OF_DAY=20,MINUTE=21,SECOND=21,MILLISECOND=320,ZONE_OFFSET=0,DST_OFFSET=0]", mockGregorianCalendar0.toString());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 1, (-605));
      calendarValidator0.compareWeeks(mockGregorianCalendar0, mockGregorianCalendar0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(false, 2305);
      Locale locale0 = Locale.ROOT;
      TimeZone timeZone0 = TimeZone.getTimeZone("org.apache.commons.validator.routines.AbstractCalendarValidator");
      // Undeclared exception!
      try { 
        calendarValidator0.validate5("org.apache.commons.validator.routines.AbstractCalendarValidator", locale0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 2305
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar((-2998), (-2998), (-1163));
      int int0 = calendarValidator0.compareYears(mockGregorianCalendar0, mockGregorianCalendar0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone((-251), "");
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(simpleTimeZone0);
      calendarValidator0.compareDates(mockGregorianCalendar0, mockGregorianCalendar0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Calendar calendar0 = calendarValidator0.validate2(".96", ".96");
      assertFalse(calendar0.isLenient());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.GERMAN;
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(locale0);
      calendarValidator0.compareQuarters0(mockGregorianCalendar0, mockGregorianCalendar0);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(false, 13);
      Locale locale0 = Locale.CHINA;
      // Undeclared exception!
      try { 
        calendarValidator0.validate4("6'+3X-48#?$L", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 13
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      calendarValidator0.validate0("uLBUHe[ wN");
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.compareMonths((Calendar) null, (Calendar) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(1292, 10, 1147);
      calendarValidator0.compareQuarters1(mockGregorianCalendar0, mockGregorianCalendar0, 1);
      assertTrue(calendarValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Calendar calendar0 = calendarValidator0.validate6("],", "],", (Locale) null);
      assertFalse(calendar0.isLenient());
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Calendar calendar0 = calendarValidator0.validate3("?", "?", (TimeZone) null);
      assertFalse(calendar0.isLenient());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(true, 2540);
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        calendarValidator0.validate1("r", timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 2540
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.FRENCH;
      TimeZone timeZone0 = TimeZone.getTimeZone("");
      // Undeclared exception!
      try { 
        calendarValidator0.validate7("5W].KF(ZY&=>5fv\"\",", "5W].KF(ZY&=>5fv\"\",", locale0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'f'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }
}
