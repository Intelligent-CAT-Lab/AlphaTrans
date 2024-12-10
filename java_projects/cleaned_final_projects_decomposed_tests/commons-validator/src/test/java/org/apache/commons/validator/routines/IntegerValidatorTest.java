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
 * Test Case for IntegerValidator.
 *
 * @version $Revision$
 */
public class IntegerValidatorTest extends AbstractNumberValidatorTest {

    private static final Integer INT_MIN_VAL = Integer.valueOf(Integer.MIN_VALUE);
    private static final Integer INT_MAX_VAL = Integer.valueOf(Integer.MAX_VALUE);
    private static final String INT_MAX = "2147483647";
    private static final String INT_MAX_0 =
            "2147483647.99999999999999999999999"; // force double rounding
    private static final String INT_MAX_1 = "2147483648";
    private static final String INT_MIN = "-2147483648";
    private static final String INT_MIN_0 =
            "-2147483648.99999999999999999999999"; // force double rounding";
    private static final String INT_MIN_1 = "-2147483649";

    /**
     * Constructor
     *
     * @param name test name
     */
    public IntegerValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new IntegerValidator(false, 0);
        strictValidator = IntegerValidator.IntegerValidator1();

        testPattern = "#,###";

        max = Integer.valueOf(Integer.MAX_VALUE);
        maxPlusOne = Long.valueOf(max.longValue() + 1);
        min = Integer.valueOf(Integer.MIN_VALUE);
        minMinusOne = Long.valueOf(min.longValue() - 1);

        invalidStrict =
                new String[] {null, "", "X", "X12", "12X", "1X2", "1.2", INT_MAX_1, INT_MIN_1};

        invalid = new String[] {null, "", "X", "X12", INT_MAX_1, INT_MIN_1};

        testNumber = Integer.valueOf(1234);
        testZero = Integer.valueOf(0);
        validStrict = new String[] {"0", "1234", "1,234", INT_MAX, INT_MIN};
        validStrictCompare =
                new Number[] {testZero, testNumber, testNumber, INT_MAX_VAL, INT_MIN_VAL};
        valid =
                new String[] {
                    "0", "1234", "1,234", "1,234.5", "1234X", INT_MAX, INT_MIN, INT_MAX_0, INT_MIN_0
                };
        validCompare =
                new Number[] {
                    testZero,
                    testNumber,
                    testNumber,
                    testNumber,
                    testNumber,
                    INT_MAX_VAL,
                    INT_MIN_VAL,
                    INT_MAX_VAL,
                    INT_MIN_VAL
                };

        testStringUS = "1,234";
        testStringDE = "1.234";

        localeValue = testStringDE;
        localePattern = "#.###";
        testLocale = Locale.GERMANY;
        localeExpected = testNumber;
    }

    /** Test IntegerValidator validate Methods */
    

    /** Test Integer Range/Min/Max */

    @Test
    public void testIntegerValidatorMethods_test0_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test1_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
    }

    @Test
    public void testIntegerValidatorMethods_test2_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test3_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
    }

    @Test
    public void testIntegerValidatorMethods_test4_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test5_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
    }

    @Test
    public void testIntegerValidatorMethods_test6_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test7_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testIntegerValidatorMethods_test8_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test9_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
    }

    @Test
    public void testIntegerValidatorMethods_test10_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test11_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
    }

    @Test
    public void testIntegerValidatorMethods_test12_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test13_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
    }

    @Test
    public void testIntegerValidatorMethods_test14_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test15_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testIntegerValidatorMethods_test16_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test17_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
    }

    @Test
    public void testIntegerValidatorMethods_test18_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test19_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
    }

    @Test
    public void testIntegerValidatorMethods_test20_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test21_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
    }

    @Test
    public void testIntegerValidatorMethods_test22_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test23_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testIntegerValidatorMethods_test24_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test25_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
    }

    @Test
    public void testIntegerValidatorMethods_test26_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test27_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", IntegerValidator.getInstance().isValid2(XXXX, locale));
    }

    @Test
    public void testIntegerValidatorMethods_test28_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", IntegerValidator.getInstance().isValid2(XXXX, locale));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test29_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", IntegerValidator.getInstance().isValid2(XXXX, locale));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) pattern", IntegerValidator.getInstance().isValid1(XXXX, pattern));
    }

    @Test
    public void testIntegerValidatorMethods_test30_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", IntegerValidator.getInstance().isValid2(XXXX, locale));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) pattern", IntegerValidator.getInstance().isValid1(XXXX, pattern));
        IntegerValidator.getInstance();
    }

    @Test
    public void testIntegerValidatorMethods_test31_decomposed()  {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Integer expected = Integer.valueOf(12345);
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) default",
                expected,
                IntegerValidator.getInstance().validate0(defaultVal));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) locale ",
                expected,
                IntegerValidator.getInstance().validate2(localeVal, locale));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) pattern",
                expected,
                IntegerValidator.getInstance().validate1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertEquals(
                "validate(A) both",
                expected,
                IntegerValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertTrue("isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) locale ", IntegerValidator.getInstance().isValid2(localeVal, locale));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) pattern", IntegerValidator.getInstance().isValid1(patternVal, pattern));
        IntegerValidator.getInstance();
        assertTrue(
                "isValid(A) both",
                IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertNull("validate(B) default", IntegerValidator.getInstance().validate0(XXXX));
        IntegerValidator.getInstance();
        assertNull("validate(B) locale ", IntegerValidator.getInstance().validate2(XXXX, locale));
        IntegerValidator.getInstance();
        assertNull("validate(B) pattern", IntegerValidator.getInstance().validate1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertNull(
                "validate(B) both",
                IntegerValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) locale ", IntegerValidator.getInstance().isValid2(XXXX, locale));
        IntegerValidator.getInstance();
        assertFalse("isValid(B) pattern", IntegerValidator.getInstance().isValid1(XXXX, pattern));
        IntegerValidator.getInstance();
        assertFalse(
                "isValid(B) both",
                IntegerValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    @Test
    public void testIntegerRangeMinMax_test0_decomposed()  {
        IntegerValidator validator = (IntegerValidator) strictValidator;
        Integer number9 = validator.validate1("9", "#");
    }

    @Test
    public void testIntegerRangeMinMax_test1_decomposed()  {
        IntegerValidator validator = (IntegerValidator) strictValidator;
        Integer number9 = validator.validate1("9", "#");
        Integer number10 = validator.validate1("10", "#");
        Integer number11 = validator.validate1("11", "#");
        Integer number19 = validator.validate1("19", "#");
        Integer number20 = validator.validate1("20", "#");
        Integer number21 = validator.validate1("21", "#");
    }

    @Test
    public void testIntegerRangeMinMax_test2_decomposed()  {
        IntegerValidator validator = (IntegerValidator) strictValidator;
        Integer number9 = validator.validate1("9", "#");
        Integer number10 = validator.validate1("10", "#");
        Integer number11 = validator.validate1("11", "#");
        Integer number19 = validator.validate1("19", "#");
        Integer number20 = validator.validate1("20", "#");
        Integer number21 = validator.validate1("21", "#");
        assertFalse("isInRange() < min", validator.isInRange1(number9, 10, 20));
        assertTrue("isInRange() = min", validator.isInRange1(number10, 10, 20));
        assertTrue("isInRange() in range", validator.isInRange1(number11, 10, 20));
        assertTrue("isInRange() = max", validator.isInRange1(number20, 10, 20));
        assertFalse("isInRange() > max", validator.isInRange1(number21, 10, 20));
    }

    @Test
    public void testIntegerRangeMinMax_test3_decomposed()  {
        IntegerValidator validator = (IntegerValidator) strictValidator;
        Integer number9 = validator.validate1("9", "#");
        Integer number10 = validator.validate1("10", "#");
        Integer number11 = validator.validate1("11", "#");
        Integer number19 = validator.validate1("19", "#");
        Integer number20 = validator.validate1("20", "#");
        Integer number21 = validator.validate1("21", "#");
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
    public void testIntegerRangeMinMax_test4_decomposed()  {
        IntegerValidator validator = (IntegerValidator) strictValidator;
        Integer number9 = validator.validate1("9", "#");
        Integer number10 = validator.validate1("10", "#");
        Integer number11 = validator.validate1("11", "#");
        Integer number19 = validator.validate1("19", "#");
        Integer number20 = validator.validate1("20", "#");
        Integer number21 = validator.validate1("21", "#");
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

    @Test
    public void testMinMaxValues_test0_decomposed()  {
        assertTrue("2147483647 is max integer", validator.isValid0("2147483647"));
        assertFalse("2147483648 > max integer", validator.isValid0("2147483648"));
        assertTrue("-2147483648 is min integer", validator.isValid0("-2147483648"));
        assertFalse("-2147483649 < min integer", validator.isValid0("-2147483649"));
    }
}