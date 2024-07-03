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
package org.apache.commons.validator;

import org.apache.commons.validator.routines.CreditCardValidator;
import org.apache.commons.validator.routines.DateValidator;
import org.apache.commons.validator.routines.EmailValidator;
import org.apache.commons.validator.routines.UrlValidator;

import java.io.Serializable;
import java.util.Locale;
import java.util.regex.Pattern;

/**
 * This class contains basic methods for performing validations.
 *
 * @version $Revision$
 */
public class GenericValidator implements Serializable {

    private static final long serialVersionUID = -7212095066891517618L;

    /** UrlValidator used in wrapper method. */
    private static final UrlValidator URL_VALIDATOR = UrlValidator.UrlValidator6();

    /** CreditCardValidator used in wrapper method. */
    private static final CreditCardValidator CREDIT_CARD_VALIDATOR =
            CreditCardValidator.CreditCardValidator0();

    /**
     * Checks if the field isn't null and length of the field is greater than zero not including
     * whitespace.
     *
     * @param value The value validation is being performed on.
     * @return true if blank or null.
     */
    public static boolean isBlankOrNull(String value) {
        return ((value == null) || (value.trim().length() == 0));
    }

    /**
     * Checks if the value matches the regular expression.
     *
     * @param value The value validation is being performed on.
     * @param regexp The regular expression.
     * @return true if matches the regular expression.
     */
    public static boolean matchRegexp(String value, String regexp) {
        if (regexp == null || regexp.length() <= 0) {
            return false;
        }

        return Pattern.matches(regexp, value);
    }

    /**
     * Checks if the value can safely be converted to a byte primitive.
     *
     * @param value The value validation is being performed on.
     * @return true if the value can be converted to a Byte.
     */
    public static boolean isByte(String value) {
        return (GenericTypeValidator.formatByte0(value) != null);
    }

    /**
     * Checks if the value can safely be converted to a short primitive.
     *
     * @param value The value validation is being performed on.
     * @return true if the value can be converted to a Short.
     */
    public static boolean isShort(String value) {
        return (GenericTypeValidator.formatShort0(value) != null);
    }

    /**
     * Checks if the value can safely be converted to a int primitive.
     *
     * @param value The value validation is being performed on.
     * @return true if the value can be converted to an Integer.
     */
    public static boolean isInt(String value) {
        return (GenericTypeValidator.formatInt0(value) != null);
    }

    /**
     * Checks if the value can safely be converted to a long primitive.
     *
     * @param value The value validation is being performed on.
     * @return true if the value can be converted to a Long.
     */
    public static boolean isLong(String value) {
        return (GenericTypeValidator.formatLong0(value) != null);
    }

    /**
     * Checks if the value can safely be converted to a float primitive.
     *
     * @param value The value validation is being performed on.
     * @return true if the value can be converted to a Float.
     */
    public static boolean isFloat(String value) {
        return (GenericTypeValidator.formatFloat0(value) != null);
    }

    /**
     * Checks if the value can safely be converted to a double primitive.
     *
     * @param value The value validation is being performed on.
     * @return true if the value can be converted to a Double.
     */
    public static boolean isDouble(String value) {
        return (GenericTypeValidator.formatDouble0(value) != null);
    }

    /**
     * Checks if the field is a valid date. The <code>Locale</code> is used with <code>
     * java.text.DateFormat</code>. The setLenient method is set to <code>false</code> for all.
     *
     * @param value The value validation is being performed on.
     * @param locale The locale to use for the date format, defaults to the system default if null.
     * @return true if the value can be converted to a Date.
     */
    public static boolean isDate0(String value, Locale locale) {
        return DateValidator.getInstance().isValid2(value, locale);
    }

    /**
     * Checks if the field is a valid date. The pattern is used with <code>
     * java.text.SimpleDateFormat</code>. If strict is true, then the length will be checked so
     * '2/12/1999' will not pass validation with the format 'MM/dd/yyyy' because the month isn't two
     * digits. The setLenient method is set to <code>false</code> for all.
     *
     * @param value The value validation is being performed on.
     * @param datePattern The pattern passed to <code>SimpleDateFormat</code>.
     * @param strict Whether or not to have an exact match of the datePattern.
     * @return true if the value can be converted to a Date.
     */
    public static boolean isDate1(String value, String datePattern, boolean strict) {
        return org.apache.commons.validator.DateValidator.getInstance()
                .isValid0(value, datePattern, strict);
    }

    /**
     * Checks if a value is within a range (min &amp; max specified in the vars attribute).
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return true if the value is in the specified range.
     */
    public static boolean isInRange0(byte value, byte min, byte max) {
        return ((value >= min) && (value <= max));
    }

    /**
     * Checks if a value is within a range (min &amp; max specified in the vars attribute).
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return true if the value is in the specified range.
     */
    public static boolean isInRange1(int value, int min, int max) {
        return ((value >= min) && (value <= max));
    }

    /**
     * Checks if a value is within a range (min &amp; max specified in the vars attribute).
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return true if the value is in the specified range.
     */
    public static boolean isInRange2(float value, float min, float max) {
        return ((value >= min) && (value <= max));
    }

    /**
     * Checks if a value is within a range (min &amp; max specified in the vars attribute).
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return true if the value is in the specified range.
     */
    public static boolean isInRange3(short value, short min, short max) {
        return ((value >= min) && (value <= max));
    }

    /**
     * Checks if a value is within a range (min &amp; max specified in the vars attribute).
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return true if the value is in the specified range.
     */
    public static boolean isInRange4(long value, long min, long max) {
        return ((value >= min) && (value <= max));
    }

    /**
     * Checks if a value is within a range (min &amp; max specified in the vars attribute).
     *
     * @param value The value validation is being performed on.
     * @param min The minimum value of the range.
     * @param max The maximum value of the range.
     * @return true if the value is in the specified range.
     */
    public static boolean isInRange5(double value, double min, double max) {
        return ((value >= min) && (value <= max));
    }

    /**
     * Checks if the field is a valid credit card number.
     *
     * @param value The value validation is being performed on.
     * @return true if the value is valid Credit Card Number.
     */
    public static boolean isCreditCard(String value) {
        return CREDIT_CARD_VALIDATOR.isValid(value);
    }

    /**
     * Checks if a field has a valid e-mail address.
     *
     * @param value The value validation is being performed on.
     * @return true if the value is valid Email Address.
     */
    public static boolean isEmail(String value) {
        return EmailValidator.getInstance0().isValid(value);
    }

    /**
     * Checks if a field is a valid url address. If you need to modify what is considered valid then
     * consider using the UrlValidator directly.
     *
     * @param value The value validation is being performed on.
     * @return true if the value is valid Url.
     */
    public static boolean isUrl(String value) {
        return URL_VALIDATOR.isValid(value);
    }

    /**
     * Checks if the value's length is less than or equal to the max.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum length.
     * @return true if the value's length is less than the specified maximum.
     */
    public static boolean maxLength0(String value, int max) {
        return (value.length() <= max);
    }

    /**
     * Checks if the value's adjusted length is less than or equal to the max.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum length.
     * @param lineEndLength The length to use for line endings.
     * @return true if the value's length is less than the specified maximum.
     */
    public static boolean maxLength1(String value, int max, int lineEndLength) {
        int adjustAmount = adjustForLineEnding(value, lineEndLength);
        return ((value.length() + adjustAmount) <= max);
    }

    /**
     * Checks if the value's length is greater than or equal to the min.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum length.
     * @return true if the value's length is more than the specified minimum.
     */
    public static boolean minLength0(String value, int min) {
        return (value.length() >= min);
    }

    /**
     * Checks if the value's adjusted length is greater than or equal to the min.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum length.
     * @param lineEndLength The length to use for line endings.
     * @return true if the value's length is more than the specified minimum.
     */
    public static boolean minLength1(String value, int min, int lineEndLength) {
        int adjustAmount = adjustForLineEnding(value, lineEndLength);
        return ((value.length() + adjustAmount) >= min);
    }

    /**
     * Calculate an adjustment amount for line endings.
     *
     * <p>See Bug 37962 for the rational behind this.
     *
     * @param value The value validation is being performed on.
     * @param lineEndLength The length to use for line endings.
     * @return the adjustment amount.
     */
    private static int adjustForLineEnding(String value, int lineEndLength) {
        int nCount = 0;
        int rCount = 0;
        for (int i = 0; i < value.length(); i++) {
            if (value.charAt(i) == '\n') {
                nCount++;
            }
            if (value.charAt(i) == '\r') {
                rCount++;
            }
        }
        return ((nCount * lineEndLength) - (rCount + nCount));
    }

    /**
     * Checks if the value is greater than or equal to the min.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum numeric value.
     * @return true if the value is &gt;= the specified minimum.
     */
    public static boolean minValue0(int value, int min) {
        return (value >= min);
    }

    /**
     * Checks if the value is greater than or equal to the min.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum numeric value.
     * @return true if the value is &gt;= the specified minimum.
     */
    public static boolean minValue1(long value, long min) {
        return (value >= min);
    }

    /**
     * Checks if the value is greater than or equal to the min.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum numeric value.
     * @return true if the value is &gt;= the specified minimum.
     */
    public static boolean minValue2(double value, double min) {
        return (value >= min);
    }

    /**
     * Checks if the value is greater than or equal to the min.
     *
     * @param value The value validation is being performed on.
     * @param min The minimum numeric value.
     * @return true if the value is &gt;= the specified minimum.
     */
    public static boolean minValue3(float value, float min) {
        return (value >= min);
    }

    /**
     * Checks if the value is less than or equal to the max.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum numeric value.
     * @return true if the value is &lt;= the specified maximum.
     */
    public static boolean maxValue0(int value, int max) {
        return (value <= max);
    }

    /**
     * Checks if the value is less than or equal to the max.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum numeric value.
     * @return true if the value is &lt;= the specified maximum.
     */
    public static boolean maxValue1(long value, long max) {
        return (value <= max);
    }

    /**
     * Checks if the value is less than or equal to the max.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum numeric value.
     * @return true if the value is &lt;= the specified maximum.
     */
    public static boolean maxValue2(double value, double max) {
        return (value <= max);
    }

    /**
     * Checks if the value is less than or equal to the max.
     *
     * @param value The value validation is being performed on.
     * @param max The maximum numeric value.
     * @return true if the value is &lt;= the specified maximum.
     */
    public static boolean maxValue3(float value, float max) {
        return (value <= max);
    }
}
