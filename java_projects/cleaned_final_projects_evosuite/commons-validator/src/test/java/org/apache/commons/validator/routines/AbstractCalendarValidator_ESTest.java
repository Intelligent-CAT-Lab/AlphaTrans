

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
import java.text.DateFormatSymbols;
import java.text.Format;
import java.text.MessageFormat;
import java.text.SimpleDateFormat;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;
import java.util.SimpleTimeZone;
import java.util.TimeZone;
import org.apache.commons.validator.routines.CalendarValidator;
import org.apache.commons.validator.routines.DateValidator;
import org.apache.commons.validator.routines.TimeValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockSimpleDateFormat;
import org.evosuite.runtime.mock.java.util.MockCalendar;
import org.evosuite.runtime.mock.java.util.MockGregorianCalendar;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AbstractCalendarValidator_ESTest extends AbstractCalendarValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 0, 0);
      ZonedDateTime zonedDateTime0 = mockGregorianCalendar0.toZonedDateTime();
      GregorianCalendar gregorianCalendar0 = MockGregorianCalendar.from(zonedDateTime0);
      timeValidator0.compareTime(gregorianCalendar0, mockGregorianCalendar0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      Calendar calendar0 = MockCalendar.getInstance(locale0);
      // Undeclared exception!
      try { 
        calendarValidator0.compareTime(calendar0, calendar0, 51);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid field: 51
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Calendar calendar0 = mockSimpleDateFormat0.getCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone((-1437), "F>@");
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(simpleTimeZone0);
      int int0 = timeValidator0.compareTime(calendar0, mockGregorianCalendar0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(981, 3, 3, 3, 1256, 1256);
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat("");
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      Locale locale0 = Locale.ROOT;
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(timeZone0, locale0);
      int int0 = timeValidator0.compareTime(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      Locale locale0 = Locale.PRC;
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(timeZone0, locale0);
      Calendar calendar0 = MockCalendar.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.compare(calendar0, mockGregorianCalendar0, (-3250));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid field: -3250
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(4, "UKGLEv");
      Calendar calendar0 = MockCalendar.getInstance((TimeZone) simpleTimeZone0);
      int int0 = timeValidator0.compare(mockGregorianCalendar0, calendar0, 4);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2, 1, 5135, 3449, 3449);
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      TimeZone timeZone0 = TimeZone.getDefault();
      int int0 = dateValidator0.compareDates(date0, date0, timeZone0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      Calendar calendar0 = MockCalendar.getInstance();
      int int0 = timeValidator0.compare(calendar0, mockGregorianCalendar0, 6);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2, 1, 5135, 3449, 3449);
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      TimeZone timeZone0 = TimeZone.getDefault();
      int int0 = dateValidator0.compareWeeks(date0, date0, timeZone0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, 0);
      Locale locale0 = Locale.JAPANESE;
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(0, "");
      Object object0 = dateValidator0.parse("", "", locale0, simpleTimeZone0);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      TimeZone timeZone0 = TimeZone.getDefault();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.KOREAN;
      MockGregorianCalendar mockGregorianCalendar0 = (MockGregorianCalendar)timeValidator0.parse("\uC624\uC804 12:00", "", locale0, timeZone0);
      assertNotNull(mockGregorianCalendar0);
      assertFalse(mockGregorianCalendar0.isLenient());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(false, 1);
      DateFormatSymbols dateFormatSymbols0 = new DateFormatSymbols();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat("", dateFormatSymbols0);
      String string0 = calendarValidator0.format5((Object) null, mockSimpleDateFormat0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2, 1, 5135, 3449, 3449);
      DateFormat dateFormat0 = DateFormat.getTimeInstance();
      String string0 = dateValidator0.format5(mockGregorianCalendar0, dateFormat0);
      assertEquals("12:00:00 AM", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      DateValidator dateValidator0 = DateValidator.getInstance();
      Locale locale0 = Locale.UK;
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      String string0 = dateValidator0.format4((Object) null, "", locale0, timeZone0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      Locale locale0 = Locale.PRC;
      String string0 = dateValidator0.format3((Object) null, "", locale0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CalendarValidator calendarValidator0 = new CalendarValidator(false, (-2569));
      Locale locale0 = Locale.ITALY;
      DateFormat dateFormat0 = DateFormat.getDateTimeInstance();
      Object object0 = calendarValidator0.processParsedValue(locale0, dateFormat0);
      String string0 = calendarValidator0.format3(object0, "", locale0);
      //  // Unstable assertion: assertEquals("java.util.GregorianCalendar[time=-805541510593,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=sun.util.calendar.ZoneInfo[id=\"GMT\",offset=0,dstSavings=0,useDaylight=false,transitions=0,lastRule=null],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=1944,MONTH=5,WEEK_OF_YEAR=26,WEEK_OF_MONTH=4,DAY_OF_MONTH=22,DAY_OF_YEAR=174,DAY_OF_WEEK=5,DAY_OF_WEEK_IN_MONTH=4,AM_PM=1,HOUR=2,HOUR_OF_DAY=14,MINUTE=28,SECOND=9,MILLISECOND=407,ZONE_OFFSET=0,DST_OFFSET=0]", object0.toString());
      //  // Unstable assertion: assertEquals("22/06/44", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      String string0 = timeValidator0.format1((Object) null, (String) null, (TimeZone) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Calendar calendar0 = mockSimpleDateFormat0.getCalendar();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(3847, "");
      String string0 = calendarValidator0.format1((Object) calendar0, "", (TimeZone) simpleTimeZone0);
      assertEquals("2/14/14", string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      String string0 = timeValidator0.format0((Object) null, timeZone0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(981, 3, 3, 3, 1256, 1256);
      TimeZone timeZone0 = TimeZone.getDefault();
      DateValidator dateValidator0 = new DateValidator(true, 3);
      String string0 = dateValidator0.format0((Object) mockGregorianCalendar0, timeZone0);
      assertEquals("1/1/70", string0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      int int0 = timeValidator0.compareTime(mockGregorianCalendar0, mockGregorianCalendar0, 10);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(2, 1, 5135, 3449, 3449);
      ZoneId zoneId0 = ZoneId.systemDefault();
      TimeZone timeZone0 = TimeZone.getTimeZone(zoneId0);
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(timeZone0);
      int int0 = dateValidator0.compareQuarters(mockGregorianCalendar0, mockGregorianCalendar1, 2);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(11, 11, 11);
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar1, 1779);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.US;
      // Undeclared exception!
      try { 
        calendarValidator0.parse("1Z_Q", "1Z_Q", locale0, (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'Q'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Locale locale0 = Locale.CHINESE;
      CalendarValidator calendarValidator0 = new CalendarValidator(true, 948);
      // Undeclared exception!
      try { 
        calendarValidator0.getFormat1(locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 948
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.TAIWAN;
      // Undeclared exception!
      try { 
        calendarValidator0.getFormat0("org.apache.commons.validator.routines.AbstractCalendarValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'o'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      Locale locale0 = Locale.CANADA_FRENCH;
      // Undeclared exception!
      try { 
        timeValidator0.getFormat("f%,1iAt", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'f'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.TAIWAN;
      // Undeclared exception!
      try { 
        calendarValidator0.format5(locale0, (Format) null);
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
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.US;
      Format format0 = calendarValidator0.getFormat1(locale0);
      // Undeclared exception!
      try { 
        calendarValidator0.format5(format0, format0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Object object0 = new Object();
      MessageFormat messageFormat0 = new MessageFormat("");
      // Undeclared exception!
      try { 
        calendarValidator0.format5(object0, messageFormat0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.Object cannot be cast to class [Ljava.lang.Object; (java.lang.Object and [Ljava.lang.Object; are in module java.base of loader 'bootstrap')
         //
         verifyException("java.text.MessageFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Locale locale0 = Locale.US;
      // Undeclared exception!
      try { 
        calendarValidator0.format3(locale0, "", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.compareTime((Calendar) null, (Calendar) null, 981);
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
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      // Undeclared exception!
      try { 
        calendarValidator0.compareQuarters((Calendar) null, (Calendar) null, (-2445));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.compare((Calendar) null, (Calendar) null, (-14));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.AbstractCalendarValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      mockGregorianCalendar0.set(1013, 1013, 0, 0, 0, 153);
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      mockGregorianCalendar0.setLenient(false);
      // Undeclared exception!
      try { 
        timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 11);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // MONTH
         //
         verifyException("java.util.GregorianCalendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Locale locale0 = Locale.CHINESE;
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      // Undeclared exception!
      try { 
        calendarValidator0.format4(locale0, "", locale0, (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Calendar calendar0 = MockCalendar.getInstance();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(4, 20, (-64));
      int int0 = calendarValidator0.compareQuarters(calendar0, mockGregorianCalendar0, (-832));
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      int int0 = timeValidator0.compareQuarters(mockGregorianCalendar0, mockGregorianCalendar0, 4);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 13);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(1044, "org.apache.commons.validator.routines.AbstractCalendarValidator");
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar(simpleTimeZone0);
      int int0 = timeValidator0.compareSeconds(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 12);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 11);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar((-1616), (-1616), (-1616));
      int int0 = timeValidator0.compareTime(mockGregorianCalendar0, mockGregorianCalendar1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 8);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 7);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      int int0 = calendarValidator0.compareMonths(mockGregorianCalendar0, mockGregorianCalendar0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.TimeValidator1();
      int int0 = timeValidator0.compare(mockGregorianCalendar0, mockGregorianCalendar0, 1);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      MockGregorianCalendar mockGregorianCalendar1 = new MockGregorianCalendar((-376), (-376), (-376), (-376), (-376));
      int int0 = timeValidator0.compare(mockGregorianCalendar1, mockGregorianCalendar0, (-376));
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, (-498));
      boolean boolean0 = dateValidator0.isValid0("c\"u@s|RFy#w0Hc tgK");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      // Undeclared exception!
      try { 
        calendarValidator0.isValid3("##FbpU9j", "##FbpU9j", (Locale) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'b'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, (-498));
      Locale locale0 = Locale.ENGLISH;
      Date date0 = dateValidator0.validate6((String) null, (String) null, locale0);
      assertNull(date0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.ENGLISH;
      String string0 = calendarValidator0.format2((Object) null, locale0, (TimeZone) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      Locale locale0 = Locale.CHINESE;
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      boolean boolean0 = calendarValidator0.isValid3("", "", locale0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.CHINESE;
      boolean boolean0 = calendarValidator0.isValid3("2", "2", locale0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.CalendarValidator1();
      Object object0 = new Object();
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        calendarValidator0.format0(object0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      Locale locale0 = Locale.US;
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        calendarValidator0.format2((Object) locale0, locale0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      CalendarValidator calendarValidator0 = CalendarValidator.getInstance();
      TimeValidator timeValidator0 = TimeValidator.getInstance();
      // Undeclared exception!
      try { 
        timeValidator0.format1((Object) calendarValidator0, (String) null, (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }
}
