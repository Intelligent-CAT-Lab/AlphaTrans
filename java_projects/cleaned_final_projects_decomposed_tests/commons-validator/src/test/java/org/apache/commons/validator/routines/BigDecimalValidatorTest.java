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

import java.math.BigDecimal;
import java.util.Locale;

/**
 * Test Case for BigDecimalValidator.
 *
 * @version $Revision$
 */
public class BigDecimalValidatorTest extends AbstractNumberValidatorTest {

    /**
     * Constructor
     *
     * @param name test name
     */
    public BigDecimalValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = BigDecimalValidator.BigDecimalValidator1(false);
        strictValidator = BigDecimalValidator.BigDecimalValidator2();

        testPattern = "#,###.###";

        max = null;
        maxPlusOne = null;
        min = null;
        minMinusOne = null;

        invalidStrict = new String[] {null, "", "X", "X12", "12X", "1X2", "1.234X"};

        invalid = new String[] {null, "", "X", "X12"};

        testNumber = new BigDecimal("1234.5");
        Number testNumber2 = new BigDecimal(".1");
        Number testNumber3 = new BigDecimal("12345.67899");
        testZero = new BigDecimal("0");
        validStrict = new String[] {"0", "1234.5", "1,234.5", ".1", "12345.678990"};
        validStrictCompare =
                new Number[] {testZero, testNumber, testNumber, testNumber2, testNumber3};
        valid = new String[] {"0", "1234.5", "1,234.5", "1,234.5", "1234.5X"};
        validCompare = new Number[] {testZero, testNumber, testNumber, testNumber, testNumber};

        testStringUS = "1,234.5";
        testStringDE = "1.234,5";

        localeValue = testStringDE;
        localePattern = "#.###,#";
        testLocale = Locale.GERMANY;
        localeExpected = testNumber;
    }

    /** Test BigDecimalValidator validate Methods */
    

    /** Test BigDecimal Range/Min/Max */

    @Test
    public void testBigDecimalValidatorMethods_test0_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test1_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
    }

    @Test
    public void testBigDecimalValidatorMethods_test2_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test3_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
    }

    @Test
    public void testBigDecimalValidatorMethods_test4_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test5_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
    }

    @Test
    public void testBigDecimalValidatorMethods_test6_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test7_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigDecimalValidatorMethods_test8_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test9_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testBigDecimalValidatorMethods_test10_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test11_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testBigDecimalValidatorMethods_test12_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test13_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testBigDecimalValidatorMethods_test14_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test15_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigDecimalValidatorMethods_test16_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test17_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testBigDecimalValidatorMethods_test18_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test19_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
    }

    @Test
    public void testBigDecimalValidatorMethods_test20_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test21_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
    }

    @Test
    public void testBigDecimalValidatorMethods_test22_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test23_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigDecimalValidatorMethods_test24_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test25_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testBigDecimalValidatorMethods_test26_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test27_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) locale ", BigDecimalValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testBigDecimalValidatorMethods_test28_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) locale ", BigDecimalValidator.getInstance().isValid2(XXXX, locale));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test29_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) locale ", BigDecimalValidator.getInstance().isValid2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertFalse(
                "isValid(B) pattern", BigDecimalValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testBigDecimalValidatorMethods_test30_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) locale ", BigDecimalValidator.getInstance().isValid2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertFalse(
                "isValid(B) pattern", BigDecimalValidator.getInstance().isValid1(XXXX, pattern));
        BigDecimalValidator.getInstance();
    }

    @Test
    public void testBigDecimalValidatorMethods_test31_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigDecimal expected = new BigDecimal(12345);
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigDecimalValidator.getInstance().validate0(defaultVal));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigDecimalValidator.getInstance().validate2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigDecimalValidator.getInstance().validate1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigDecimalValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertTrue("isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigDecimalValidator.getInstance().isValid2(localeVal, locale));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigDecimalValidator.getInstance().isValid1(patternVal, pattern));
        BigDecimalValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigDecimalValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertNull("validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigDecimalValidator.getInstance().validate2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigDecimalValidator.getInstance().validate1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigDecimalValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX));
        BigDecimalValidator.getInstance();
        assertFalse("isValid(B) locale ", BigDecimalValidator.getInstance().isValid2(XXXX, locale));
        BigDecimalValidator.getInstance();
        assertFalse(
                "isValid(B) pattern", BigDecimalValidator.getInstance().isValid1(XXXX, pattern));
        BigDecimalValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                BigDecimalValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigDecimalRangeMinMax_test0_decomposed()  {
        BigDecimalValidator validator =
                new BigDecimalValidator(true, AbstractNumberValidator.STANDARD_FORMAT, true);
    }

    @Test
    public void testBigDecimalRangeMinMax_test1_decomposed()  {
        BigDecimalValidator validator =
                new BigDecimalValidator(true, AbstractNumberValidator.STANDARD_FORMAT, true);
        BigDecimal number9 = new BigDecimal("9");
        BigDecimal number10 = new BigDecimal("10");
        BigDecimal number11 = new BigDecimal("11");
        BigDecimal number19 = new BigDecimal("19");
        BigDecimal number20 = new BigDecimal("20");
        BigDecimal number21 = new BigDecimal("21");
        float min = 10;
        float max = 20;
        assertFalse("isInRange(A) < min", validator.isInRange(number9, min, max));
    }

    @Test
    public void testBigDecimalRangeMinMax_test2_decomposed()  {
        BigDecimalValidator validator =
                new BigDecimalValidator(true, AbstractNumberValidator.STANDARD_FORMAT, true);
        BigDecimal number9 = new BigDecimal("9");
        BigDecimal number10 = new BigDecimal("10");
        BigDecimal number11 = new BigDecimal("11");
        BigDecimal number19 = new BigDecimal("19");
        BigDecimal number20 = new BigDecimal("20");
        BigDecimal number21 = new BigDecimal("21");
        float min = 10;
        float max = 20;
        assertFalse("isInRange(A) < min", validator.isInRange(number9, min, max));
        assertTrue("isInRange(A) = min", validator.isInRange(number10, min, max));
        assertTrue("isInRange(A) in range", validator.isInRange(number11, min, max));
        assertTrue("isInRange(A) = max", validator.isInRange(number20, min, max));
        assertFalse("isInRange(A) > max", validator.isInRange(number21, min, max));
    }

    @Test
    public void testBigDecimalRangeMinMax_test3_decomposed()  {
        BigDecimalValidator validator =
                new BigDecimalValidator(true, AbstractNumberValidator.STANDARD_FORMAT, true);
        BigDecimal number9 = new BigDecimal("9");
        BigDecimal number10 = new BigDecimal("10");
        BigDecimal number11 = new BigDecimal("11");
        BigDecimal number19 = new BigDecimal("19");
        BigDecimal number20 = new BigDecimal("20");
        BigDecimal number21 = new BigDecimal("21");
        float min = 10;
        float max = 20;
        assertFalse("isInRange(A) < min", validator.isInRange(number9, min, max));
        assertTrue("isInRange(A) = min", validator.isInRange(number10, min, max));
        assertTrue("isInRange(A) in range", validator.isInRange(number11, min, max));
        assertTrue("isInRange(A) = max", validator.isInRange(number20, min, max));
        assertFalse("isInRange(A) > max", validator.isInRange(number21, min, max));
        assertFalse("minValue(A) < min", validator.minValue(number9, min));
        assertTrue("minValue(A) = min", validator.minValue(number10, min));
        assertTrue("minValue(A) > min", validator.minValue(number11, min));
    }

    @Test
    public void testBigDecimalRangeMinMax_test4_decomposed()  {
        BigDecimalValidator validator =
                new BigDecimalValidator(true, AbstractNumberValidator.STANDARD_FORMAT, true);
        BigDecimal number9 = new BigDecimal("9");
        BigDecimal number10 = new BigDecimal("10");
        BigDecimal number11 = new BigDecimal("11");
        BigDecimal number19 = new BigDecimal("19");
        BigDecimal number20 = new BigDecimal("20");
        BigDecimal number21 = new BigDecimal("21");
        float min = 10;
        float max = 20;
        assertFalse("isInRange(A) < min", validator.isInRange(number9, min, max));
        assertTrue("isInRange(A) = min", validator.isInRange(number10, min, max));
        assertTrue("isInRange(A) in range", validator.isInRange(number11, min, max));
        assertTrue("isInRange(A) = max", validator.isInRange(number20, min, max));
        assertFalse("isInRange(A) > max", validator.isInRange(number21, min, max));
        assertFalse("minValue(A) < min", validator.minValue(number9, min));
        assertTrue("minValue(A) = min", validator.minValue(number10, min));
        assertTrue("minValue(A) > min", validator.minValue(number11, min));
        assertTrue("maxValue(A) < max", validator.maxValue(number19, max));
        assertTrue("maxValue(A) = max", validator.maxValue(number20, max));
        assertFalse("maxValue(A) > max", validator.maxValue(number21, max));
    }
}