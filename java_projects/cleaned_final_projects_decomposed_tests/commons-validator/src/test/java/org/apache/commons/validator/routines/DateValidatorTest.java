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
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;

/**
 * Test Case for DateValidator.
 *
 * @version $Revision$
 */
public class DateValidatorTest extends AbstractCalendarValidatorTest {

    private DateValidator dateValidator;

    /**
     * Constructor
     *
     * @param name test name
     */
    public DateValidatorTest(String name) {
        super(name);
    }

    /**
     * Set Up.
     *
     * @throws Exception
     */
    @Override
    protected void setUp() throws Exception {
        super.setUp();
        dateValidator = DateValidator.DateValidator1();
        validator = dateValidator;
    }

    /** Check that locale providers are set up correctly If not, the parse will fail */
    

    /** Test DateValidator validate Methods */
    

    /** Test compare date methods */

    @Test
    public void testLocaleProviders_test0_decomposed() throws Exception {
        String localeProviders = System.getProperty("java.locale.providers");
    }

    @Test
    public void testLocaleProviders_test1_decomposed() throws Exception {
        String localeProviders = System.getProperty("java.locale.providers");
        if (localeProviders != null) { // may be null before Java 9
            assertTrue(
                    "java.locale.providers must start with COMPAT",
                    localeProviders.startsWith("COMPAT"));
        }
        String txt =
                "3/20/15 10:59:00 PM";
        DateFormat dateformat =
                DateFormat.getDateTimeInstance(DateFormat.SHORT, DateFormat.MEDIUM, Locale.US);
        dateformat.setTimeZone(TimeZone.getTimeZone("GMT"));
        Date date = dateformat.parse(txt);
    }

    @Test
    public void testLocaleProviders_test2_decomposed() throws Exception {
        String localeProviders = System.getProperty("java.locale.providers");
        if (localeProviders != null) { // may be null before Java 9
            assertTrue(
                    "java.locale.providers must start with COMPAT",
                    localeProviders.startsWith("COMPAT"));
        }
        String txt =
                "3/20/15 10:59:00 PM";
        DateFormat dateformat =
                DateFormat.getDateTimeInstance(DateFormat.SHORT, DateFormat.MEDIUM, Locale.US);
        dateformat.setTimeZone(TimeZone.getTimeZone("GMT"));
        Date date = dateformat.parse(txt);
        assertNotNull(date);
    }

    @Test
    public void testDateValidatorMethods_test0_decomposed()  {
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
    public void testDateValidatorMethods_test1_decomposed()  {
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
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test2_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
    }

    @Test
    public void testDateValidatorMethods_test3_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test4_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
    }

    @Test
    public void testDateValidatorMethods_test5_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test6_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
    }

    @Test
    public void testDateValidatorMethods_test7_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test8_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
    }

    @Test
    public void testDateValidatorMethods_test9_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test10_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testDateValidatorMethods_test11_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test12_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testDateValidatorMethods_test13_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test14_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testDateValidatorMethods_test15_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test16_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
    }

    @Test
    public void testDateValidatorMethods_test17_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test18_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testDateValidatorMethods_test19_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test20_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
    }

    @Test
    public void testDateValidatorMethods_test21_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test22_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
    }

    @Test
    public void testDateValidatorMethods_test23_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test24_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
    }

    @Test
    public void testDateValidatorMethods_test25_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test26_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testDateValidatorMethods_test27_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test28_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testDateValidatorMethods_test29_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test30_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testDateValidatorMethods_test31_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test32_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
    }

    @Test
    public void testDateValidatorMethods_test33_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
    }

    @Test
    public void testDateValidatorMethods_test34_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test35_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
    }

    @Test
    public void testDateValidatorMethods_test36_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test37_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                DateValidator.getInstance().validate5(localeVal, locale, zone));
    }

    @Test
    public void testDateValidatorMethods_test38_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                DateValidator.getInstance().validate5(localeVal, locale, zone));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test39_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                DateValidator.getInstance().validate5(localeVal, locale, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) pattern",
                expectedZone,
                DateValidator.getInstance().validate3(patternVal, pattern, zone));
    }

    @Test
    public void testDateValidatorMethods_test40_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                DateValidator.getInstance().validate5(localeVal, locale, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) pattern",
                expectedZone,
                DateValidator.getInstance().validate3(patternVal, pattern, zone));
        DateValidator.getInstance();
    }

    @Test
    public void testDateValidatorMethods_test41_decomposed()  {
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
        DateValidator.getInstance();
        assertEquals(
                "validate(A) default", expected, DateValidator.getInstance().validate0(defaultVal));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                DateValidator.getInstance().validate4(localeVal, locale));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                DateValidator.getInstance().validate2(patternVal, pattern));
        DateValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                DateValidator.getInstance().validate6(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertTrue("isValid(A) default", DateValidator.getInstance().isValid0(defaultVal));
        DateValidator.getInstance();
        assertTrue("isValid(A) locale ", DateValidator.getInstance().isValid2(localeVal, locale));
        DateValidator.getInstance();
        assertTrue("isValid(A) pattern", DateValidator.getInstance().isValid1(patternVal, pattern));
        DateValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                DateValidator.getInstance().isValid3(germanVal, germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertNull("validate(B) default", DateValidator.getInstance().validate0(XXXX));
        DateValidator.getInstance();
        assertNull("validate(B) locale ", DateValidator.getInstance().validate4(XXXX, locale));
        DateValidator.getInstance();
        assertNull("validate(B) pattern", DateValidator.getInstance().validate2(XXXX, pattern));
        DateValidator.getInstance();
        assertNull(
                "validate(B) both",
                DateValidator.getInstance().validate6("31 Dec 2005", germanPattern, Locale.GERMAN));
        DateValidator.getInstance();
        assertFalse("isValid(B) default", DateValidator.getInstance().isValid0(XXXX));
        DateValidator.getInstance();
        assertFalse("isValid(B) locale ", DateValidator.getInstance().isValid2(XXXX, locale));
        DateValidator.getInstance();
        assertFalse("isValid(B) pattern", DateValidator.getInstance().isValid1(XXXX, pattern));
        DateValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                DateValidator.getInstance().isValid3("31 Dec 2005", germanPattern, Locale.GERMAN));
        TimeZone zone = (TimeZone.getDefault().getRawOffset() == EET.getRawOffset() ? EST : EET);
        Date expectedZone = createCalendar(zone, 20051231, 0).getTime();
        assertFalse("default/zone same " + zone, expected.getTime() == expectedZone.getTime());
        DateValidator.getInstance();
        assertEquals(
                "validate(C) default",
                expectedZone,
                DateValidator.getInstance().validate1(defaultVal, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) locale ",
                expectedZone,
                DateValidator.getInstance().validate5(localeVal, locale, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) pattern",
                expectedZone,
                DateValidator.getInstance().validate3(patternVal, pattern, zone));
        DateValidator.getInstance();
        assertEquals(
                "validate(C) both",
                expectedZone,
                DateValidator.getInstance()
                        .validate7(germanVal, germanPattern, Locale.GERMAN, zone));
    }

    @Test
    public void testCompare_test0_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
    }

    @Test
    public void testCompare_test1_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
    }

    @Test
    public void testCompare_test2_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
    }

    @Test
    public void testCompare_test3_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
    }

    @Test
    public void testCompare_test4_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
        assertEquals(
                "mnth LT", -1, dateValidator.compareMonths(value, date20050901, GMT));
        assertEquals(
                "mnth =1", 0, dateValidator.compareMonths(value, date20050830, GMT));
        assertEquals(
                "mnth =2", 0, dateValidator.compareMonths(value, date20050801, GMT));
        assertEquals(
                "mnth =3", 0, dateValidator.compareMonths(value, date20050816, GMT));
        assertEquals(
                "mnth GT", 1, dateValidator.compareMonths(value, date20050731, GMT));
    }

    @Test
    public void testCompare_test5_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
        assertEquals(
                "mnth LT", -1, dateValidator.compareMonths(value, date20050901, GMT));
        assertEquals(
                "mnth =1", 0, dateValidator.compareMonths(value, date20050830, GMT));
        assertEquals(
                "mnth =2", 0, dateValidator.compareMonths(value, date20050801, GMT));
        assertEquals(
                "mnth =3", 0, dateValidator.compareMonths(value, date20050816, GMT));
        assertEquals(
                "mnth GT", 1, dateValidator.compareMonths(value, date20050731, GMT));
        assertEquals(
                "qtrA <1",
                -1,
                dateValidator.compareQuarters0(value, date20051101, GMT));
        assertEquals(
                "qtrA <2",
                -1,
                dateValidator.compareQuarters0(value, date20051001, GMT));
        assertEquals(
                "qtrA =1", 0, dateValidator.compareQuarters0(value, date20050901, GMT));
        assertEquals(
                "qtrA =2",
                0,
                dateValidator.compareQuarters0(value, date20050701, GMT));
        assertEquals(
                "qtrA =3", 0, dateValidator.compareQuarters0(value, date20050731, GMT));
        assertEquals(
                "qtrA GT",
                1,
                dateValidator.compareQuarters0(value, date20050630, GMT));
    }

    @Test
    public void testCompare_test6_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
        assertEquals(
                "mnth LT", -1, dateValidator.compareMonths(value, date20050901, GMT));
        assertEquals(
                "mnth =1", 0, dateValidator.compareMonths(value, date20050830, GMT));
        assertEquals(
                "mnth =2", 0, dateValidator.compareMonths(value, date20050801, GMT));
        assertEquals(
                "mnth =3", 0, dateValidator.compareMonths(value, date20050816, GMT));
        assertEquals(
                "mnth GT", 1, dateValidator.compareMonths(value, date20050731, GMT));
        assertEquals(
                "qtrA <1",
                -1,
                dateValidator.compareQuarters0(value, date20051101, GMT));
        assertEquals(
                "qtrA <2",
                -1,
                dateValidator.compareQuarters0(value, date20051001, GMT));
        assertEquals(
                "qtrA =1", 0, dateValidator.compareQuarters0(value, date20050901, GMT));
        assertEquals(
                "qtrA =2",
                0,
                dateValidator.compareQuarters0(value, date20050701, GMT));
        assertEquals(
                "qtrA =3", 0, dateValidator.compareQuarters0(value, date20050731, GMT));
        assertEquals(
                "qtrA GT",
                1,
                dateValidator.compareQuarters0(value, date20050630, GMT));
        assertEquals(
                "qtrB LT",
                -1,
                dateValidator.compareQuarters1(value, date20051101, GMT, 2));
        assertEquals(
                "qtrB =1",
                0,
                dateValidator.compareQuarters1(value, date20051001, GMT, 2));
        assertEquals(
                "qtrB =2",
                0,
                dateValidator.compareQuarters1(value, date20050901, GMT, 2));
        assertEquals(
                "qtrB =3",
                1,
                dateValidator.compareQuarters1(value, date20050701, GMT, 2));
        assertEquals(
                "qtrB =4",
                1,
                dateValidator.compareQuarters1(value, date20050731, GMT, 2));
        assertEquals(
                "qtrB GT",
                1,
                dateValidator.compareQuarters1(value, date20050630, GMT, 2));
        assertEquals(
                "qtrB prev",
                1,
                dateValidator.compareQuarters1(value, date20050110, GMT, 2));
    }

    @Test
    public void testCompare_test7_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
        assertEquals(
                "mnth LT", -1, dateValidator.compareMonths(value, date20050901, GMT));
        assertEquals(
                "mnth =1", 0, dateValidator.compareMonths(value, date20050830, GMT));
        assertEquals(
                "mnth =2", 0, dateValidator.compareMonths(value, date20050801, GMT));
        assertEquals(
                "mnth =3", 0, dateValidator.compareMonths(value, date20050816, GMT));
        assertEquals(
                "mnth GT", 1, dateValidator.compareMonths(value, date20050731, GMT));
        assertEquals(
                "qtrA <1",
                -1,
                dateValidator.compareQuarters0(value, date20051101, GMT));
        assertEquals(
                "qtrA <2",
                -1,
                dateValidator.compareQuarters0(value, date20051001, GMT));
        assertEquals(
                "qtrA =1", 0, dateValidator.compareQuarters0(value, date20050901, GMT));
        assertEquals(
                "qtrA =2",
                0,
                dateValidator.compareQuarters0(value, date20050701, GMT));
        assertEquals(
                "qtrA =3", 0, dateValidator.compareQuarters0(value, date20050731, GMT));
        assertEquals(
                "qtrA GT",
                1,
                dateValidator.compareQuarters0(value, date20050630, GMT));
        assertEquals(
                "qtrB LT",
                -1,
                dateValidator.compareQuarters1(value, date20051101, GMT, 2));
        assertEquals(
                "qtrB =1",
                0,
                dateValidator.compareQuarters1(value, date20051001, GMT, 2));
        assertEquals(
                "qtrB =2",
                0,
                dateValidator.compareQuarters1(value, date20050901, GMT, 2));
        assertEquals(
                "qtrB =3",
                1,
                dateValidator.compareQuarters1(value, date20050701, GMT, 2));
        assertEquals(
                "qtrB =4",
                1,
                dateValidator.compareQuarters1(value, date20050731, GMT, 2));
        assertEquals(
                "qtrB GT",
                1,
                dateValidator.compareQuarters1(value, date20050630, GMT, 2));
        assertEquals(
                "qtrB prev",
                1,
                dateValidator.compareQuarters1(value, date20050110, GMT, 2));
        assertEquals(
                "year LT", -1, dateValidator.compareYears(value, date20060101, GMT));
        assertEquals(
                "year EQ", 0, dateValidator.compareYears(value, date20050101, GMT));
        assertEquals("year GT", 1, dateValidator.compareYears(value, date20041231, GMT));
    }

    @Test
    public void testCompare_test8_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
        assertEquals(
                "mnth LT", -1, dateValidator.compareMonths(value, date20050901, GMT));
        assertEquals(
                "mnth =1", 0, dateValidator.compareMonths(value, date20050830, GMT));
        assertEquals(
                "mnth =2", 0, dateValidator.compareMonths(value, date20050801, GMT));
        assertEquals(
                "mnth =3", 0, dateValidator.compareMonths(value, date20050816, GMT));
        assertEquals(
                "mnth GT", 1, dateValidator.compareMonths(value, date20050731, GMT));
        assertEquals(
                "qtrA <1",
                -1,
                dateValidator.compareQuarters0(value, date20051101, GMT));
        assertEquals(
                "qtrA <2",
                -1,
                dateValidator.compareQuarters0(value, date20051001, GMT));
        assertEquals(
                "qtrA =1", 0, dateValidator.compareQuarters0(value, date20050901, GMT));
        assertEquals(
                "qtrA =2",
                0,
                dateValidator.compareQuarters0(value, date20050701, GMT));
        assertEquals(
                "qtrA =3", 0, dateValidator.compareQuarters0(value, date20050731, GMT));
        assertEquals(
                "qtrA GT",
                1,
                dateValidator.compareQuarters0(value, date20050630, GMT));
        assertEquals(
                "qtrB LT",
                -1,
                dateValidator.compareQuarters1(value, date20051101, GMT, 2));
        assertEquals(
                "qtrB =1",
                0,
                dateValidator.compareQuarters1(value, date20051001, GMT, 2));
        assertEquals(
                "qtrB =2",
                0,
                dateValidator.compareQuarters1(value, date20050901, GMT, 2));
        assertEquals(
                "qtrB =3",
                1,
                dateValidator.compareQuarters1(value, date20050701, GMT, 2));
        assertEquals(
                "qtrB =4",
                1,
                dateValidator.compareQuarters1(value, date20050731, GMT, 2));
        assertEquals(
                "qtrB GT",
                1,
                dateValidator.compareQuarters1(value, date20050630, GMT, 2));
        assertEquals(
                "qtrB prev",
                1,
                dateValidator.compareQuarters1(value, date20050110, GMT, 2));
        assertEquals(
                "year LT", -1, dateValidator.compareYears(value, date20060101, GMT));
        assertEquals(
                "year EQ", 0, dateValidator.compareYears(value, date20050101, GMT));
        assertEquals("year GT", 1, dateValidator.compareYears(value, date20041231, GMT));
        Date sameDayTwoAm = createDate(GMT, testDate, 20000);
    }

    @Test
    public void testCompare_test9_decomposed()  {
        int sameTime = 124522;
        int testDate = 20050823;
        Date diffHour = createDate(GMT, testDate, 115922);
        Date value = createDate(GMT, testDate, sameTime);
        Date date20050824 = createDate(GMT, 20050824, sameTime);
        Date date20050822 = createDate(GMT, 20050822, sameTime);
        Date date20050830 = createDate(GMT, 20050830, sameTime);
        Date date20050816 = createDate(GMT, 20050816, sameTime);
        Date date20050901 = createDate(GMT, 20050901, sameTime);
        Date date20050801 = createDate(GMT, 20050801, sameTime);
        Date date20050731 = createDate(GMT, 20050731, sameTime);
        Date date20051101 = createDate(GMT, 20051101, sameTime);
        Date date20051001 = createDate(GMT, 20051001, sameTime);
        Date date20050701 = createDate(GMT, 20050701, sameTime);
        Date date20050630 = createDate(GMT, 20050630, sameTime);
        Date date20050110 = createDate(GMT, 20050110, sameTime);
        Date date20060101 = createDate(GMT, 20060101, sameTime);
        Date date20050101 = createDate(GMT, 20050101, sameTime);
        Date date20041231 = createDate(GMT, 20041231, sameTime);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, GMT));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, GMT));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, GMT));
        assertEquals(
                "week LT", -1, dateValidator.compareWeeks(value, date20050830, GMT));
        assertEquals("week =1", 0, dateValidator.compareWeeks(value, date20050824, GMT));
        assertEquals(
                "week =2", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week =3", 0, dateValidator.compareWeeks(value, date20050822, GMT));
        assertEquals("week GT", 1, dateValidator.compareWeeks(value, date20050816, GMT));
        assertEquals(
                "mnth LT", -1, dateValidator.compareMonths(value, date20050901, GMT));
        assertEquals(
                "mnth =1", 0, dateValidator.compareMonths(value, date20050830, GMT));
        assertEquals(
                "mnth =2", 0, dateValidator.compareMonths(value, date20050801, GMT));
        assertEquals(
                "mnth =3", 0, dateValidator.compareMonths(value, date20050816, GMT));
        assertEquals(
                "mnth GT", 1, dateValidator.compareMonths(value, date20050731, GMT));
        assertEquals(
                "qtrA <1",
                -1,
                dateValidator.compareQuarters0(value, date20051101, GMT));
        assertEquals(
                "qtrA <2",
                -1,
                dateValidator.compareQuarters0(value, date20051001, GMT));
        assertEquals(
                "qtrA =1", 0, dateValidator.compareQuarters0(value, date20050901, GMT));
        assertEquals(
                "qtrA =2",
                0,
                dateValidator.compareQuarters0(value, date20050701, GMT));
        assertEquals(
                "qtrA =3", 0, dateValidator.compareQuarters0(value, date20050731, GMT));
        assertEquals(
                "qtrA GT",
                1,
                dateValidator.compareQuarters0(value, date20050630, GMT));
        assertEquals(
                "qtrB LT",
                -1,
                dateValidator.compareQuarters1(value, date20051101, GMT, 2));
        assertEquals(
                "qtrB =1",
                0,
                dateValidator.compareQuarters1(value, date20051001, GMT, 2));
        assertEquals(
                "qtrB =2",
                0,
                dateValidator.compareQuarters1(value, date20050901, GMT, 2));
        assertEquals(
                "qtrB =3",
                1,
                dateValidator.compareQuarters1(value, date20050701, GMT, 2));
        assertEquals(
                "qtrB =4",
                1,
                dateValidator.compareQuarters1(value, date20050731, GMT, 2));
        assertEquals(
                "qtrB GT",
                1,
                dateValidator.compareQuarters1(value, date20050630, GMT, 2));
        assertEquals(
                "qtrB prev",
                1,
                dateValidator.compareQuarters1(value, date20050110, GMT, 2));
        assertEquals(
                "year LT", -1, dateValidator.compareYears(value, date20060101, GMT));
        assertEquals(
                "year EQ", 0, dateValidator.compareYears(value, date20050101, GMT));
        assertEquals("year GT", 1, dateValidator.compareYears(value, date20041231, GMT));
        Date sameDayTwoAm = createDate(GMT, testDate, 20000);
        assertEquals("date LT", -1, dateValidator.compareDates(value, date20050824, EST));
        assertEquals(
                "date EQ",
                0,
                dateValidator.compareDates(value, diffHour, EST));
        assertEquals(
                "date EQ",
                1,
                dateValidator.compareDates(value, sameDayTwoAm, EST));
        assertEquals("date GT", 1, dateValidator.compareDates(value, date20050822, EST));
    }
}