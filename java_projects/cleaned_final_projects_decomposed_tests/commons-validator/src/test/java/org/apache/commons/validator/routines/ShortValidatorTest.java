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

import java.util.Locale;

/**
 * Test Case for ShortValidator.
 *
 * @version $Revision$
 */
public class ShortValidatorTest extends AbstractNumberValidatorTest {

    /**
     * Constructor
     *
     * @param name test name
     */
    public ShortValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new ShortValidator(false, 0);
        strictValidator = ShortValidator.ShortValidator1();

        testPattern = "#,###";

        max = Short.valueOf(Short.MAX_VALUE);
        maxPlusOne = Long.valueOf(max.longValue() + 1);
        min = Short.valueOf(Short.MIN_VALUE);
        minMinusOne = Long.valueOf(min.longValue() - 1);

        invalidStrict = new String[] {null, "", "X", "X12", "12X", "1X2", "1.2"};

        invalid = new String[] {null, "", "X", "X12"};

        testNumber = Short.valueOf((short) 1234);
        testZero = Short.valueOf((short) 0);
        validStrict = new String[] {"0", "1234", "1,234"};
        validStrictCompare = new Number[] {testZero, testNumber, testNumber};
        valid = new String[] {"0", "1234", "1,234", "1,234.5", "1234X"};
        validCompare = new Number[] {testZero, testNumber, testNumber, testNumber, testNumber};

        testStringUS = "1,234";
        testStringDE = "1.234";

        localeValue = testStringDE;
        localePattern = "#.###";
        testLocale = Locale.GERMANY;
        localeExpected = testNumber;
    }

    /** Test ShortValidator validate Methods */
    

    /** Test Short Range/Min/Max */

    @Test
    public void testShortValidatorMethods_test0_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test1_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
    }

    @Test
    public void testShortValidatorMethods_test2_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test3_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
    }

    @Test
    public void testShortValidatorMethods_test4_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test5_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
    }

    @Test
    public void testShortValidatorMethods_test6_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test7_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testShortValidatorMethods_test8_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test9_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testShortValidatorMethods_test10_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test11_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testShortValidatorMethods_test12_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test13_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testShortValidatorMethods_test14_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test15_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testShortValidatorMethods_test16_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test17_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testShortValidatorMethods_test18_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test19_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
    }

    @Test
    public void testShortValidatorMethods_test20_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test21_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
    }

    @Test
    public void testShortValidatorMethods_test22_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test23_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testShortValidatorMethods_test24_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test25_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testShortValidatorMethods_test26_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test27_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
        ShortValidator.getInstance();
        assertFalse("isValid(B) locale ", ShortValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testShortValidatorMethods_test28_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
        ShortValidator.getInstance();
        assertFalse("isValid(B) locale ", ShortValidator.getInstance().isValid2(XXXX, locale));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test29_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
        ShortValidator.getInstance();
        assertFalse("isValid(B) locale ", ShortValidator.getInstance().isValid2(XXXX, locale));
        ShortValidator.getInstance();
        assertFalse("isValid(B) pattern", ShortValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testShortValidatorMethods_test30_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
        ShortValidator.getInstance();
        assertFalse("isValid(B) locale ", ShortValidator.getInstance().isValid2(XXXX, locale));
        ShortValidator.getInstance();
        assertFalse("isValid(B) pattern", ShortValidator.getInstance().isValid1(XXXX, pattern));
        ShortValidator.getInstance();
    }

    @Test
    public void testShortValidatorMethods_test31_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Short expected = Short.valueOf((short) 12345);
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                ShortValidator.getInstance().validate0(defaultVal));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                ShortValidator.getInstance().validate2(localeVal, locale));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                ShortValidator.getInstance().validate1(patternVal, pattern));
        ShortValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                ShortValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertTrue("isValid(A) default", ShortValidator.getInstance().isValid0(defaultVal));
        ShortValidator.getInstance();
        assertTrue("isValid(A) locale ", ShortValidator.getInstance().isValid2(localeVal, locale));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", ShortValidator.getInstance().isValid1(patternVal, pattern));
        ShortValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                ShortValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertNull("validate(B) default", ShortValidator.getInstance().validate0(XXXX));
        ShortValidator.getInstance();
        assertNull("validate(B) locale ", ShortValidator.getInstance().validate2(XXXX, locale));
        ShortValidator.getInstance();
        assertNull("validate(B) pattern", ShortValidator.getInstance().validate1(XXXX, pattern));
        ShortValidator.getInstance();
        assertNull(
                "validate(B) both",
                ShortValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        ShortValidator.getInstance();
        assertFalse("isValid(B) default", ShortValidator.getInstance().isValid0(XXXX));
        ShortValidator.getInstance();
        assertFalse("isValid(B) locale ", ShortValidator.getInstance().isValid2(XXXX, locale));
        ShortValidator.getInstance();
        assertFalse("isValid(B) pattern", ShortValidator.getInstance().isValid1(XXXX, pattern));
        ShortValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                ShortValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testShortRangeMinMax_test0_decomposed()  {
        ShortValidator validator = (ShortValidator) strictValidator;
        Short number9 = validator.validate1("9", "#");
    }

    @Test
    public void testShortRangeMinMax_test1_decomposed()  {
        ShortValidator validator = (ShortValidator) strictValidator;
        Short number9 = validator.validate1("9", "#");
        Short number10 = validator.validate1("10", "#");
        Short number11 = validator.validate1("11", "#");
        Short number19 = validator.validate1("19", "#");
        Short number20 = validator.validate1("20", "#");
        Short number21 = validator.validate1("21", "#");
    }

    @Test
    public void testShortRangeMinMax_test2_decomposed()  {
        ShortValidator validator = (ShortValidator) strictValidator;
        Short number9 = validator.validate1("9", "#");
        Short number10 = validator.validate1("10", "#");
        Short number11 = validator.validate1("11", "#");
        Short number19 = validator.validate1("19", "#");
        Short number20 = validator.validate1("20", "#");
        Short number21 = validator.validate1("21", "#");
        short min = (short) 10;
        short max = (short) 20;
        assertFalse("isInRange() < min", validator.isInRange1(number9, min, max));
    }

    @Test
    public void testShortRangeMinMax_test3_decomposed()  {
        ShortValidator validator = (ShortValidator) strictValidator;
        Short number9 = validator.validate1("9", "#");
        Short number10 = validator.validate1("10", "#");
        Short number11 = validator.validate1("11", "#");
        Short number19 = validator.validate1("19", "#");
        Short number20 = validator.validate1("20", "#");
        Short number21 = validator.validate1("21", "#");
        short min = (short) 10;
        short max = (short) 20;
        assertFalse("isInRange() < min", validator.isInRange1(number9, min, max));
        assertTrue("isInRange() = min", validator.isInRange1(number10, min, max));
        assertTrue("isInRange() in range", validator.isInRange1(number11, min, max));
        assertTrue("isInRange() = max", validator.isInRange1(number20, min, max));
        assertFalse("isInRange() > max", validator.isInRange1(number21, min, max));
    }

    @Test
    public void testShortRangeMinMax_test4_decomposed()  {
        ShortValidator validator = (ShortValidator) strictValidator;
        Short number9 = validator.validate1("9", "#");
        Short number10 = validator.validate1("10", "#");
        Short number11 = validator.validate1("11", "#");
        Short number19 = validator.validate1("19", "#");
        Short number20 = validator.validate1("20", "#");
        Short number21 = validator.validate1("21", "#");
        short min = (short) 10;
        short max = (short) 20;
        assertFalse("isInRange() < min", validator.isInRange1(number9, min, max));
        assertTrue("isInRange() = min", validator.isInRange1(number10, min, max));
        assertTrue("isInRange() in range", validator.isInRange1(number11, min, max));
        assertTrue("isInRange() = max", validator.isInRange1(number20, min, max));
        assertFalse("isInRange() > max", validator.isInRange1(number21, min, max));
        assertFalse("minValue() < min", validator.minValue1(number9, min));
        assertTrue("minValue() = min", validator.minValue1(number10, min));
        assertTrue("minValue() > min", validator.minValue1(number11, min));
    }

    @Test
    public void testShortRangeMinMax_test5_decomposed()  {
        ShortValidator validator = (ShortValidator) strictValidator;
        Short number9 = validator.validate1("9", "#");
        Short number10 = validator.validate1("10", "#");
        Short number11 = validator.validate1("11", "#");
        Short number19 = validator.validate1("19", "#");
        Short number20 = validator.validate1("20", "#");
        Short number21 = validator.validate1("21", "#");
        short min = (short) 10;
        short max = (short) 20;
        assertFalse("isInRange() < min", validator.isInRange1(number9, min, max));
        assertTrue("isInRange() = min", validator.isInRange1(number10, min, max));
        assertTrue("isInRange() in range", validator.isInRange1(number11, min, max));
        assertTrue("isInRange() = max", validator.isInRange1(number20, min, max));
        assertFalse("isInRange() > max", validator.isInRange1(number21, min, max));
        assertFalse("minValue() < min", validator.minValue1(number9, min));
        assertTrue("minValue() = min", validator.minValue1(number10, min));
        assertTrue("minValue() > min", validator.minValue1(number11, min));
        assertTrue("maxValue() < max", validator.maxValue1(number19, max));
        assertTrue("maxValue() = max", validator.maxValue1(number20, max));
        assertFalse("maxValue() > max", validator.maxValue1(number21, max));
    }
}