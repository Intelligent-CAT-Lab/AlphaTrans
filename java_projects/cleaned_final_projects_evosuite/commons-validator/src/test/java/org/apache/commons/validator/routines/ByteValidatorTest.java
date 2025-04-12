
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

import java.util.Locale;

/**
 * Test Case for ByteValidator.
 *
 * @version $Revision$
 */
public class ByteValidatorTest extends AbstractNumberValidatorTest {

    private static final Byte BYTE_MIN_VAL = Byte.valueOf(Byte.MIN_VALUE);
    private static final Byte BYTE_MAX_VAL = Byte.valueOf(Byte.MAX_VALUE);
    private static final String BYTE_MAX = "127";
    private static final String BYTE_MAX_0 = "127.99999999999999999999999"; // force double rounding
    private static final String BYTE_MAX_1 = "128";
    private static final String BYTE_MIN = "-128";
    private static final String BYTE_MIN_0 =
            "-128.99999999999999999999999"; // force double rounding";
    private static final String BYTE_MIN_1 = "-129";

    /**
     * Constructor
     *
     * @param name test name
     */
    public ByteValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new ByteValidator(false, 0);
        strictValidator = ByteValidator.ByteValidator1();

        testPattern = "#,###";

        max = Byte.valueOf(Byte.MAX_VALUE);
        maxPlusOne = Long.valueOf(max.longValue() + 1);
        min = Byte.valueOf(Byte.MIN_VALUE);
        minMinusOne = Long.valueOf(min.longValue() - 1);

        invalidStrict =
                new String[] {
                    null,
                    "",
                    "X",
                    "X12",
                    "12X",
                    "1X2",
                    "1.2",
                    BYTE_MAX_1,
                    BYTE_MIN_1,
                    BYTE_MAX_0,
                    BYTE_MIN_0
                };

        invalid = new String[] {null, "", "X", "X12", BYTE_MAX_1, BYTE_MIN_1};

        testNumber = Byte.valueOf((byte) 123);
        testZero = Byte.valueOf((byte) 0);
        validStrict = new String[] {"0", "123", ",123", BYTE_MAX, BYTE_MIN};
        validStrictCompare =
                new Number[] {testZero, testNumber, testNumber, BYTE_MAX_VAL, BYTE_MIN_VAL};
        valid =
                new String[] {
                    "0", "123", ",123", ",123.5", "123X", BYTE_MAX, BYTE_MIN, BYTE_MAX_0, BYTE_MIN_0
                };
        validCompare =
                new Number[] {
                    testZero,
                    testNumber,
                    testNumber,
                    testNumber,
                    testNumber,
                    BYTE_MAX_VAL,
                    BYTE_MIN_VAL,
                    BYTE_MAX_VAL,
                    BYTE_MIN_VAL
                };

        testStringUS = ",123";
        testStringDE = ".123";

        localeValue = testStringDE;
        localePattern = "#.###";
        testLocale = Locale.GERMANY;
        localeExpected = testNumber;
    }

    /** Test ByteValidator validate Methods */
    public void testByteValidatorMethods() {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00";
        String patternVal = "1,23";
        String germanPatternVal = "1.23";
        String localeVal = ".123";
        String defaultVal = ",123";
        String XXXX = "XXXX";
        Byte expected = Byte.valueOf((byte) 123);
        assertEquals(
                "validate(A) default", expected, ByteValidator.getInstance().validate0(defaultVal));
        assertEquals(
                "validate(A) locale ",
                expected,
                ByteValidator.getInstance().validate2(localeVal, locale));
        assertEquals(
                "validate(A) pattern",
                expected,
                ByteValidator.getInstance().validate1(patternVal, pattern));
        assertEquals(
                "validate(A) both",
                expected,
                ByteValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));

        assertTrue("isValid(A) default", ByteValidator.getInstance().isValid0(defaultVal));
        assertTrue("isValid(A) locale ", ByteValidator.getInstance().isValid2(localeVal, locale));
        assertTrue("isValid(A) pattern", ByteValidator.getInstance().isValid1(patternVal, pattern));
        assertTrue(
                "isValid(A) both",
                ByteValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));

        assertNull("validate(B) default", ByteValidator.getInstance().validate0(XXXX));
        assertNull("validate(B) locale ", ByteValidator.getInstance().validate2(XXXX, locale));
        assertNull("validate(B) pattern", ByteValidator.getInstance().validate1(XXXX, pattern));
        assertNull(
                "validate(B) both",
                ByteValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));

        assertFalse("isValid(B) default", ByteValidator.getInstance().isValid0(XXXX));
        assertFalse("isValid(B) locale ", ByteValidator.getInstance().isValid2(XXXX, locale));
        assertFalse("isValid(B) pattern", ByteValidator.getInstance().isValid1(XXXX, pattern));
        assertFalse(
                "isValid(B) both",
                ByteValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    /** Test Byte Range/Min/Max */
    public void testByteRangeMinMax() {
        ByteValidator validator = (ByteValidator) strictValidator;
        Byte number9 = validator.validate1("9", "#");
        Byte number10 = validator.validate1("10", "#");
        Byte number11 = validator.validate1("11", "#");
        Byte number19 = validator.validate1("19", "#");
        Byte number20 = validator.validate1("20", "#");
        Byte number21 = validator.validate1("21", "#");
        byte min = (byte) 10;
        byte max = (byte) 20;

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
