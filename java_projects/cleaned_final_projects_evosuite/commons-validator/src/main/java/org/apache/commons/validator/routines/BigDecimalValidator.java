
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

import java.math.BigDecimal;
import java.text.Format;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * <b>BigDecimal Validation</b> and Conversion routines (<code>java.math.BigDecimal</code>).
 *
 * <p>This validator provides a number of methods for validating/converting a <code>String</code>
 * value to a <code>BigDecimal</code> using <code>java.text.NumberFormat</code> to parse either:
 *
 * <ul>
 *   <li>using the default format for the default <code>Locale</code>
 *   <li>using a specified pattern with the default <code>Locale</code>
 *   <li>using the default format for a specified <code>Locale</code>
 *   <li>using a specified pattern with a specified <code>Locale</code>
 * </ul>
 *
 * <p>Use one of the <code>isValid()</code> methods to just validate or one of the <code>validate()
 * </code> methods to validate and receive a <i>converted</i> <code>BigDecimal</code> value.
 *
 * <p>Fraction/decimal values are automatically trimmed to the appropriate length.
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
 *   <li>using the default format for the default <code>Locale</code>
 *   <li>using a specified pattern with the default <code>Locale</code>
 *   <li>using the default format for a specified <code>Locale</code>
 *   <li>using a specified pattern with a specified <code>Locale</code>
 * </ul>
 *
 * @version $Revision$
 * @since Validator 1.3.0
 */
public class BigDecimalValidator extends AbstractNumberValidator {

    private static final long serialVersionUID = -670320911490506772L;

    private static final BigDecimalValidator VALIDATOR = BigDecimalValidator.BigDecimalValidator2();

    /**
     * Return a singleton instance of this validator.
     *
     * @return A singleton instance of the BigDecimalValidator.
     */
    public static BigDecimalValidator getInstance() {
        return VALIDATOR;
    }

    /** Construct a <i>strict</i> instance. */
    protected BigDecimalValidator(boolean strict, int formatType, boolean allowFractions) {
        super(strict, formatType, allowFractions);
    }

    public static BigDecimalValidator BigDecimalValidator1(boolean strict) {
        return new BigDecimalValidator(strict, STANDARD_FORMAT, true);
    }

    public static BigDecimalValidator BigDecimalValidator2() {
        return BigDecimalValidator1(true);
    }

    /**
     * Construct an instance with the specified strict setting.
     *
     * @param strict <code>true</code> if strict <code>Format</code> parsing should be used.
     */

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
     * @param allowFractions <code>true</code> if fractions are allowed or <code>false</code> if
     *     integers only.
     */

    /**
     * Validate/convert a <code>BigDecimal</code> using the default <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @return The parsed <code>BigDecimal</code> if valid or <code>null</code> if invalid.
     */
    public BigDecimal validate0(String value) {
        return (BigDecimal) parse(value, (String) null, (Locale) null);
    }

    /**
     * Validate/convert a <code>BigDecimal</code> using the specified <i>pattern</i>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against, or the default for the <code>
     *     Locale</code> if <code>null</code>.
     * @return The parsed <code>BigDecimal</code> if valid or <code>null</code> if invalid.
     */
    public BigDecimal validate1(String value, String pattern) {
        return (BigDecimal) parse(value, pattern, (Locale) null);
    }

    /**
     * Validate/convert a <code>BigDecimal</code> using the specified <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param locale The locale to use for the number format, system default if null.
     * @return The parsed <code>BigDecimal</code> if valid or <code>null</code> if invalid.
     */
    public BigDecimal validate2(String value, Locale locale) {
        return (BigDecimal) parse(value, (String) null, locale);
    }

    /**
     * Validate/convert a <code>BigDecimal</code> using the specified pattern and/ or <code>Locale
     * </code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against, or the default for the <code>
     *     Locale</code> if <code>null</code>.
     * @param locale The locale to use for the date format, system default if null.
     * @return The parsed <code>BigDecimal</code> if valid or <code>null</code> if invalid.
     */
    public BigDecimal validate3(String value, String pattern, Locale locale) {
        return (BigDecimal) parse(value, pattern, locale);
    }

    /**
     * Check if the value is within a specified range.
     *
     * @param value The <code>Number</code> value to check.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return <code>true</code> if the value is within the specified range.
     */
    public boolean isInRange(BigDecimal value, double min, double max) {
        return (value.doubleValue() >= min && value.doubleValue() <= max);
    }

    /**
     * Check if the value is greater than or equal to a minimum.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value.
     * @return <code>true</code> if the value is greater than or equal to the minimum.
     */
    public boolean minValue(BigDecimal value, double min) {
        return (value.doubleValue() >= min);
    }

    /**
     * Check if the value is less than or equal to a maximum.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum value.
     * @return <code>true</code> if the value is less than or equal to the maximum.
     */
    public boolean maxValue(BigDecimal value, double max) {
        return (value.doubleValue() <= max);
    }

    /**
     * Convert the parsed value to a <code>BigDecimal</code>.
     *
     * @param value The parsed <code>Number</code> object created.
     * @param formatter The Format used to parse the value with.
     * @return The parsed <code>Number</code> converted to a <code>BigDecimal</code>.
     */
    @Override
    protected Object processParsedValue(Object value, Format formatter) {
        BigDecimal decimal = null;
        if (value instanceof Long) {
            decimal = BigDecimal.valueOf(((Long) value).longValue());
        } else {
            decimal = new BigDecimal(value.toString());
        }

        int scale = determineScale((NumberFormat) formatter);
        if (scale >= 0) {
            decimal = decimal.setScale(scale, BigDecimal.ROUND_DOWN);
        }

        return decimal;
    }
}
