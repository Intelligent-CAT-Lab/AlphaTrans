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

import java.util.Locale;

/**
 * Test Case for LongValidator.
 *
 * @version $Revision$
 */
public class LongValidatorTest extends AbstractNumberValidatorTest {

    private static final Long LONG_MIN_VAL = Long.valueOf(Long.MIN_VALUE);
    private static final Long LONG_MAX_VAL = Long.valueOf(Long.MAX_VALUE);
    private static final String LONG_MAX = "9223372036854775807";
    private static final String LONG_MAX_0 =
            "9223372036854775807.99999999999999999999999"; // force double rounding
    private static final String LONG_MAX_1 = "9223372036854775808";
    private static final String LONG_MIN = "-9223372036854775808";
    private static final String LONG_MIN_0 =
            "-9223372036854775808.99999999999999999999999"; // force double rounding
    private static final String LONG_MIN_1 = "-9223372036854775809";

    private static final String NINES = "9999999999999999999999999999999999999";

    /**
     * Constructor
     *
     * @param name test name
     */
    public LongValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new LongValidator(false, 0);
        strictValidator = LongValidator.LongValidator1();

        testPattern = "#,###";

        max = null;
        maxPlusOne = null;
        min = null;
        minMinusOne = null;

        invalidStrict =
                new String[] {
                    null, "", "X", "X12", "12X", "1X2", "1.2", LONG_MAX_1, LONG_MIN_1, NINES
                };

        invalid = new String[] {null, "", "X", "X12", "", LONG_MAX_1, LONG_MIN_1, NINES};

        testNumber = Long.valueOf(1234);
        testZero = Long.valueOf(0);
        validStrict = new String[] {"0", "1234", "1,234", LONG_MAX, LONG_MIN};
        validStrictCompare =
                new Number[] {testZero, testNumber, testNumber, LONG_MAX_VAL, LONG_MIN_VAL};
        valid =
                new String[] {
                    "0",
                    "1234",
                    "1,234",
                    "1,234.5",
                    "1234X",
                    LONG_MAX,
                    LONG_MIN,
                    LONG_MAX_0,
                    LONG_MIN_0
                };
        validCompare =
                new Number[] {
                    testZero,
                    testNumber,
                    testNumber,
                    testNumber,
                    testNumber,
                    LONG_MAX_VAL,
                    LONG_MIN_VAL,
                    LONG_MAX_VAL,
                    LONG_MIN_VAL
                };

        testStringUS = "1,234";
        testStringDE = "1.234";

        localeValue = testStringDE;
        localePattern = "#.###";
        testLocale = Locale.GERMANY;
        localeExpected = testNumber;
    }

    /** Test LongValidator validate Methods */
    public void testLongValidatorMethods() {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Long expected = Long.valueOf(12345);
        assertEquals(
                "validate(A) default", expected, LongValidator.getInstance().validate0(defaultVal));
        assertEquals(
                "validate(A) locale ",
                expected,
                LongValidator.getInstance().validate2(localeVal, locale));
        assertEquals(
                "validate(A) pattern",
                expected,
                LongValidator.getInstance().validate1(patternVal, pattern));
        assertEquals(
                "validate(A) both",
                expected,
                LongValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));

        assertTrue("isValid(A) default", LongValidator.getInstance().isValid0(defaultVal));
        assertTrue("isValid(A) locale ", LongValidator.getInstance().isValid2(localeVal, locale));
        assertTrue("isValid(A) pattern", LongValidator.getInstance().isValid1(patternVal, pattern));
        assertTrue(
                "isValid(A) both",
                LongValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));

        assertNull("validate(B) default", LongValidator.getInstance().validate0(XXXX));
        assertNull("validate(B) locale ", LongValidator.getInstance().validate2(XXXX, locale));
        assertNull("validate(B) pattern", LongValidator.getInstance().validate1(XXXX, pattern));
        assertNull(
                "validate(B) both",
                LongValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));

        assertFalse("isValid(B) default", LongValidator.getInstance().isValid0(XXXX));
        assertFalse("isValid(B) locale ", LongValidator.getInstance().isValid2(XXXX, locale));
        assertFalse("isValid(B) pattern", LongValidator.getInstance().isValid1(XXXX, pattern));
        assertFalse(
                "isValid(B) both",
                LongValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    /** Test Long Range/Min/Max */
    public void testLongRangeMinMax() {
        LongValidator validator = (LongValidator) strictValidator;
        Long number9 = validator.validate1("9", "#");
        Long number10 = validator.validate1("10", "#");
        Long number11 = validator.validate1("11", "#");
        Long number19 = validator.validate1("19", "#");
        Long number20 = validator.validate1("20", "#");
        Long number21 = validator.validate1("21", "#");

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
