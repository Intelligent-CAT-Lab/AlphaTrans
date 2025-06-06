

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
import java.text.NumberFormat;
import java.text.ParsePosition;
import java.time.Instant;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.util.Date;
import java.util.Locale;
import java.util.SimpleTimeZone;
import java.util.TimeZone;
import org.apache.commons.validator.routines.DateValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.text.MockSimpleDateFormat;
import org.evosuite.runtime.mock.java.time.MockInstant;
import org.evosuite.runtime.mock.java.util.MockDate;
import org.evosuite.runtime.mock.java.util.MockGregorianCalendar;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DateValidator_ESTest extends DateValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Locale locale0 = Locale.CHINA;
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        dateValidator0.validate7("Invalid field: ", ")NITs-IO", locale0, timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'N'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      Locale locale0 = Locale.JAPANESE;
      // Undeclared exception!
      try { 
        dateValidator0.validate6("Invalid field: ", "org.apache.commons.validator.routines.DateValidator", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'o'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(12, "");
      dateValidator0.validate3("M+WGQ*|-[z", "", simpleTimeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      dateValidator0.validate2("", ":E|Fr(<BTFD");
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      Locale locale0 = Locale.JAPANESE;
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(12, "");
      dateValidator0.validate7("", "", locale0, simpleTimeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Locale locale0 = Locale.ITALY;
      Date date0 = dateValidator0.validate6("", "", locale0);
      assertNull(date0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Date date0 = dateValidator0.validate4((String) null, (Locale) null);
      assertNull(date0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      dateValidator0.validate2("$_2&&|@", "$_2&&|@");
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      TimeZone timeZone0 = TimeZone.getDefault();
      Date date0 = dateValidator0.validate1("", timeZone0);
      assertNull(date0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Date date0 = dateValidator0.validate0("VI0[1jIl");
      assertNull(date0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, 1621);
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      NumberFormat numberFormat0 = NumberFormat.getNumberInstance(locale0);
      Object object0 = dateValidator0.processParsedValue((Object) null, numberFormat0);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      NumberFormat numberFormat0 = NumberFormat.getNumberInstance();
      Object object0 = dateValidator0.processParsedValue(dateValidator0, numberFormat0);
      assertSame(dateValidator0, object0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      MockDate mockDate0 = new MockDate();
      DateValidator dateValidator0 = DateValidator.getInstance();
      int int0 = dateValidator0.compareYears(mockDate0, mockDate0, (TimeZone) null);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 0, (-32), 0, 0);
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone((-2153), "org.apache.commons.validator.routines.AstractCalendarValidator");
      int int0 = dateValidator0.compareYears(mockDate0, date0, simpleTimeZone0);
      assertEquals(1, int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(0, "org.apache.commons.validator.routines.AstractCalendarValidator");
      int int0 = dateValidator0.compareYears(date0, mockDate0, simpleTimeZone0);
      assertTrue(dateValidator0.isStrict());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      ZoneOffset zoneOffset0 = ZoneOffset.ofHoursMinutesSeconds(0, 0, 0);
      TimeZone timeZone0 = TimeZone.getTimeZone((ZoneId) zoneOffset0);
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      MockDate mockDate0 = new MockDate(0, 0, (-2503), 0, (-3665));
      int int0 = dateValidator0.compareWeeks(mockDate0, date0, timeZone0);
      assertEquals(1, int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate(2, (-1906), (-1906), (-1906), 3, 0);
      Instant instant0 = MockInstant.now();
      Date date0 = Date.from(instant0);
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(0, "_E");
      int int0 = dateValidator0.compareWeeks(mockDate0, date0, simpleTimeZone0);
      assertEquals((-1), int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Locale locale0 = Locale.UK;
      DateFormatSymbols dateFormatSymbols0 = DateFormatSymbols.getInstance(locale0);
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat("", dateFormatSymbols0);
      ParsePosition parsePosition0 = new ParsePosition((-2792));
      Date date0 = mockSimpleDateFormat0.parse("tU`s-FaSAw/@s7o8", parsePosition0);
      TimeZone timeZone0 = TimeZone.getDefault();
      int int0 = dateValidator0.compareQuarters1(date0, date0, timeZone0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockDate mockDate0 = new MockDate();
      MockDate mockDate1 = new MockDate(0, 0, 0, 0, (-1635));
      ZoneOffset zoneOffset0 = ZoneOffset.UTC;
      TimeZone timeZone0 = TimeZone.getTimeZone((ZoneId) zoneOffset0);
      int int0 = dateValidator0.compareQuarters1(mockDate0, mockDate1, timeZone0, (-1635));
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar(0, 0, 869, 7, (-567));
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      MockDate mockDate0 = new MockDate();
      ZoneId zoneId0 = ZoneId.systemDefault();
      TimeZone timeZone0 = TimeZone.getTimeZone(zoneId0);
      int int0 = dateValidator0.compareQuarters1(date0, mockDate0, timeZone0, 869);
      assertEquals((-1), int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      ZoneOffset zoneOffset0 = ZoneOffset.ofHoursMinutesSeconds(0, 0, 0);
      TimeZone timeZone0 = TimeZone.getTimeZone((ZoneId) zoneOffset0);
      Instant instant0 = MockInstant.ofEpochSecond((-1L), (long) 0);
      Date date0 = Date.from(instant0);
      MockDate mockDate0 = new MockDate(0, (-3655), 0, (-3655), 3);
      int int0 = dateValidator0.compareQuarters0(date0, mockDate0, timeZone0);
      assertEquals(1, int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockDate mockDate0 = new MockDate();
      MockDate mockDate1 = new MockDate(2480, (-1), 1, 3870, 5, 2);
      TimeZone timeZone0 = TimeZone.getTimeZone("");
      int int0 = dateValidator0.compareQuarters0(mockDate0, mockDate1, timeZone0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockDate mockDate0 = new MockDate();
      TimeZone timeZone0 = TimeZone.getDefault();
      int int0 = dateValidator0.compareMonths(mockDate0, mockDate0, timeZone0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate(309, (-2191), 309, 13, (-2191));
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Date date0 = mockSimpleDateFormat0.get2DigitYearStart();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      int int0 = dateValidator0.compareMonths(mockDate0, date0, timeZone0);
      assertTrue(dateValidator0.isStrict());
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockGregorianCalendar mockGregorianCalendar0 = new MockGregorianCalendar();
      Date date0 = mockGregorianCalendar0.getGregorianChange();
      MockDate mockDate0 = new MockDate(1L);
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(0, "org.apache.commons.validator.routines.DateValidator");
      int int0 = dateValidator0.compareMonths(date0, mockDate0, simpleTimeZone0);
      assertEquals((-1), int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate(12, 3360, 5, 0, 0, 384);
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Date date0 = mockSimpleDateFormat0.get2DigitYearStart();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      int int0 = dateValidator0.compareDates(mockDate0, date0, timeZone0);
      assertEquals(1, int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate(12, 12, 5, 12, 0, 384);
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      Date date0 = mockSimpleDateFormat0.get2DigitYearStart();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      int int0 = dateValidator0.compareDates(mockDate0, date0, timeZone0);
      assertEquals((-1), int0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, 8);
      Locale locale0 = Locale.CHINESE;
      // Undeclared exception!
      try { 
        dateValidator0.validate5("pnIB'V&1\u0001S7.", locale0, (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 8
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      // Undeclared exception!
      try { 
        dateValidator0.validate3("m2xj2+L4@=JwpFP", "m2xj2+L4@=JwpFP", (TimeZone) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'x'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        dateValidator0.compareWeeks((Date) null, (Date) null, timeZone0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Calendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        dateValidator0.compareQuarters0((Date) null, (Date) null, timeZone0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Calendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        dateValidator0.compareDates((Date) null, (Date) null, timeZone0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Calendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        dateValidator0.compareQuarters1((Date) null, (Date) null, timeZone0, (-738));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Calendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate(2, (-1906), (-1906), (-1906), 3, 0);
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(0, "_E");
      dateValidator0.compareWeeks(mockDate0, mockDate0, simpleTimeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      // Undeclared exception!
      try { 
        dateValidator0.validate2("Invalid field: ", "Invalid field: ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'I'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      // Undeclared exception!
      try { 
        dateValidator0.compareMonths((Date) null, (Date) null, (TimeZone) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Calendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockDate mockDate0 = new MockDate(12, 12, 5, 12, 0, 384);
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      dateValidator0.compareDates(mockDate0, mockDate0, timeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(true, 7);
      TimeZone timeZone0 = TimeZone.getDefault();
      // Undeclared exception!
      try { 
        dateValidator0.validate1("MFi}S>V3s/pbPJ3", timeZone0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 7
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      // Undeclared exception!
      try { 
        dateValidator0.compareYears((Date) null, (Date) null, (TimeZone) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Calendar", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      Locale locale0 = Locale.ITALIAN;
      ZoneOffset zoneOffset0 = ZoneOffset.MAX;
      TimeZone timeZone0 = TimeZone.getTimeZone((ZoneId) zoneOffset0);
      dateValidator0.validate7("7", "7", locale0, timeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      MockSimpleDateFormat mockSimpleDateFormat0 = new MockSimpleDateFormat();
      TimeZone timeZone0 = mockSimpleDateFormat0.getTimeZone();
      Locale locale0 = Locale.PRC;
      dateValidator0.validate5("+D", locale0, timeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, 5);
      // Undeclared exception!
      try { 
        dateValidator0.validate0("^Kr@Kls6[");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 5
         //
         verifyException("java.text.DateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      MockDate mockDate0 = new MockDate();
      TimeZone timeZone0 = TimeZone.getTimeZone("");
      int int0 = dateValidator0.compareQuarters0(mockDate0, mockDate0, timeZone0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.DateValidator1();
      SimpleTimeZone simpleTimeZone0 = new SimpleTimeZone(2337, "^3");
      dateValidator0.validate3("^3", "^3", simpleTimeZone0);
      assertTrue(dateValidator0.isStrict());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Locale locale0 = Locale.CHINA;
      Date date0 = dateValidator0.validate6("@1~", "@1~", locale0);
      assertEquals("Fri Feb 14 20:21:21 GMT 2014", date0.toString());
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator(false, 119);
      Locale locale0 = Locale.FRANCE;
      // Undeclared exception!
      try { 
        dateValidator0.validate4("[G4%ktnO)ldR", locale0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal date style 119
         //
         verifyException("java.text.DateFormat", e);
      }
  }
}
