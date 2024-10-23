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

import java.math.BigInteger;
import java.util.Locale;

/**
 * Test Case for BigIntegerValidator.
 *
 * @version $Revision$
 */
public class BigIntegerValidatorTest extends AbstractNumberValidatorTest {

    /**
     * Constructor
     *
     * @param name test name
     */
    public BigIntegerValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new BigIntegerValidator(false, 0);
        strictValidator = BigIntegerValidator.BigIntegerValidator1();

        testPattern = "#,###";

        max = null;
        maxPlusOne = null;
        min = null;
        minMinusOne = null;

        invalidStrict = new String[] {null, "", "X", "X12", "12X", "1X2", "1.2"};

        invalid = new String[] {null, "", "X", "X12"};

        testNumber = new BigInteger("1234");
        testZero = new BigInteger("0");
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

    /** Test BigIntegerValidator validate Methods */
    

    /** Test BigInteger Range/Min/Max */

    @Test
    public void testBigIntegerValidatorMethods_test0_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test1_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
    }

    @Test
    public void testBigIntegerValidatorMethods_test2_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test3_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
    }

    @Test
    public void testBigIntegerValidatorMethods_test4_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test5_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
    }

    @Test
    public void testBigIntegerValidatorMethods_test6_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test7_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigIntegerValidatorMethods_test8_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test9_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testBigIntegerValidatorMethods_test10_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test11_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testBigIntegerValidatorMethods_test12_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test13_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testBigIntegerValidatorMethods_test14_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test15_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigIntegerValidatorMethods_test16_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test17_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testBigIntegerValidatorMethods_test18_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test19_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
    }

    @Test
    public void testBigIntegerValidatorMethods_test20_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test21_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
    }

    @Test
    public void testBigIntegerValidatorMethods_test22_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test23_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigIntegerValidatorMethods_test24_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test25_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testBigIntegerValidatorMethods_test26_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test27_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", BigIntegerValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testBigIntegerValidatorMethods_test28_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", BigIntegerValidator.getInstance().isValid2(XXXX, locale));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test29_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", BigIntegerValidator.getInstance().isValid2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertFalse(
                "isValid(B) pattern", BigIntegerValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testBigIntegerValidatorMethods_test30_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", BigIntegerValidator.getInstance().isValid2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertFalse(
                "isValid(B) pattern", BigIntegerValidator.getInstance().isValid1(XXXX, pattern));
        BigIntegerValidator.getInstance();
    }

    @Test
    public void testBigIntegerValidatorMethods_test31_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        BigInteger expected = new BigInteger("12345");
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                BigIntegerValidator.getInstance().validate0(defaultVal));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                BigIntegerValidator.getInstance().validate2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                BigIntegerValidator.getInstance().validate1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                BigIntegerValidator.getInstance()
                        .validate3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertTrue("isValid(A) default", BigIntegerValidator.getInstance().isValid0(defaultVal));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ",
                BigIntegerValidator.getInstance().isValid2(localeVal, locale));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern",
                BigIntegerValidator.getInstance().isValid1(patternVal, pattern));
        BigIntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                BigIntegerValidator.getInstance()
                        .isValid3(germanPatternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertNull("validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) locale ", BigIntegerValidator.getInstance().validate2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) pattern", BigIntegerValidator.getInstance().validate1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                BigIntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX));
        BigIntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", BigIntegerValidator.getInstance().isValid2(XXXX, locale));
        BigIntegerValidator.getInstance();
        assertFalse(
                "isValid(B) pattern", BigIntegerValidator.getInstance().isValid1(XXXX, pattern));
        BigIntegerValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                BigIntegerValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testBigIntegerRangeMinMax_test0_decomposed()  {
        BigIntegerValidator validator = (BigIntegerValidator) strictValidator;
        BigInteger number9 = validator.validate1("9", "#");
    }

    @Test
    public void testBigIntegerRangeMinMax_test1_decomposed()  {
        BigIntegerValidator validator = (BigIntegerValidator) strictValidator;
        BigInteger number9 = validator.validate1("9", "#");
        BigInteger number10 = validator.validate1("10", "#");
        BigInteger number11 = validator.validate1("11", "#");
        BigInteger number19 = validator.validate1("19", "#");
        BigInteger number20 = validator.validate1("20", "#");
        BigInteger number21 = validator.validate1("21", "#");
    }

    @Test
    public void testBigIntegerRangeMinMax_test2_decomposed()  {
        BigIntegerValidator validator = (BigIntegerValidator) strictValidator;
        BigInteger number9 = validator.validate1("9", "#");
        BigInteger number10 = validator.validate1("10", "#");
        BigInteger number11 = validator.validate1("11", "#");
        BigInteger number19 = validator.validate1("19", "#");
        BigInteger number20 = validator.validate1("20", "#");
        BigInteger number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange(number21, 10, 20));
    }

    @Test
    public void testBigIntegerRangeMinMax_test3_decomposed()  {
        BigIntegerValidator validator = (BigIntegerValidator) strictValidator;
        BigInteger number9 = validator.validate1("9", "#");
        BigInteger number10 = validator.validate1("10", "#");
        BigInteger number11 = validator.validate1("11", "#");
        BigInteger number19 = validator.validate1("19", "#");
        BigInteger number20 = validator.validate1("20", "#");
        BigInteger number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange(number21, 10, 20));
        assertFalse("minValue() < min", validator.minValue(number9, 10));
        assertTrue("minValue() = min", validator.minValue(number10, 10));
        assertTrue("minValue() > min", validator.minValue(number11, 10));
    }

    @Test
    public void testBigIntegerRangeMinMax_test4_decomposed()  {
        BigIntegerValidator validator = (BigIntegerValidator) strictValidator;
        BigInteger number9 = validator.validate1("9", "#");
        BigInteger number10 = validator.validate1("10", "#");
        BigInteger number11 = validator.validate1("11", "#");
        BigInteger number19 = validator.validate1("19", "#");
        BigInteger number20 = validator.validate1("20", "#");
        BigInteger number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange(number21, 10, 20));
        assertFalse("minValue() < min", validator.minValue(number9, 10));
        assertTrue("minValue() = min", validator.minValue(number10, 10));
        assertTrue("minValue() > min", validator.minValue(number11, 10));
        assertTrue("maxValue() < max", validator.maxValue(number19, 20));
        assertTrue("maxValue() = max", validator.maxValue(number20, 20));
        assertFalse("maxValue() > max", validator.maxValue(number21, 20));
    }
}