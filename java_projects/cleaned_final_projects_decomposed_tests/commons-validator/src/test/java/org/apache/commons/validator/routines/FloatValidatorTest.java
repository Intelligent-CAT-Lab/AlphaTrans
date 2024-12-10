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

import java.text.DecimalFormat;
import java.util.Locale;

/**
 * Test Case for FloatValidator.
 *
 * @version $Revision$
 */
public class FloatValidatorTest extends AbstractNumberValidatorTest {

    /**
     * Constructor
     *
     * @param name test name
     */
    public FloatValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new FloatValidator(false, 0);
        strictValidator = FloatValidator.FloatValidator1();

        testPattern = "#,###.#";

        max = Float.valueOf(Float.MAX_VALUE);
        maxPlusOne = Double.valueOf(max.doubleValue() * 10);
        min = Float.valueOf(Float.MAX_VALUE * -1);
        minMinusOne = Double.valueOf(min.doubleValue() * 10);

        invalidStrict = new String[] {null, "", "X", "X12", "12X", "1X2"};

        invalid = new String[] {null, "", "X", "X12"};

        testNumber = Float.valueOf(1234.5f);
        testZero = Float.valueOf(0);
        validStrict = new String[] {"0", "1234.5", "1,234.5"};
        validStrictCompare = new Number[] {testZero, testNumber, testNumber};
        valid = new String[] {"0", "1234.5", "1,234.5", "1,234.5", "1234.5X"};
        validCompare = new Number[] {testZero, testNumber, testNumber, testNumber, testNumber};

        testStringUS = "1,234.5";
        testStringDE = "1.234,5";

        localeValue = testStringDE;
        localePattern = "#.###,#";
        testLocale = Locale.GERMANY;
        localeExpected = testNumber;
    }

    /** Test FloatValidator validate Methods */
    

    /**
     * Test Float validation for values too small to handle. (slightly different from max/min which
     * are the largest +ve/-ve
     */
    

    /** Test Float Range/Min/Max */

    @Test
    public void testFloatValidatorMethods_test0_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test1_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
    }

    @Test
    public void testFloatValidatorMethods_test2_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test3_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
    }

    @Test
    public void testFloatValidatorMethods_test4_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test5_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
    }

    @Test
    public void testFloatValidatorMethods_test6_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test7_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testFloatValidatorMethods_test8_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test9_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testFloatValidatorMethods_test10_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test11_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testFloatValidatorMethods_test12_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test13_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testFloatValidatorMethods_test14_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test15_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testFloatValidatorMethods_test16_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test17_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testFloatValidatorMethods_test18_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test19_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
    }

    @Test
    public void testFloatValidatorMethods_test20_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test21_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
    }

    @Test
    public void testFloatValidatorMethods_test22_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test23_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testFloatValidatorMethods_test24_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test25_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testFloatValidatorMethods_test26_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test27_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
        FloatValidator.getInstance();
        assertFalse("isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testFloatValidatorMethods_test28_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
        FloatValidator.getInstance();
        assertFalse("isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test29_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
        FloatValidator.getInstance();
        assertFalse("isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale));
        FloatValidator.getInstance();
        assertFalse("isValid(B) pattern", FloatValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testFloatValidatorMethods_test30_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
        FloatValidator.getInstance();
        assertFalse("isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale));
        FloatValidator.getInstance();
        assertFalse("isValid(B) pattern", FloatValidator.getInstance().isValid1(XXXX, pattern));
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatValidatorMethods_test31_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String localeVal = "12.345";
        String germanPatternVal = "1.23.45";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Float expected = Float.valueOf(12345);
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                FloatValidator.getInstance().validate0(defaultVal));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                FloatValidator.getInstance().validate2(localeVal, locale));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                FloatValidator.getInstance().validate1(patternVal, pattern));
        FloatValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                FloatValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertTrue("isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal));
        FloatValidator.getInstance();
        assertTrue("isValid(A) locale ", FloatValidator.getInstance().isValid2(localeVal, locale));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", FloatValidator.getInstance().isValid1(patternVal, pattern));
        FloatValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                FloatValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertNull("validate(B) default", FloatValidator.getInstance().validate0(XXXX));
        FloatValidator.getInstance();
        assertNull("validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale));
        FloatValidator.getInstance();
        assertNull("validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern));
        FloatValidator.getInstance();
        assertNull(
                "validate(B) both",
                FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        FloatValidator.getInstance();
        assertFalse("isValid(B) default", FloatValidator.getInstance().isValid0(XXXX));
        FloatValidator.getInstance();
        assertFalse("isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale));
        FloatValidator.getInstance();
        assertFalse("isValid(B) pattern", FloatValidator.getInstance().isValid1(XXXX, pattern));
        FloatValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                FloatValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testFloatSmallestValues_test0_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatSmallestValues_test1_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
    }

    @Test
    public void testFloatSmallestValues_test2_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
        Float smallestNegative = Float.valueOf(Float.MIN_VALUE * -1);
        String strSmallestNegative = fmt.format(smallestNegative);
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatSmallestValues_test3_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
        Float smallestNegative = Float.valueOf(Float.MIN_VALUE * -1);
        String strSmallestNegative = fmt.format(smallestNegative);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest -ve",
                smallestNegative,
                FloatValidator.getInstance().validate1(strSmallestNegative, pattern));
    }

    @Test
    public void testFloatSmallestValues_test4_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
        Float smallestNegative = Float.valueOf(Float.MIN_VALUE * -1);
        String strSmallestNegative = fmt.format(smallestNegative);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest -ve",
                smallestNegative,
                FloatValidator.getInstance().validate1(strSmallestNegative, pattern));
        Double tooSmallPositive = Double.valueOf(((double) Float.MIN_VALUE / (double) 10));
        String strTooSmallPositive = fmt.format(tooSmallPositive);
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatSmallestValues_test5_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
        Float smallestNegative = Float.valueOf(Float.MIN_VALUE * -1);
        String strSmallestNegative = fmt.format(smallestNegative);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest -ve",
                smallestNegative,
                FloatValidator.getInstance().validate1(strSmallestNegative, pattern));
        Double tooSmallPositive = Double.valueOf(((double) Float.MIN_VALUE / (double) 10));
        String strTooSmallPositive = fmt.format(tooSmallPositive);
        FloatValidator.getInstance();
        assertFalse(
                "Too small +ve",
                FloatValidator.getInstance().isValid1(strTooSmallPositive, pattern));
    }

    @Test
    public void testFloatSmallestValues_test6_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
        Float smallestNegative = Float.valueOf(Float.MIN_VALUE * -1);
        String strSmallestNegative = fmt.format(smallestNegative);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest -ve",
                smallestNegative,
                FloatValidator.getInstance().validate1(strSmallestNegative, pattern));
        Double tooSmallPositive = Double.valueOf(((double) Float.MIN_VALUE / (double) 10));
        String strTooSmallPositive = fmt.format(tooSmallPositive);
        FloatValidator.getInstance();
        assertFalse(
                "Too small +ve",
                FloatValidator.getInstance().isValid1(strTooSmallPositive, pattern));
        Double tooSmallNegative = Double.valueOf(tooSmallPositive.doubleValue() * -1);
        String strTooSmallNegative = fmt.format(tooSmallNegative);
        FloatValidator.getInstance();
    }

    @Test
    public void testFloatSmallestValues_test7_decomposed()  {
        String pattern = "#.#################################################################";
        DecimalFormat fmt = new DecimalFormat(pattern);
        Float smallestPositive = Float.valueOf(Float.MIN_VALUE);
        String strSmallestPositive = fmt.format(smallestPositive);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest +ve",
                smallestPositive,
                FloatValidator.getInstance().validate1(strSmallestPositive, pattern));
        Float smallestNegative = Float.valueOf(Float.MIN_VALUE * -1);
        String strSmallestNegative = fmt.format(smallestNegative);
        FloatValidator.getInstance();
        assertEquals(
                "Smallest -ve",
                smallestNegative,
                FloatValidator.getInstance().validate1(strSmallestNegative, pattern));
        Double tooSmallPositive = Double.valueOf(((double) Float.MIN_VALUE / (double) 10));
        String strTooSmallPositive = fmt.format(tooSmallPositive);
        FloatValidator.getInstance();
        assertFalse(
                "Too small +ve",
                FloatValidator.getInstance().isValid1(strTooSmallPositive, pattern));
        Double tooSmallNegative = Double.valueOf(tooSmallPositive.doubleValue() * -1);
        String strTooSmallNegative = fmt.format(tooSmallNegative);
        FloatValidator.getInstance();
        assertFalse(
                "Too small -ve",
                FloatValidator.getInstance().isValid1(strTooSmallNegative, pattern));
    }

    @Test
    public void testFloatRangeMinMax_test0_decomposed()  {
        FloatValidator validator = (FloatValidator) strictValidator;
        Float number9 = validator.validate1("9", "#");
    }

    @Test
    public void testFloatRangeMinMax_test1_decomposed()  {
        FloatValidator validator = (FloatValidator) strictValidator;
        Float number9 = validator.validate1("9", "#");
        Float number10 = validator.validate1("10", "#");
        Float number11 = validator.validate1("11", "#");
        Float number19 = validator.validate1("19", "#");
        Float number20 = validator.validate1("20", "#");
        Float number21 = validator.validate1("21", "#");
    }

    @Test
    public void testFloatRangeMinMax_test2_decomposed()  {
        FloatValidator validator = (FloatValidator) strictValidator;
        Float number9 = validator.validate1("9", "#");
        Float number10 = validator.validate1("10", "#");
        Float number11 = validator.validate1("11", "#");
        Float number19 = validator.validate1("19", "#");
        Float number20 = validator.validate1("20", "#");
        Float number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange1(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange1(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange1(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange1(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange1(number21, 10, 20));
    }

    @Test
    public void testFloatRangeMinMax_test3_decomposed()  {
        FloatValidator validator = (FloatValidator) strictValidator;
        Float number9 = validator.validate1("9", "#");
        Float number10 = validator.validate1("10", "#");
        Float number11 = validator.validate1("11", "#");
        Float number19 = validator.validate1("19", "#");
        Float number20 = validator.validate1("20", "#");
        Float number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange1(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange1(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange1(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange1(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange1(number21, 10, 20));
        assertFalse("minValue() < min", validator.minValue1(number9, 10));
        assertTrue("minValue() = min", validator.minValue1(number10, 10));
        assertTrue("minValue() > min", validator.minValue1(number11, 10));
    }

    @Test
    public void testFloatRangeMinMax_test4_decomposed()  {
        FloatValidator validator = (FloatValidator) strictValidator;
        Float number9 = validator.validate1("9", "#");
        Float number10 = validator.validate1("10", "#");
        Float number11 = validator.validate1("11", "#");
        Float number19 = validator.validate1("19", "#");
        Float number20 = validator.validate1("20", "#");
        Float number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange1(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange1(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange1(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange1(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange1(number21, 10, 20));
        assertFalse("minValue() < min", validator.minValue1(number9, 10));
        assertTrue("minValue() = min", validator.minValue1(number10, 10));
        assertTrue("minValue() > min", validator.minValue1(number11, 10));
        assertTrue("maxValue() < max", validator.maxValue1(number19, 20));
        assertTrue("maxValue() = max", validator.maxValue1(number20, 20));
        assertFalse("maxValue() > max", validator.maxValue1(number21, 20));
    }
}