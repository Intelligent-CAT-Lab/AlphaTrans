
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

import java.text.Format;
import java.util.Locale;

/**
 * <b>Long Validation</b> and Conversion routines (<code>java.lang.Long</code>).
 *
 * <p>This validator provides a number of methods for validating/converting a <code>String</code>
 * value to a <code>Long</code> using <code>java.text.NumberFormat</code> to parse either:
 *
 * <ul>
 *   <li>using the default format for the default <code>Locale</code>
 *   <li>using a specified pattern with the default <code>Locale</code>
 *   <li>using the default format for a specified <code>Locale</code>
 *   <li>using a specified pattern with a specified <code>Locale</code>
 * </ul>
 *
 * <p>Use one of the <code>isValid()</code> methods to just validate or one of the <code>validate()
 * </code> methods to validate and receive a <i>converted</i> <code>Long</code> value.
 *
 * <p>Once a value has been successfully converted the following methods can be used to perform
 * minimum, maximum and range checks:
 *
 * <ul>
 *   <li><code>minValue()</code> checks whether the value is greater than or equal to a specified
 *       minimum.
 *   <li><code>maxValue()</code> checks whether the value is less than or equal to a specified
 *       maximum.
 *   <li><code>isInRange()</code> checks whether the value is within a specified range of values.
 * </ul>
 *
 * <p>So that the same mechanism used for parsing an <i>input</i> value for validation can be used
 * to format <i>output</i>, corresponding <code>format()</code> methods are also provided. That is
 * you can format either:
 *
 * <ul>
 *   <li>using a specified pattern
 *   <li>using the format for a specified <code>Locale</code>
 *   <li>using the format for the <i>default</i> <code>Locale</code>
 * </ul>
 *
 * @version $Revision$
 * @since Validator 1.3.0
 */
public class LongValidator extends AbstractNumberValidator {

    private static final long serialVersionUID = -5117231731027866098L;

    private static final LongValidator VALIDATOR = LongValidator.LongValidator1();

    /**
     * Return a singleton instance of this validator.
     *
     * @return A singleton instance of the LongValidator.
     */
    public static LongValidator getInstance() {
        return VALIDATOR;
    }

    /** Construct a <i>strict</i> instance. */
    public LongValidator(boolean strict, int formatType) {
        super(strict, formatType, false);
    }

    public static LongValidator LongValidator1() {
        return new LongValidator(true, STANDARD_FORMAT);
    }

    /**
     * Construct an instance with the specified strict setting and format type.
     *
     * <p>The <code>formatType</code> specified what type of <code>NumberFormat</code> is created -
     * valid types are:
     *
     * <ul>
     *   <li>AbstractNumberValidator.STANDARD_FORMAT -to create <i>standard</i> number formats (the
     *       default).
     *   <li>AbstractNumberValidator.CURRENCY_FORMAT -to create <i>currency</i> number formats.
     *   <li>AbstractNumberValidator.PERCENT_FORMAT -to create <i>percent</i> number formats (the
     *       default).
     * </ul>
     *
     * @param strict <code>true</code> if strict <code>Format</code> parsing should be used.
     * @param formatType The <code>NumberFormat</code> type to create for validation, default is
     *     STANDARD_FORMAT.
     */

    /**
     * Validate/convert a <code>Long</code> using the default <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @return The parsed <code>Long</code> if valid or <code>null</code> if invalid.
     */
    public Long validate0(String value) {
        return (Long) parse(value, (String) null, (Locale) null);
    }

    /**
     * Validate/convert a <code>Long</code> using the specified <i>pattern</i>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against.
     * @return The parsed <code>Long</code> if valid or <code>null</code> if invalid.
     */
    public Long validate1(String value, String pattern) {
        return (Long) parse(value, pattern, (Locale) null);
    }

    /**
     * Validate/convert a <code>Long</code> using the specified <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param locale The locale to use for the number format, system default if null.
     * @return The parsed <code>Long</code> if valid or <code>null</code> if invalid.
     */
    public Long validate2(String value, Locale locale) {
        return (Long) parse(value, (String) null, locale);
    }

    /**
     * Validate/convert a <code>Long</code> using the specified pattern and/ or <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against, or the default for the <code>
     *     Locale</code> if <code>null</code>.
     * @param locale The locale to use for the date format, system default if null.
     * @return The parsed <code>Long</code> if valid or <code>null</code> if invalid.
     */
    public Long validate3(String value, String pattern, Locale locale) {
        return (Long) parse(value, pattern, locale);
    }

    /**
     * Check if the value is within a specified range.
     *
     * @param value The <code>Number</code> value to check.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return <code>true</code> if the value is within the specified range.
     */
    public boolean isInRange0(long value, long min, long max) {
        return (value >= min && value <= max);
    }

    /**
     * Check if the value is within a specified range.
     *
     * @param value The <code>Number</code> value to check.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return <code>true</code> if the value is within the specified range.
     */
    public boolean isInRange1(Long value, long min, long max) {
        return isInRange0(value.longValue(), min, max);
    }

    /**
     * Check if the value is greater than or equal to a minimum.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value.
     * @return <code>true</code> if the value is greater than or equal to the minimum.
     */
    public boolean minValue0(long value, long min) {
        return (value >= min);
    }

    /**
     * Check if the value is greater than or equal to a minimum.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value.
     * @return <code>true</code> if the value is greater than or equal to the minimum.
     */
    public boolean minValue1(Long value, long min) {
        return minValue0(value.longValue(), min);
    }

    /**
     * Check if the value is less than or equal to a maximum.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum value.
     * @return <code>true</code> if the value is less than or equal to the maximum.
     */
    public boolean maxValue0(long value, long max) {
        return (value <= max);
    }

    /**
     * Check if the value is less than or equal to a maximum.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum value.
     * @return <code>true</code> if the value is less than or equal to the maximum.
     */
    public boolean maxValue1(Long value, long max) {
        return maxValue0(value.longValue(), max);
    }

    /**
     * Convert the parsed value to a <code>Long</code>.
     *
     * @param value The parsed <code>Number</code> object created.
     * @param formatter The Format used to parse the value with.
     * @return The parsed <code>Number</code> converted to a <code>Long</code>.
     */
    @Override
    protected Object processParsedValue(Object value, Format formatter) {

        if (value instanceof Long) {
            return value;
        }
        return null;
    }
}
