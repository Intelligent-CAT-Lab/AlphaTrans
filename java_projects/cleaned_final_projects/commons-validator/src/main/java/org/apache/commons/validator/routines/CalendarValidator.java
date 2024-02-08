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

import java.text.DateFormat;
import java.text.Format;
import java.util.Calendar;
import java.util.Locale;
import java.util.TimeZone;

/**
 * <b>Calendar Validation</b> and Conversion routines (<code>java.util.Calendar</code>).
 *
 * <p>This validator provides a number of methods for validating/converting a <code>String</code>
 * date value to a <code>java.util.Calendar</code> using <code>java.text.DateFormat</code> to parse
 * either:
 *
 * <ul>
 *   <li>using the default format for the default <code>Locale</code>
 *   <li>using a specified pattern with the default <code>Locale</code>
 *   <li>using the default format for a specified <code>Locale</code>
 *   <li>using a specified pattern with a specified <code>Locale</code>
 * </ul>
 *
 * <p>For each of the above mechanisms, conversion method (i.e the <code>validate</code> methods)
 * implementations are provided which either use the default <code>TimeZone</code> or allow the
 * <code>TimeZone</code> to be specified.
 *
 * <p>Use one of the <code>isValid()</code> methods to just validate or one of the <code>validate()
 * </code> methods to validate and receive a <i>converted</i> <code>Calendar</code> value.
 *
 * <p>Implementations of the <code>validate()</code> method are provided to create <code>Calendar
 * </code> objects for different <i>time zones</i> if the system default is not appropriate.
 *
 * <p>Alternatively the CalendarValidator's <code>adjustToTimeZone()</code> method can be used to
 * adjust the <code>TimeZone</code> of the <code>Calendar</code> object afterwards.
 *
 * <p>Once a value has been successfully converted the following methods can be used to perform
 * various date comparison checks:
 *
 * <ul>
 *   <li><code>compareDates()</code> compares the day, month and year of two calendars, returning 0,
 *       -1 or +1 indicating whether the first date is equal, before or after the second.
 *   <li><code>compareWeeks()</code> compares the week and year of two calendars, returning 0, -1 or
 *       +1 indicating whether the first week is equal, before or after the second.
 *   <li><code>compareMonths()</code> compares the month and year of two calendars, returning 0, -1
 *       or +1 indicating whether the first month is equal, before or after the second.
 *   <li><code>compareQuarters()</code> compares the quarter and year of two calendars, returning 0,
 *       -1 or +1 indicating whether the first quarter is equal, before or after the second.
 *   <li><code>compareYears()</code> compares the year of two calendars, returning 0, -1 or +1
 *       indicating whether the first year is equal, before or after the second.
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
public class CalendarValidator extends AbstractCalendarValidator {

    private static final long serialVersionUID = 9109652318762134167L;

    private static final CalendarValidator VALIDATOR = CalendarValidator.CalendarValidator1();

    /**
     * Return a singleton instance of this validator.
     *
     * @return A singleton instance of the CalendarValidator.
     */
    public static CalendarValidator getInstance() {
        return VALIDATOR;
    }

    /** Construct a <i>strict</i> instance with <i>short</i> date style. */
    public CalendarValidator(boolean strict, int dateStyle) {
        super(strict, dateStyle, -1);
    }

    public static CalendarValidator CalendarValidator1() {
        return new CalendarValidator(true, DateFormat.SHORT);
    }

    /**
     * Construct an instance with the specified <i>strict</i> and <i>date style</i> parameters.
     *
     * @param strict <code>true</code> if strict <code>Format</code> parsing should be used.
     * @param dateStyle the date style to use for Locale validation.
     */

    /**
     * Validate/convert a <code>Calendar</code> using the default <code>Locale</code> and <code>
     * TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate0(String value) {
        return (Calendar) parse(value, (String) null, (Locale) null, (TimeZone) null);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified <code>TimeZone</code> and
     * default <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param timeZone The Time Zone used to parse the date, system default if null.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate1(String value, TimeZone timeZone) {
        return (Calendar) parse(value, (String) null, (Locale) null, timeZone);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified <i>pattern</i> and default
     * <code>TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate2(String value, String pattern) {
        return (Calendar) parse(value, pattern, (Locale) null, (TimeZone) null);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified <i>pattern</i> and <code>
     * TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against.
     * @param timeZone The Time Zone used to parse the date, system default if null.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate3(String value, String pattern, TimeZone timeZone) {
        return (Calendar) parse(value, pattern, (Locale) null, timeZone);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified <code>Locale</code> and default
     * <code>TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @param locale The locale to use for the date format, system default if null.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate4(String value, Locale locale) {
        return (Calendar) parse(value, (String) null, locale, (TimeZone) null);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified <code>Locale</code> and <code>
     * TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @param locale The locale to use for the date format, system default if null.
     * @param timeZone The Time Zone used to parse the date, system default if null.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate5(String value, Locale locale, TimeZone timeZone) {
        return (Calendar) parse(value, (String) null, locale, timeZone);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified pattern and <code>Locale</code>
     * and the default <code>TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against, or the default for the <code>
     *     Locale</code> if <code>null</code>.
     * @param locale The locale to use for the date format, system default if null.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate6(String value, String pattern, Locale locale) {
        return (Calendar) parse(value, pattern, locale, (TimeZone) null);
    }

    /**
     * Validate/convert a <code>Calendar</code> using the specified pattern, and <code>Locale</code>
     * and <code>TimeZone</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against, or the default for the <code>
     *     Locale</code> if <code>null</code>.
     * @param locale The locale to use for the date format, system default if null.
     * @param timeZone The Time Zone used to parse the date, system default if null.
     * @return The parsed <code>Calendar</code> if valid or <code>null</code> if invalid.
     */
    public Calendar validate7(String value, String pattern, Locale locale, TimeZone timeZone) {
        return (Calendar) parse(value, pattern, locale, timeZone);
    }

    /**
     * Adjusts a Calendar's value to a different TimeZone.
     *
     * @param value The value to adjust.
     * @param timeZone The new time zone to use to adjust the Calendar to.
     */
    public static void adjustToTimeZone(Calendar value, TimeZone timeZone) {
        if (value.getTimeZone().hasSameRules(timeZone)) {
            value.setTimeZone(timeZone);
        } else {
            int year = value.get(Calendar.YEAR);
            int month = value.get(Calendar.MONTH);
            int date = value.get(Calendar.DATE);
            int hour = value.get(Calendar.HOUR_OF_DAY);
            int minute = value.get(Calendar.MINUTE);
            value.setTimeZone(timeZone);
            value.set(year, month, date, hour, minute);
        }
    }

    /**
     * Compare Dates (day, month and year - not time).
     *
     * @param value The <code>Calendar</code> value to check.
     * @param compare The <code>Calendar</code> to compare the value to.
     * @return Zero if the dates are equal, -1 if first date is less than the seconds and +1 if the
     *     first date is greater than.
     */
    public int compareDates(Calendar value, Calendar compare) {
        return compare(value, compare, Calendar.DATE);
    }

    /**
     * Compare Weeks (week and year).
     *
     * @param value The <code>Calendar</code> value to check.
     * @param compare The <code>Calendar</code> to compare the value to.
     * @return Zero if the weeks are equal, -1 if first parameter's week is less than the seconds
     *     and +1 if the first parameter's week is greater than.
     */
    public int compareWeeks(Calendar value, Calendar compare) {
        return compare(value, compare, Calendar.WEEK_OF_YEAR);
    }

    /**
     * Compare Months (month and year).
     *
     * @param value The <code>Calendar</code> value to check.
     * @param compare The <code>Calendar</code> to compare the value to.
     * @return Zero if the months are equal, -1 if first parameter's month is less than the seconds
     *     and +1 if the first parameter's month is greater than.
     */
    public int compareMonths(Calendar value, Calendar compare) {
        return compare(value, compare, Calendar.MONTH);
    }

    /**
     * Compare Quarters (quarter and year).
     *
     * @param value The <code>Calendar</code> value to check.
     * @param compare The <code>Calendar</code> to check the value against.
     * @return Zero if the quarters are equal, -1 if first parameter's quarter is less than the
     *     seconds and +1 if the first parameter's quarter is greater than.
     */
    public int compareQuarters0(Calendar value, Calendar compare) {
        return compareQuarters1(value, compare, 1);
    }

    /**
     * Compare Quarters (quarter and year).
     *
     * @param value The <code>Calendar</code> value to check.
     * @param compare The <code>Calendar</code> to compare the value to.
     * @param monthOfFirstQuarter The month that the first quarter starts.
     * @return Zero if the quarters are equal, -1 if first parameter's quarter is less than the
     *     seconds and +1 if the first parameter's quarter is greater than.
     */
    public int compareQuarters1(Calendar value, Calendar compare, int monthOfFirstQuarter) {
        return super.compareQuarters(value, compare, monthOfFirstQuarter);
    }

    /**
     * Compare Years.
     *
     * @param value The <code>Calendar</code> value to check.
     * @param compare The <code>Calendar</code> to compare the value to.
     * @return Zero if the years are equal, -1 if first parameter's year is less than the seconds
     *     and +1 if the first parameter's year is greater than.
     */
    public int compareYears(Calendar value, Calendar compare) {
        return compare(value, compare, Calendar.YEAR);
    }

    /**
     * Convert the parsed <code>Date</code> to a <code>Calendar</code>.
     *
     * @param value The parsed <code>Date</code> object created.
     * @param formatter The Format used to parse the value with.
     * @return The parsed value converted to a <code>Calendar</code>.
     */
    @Override
    protected Object processParsedValue(Object value, Format formatter) {
        return ((DateFormat) formatter).getCalendar();
    }
}
