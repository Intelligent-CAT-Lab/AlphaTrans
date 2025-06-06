
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

import java.text.DateFormat;
import java.text.DateFormatSymbols;
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Locale;
import java.util.TimeZone;

/**
 * Abstract class for Date/Time/Calendar validation.
 *
 * <p>This is a <i>base</i> class for building Date / Time Validators using format parsing.
 *
 * @version $Revision$
 * @since Validator 1.3.0
 */
public abstract class AbstractCalendarValidator extends AbstractFormatValidator {

    private static final long serialVersionUID = -1410008585975827379L;

    private final int dateStyle;

    private final int timeStyle;

    /**
     * Construct an instance with the specified <i>strict</i>, <i>time</i> and <i>date</i> style
     * parameters.
     *
     * @param strict <code>true</code> if strict <code>Format</code> parsing should be used.
     * @param dateStyle the date style to use for Locale validation.
     * @param timeStyle the time style to use for Locale validation.
     */
    public AbstractCalendarValidator(boolean strict, int dateStyle, int timeStyle) {
        super(strict);
        this.dateStyle = dateStyle;
        this.timeStyle = timeStyle;
    }

    /**
     * Validate using the specified <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to format the value.
     * @param locale The locale to use for the Format, defaults to the default
     * @return <code>true</code> if the value is valid.
     */
    @Override
    public boolean isValid3(String value, String pattern, Locale locale) {
        Object parsedValue = parse(value, pattern, locale, (TimeZone) null);
        return (parsedValue == null ? false : true);
    }

    /**
     * Format an object into a <code>String</code> using the default Locale.
     *
     * @param value The value validation is being performed on.
     * @param timeZone The Time Zone used to format the date, system default if null (unless value
     *     is a <code>Calendar</code>.
     * @return The value formatted as a <code>String</code>.
     */
    public String format0(Object value, TimeZone timeZone) {
        return format4(value, (String) null, (Locale) null, timeZone);
    }

    /**
     * Format an object into a <code>String</code> using the specified pattern.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to format the value.
     * @param timeZone The Time Zone used to format the date, system default if null (unless value
     *     is a <code>Calendar</code>.
     * @return The value formatted as a <code>String</code>.
     */
    public String format1(Object value, String pattern, TimeZone timeZone) {
        return format4(value, pattern, (Locale) null, timeZone);
    }

    /**
     * Format an object into a <code>String</code> using the specified Locale.
     *
     * @param value The value validation is being performed on.
     * @param locale The locale to use for the Format.
     * @param timeZone The Time Zone used to format the date, system default if null (unless value
     *     is a <code>Calendar</code>.
     * @return The value formatted as a <code>String</code>.
     */
    public String format2(Object value, Locale locale, TimeZone timeZone) {
        return format4(value, (String) null, locale, timeZone);
    }

    /**
     * Format an object using the specified pattern and/or <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to format the value.
     * @param locale The locale to use for the Format.
     * @return The value formatted as a <code>String</code>.
     */
    public String format3(Object value, String pattern, Locale locale) {
        return format4(value, pattern, locale, (TimeZone) null);
    }

    /**
     * Format an object using the specified pattern and/or <code>Locale</code>.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to format the value.
     * @param locale The locale to use for the Format.
     * @param timeZone The Time Zone used to format the date, system default if null (unless value
     *     is a <code>Calendar</code>.
     * @return The value formatted as a <code>String</code>.
     */
    public String format4(Object value, String pattern, Locale locale, TimeZone timeZone) {
        DateFormat formatter = (DateFormat) getFormat0(pattern, locale);
        if (timeZone != null) {
            formatter.setTimeZone(timeZone);
        } else if (value instanceof Calendar) {
            formatter.setTimeZone(((Calendar) value).getTimeZone());
        }
        return format5(value, formatter);
    }

    /**
     * Format a value with the specified <code>DateFormat</code>.
     *
     * @param value The value to be formatted.
     * @param formatter The Format to use.
     * @return The formatted value.
     */
    protected String format5(Object value, Format formatter) {
        if (value == null) {
            return null;
        } else if (value instanceof Calendar) {
            value = ((Calendar) value).getTime();
        }
        return formatter.format(value);
    }

    /**
     * Checks if the value is valid against a specified pattern.
     *
     * @param value The value validation is being performed on.
     * @param pattern The pattern used to validate the value against, or the default for the <code>
     *     Locale</code> if <code>null</code>.
     * @param locale The locale to use for the date format, system default if null.
     * @param timeZone The Time Zone used to parse the date, system default if null.
     * @return The parsed value if valid or <code>null</code> if invalid.
     */
    protected Object parse(String value, String pattern, Locale locale, TimeZone timeZone) {

        value = (value == null ? null : value.trim());
        if (value == null || value.length() == 0) {
            return null;
        }
        DateFormat formatter = (DateFormat) getFormat0(pattern, locale);
        if (timeZone != null) {
            formatter.setTimeZone(timeZone);
        }
        return parse(value, formatter);
    }

    /**
     * Process the parsed value, performing any further validation and type conversion required.
     *
     * @param value The parsed object created.
     * @param formatter The Format used to parse the value with.
     * @return The parsed value converted to the appropriate type if valid or <code>null</code> if
     *     invalid.
     */
    @Override
    protected abstract Object processParsedValue(Object value, Format formatter);

    /**
     * Returns a <code>DateFormat</code> for the specified <i>pattern</i> and/or <code>Locale</code>
     * .
     *
     * @param pattern The pattern used to validate the value against or <code>null</code> to use the
     *     default for the <code>Locale</code>.
     * @param locale The locale to use for the currency format, system default if null.
     * @return The <code>DateFormat</code> to created.
     */
    @Override
    protected Format getFormat(String pattern, Locale locale) {
        return getFormat0(pattern, locale);
    }

    protected Format getFormat0(String pattern, Locale locale) {
        DateFormat formatter = null;
        boolean usePattern = (pattern != null && pattern.length() > 0);
        if (!usePattern) {
            formatter = (DateFormat) getFormat1(locale);
        } else if (locale == null) {
            formatter = new SimpleDateFormat(pattern);
        } else {
            DateFormatSymbols symbols = new DateFormatSymbols(locale);
            formatter = new SimpleDateFormat(pattern, symbols);
        }
        formatter.setLenient(false);
        return formatter;
    }

    /**
     * Returns a <code>DateFormat</code> for the specified Locale.
     *
     * @param locale The locale a <code>DateFormat</code> is required for, system default if null.
     * @return The <code>DateFormat</code> to created.
     */
    protected Format getFormat1(Locale locale) {

        DateFormat formatter = null;
        if (dateStyle >= 0 && timeStyle >= 0) {
            if (locale == null) {
                formatter = DateFormat.getDateTimeInstance(dateStyle, timeStyle);
            } else {
                formatter = DateFormat.getDateTimeInstance(dateStyle, timeStyle, locale);
            }
        } else if (timeStyle >= 0) {
            if (locale == null) {
                formatter = DateFormat.getTimeInstance(timeStyle);
            } else {
                formatter = DateFormat.getTimeInstance(timeStyle, locale);
            }
        } else {
            int useDateStyle = dateStyle >= 0 ? dateStyle : DateFormat.SHORT;
            if (locale == null) {
                formatter = DateFormat.getDateInstance(useDateStyle);
            } else {
                formatter = DateFormat.getDateInstance(useDateStyle, locale);
            }
        }
        formatter.setLenient(false);
        return formatter;
    }

    /**
     * Compares a calendar value to another, indicating whether it is equal, less then or more than
     * at a specified level.
     *
     * @param value The Calendar value.
     * @param compare The <code>Calendar</code> to check the value against.
     * @param field The field <i>level</i> to compare to - e.g. specifying <code>Calendar.MONTH
     *     </code> will compare the year and month portions of the calendar.
     * @return Zero if the first value is equal to the second, -1 if it is less than the second or
     *     +1 if it is greater than the second.
     */
    protected int compare(Calendar value, Calendar compare, int field) {

        int result = 0;

        result = calculateCompareResult(value, compare, Calendar.YEAR);
        if (result != 0 || field == Calendar.YEAR) {
            return result;
        }

        if (field == Calendar.WEEK_OF_YEAR) {
            return calculateCompareResult(value, compare, Calendar.WEEK_OF_YEAR);
        }

        if (field == Calendar.DAY_OF_YEAR) {
            return calculateCompareResult(value, compare, Calendar.DAY_OF_YEAR);
        }

        result = calculateCompareResult(value, compare, Calendar.MONTH);
        if (result != 0 || field == Calendar.MONTH) {
            return result;
        }

        if (field == Calendar.WEEK_OF_MONTH) {
            return calculateCompareResult(value, compare, Calendar.WEEK_OF_MONTH);
        }

        result = calculateCompareResult(value, compare, Calendar.DATE);
        if (result != 0
                || (field == Calendar.DATE
                        || field == Calendar.DAY_OF_WEEK
                        || field == Calendar.DAY_OF_WEEK_IN_MONTH)) {
            return result;
        }

        return compareTime(value, compare, field);
    }

    /**
     * Compares a calendar time value to another, indicating whether it is equal, less then or more
     * than at a specified level.
     *
     * @param value The Calendar value.
     * @param compare The <code>Calendar</code> to check the value against.
     * @param field The field <i>level</i> to compare to - e.g. specifying <code>Calendar.MINUTE
     *     </code> will compare the hours and minutes portions of the calendar.
     * @return Zero if the first value is equal to the second, -1 if it is less than the second or
     *     +1 if it is greater than the second.
     */
    protected int compareTime(Calendar value, Calendar compare, int field) {

        int result = 0;

        result = calculateCompareResult(value, compare, Calendar.HOUR_OF_DAY);
        if (result != 0 || (field == Calendar.HOUR || field == Calendar.HOUR_OF_DAY)) {
            return result;
        }

        result = calculateCompareResult(value, compare, Calendar.MINUTE);
        if (result != 0 || field == Calendar.MINUTE) {
            return result;
        }

        result = calculateCompareResult(value, compare, Calendar.SECOND);
        if (result != 0 || field == Calendar.SECOND) {
            return result;
        }

        if (field == Calendar.MILLISECOND) {
            return calculateCompareResult(value, compare, Calendar.MILLISECOND);
        }

        throw new IllegalArgumentException("Invalid field: " + field);
    }

    /**
     * Compares a calendar's quarter value to another, indicating whether it is equal, less then or
     * more than the specified quarter.
     *
     * @param value The Calendar value.
     * @param compare The <code>Calendar</code> to check the value against.
     * @param monthOfFirstQuarter The month that the first quarter starts.
     * @return Zero if the first quarter is equal to the second, -1 if it is less than the second or
     *     +1 if it is greater than the second.
     */
    protected int compareQuarters(Calendar value, Calendar compare, int monthOfFirstQuarter) {
        int valueQuarter = calculateQuarter(value, monthOfFirstQuarter);
        int compareQuarter = calculateQuarter(compare, monthOfFirstQuarter);
        if (valueQuarter < compareQuarter) {
            return -1;
        } else if (valueQuarter > compareQuarter) {
            return 1;
        } else {
            return 0;
        }
    }

    /**
     * Calculate the quarter for the specified Calendar.
     *
     * @param calendar The Calendar value.
     * @param monthOfFirstQuarter The month that the first quarter starts.
     * @return The calculated quarter.
     */
    private int calculateQuarter(Calendar calendar, int monthOfFirstQuarter) {
        int year = calendar.get(Calendar.YEAR);

        int month = (calendar.get(Calendar.MONTH) + 1);
        int relativeMonth =
                (month >= monthOfFirstQuarter)
                        ? (month - monthOfFirstQuarter)
                        : (month + (12 - monthOfFirstQuarter)); // CHECKSTYLE IGNORE MagicNumber
        int quarter = ((relativeMonth / 3) + 1); // CHECKSTYLE IGNORE MagicNumber
        if (month < monthOfFirstQuarter) {
            --year;
        }
        return (year * 10) + quarter; // CHECKSTYLE IGNORE MagicNumber
    }

    /**
     * Compares the field from two calendars indicating whether the field for the first calendar is
     * equal to, less than or greater than the field from the second calendar.
     *
     * @param value The Calendar value.
     * @param compare The <code>Calendar</code> to check the value against.
     * @param field The field to compare for the calendars.
     * @return Zero if the first calendar's field is equal to the seconds, -1 if it is less than the
     *     seconds or +1 if it is greater than the seconds.
     */
    private int calculateCompareResult(Calendar value, Calendar compare, int field) {
        int difference = value.get(field) - compare.get(field);
        if (difference < 0) {
            return -1;
        } else if (difference > 0) {
            return 1;
        } else {
            return 0;
        }
    }
}
