
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
 * Test Case for DoubleValidator.
 *
 * @version $Revision$
 */
public class DoubleValidatorTest extends AbstractNumberValidatorTest {

    /**
     * Constructor
     *
     * @param name test name
     */
    public DoubleValidatorTest(String name) {
        super(name);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();

        validator = new DoubleValidator(false, 0);
        strictValidator = DoubleValidator.DoubleValidator1();

        testPattern = "#,###.#";

        max = null;
        maxPlusOne = null;
        min = null;
        minMinusOne = null;

        invalidStrict = new String[] {null, "", "X", "X12", "12X", "1X2"};

        invalid = new String[] {null, "", "X", "X12"};

        testNumber = Double.valueOf(1234.5);
        testZero = Double.valueOf(0);
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

    /** Test DoubleValidator validate Methods */
    public void testDoubleValidatorMethods() {
        Locale locale = Locale.GERMAN;
        String pattern = "0,00,00";
        String patternVal = "1,23,45";
        String germanPatternVal = "1.23.45";
        String localeVal = "12.345";
        String defaultVal = "12,345";
        String XXXX = "XXXX";
        Double expected = Double.valueOf(12345);
        assertEquals(
                "validate(A) default",
                expected,
                DoubleValidator.getInstance().validate0(defaultVal));
        assertEquals(
                "validate(A) locale ",
                expected,
                DoubleValidator.getInstance().validate2(localeVal, locale));
        assertEquals(
                "validate(A) pattern",
                expected,
                DoubleValidator.getInstance().validate1(patternVal, pattern));
        assertEquals(
                "validate(A) both",
                expected,
                DoubleValidator.getInstance().validate3(germanPatternVal, pattern, Locale.GERMAN));

        assertTrue("isValid(A) default", DoubleValidator.getInstance().isValid0(defaultVal));
        assertTrue("isValid(A) locale ", DoubleValidator.getInstance().isValid2(localeVal, locale));
        assertTrue(
                "isValid(A) pattern", DoubleValidator.getInstance().isValid1(patternVal, pattern));
        assertTrue(
                "isValid(A) both",
                DoubleValidator.getInstance().isValid3(germanPatternVal, pattern, Locale.GERMAN));

        assertNull("validate(B) default", DoubleValidator.getInstance().validate0(XXXX));
        assertNull("validate(B) locale ", DoubleValidator.getInstance().validate2(XXXX, locale));
        assertNull("validate(B) pattern", DoubleValidator.getInstance().validate1(XXXX, pattern));
        assertNull(
                "validate(B) both",
                DoubleValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN));

        assertFalse("isValid(B) default", DoubleValidator.getInstance().isValid0(XXXX));
        assertFalse("isValid(B) locale ", DoubleValidator.getInstance().isValid2(XXXX, locale));
        assertFalse("isValid(B) pattern", DoubleValidator.getInstance().isValid1(XXXX, pattern));
        assertFalse(
                "isValid(B) both",
                DoubleValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN));
    }

    /** Test Double Range/Min/Max */
    public void testDoubleRangeMinMax() {
        DoubleValidator validator = (DoubleValidator) strictValidator;
        Double number9 = validator.validate1("9", "#");
        Double number10 = validator.validate1("10", "#");
        Double number11 = validator.validate1("11", "#");
        Double number19 = validator.validate1("19", "#");
        Double number20 = validator.validate1("20", "#");
        Double number21 = validator.validate1("21", "#");

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
