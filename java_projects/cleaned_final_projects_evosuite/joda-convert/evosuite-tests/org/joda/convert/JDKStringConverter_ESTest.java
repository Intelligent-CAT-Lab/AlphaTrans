
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


package org.joda.convert;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.net.Inet4Address;
import java.time.chrono.ChronoLocalDate;
import java.util.Date;
import java.util.Locale;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicBoolean;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.util.MockDate;
import org.joda.convert.JDKStringConverter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class JDKStringConverter_ESTest extends JDKStringConverter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BYTE_ARRAY;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "ZbN_| ]t?uLQ");
      String string0 = jDKStringConverter0.convertToString(object0);
      assertEquals("ZbN////t/uLQ", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CALENDAR;
      Class<Date> class0 = Date.class;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "org.joda.convert.JDKStringConverter");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unable to parse date: org.joda.convert.JDKStringConverter
         //
         verifyException("org.joda.convert.JDKStringConverter$31", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.DATE;
      Class<Date> class0 = Date.class;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "StringConverterFactory array must not contain a null element");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unable to parse date: StringConverterFactory array must not contain a null element
         //
         verifyException("org.joda.convert.JDKStringConverter$30", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.DATE;
      MockDate mockDate0 = new MockDate();
      String string0 = jDKStringConverter0.convertToString(mockDate0);
      assertEquals("2014-02-14T20:21:21.320+00:00", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      JDKStringConverter[] jDKStringConverterArray0 = JDKStringConverter.values();
      assertEquals(31, jDKStringConverterArray0.length);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHAR_SEQUENCE;
      Class<?> class0 = jDKStringConverter0.getType();
      assertFalse(class0.isPrimitive());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHAR_ARRAY;
      Class<?> class0 = jDKStringConverter0.getType();
      assertFalse(class0.isAnnotation());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BYTE_ARRAY;
      Class<Date> class0 = Date.class;
      Object object0 = jDKStringConverter0.convertFromString(class0, "QV4I#H4;eA~=");
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CALENDAR;
      Class<Object> class0 = Object.class;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "Renamed.ini enum line must be formatted as 'oldEnumConstantName = enumClassName.newEnumConstantName'");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unable to parse date: Renamed.ini enum line must be formatted as 'oldEnumConstantName = enumClassName.newEnumConstantName'
         //
         verifyException("org.joda.convert.JDKStringConverter$31", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CALENDAR;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "B]y4m");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unable to parse date: B]y4m
         //
         verifyException("org.joda.convert.JDKStringConverter$31", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CALENDAR;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertToString(jDKStringConverter0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Unable to convert calendar as it is not a GregorianCalendar
         //
         verifyException("org.joda.convert.JDKStringConverter$31", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.DATE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "==");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unable to parse date: ==
         //
         verifyException("org.joda.convert.JDKStringConverter$30", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.INET_ADDRESS;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      JDKStringConverter jDKStringConverter1 = JDKStringConverter.DATE;
      // Undeclared exception!
      try { 
        jDKStringConverter1.convertFromString(class0, "Method names must not be null");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // java.text.ParseException: Format.parseObject(String) failed
         //
         verifyException("org.joda.convert.JDKStringConverter$30", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.LOCALE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "zsed^=XjU^U_}f)f");
      assertEquals("zsed^=xju^u_}F)F", object0.toString());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.LOCALE;
      Class<Date> class0 = Date.class;
      Object object0 = jDKStringConverter0.convertFromString(class0, "r_^!1_RfW-Xv,");
      assertEquals("r_^!1_RfW-Xv,", object0.toString());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.LOCALE;
      Class<Date> class0 = Date.class;
      Locale locale0 = (Locale)jDKStringConverter0.convertFromString(class0, "CHARACTER");
      assertEquals("", locale0.getVariant());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.valueOf("ATOMIC_BOOLEAN");
      Class<ChronoLocalDate> class0 = ChronoLocalDate.class;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "ATOMIC_BOOLEAN");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Boolean value must be 'true' or 'false', case insensitive
         //
         verifyException("org.joda.convert.JDKStringConverter$19", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.valueOf("ATOMIC_BOOLEAN");
      Class<Date> class0 = Date.class;
      AtomicBoolean atomicBoolean0 = (AtomicBoolean)jDKStringConverter0.convertFromString(class0, "false");
      assertFalse(atomicBoolean0.get());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BOOLEAN;
      Class<Date> class0 = Date.class;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "6N[*v");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Boolean value must be 'true' or 'false', case insensitive
         //
         verifyException("org.joda.convert.JDKStringConverter$12", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BOOLEAN;
      Class<Date> class0 = Date.class;
      Object object0 = jDKStringConverter0.convertFromString(class0, "false");
      assertEquals(false, object0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHARACTER;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "BW94x");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Character value must be a string length 1
         //
         verifyException("org.joda.convert.JDKStringConverter$10", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Class<Date> class0 = Date.class;
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHARACTER;
      Object object0 = jDKStringConverter0.convertFromString(class0, "B");
      assertEquals('B', object0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.FILE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      MockFile mockFile0 = (MockFile)jDKStringConverter0.convertFromString(class0, "|]y4");
      assertEquals(0L, mockFile0.getTotalSpace());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.SHORT;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "javax.time.calendar.LocalDate");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"javax.time.calendar.LocalDate\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BYTE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "G3th");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"G3th\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.LONG;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "X_ciLifUQ0o{X@");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"X_ciLifUQ0o{X@\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.INTEGER;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "stfy9qdt5k\"");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"stfy9qdt5k\"\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.STRING_BUFFER;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "4O@SQ");
      assertEquals("4O@SQ", object0.toString());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.STRING_BUILDER;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "zsed^=XjU^U_}f)f");
      assertEquals("zsed^=XjU^U_}f)f", object0.toString());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.STRING;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "8");
      assertEquals("8", object0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHAR_SEQUENCE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "$S,3Mt~x-@p8MSHJB");
      assertEquals("$S,3Mt~x-@p8MSHJB", object0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CLASS;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "'U'Q");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Unable to create type: 'U'Q
         //
         verifyException("org.joda.convert.JDKStringConverter$21", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CALENDAR;
      JDKStringConverter jDKStringConverter1 = JDKStringConverter.CLASS;
      // Undeclared exception!
      try { 
        jDKStringConverter1.convertToString(jDKStringConverter0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class org.joda.convert.JDKStringConverter$31 cannot be cast to class java.lang.Class (org.joda.convert.JDKStringConverter$31 is in unnamed module of loader org.evosuite.instrumentation.InstrumentingClassLoader @7dce8d7a; java.lang.Class is in module java.base of loader 'bootstrap')
         //
         verifyException("org.joda.convert.JDKStringConverter$21", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.PACKAGE;
      MockDate mockDate0 = new MockDate((-1846777314), (-1846777314), 3962, 1, (-1846777314), (-1846777314));
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertToString(mockDate0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class org.evosuite.runtime.mock.java.util.MockDate cannot be cast to class java.lang.Package (org.evosuite.runtime.mock.java.util.MockDate is in unnamed module of loader 'app'; java.lang.Package is in module java.base of loader 'bootstrap')
         //
         verifyException("org.joda.convert.JDKStringConverter$22", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.PACKAGE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "qqKF");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CURRENCY;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "RenamedTypes");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Currency", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.TIME_ZONE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertToString(class0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.Class cannot be cast to class java.util.TimeZone (java.lang.Class and java.util.TimeZone are in module java.base of loader 'bootstrap')
         //
         verifyException("org.joda.convert.JDKStringConverter$24", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.INET_ADDRESS;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      JDKStringConverter jDKStringConverter1 = JDKStringConverter.UUID;
      UUID uUID0 = (UUID)jDKStringConverter1.convertFromString(class0, "J]D4m");
      assertEquals(16793600L, uUID0.getMostSignificantBits());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Class<Date> class0 = Date.class;
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.URL;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "org.threeten.bp.LocalDateTime");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no protocol: org.threeten.bp.LocalDateTime
         //
         verifyException("org.joda.convert.JDKStringConverter$26", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.URI;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "B]y4m");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal character in path at index 1: B]y4m
         //
         verifyException("java.net.URI", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.INET_ADDRESS;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Inet4Address inet4Address0 = (Inet4Address)jDKStringConverter0.convertFromString(class0, "BW9Pox");
      assertFalse(inet4Address0.isMCNodeLocal());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.INET_ADDRESS;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertToString(class0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.Class cannot be cast to class java.net.InetAddress (java.lang.Class and java.net.InetAddress are in module java.base of loader 'bootstrap')
         //
         verifyException("org.joda.convert.JDKStringConverter$28", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.ATOMIC_INTEGER;
      Class<Date> class0 = Date.class;
      Object object0 = jDKStringConverter0.convertFromString(class0, "4");
      assertEquals("4", object0.toString());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHAR_ARRAY;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertToString((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.CHAR_ARRAY;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      Object object0 = jDKStringConverter0.convertFromString(class0, "J3th");
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.DOUBLE;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "m-RA|La");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.FLOAT;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "G3th");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BIG_INTEGER;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "Pv+>=");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // Illegal embedded sign character
         //
         verifyException("java.math.BigInteger", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BIG_DECIMAL;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "_tRA|Ld");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // Character _ is neither a decimal digit number, decimal point, nor \"e\" notation exponential mark.
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.ATOMIC_LONG;
      Class<Date> class0 = Date.class;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, "@HFM?a{brd7*|m");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"@HFM?a{brd7*|m\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.ATOMIC_LONG;
      JDKStringConverter jDKStringConverter1 = JDKStringConverter.ATOMIC_BOOLEAN;
      Class<Object> class0 = Object.class;
      AtomicBoolean atomicBoolean0 = (AtomicBoolean)jDKStringConverter1.convertFromString(class0, "true");
      jDKStringConverter0.convertToString(atomicBoolean0);
      assertEquals("true", atomicBoolean0.toString());
      assertTrue(atomicBoolean0.get());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.BYTE_ARRAY;
      Class<?> class0 = jDKStringConverter0.getEffectiveType();
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertFromString(class0, ":");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid Base64 string
         //
         verifyException("org.joda.convert.JDKStringConverter", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      JDKStringConverter jDKStringConverter0 = JDKStringConverter.DATE;
      // Undeclared exception!
      try { 
        jDKStringConverter0.convertToString(jDKStringConverter0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot format given Object as a Date
         //
         verifyException("java.text.DateFormat", e);
      }
  }
}
