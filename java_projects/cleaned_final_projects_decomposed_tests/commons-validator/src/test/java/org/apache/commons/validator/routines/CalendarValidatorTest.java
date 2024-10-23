/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.validator.routines;
import org.junit.Test;

import java.text.DateFormat;
import java.text.Format;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;

/**
 * Test Case for CalendarValidator.
 *
 * @version $Revision$
 */
public class CalendarValidatorTest extends AbstractCalendarValidatorTest {

    private static final int DATE_2005_11_23 = 20051123;
    private static final int TIME_12_03_45 = 120345;

    private CalendarValidator calValidator;

    /**
     * Constructor
     *
     * @param name test name
     */
    public CalendarValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        calValidator = CalendarValidator.CalendarValidator1();
        validator = calValidator;
    }

    /** Test CalendarValidator validate Methods */
    

    /** Test compare date methods */
    

    /** Test Date/Time style Validator (there isn't an implementation for this) */
    

    /** Test format methods */
    @Override
    public void testFormat() {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);

        Calendar cal20050101 = createCalendar(GMT, 20051231, 11500);
        assertNull("null", calValidator.format0(null));
        assertEquals("default", "31/12/05", calValidator.format0(cal20050101));
        assertEquals("locale", "12/31/05", calValidator.format2(cal20050101, Locale.US));
        assertEquals(
                "patternA",
                "2005-12-31 01:15",
                calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm"));
        assertEquals(
                "patternB", "2005-12-31 GMT", calValidator.format1(cal20050101, "yyyy-MM-dd z"));
        assertEquals(
                "both",
                "31 Dez 2005",
                calValidator.format3(cal20050101, "dd MMM yyyy", Locale.GERMAN));

        assertEquals("EST default", "30/12/05", calValidator.format0(cal20050101, EST));
        assertEquals("EST locale", "12/30/05", calValidator.format2(cal20050101, Locale.US, EST));
        assertEquals(
                "EST patternA",
                "2005-12-30 20:15",
                calValidator.format1(cal20050101, "yyyy-MM-dd HH:mm", EST));
        assertEquals(
                "EST patternB",
                "2005-12-30 EST",
                calValidator.format1(cal20050101, "yyyy-MM-dd z", EST));
        assertEquals(
                "EST both",
                "30 Dez 2005",
                calValidator.format4(cal20050101, "dd MMM yyyy", Locale.GERMAN, EST));

        Locale.setDefault(origDefault);
    }

    /** Test adjustToTimeZone() method */

    @Test
    public void testCalendarValidatorMethods_test0_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
    }

    @Test
    public void testCalendarValidatorMethods_test1_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test2_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test3_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test4_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test5_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test6_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test7_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test8_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test9_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test10_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testCalendarValidatorMethods_test11_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test12_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testCalendarValidatorMethods_test13_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test14_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testCalendarValidatorMethods_test15_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test16_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
    }

    @Test
    public void testCalendarValidatorMethods_test17_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test18_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testCalendarValidatorMethods_test19_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test20_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
    }

    @Test
    public void testCalendarValidatorMethods_test21_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test22_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
    }

    @Test
    public void testCalendarValidatorMethods_test23_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test24_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
    }

    @Test
    public void testCalendarValidatorMethods_test25_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test26_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testCalendarValidatorMethods_test27_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test28_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testCalendarValidatorMethods_test29_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test30_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testCalendarValidatorMethods_test31_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test32_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
    }

    @Test
    public void testCalendarValidatorMethods_test33_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
    }

    @Test
    public void testCalendarValidatorMethods_test34_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test35_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test36_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test37_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate5(localeVal,locale,zone);
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                CalendarValidator.getInstance().validate5(localeVal, locale, zone).getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test38_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate5(localeVal,locale,zone);
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                CalendarValidator.getInstance().validate5(localeVal, locale, zone).getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test39_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate5(localeVal,locale,zone);
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                CalendarValidator.getInstance().validate5(localeVal, locale, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate3(patternVal,pattern,zone);
        assertEquals(
                "validate(C) pattern",
                expectedZone,
                CalendarValidator.getInstance().validate3(patternVal, pattern, zone).getTime());
    }

    @Test
    public void testCalendarValidatorMethods_test40_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate5(localeVal,locale,zone);
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                CalendarValidator.getInstance().validate5(localeVal, locale, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate3(patternVal,pattern,zone);
        assertEquals(
                "validate(C) pattern",
                expectedZone,
                CalendarValidator.getInstance().validate3(patternVal, pattern, zone).getTime());
        CalendarValidator.getInstance();
    }

    @Test
    public void testCalendarValidatorMethods_test41_decomposed()  {
        Locale.setDefault(Locale.US);
        Locale locale = Locale.GERMAN;
        String pattern = "yyyy-MM-dd";
        String patternVal = "2005-12-31";
        String germanVal = "31 Dez 2005";
        String germanPattern = "dd MMM yyyy";
        String localeVal = "31.12.2005";
        String defaultVal = "12/31/05";
        String XXXX = "XXXX";
        Date expected = createCalendar(null, 20051231, 0).getTime();
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate0(defaultVal);
        assertEquals(
                "validate(A) default",
                expected,
                CalendarValidator.getInstance().validate0(defaultVal).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate4(localeVal,locale);
        assertEquals(
                "validate(A) locale ",
                expected,
                CalendarValidator.getInstance().validate4(localeVal, locale).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate2(patternVal,pattern);
        assertEquals(
                "validate(A) pattern",
                expected,
                CalendarValidator.getInstance().validate2(patternVal, pattern).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate6(germanVal,germanPattern,Locale.GERMAN);
        assertEquals(
                "validate(A) both",
                expected,
                CalendarValidator.getInstance()
                        .validate6(germanVal, germanPattern, Locale.GERMAN)
                        .getTime());
        CalendarValidator.getInstance();
        assertTrue("isValid(A) default", CalendarValidator.getInstance().isValid0(defaultVal));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", CalendarValidator.getInstance().isValid2(localeVal, locale));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                CalendarValidator.getInstance().isValid1(patternVal, pattern));
        CalendarValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                CalendarValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertNull("validate(B) default", CalendarValidator.getInstance().validate0(XXXX));
        CalendarValidator.getInstance();
        assertNull("validate(B) locale ", CalendarValidator.getInstance().validate4(XXXX, locale));
        CalendarValidator.getInstance();
        assertNull("validate(B) pattern", CalendarValidator.getInstance().validate2(XXXX, pattern));
        CalendarValidator.getInstance();
        assertNull(
                "validate(B) both",
                CalendarValidator.getInstance()
                        .validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) default", CalendarValidator.getInstance().isValid0(XXXX));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) locale ", CalendarValidator.getInstance().isValid2(XXXX, locale));
        CalendarValidator.getInstance();
        assertFalse("isValid(B) pattern", CalendarValidator.getInstance().isValid1(XXXX, pattern));
        CalendarValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                CalendarValidator.getInstance()
                        .isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/EET same ", expected.getTime() == expectedZone.getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate1(defaultVal,zone);
        assertEquals(
                "validate(C) default",
                expectedZone,
                CalendarValidator.getInstance().validate1(defaultVal, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate5(localeVal,locale,zone);
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                CalendarValidator.getInstance().validate5(localeVal, locale, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate3(patternVal,pattern,zone);
        assertEquals(
                "validate(C) pattern",
                expectedZone,
                CalendarValidator.getInstance().validate3(patternVal, pattern, zone).getTime());
        CalendarValidator.getInstance();
        CalendarValidator.getInstance().validate7(germanVal,germanPattern,Locale.GERMAN,zone);
        assertEquals(
                "validate(C) both",
                expectedZone,
                CalendarValidator.getInstance()
                        .validate7(germanVal, germanPattern, Locale.GERMAN, zone)
                        .getTime());
    }

    @Test
    public void testCompare_test0_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
    }

    @Test
    public void testCompare_test1_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
    }

    @Test
    public void testCompare_test2_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
    }

    @Test
    public void testCompare_test3_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
    }

    @Test
    public void testCompare_test4_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
    }

    @Test
    public void testCompare_test5_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
    }

    @Test
    public void testCompare_test6_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
    }

    @Test
    public void testCompare_test7_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
    }

    @Test
    public void testCompare_test8_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
        assertEquals("week =4", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals("week GT", 1, calValidator.compareWeeks(value, cal20050816));
    }

    @Test
    public void testCompare_test9_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
        assertEquals("week =4", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals("week GT", 1, calValidator.compareWeeks(value, cal20050816));
        assertEquals("mnth LT", -1, calValidator.compareMonths(value, cal20050901));
        assertEquals("mnth =1", 0, calValidator.compareMonths(value, cal20050830));
        assertEquals("mnth =2", 0, calValidator.compareMonths(value, cal20050801));
        assertEquals("mnth =3", 0, calValidator.compareMonths(value, cal20050816));
        assertEquals("mnth GT", 1, calValidator.compareMonths(value, cal20050731));
    }

    @Test
    public void testCompare_test10_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
        assertEquals("week =4", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals("week GT", 1, calValidator.compareWeeks(value, cal20050816));
        assertEquals("mnth LT", -1, calValidator.compareMonths(value, cal20050901));
        assertEquals("mnth =1", 0, calValidator.compareMonths(value, cal20050830));
        assertEquals("mnth =2", 0, calValidator.compareMonths(value, cal20050801));
        assertEquals("mnth =3", 0, calValidator.compareMonths(value, cal20050816));
        assertEquals("mnth GT", 1, calValidator.compareMonths(value, cal20050731));
        assertEquals(
                "qtrA <1",
                -1,
                calValidator.compareQuarters0(value, cal20051101));
        assertEquals(
                "qtrA <2", -1, calValidator.compareQuarters0(value, cal20051001));
        assertEquals("qtrA =1", 0, calValidator.compareQuarters0(value, cal20050901));
        assertEquals(
                "qtrA =2", 0, calValidator.compareQuarters0(value, cal20050701));
        assertEquals("qtrA =3", 0, calValidator.compareQuarters0(value, cal20050731));
        assertEquals("qtrA GT", 1, calValidator.compareQuarters0(value, cal20050630));
    }

    @Test
    public void testCompare_test11_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
        assertEquals("week =4", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals("week GT", 1, calValidator.compareWeeks(value, cal20050816));
        assertEquals("mnth LT", -1, calValidator.compareMonths(value, cal20050901));
        assertEquals("mnth =1", 0, calValidator.compareMonths(value, cal20050830));
        assertEquals("mnth =2", 0, calValidator.compareMonths(value, cal20050801));
        assertEquals("mnth =3", 0, calValidator.compareMonths(value, cal20050816));
        assertEquals("mnth GT", 1, calValidator.compareMonths(value, cal20050731));
        assertEquals(
                "qtrA <1",
                -1,
                calValidator.compareQuarters0(value, cal20051101));
        assertEquals(
                "qtrA <2", -1, calValidator.compareQuarters0(value, cal20051001));
        assertEquals("qtrA =1", 0, calValidator.compareQuarters0(value, cal20050901));
        assertEquals(
                "qtrA =2", 0, calValidator.compareQuarters0(value, cal20050701));
        assertEquals("qtrA =3", 0, calValidator.compareQuarters0(value, cal20050731));
        assertEquals("qtrA GT", 1, calValidator.compareQuarters0(value, cal20050630));
        assertEquals(
                "qtrB LT",
                -1,
                calValidator.compareQuarters1(value, cal20051101, 2));
        assertEquals(
                "qtrB =1", 0, calValidator.compareQuarters1(value, cal20051001, 2));
        assertEquals(
                "qtrB =2", 0, calValidator.compareQuarters1(value, cal20050901, 2));
        assertEquals(
                "qtrB =3", 1, calValidator.compareQuarters1(value, cal20050701, 2));
        assertEquals(
                "qtrB =4", 1, calValidator.compareQuarters1(value, cal20050731, 2));
        assertEquals(
                "qtrB GT", 1, calValidator.compareQuarters1(value, cal20050630, 2));
    }

    @Test
    public void testCompare_test12_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
        assertEquals("week =4", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals("week GT", 1, calValidator.compareWeeks(value, cal20050816));
        assertEquals("mnth LT", -1, calValidator.compareMonths(value, cal20050901));
        assertEquals("mnth =1", 0, calValidator.compareMonths(value, cal20050830));
        assertEquals("mnth =2", 0, calValidator.compareMonths(value, cal20050801));
        assertEquals("mnth =3", 0, calValidator.compareMonths(value, cal20050816));
        assertEquals("mnth GT", 1, calValidator.compareMonths(value, cal20050731));
        assertEquals(
                "qtrA <1",
                -1,
                calValidator.compareQuarters0(value, cal20051101));
        assertEquals(
                "qtrA <2", -1, calValidator.compareQuarters0(value, cal20051001));
        assertEquals("qtrA =1", 0, calValidator.compareQuarters0(value, cal20050901));
        assertEquals(
                "qtrA =2", 0, calValidator.compareQuarters0(value, cal20050701));
        assertEquals("qtrA =3", 0, calValidator.compareQuarters0(value, cal20050731));
        assertEquals("qtrA GT", 1, calValidator.compareQuarters0(value, cal20050630));
        assertEquals(
                "qtrB LT",
                -1,
                calValidator.compareQuarters1(value, cal20051101, 2));
        assertEquals(
                "qtrB =1", 0, calValidator.compareQuarters1(value, cal20051001, 2));
        assertEquals(
                "qtrB =2", 0, calValidator.compareQuarters1(value, cal20050901, 2));
        assertEquals(
                "qtrB =3", 1, calValidator.compareQuarters1(value, cal20050701, 2));
        assertEquals(
                "qtrB =4", 1, calValidator.compareQuarters1(value, cal20050731, 2));
        assertEquals(
                "qtrB GT", 1, calValidator.compareQuarters1(value, cal20050630, 2));
        assertEquals("year LT", -1, calValidator.compareYears(value, cal20060101));
        assertEquals("year EQ", 0, calValidator.compareYears(value, cal20050101));
        assertEquals("year GT", 1, calValidator.compareYears(value, cal20041231));
    }

    @Test
    public void testCompare_test13_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Calendar diffHour = createCalendar(GMT, testDate, 115922);
        Calendar diffMin = createCalendar(GMT, testDate, 124422);
        Calendar diffSec = createCalendar(GMT, testDate, 124521);
        Calendar value = createCalendar(GMT, testDate, sameTime);
        Calendar cal20050824 = createCalendar(GMT, 20050824, sameTime);
        Calendar cal20050822 = createCalendar(GMT, 20050822, sameTime);
        Calendar cal20050830 = createCalendar(GMT, 20050830, sameTime);
        Calendar cal20050816 = createCalendar(GMT, 20050816, sameTime);
        Calendar cal20050901 = createCalendar(GMT, 20050901, sameTime);
        Calendar cal20050801 = createCalendar(GMT, 20050801, sameTime);
        Calendar cal20050731 = createCalendar(GMT, 20050731, sameTime);
        Calendar cal20051101 = createCalendar(GMT, 20051101, sameTime);
        Calendar cal20051001 = createCalendar(GMT, 20051001, sameTime);
        Calendar cal20050701 = createCalendar(GMT, 20050701, sameTime);
        Calendar cal20050630 = createCalendar(GMT, 20050630, sameTime);
        Calendar cal20060101 = createCalendar(GMT, 20060101, sameTime);
        Calendar cal20050101 = createCalendar(GMT, 20050101, sameTime);
        Calendar cal20041231 = createCalendar(GMT, 20041231, sameTime);
        assertEquals("hour GT", 1, calValidator.compare(value, diffHour, Calendar.HOUR_OF_DAY));
        assertEquals("hour EQ", 0, calValidator.compare(value, diffMin, Calendar.HOUR_OF_DAY));
        assertEquals("mins GT", 1, calValidator.compare(value, diffMin, Calendar.MINUTE));
        assertEquals("mins EQ", 0, calValidator.compare(value, diffSec, Calendar.MINUTE));
        assertEquals("secs GT", 1, calValidator.compare(value, diffSec, Calendar.SECOND));
        assertEquals("date LT", -1, calValidator.compareDates(value, cal20050824));
        assertEquals(
                "date EQ", 0, calValidator.compareDates(value, diffHour));
        assertEquals(
                "date(B)",
                0,
                calValidator.compare(value, diffHour, Calendar.DAY_OF_YEAR));
        assertEquals("date GT", 1, calValidator.compareDates(value, cal20050822));
        assertEquals("week LT", -1, calValidator.compareWeeks(value, cal20050830));
        assertEquals("week =1", 0, calValidator.compareWeeks(value, cal20050824));
        assertEquals("week =2", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals(
                "week =3",
                0,
                calValidator.compare(value, cal20050822, Calendar.WEEK_OF_MONTH));
        assertEquals("week =4", 0, calValidator.compareWeeks(value, cal20050822));
        assertEquals("week GT", 1, calValidator.compareWeeks(value, cal20050816));
        assertEquals("mnth LT", -1, calValidator.compareMonths(value, cal20050901));
        assertEquals("mnth =1", 0, calValidator.compareMonths(value, cal20050830));
        assertEquals("mnth =2", 0, calValidator.compareMonths(value, cal20050801));
        assertEquals("mnth =3", 0, calValidator.compareMonths(value, cal20050816));
        assertEquals("mnth GT", 1, calValidator.compareMonths(value, cal20050731));
        assertEquals(
                "qtrA <1",
                -1,
                calValidator.compareQuarters0(value, cal20051101));
        assertEquals(
                "qtrA <2", -1, calValidator.compareQuarters0(value, cal20051001));
        assertEquals("qtrA =1", 0, calValidator.compareQuarters0(value, cal20050901));
        assertEquals(
                "qtrA =2", 0, calValidator.compareQuarters0(value, cal20050701));
        assertEquals("qtrA =3", 0, calValidator.compareQuarters0(value, cal20050731));
        assertEquals("qtrA GT", 1, calValidator.compareQuarters0(value, cal20050630));
        assertEquals(
                "qtrB LT",
                -1,
                calValidator.compareQuarters1(value, cal20051101, 2));
        assertEquals(
                "qtrB =1", 0, calValidator.compareQuarters1(value, cal20051001, 2));
        assertEquals(
                "qtrB =2", 0, calValidator.compareQuarters1(value, cal20050901, 2));
        assertEquals(
                "qtrB =3", 1, calValidator.compareQuarters1(value, cal20050701, 2));
        assertEquals(
                "qtrB =4", 1, calValidator.compareQuarters1(value, cal20050731, 2));
        assertEquals(
                "qtrB GT", 1, calValidator.compareQuarters1(value, cal20050630, 2));
        assertEquals("year LT", -1, calValidator.compareYears(value, cal20060101));
        assertEquals("year EQ", 0, calValidator.compareYears(value, cal20050101));
        assertEquals("year GT", 1, calValidator.compareYears(value, cal20041231));
        try {
            calValidator.compare(value, value, -1);
            fail("Invalid Compare field - expected IllegalArgumentException to be thrown");
        } catch (IllegalArgumentException e) {
            assertEquals("check message", "Invalid field: -1", e.getMessage());
        }
    }

    @Test
    public void testDateTimeStyle_test0_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        AbstractCalendarValidator dateTimeValidator =
                new AbstractCalendarValidator(true, DateFormat.SHORT, DateFormat.SHORT) {
                    private static final long serialVersionUID = 1L;

                    @Override
                    protected Object processParsedValue(Object value, Format formatter) {
                        return value;
                    }
                };
    }

    @Test
    public void testDateTimeStyle_test1_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        AbstractCalendarValidator dateTimeValidator =
                new AbstractCalendarValidator(true, DateFormat.SHORT, DateFormat.SHORT) {
                    private static final long serialVersionUID = 1L;

                    @Override
                    protected Object processParsedValue(Object value, Format formatter) {
                        return value;
                    }
                };
        assertTrue("validate(A) default", dateTimeValidator.isValid0("31/12/05 14:23"));
    }

    @Test
    public void testDateTimeStyle_test2_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        AbstractCalendarValidator dateTimeValidator =
                new AbstractCalendarValidator(true, DateFormat.SHORT, DateFormat.SHORT) {
                    private static final long serialVersionUID = 1L;

                    @Override
                    protected Object processParsedValue(Object value, Format formatter) {
                        return value;
                    }
                };
        assertTrue("validate(A) default", dateTimeValidator.isValid0("31/12/05 14:23"));
        assertTrue(
                "validate(A) locale ", dateTimeValidator.isValid2("12/31/05 2:23 PM", Locale.US));
    }

    @Test
    public void testDateTimeStyle_test3_decomposed()  {
        Locale origDefault = Locale.getDefault();
        Locale.setDefault(Locale.UK);
        AbstractCalendarValidator dateTimeValidator =
                new AbstractCalendarValidator(true, DateFormat.SHORT, DateFormat.SHORT) {
                    private static final long serialVersionUID = 1L;

                    @Override
                    protected Object processParsedValue(Object value, Format formatter) {
                        return value;
                    }
                };
        assertTrue("validate(A) default", dateTimeValidator.isValid0("31/12/05 14:23"));
        assertTrue(
                "validate(A) locale ", dateTimeValidator.isValid2("12/31/05 2:23 PM", Locale.US));
        Locale.setDefault(origDefault);
    }

    @Test
    public void testAdjustToTimeZone_test0_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
    }

    @Test
    public void testAdjustToTimeZone_test1_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
    }

    @Test
    public void testAdjustToTimeZone_test2_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
    }

    @Test
    public void testAdjustToTimeZone_test3_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test4_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test5_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
    }

    @Test
    public void testAdjustToTimeZone_test6_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test7_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
    }

    @Test
    public void testAdjustToTimeZone_test8_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test9_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
    }

    @Test
    public void testAdjustToTimeZone_test10_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test11_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
    }

    @Test
    public void testAdjustToTimeZone_test12_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test13_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
        Calendar calUTC = createCalendar(UTC, DATE_2005_11_23, TIME_12_03_45);
    }

    @Test
    public void testAdjustToTimeZone_test14_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
        Calendar calUTC = createCalendar(UTC, DATE_2005_11_23, TIME_12_03_45);
        assertTrue("SAME: UTC = GMT", UTC.hasSameRules(GMT));
        assertEquals("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime());
    }

    @Test
    public void testAdjustToTimeZone_test15_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
        Calendar calUTC = createCalendar(UTC, DATE_2005_11_23, TIME_12_03_45);
        assertTrue("SAME: UTC = GMT", UTC.hasSameRules(GMT));
        assertEquals("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime());
        assertFalse("SAME: Check GMT(A)", GMT.equals(calUTC.getTimeZone()));
        assertTrue("SAME: Check UTC(A)", UTC.equals(calUTC.getTimeZone()));
    }

    @Test
    public void testAdjustToTimeZone_test16_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
        Calendar calUTC = createCalendar(UTC, DATE_2005_11_23, TIME_12_03_45);
        assertTrue("SAME: UTC = GMT", UTC.hasSameRules(GMT));
        assertEquals("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime());
        assertFalse("SAME: Check GMT(A)", GMT.equals(calUTC.getTimeZone()));
        assertTrue("SAME: Check UTC(A)", UTC.equals(calUTC.getTimeZone()));
        CalendarValidator.adjustToTimeZone(calUTC, GMT);
    }

    @Test
    public void testAdjustToTimeZone_test17_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
        Calendar calUTC = createCalendar(UTC, DATE_2005_11_23, TIME_12_03_45);
        assertTrue("SAME: UTC = GMT", UTC.hasSameRules(GMT));
        assertEquals("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime());
        assertFalse("SAME: Check GMT(A)", GMT.equals(calUTC.getTimeZone()));
        assertTrue("SAME: Check UTC(A)", UTC.equals(calUTC.getTimeZone()));
        CalendarValidator.adjustToTimeZone(calUTC, GMT);
        assertEquals("SAME: Check time (B)", calUTC.getTime(), calGMT.getTime());
        assertTrue("SAME: Check GMT(B)", GMT.equals(calUTC.getTimeZone()));
    }

    @Test
    public void testAdjustToTimeZone_test18_decomposed()  {
        Calendar calEST = createCalendar(EST, DATE_2005_11_23, TIME_12_03_45);
        Date dateEST = calEST.getTime();
        Calendar calGMT = createCalendar(GMT, DATE_2005_11_23, TIME_12_03_45);
        Date dateGMT = calGMT.getTime();
        Calendar calCET = createCalendar(EET, DATE_2005_11_23, TIME_12_03_45);
        Date dateCET = calCET.getTime();
        assertFalse("Check GMT != CET", dateGMT.getTime() == dateCET.getTime());
        assertFalse("Check GMT != EST", dateGMT.getTime() == dateEST.getTime());
        assertFalse("Check CET != EST", dateCET.getTime() == dateEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, GMT);
        assertEquals("EST to GMT", dateGMT, calEST.getTime());
        assertFalse("Check EST = GMT", dateEST == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calEST, EST);
        assertEquals("back to EST", dateEST, calEST.getTime());
        assertFalse("Check EST != GMT", dateGMT == calEST.getTime());
        CalendarValidator.adjustToTimeZone(calCET, GMT);
        assertEquals("CET to GMT", dateGMT, calCET.getTime());
        assertFalse("Check CET = GMT", dateCET == calCET.getTime());
        CalendarValidator.adjustToTimeZone(calCET, EET);
        assertEquals("back to CET", dateCET, calCET.getTime());
        assertFalse("Check CET != GMT", dateGMT == calCET.getTime());
        Calendar calUTC = createCalendar(UTC, DATE_2005_11_23, TIME_12_03_45);
        assertTrue("SAME: UTC = GMT", UTC.hasSameRules(GMT));
        assertEquals("SAME: Check time (A)", calUTC.getTime(), calGMT.getTime());
        assertFalse("SAME: Check GMT(A)", GMT.equals(calUTC.getTimeZone()));
        assertTrue("SAME: Check UTC(A)", UTC.equals(calUTC.getTimeZone()));
        CalendarValidator.adjustToTimeZone(calUTC, GMT);
        assertEquals("SAME: Check time (B)", calUTC.getTime(), calGMT.getTime());
        assertTrue("SAME: Check GMT(B)", GMT.equals(calUTC.getTimeZone()));
        assertFalse("SAME: Check UTC(B)", UTC.equals(calUTC.getTimeZone()));
    }
}