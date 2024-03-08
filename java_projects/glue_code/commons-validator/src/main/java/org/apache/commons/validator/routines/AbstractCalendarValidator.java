package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Calendar;
import java.util.Locale;
import java.util.TimeZone;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public abstract class AbstractCalendarValidator extends AbstractFormatValidator {
  private static final long serialVersionUID = -1410008585975827379L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/AbstractCalendarValidator.py", "AbstractCalendarValidator");
  private Value obj;

  public AbstractCalendarValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Format getFormat(String pattern, Locale locale) {
    //
    // return getFormat0(pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormat", pattern, locale).as(Format.class);
  }

  public boolean isValid3(String value, String pattern, Locale locale) {
    //
    // Object parsedValue = parse(value, pattern, locale, (TimeZone) null);
    // return (parsedValue == null ? false : true);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid3", value, pattern, locale).as(boolean.class);
  }

  protected int compareQuarters(Calendar value, Calendar compare, int monthOfFirstQuarter) {
    //
    // int valueQuarter = calculateQuarter(value, monthOfFirstQuarter);
    // int compareQuarter = calculateQuarter(compare, monthOfFirstQuarter);
    // if (valueQuarter < compareQuarter) {
    // return -1;
    // } else if (valueQuarter > compareQuarter) {
    // return 1;
    // } else {
    // return 0;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareQuarters", value, compare, monthOfFirstQuarter).as(int.class);
  }

  protected int compareTime(Calendar value, Calendar compare, int field) {
    //
    //
    // int result = 0;
    //
    // result = calculateCompareResult(value, compare, Calendar.HOUR_OF_DAY);
    // if (result != 0 || (field == Calendar.HOUR || field == Calendar.HOUR_OF_DAY)) {
    // return result;
    // }
    //
    // result = calculateCompareResult(value, compare, Calendar.MINUTE);
    // if (result != 0 || field == Calendar.MINUTE) {
    // return result;
    // }
    //
    // result = calculateCompareResult(value, compare, Calendar.SECOND);
    // if (result != 0 || field == Calendar.SECOND) {
    // return result;
    // }
    //
    // if (field == Calendar.MILLISECOND) {
    // return calculateCompareResult(value, compare, Calendar.MILLISECOND);
    // }
    //
    // throw new IllegalArgumentException("Invalid field: " + field);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareTime", value, compare, field).as(int.class);
  }

  protected int compare(Calendar value, Calendar compare, int field) {
    //
    //
    // int result = 0;
    //
    // result = calculateCompareResult(value, compare, Calendar.YEAR);
    // if (result != 0 || field == Calendar.YEAR) {
    // return result;
    // }
    //
    // if (field == Calendar.WEEK_OF_YEAR) {
    // return calculateCompareResult(value, compare, Calendar.WEEK_OF_YEAR);
    // }
    //
    // if (field == Calendar.DAY_OF_YEAR) {
    // return calculateCompareResult(value, compare, Calendar.DAY_OF_YEAR);
    // }
    //
    // result = calculateCompareResult(value, compare, Calendar.MONTH);
    // if (result != 0 || field == Calendar.MONTH) {
    // return result;
    // }
    //
    // if (field == Calendar.WEEK_OF_MONTH) {
    // return calculateCompareResult(value, compare, Calendar.WEEK_OF_MONTH);
    // }
    //
    // result = calculateCompareResult(value, compare, Calendar.DATE);
    // if (result != 0
    // || (field == Calendar.DATE
    // || field == Calendar.DAY_OF_WEEK
    // || field == Calendar.DAY_OF_WEEK_IN_MONTH)) {
    // return result;
    // }
    //
    // return compareTime(value, compare, field);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", value, compare, field).as(int.class);
  }

  protected Format getFormat1(Locale locale) {
    //
    //
    // DateFormat formatter = null;
    // if (dateStyle >= 0 && timeStyle >= 0) {
    // if (locale == null) {
    // formatter = DateFormat.getDateTimeInstance(dateStyle, timeStyle);
    // } else {
    // formatter = DateFormat.getDateTimeInstance(dateStyle, timeStyle, locale);
    // }
    // } else if (timeStyle >= 0) {
    // if (locale == null) {
    // formatter = DateFormat.getTimeInstance(timeStyle);
    // } else {
    // formatter = DateFormat.getTimeInstance(timeStyle, locale);
    // }
    // } else {
    // int useDateStyle = dateStyle >= 0 ? dateStyle : DateFormat.SHORT;
    // if (locale == null) {
    // formatter = DateFormat.getDateInstance(useDateStyle);
    // } else {
    // formatter = DateFormat.getDateInstance(useDateStyle, locale);
    // }
    // }
    // formatter.setLenient(false);
    // return formatter;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormat1", locale).as(Format.class);
  }

  protected Format getFormat0(String pattern, Locale locale) {
    //
    // DateFormat formatter = null;
    // boolean usePattern = (pattern != null && pattern.length() > 0);
    // if (!usePattern) {
    // formatter = (DateFormat) getFormat1(locale);
    // } else if (locale == null) {
    // formatter = new SimpleDateFormat(pattern);
    // } else {
    // DateFormatSymbols symbols = new DateFormatSymbols(locale);
    // formatter = new SimpleDateFormat(pattern, symbols);
    // }
    // formatter.setLenient(false);
    // return formatter;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormat0", pattern, locale).as(Format.class);
  }

  protected Object parse(String value, String pattern, Locale locale, TimeZone timeZone) {
    //
    //
    // value = (value == null ? null : value.trim());
    // if (value == null || value.length() == 0) {
    // return null;
    // }
    // DateFormat formatter = (DateFormat) getFormat0(pattern, locale);
    // if (timeZone != null) {
    // formatter.setTimeZone(timeZone);
    // }
    // return parse(value, formatter);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse", value, pattern, locale, timeZone).as(Object.class);
  }

  protected String format5(Object value, Format formatter) {
    //
    // if (value == null) {
    // return null;
    // } else if (value instanceof Calendar) {
    // value = ((Calendar) value).getTime();
    // }
    // return formatter.format(value);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format5", value, formatter).as(String.class);
  }

  public String format4(Object value, String pattern, Locale locale, TimeZone timeZone) {
    //
    // DateFormat formatter = (DateFormat) getFormat0(pattern, locale);
    // if (timeZone != null) {
    // formatter.setTimeZone(timeZone);
    // } else if (value instanceof Calendar) {
    // formatter.setTimeZone(((Calendar) value).getTimeZone());
    // }
    // return format5(value, formatter);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format4", value, pattern, locale, timeZone).as(String.class);
  }

  public String format3(Object value, String pattern, Locale locale) {
    //
    // return format4(value, pattern, locale, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format3", value, pattern, locale).as(String.class);
  }

  public String format2(Object value, Locale locale, TimeZone timeZone) {
    //
    // return format4(value, (String) null, locale, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format2", value, locale, timeZone).as(String.class);
  }

  public String format1(Object value, String pattern, TimeZone timeZone) {
    //
    // return format4(value, pattern, (Locale) null, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format1", value, pattern, timeZone).as(String.class);
  }

  public String format0(Object value, TimeZone timeZone) {
    //
    // return format4(value, (String) null, (Locale) null, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format0", value, timeZone).as(String.class);
  }

  public AbstractCalendarValidator(boolean strict, int dateStyle, int timeStyle) {
    //
    // super(strict);
    // this.dateStyle = dateStyle;
    // this.timeStyle = timeStyle;
    //

    this.obj = clz.invokeMember("__init__", strict, dateStyle, timeStyle);
  }

  private int calculateCompareResult(Calendar value, Calendar compare, int field) {
    //
    // int difference = value.get(field) - compare.get(field);
    // if (difference < 0) {
    // return -1;
    // } else if (difference > 0) {
    // return 1;
    // } else {
    // return 0;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("calculateCompareResult", value, compare, field).as(int.class);
  }

  private int calculateQuarter(Calendar calendar, int monthOfFirstQuarter) {
    //
    // int year = calendar.get(Calendar.YEAR);
    //
    // int month = (calendar.get(Calendar.MONTH) + 1);
    // int relativeMonth =
    // (month >= monthOfFirstQuarter)
    // ? (month - monthOfFirstQuarter)
    // : (month + (12 - monthOfFirstQuarter)); // CHECKSTYLE IGNORE MagicNumber
    // int quarter = ((relativeMonth / 3) + 1); // CHECKSTYLE IGNORE MagicNumber
    // if (month < monthOfFirstQuarter) {
    // --year;
    // }
    // return (year * 10) + quarter; // CHECKSTYLE IGNORE MagicNumber
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("calculateQuarter", calendar, monthOfFirstQuarter).as(int.class);
  }

  protected abstract Object processParsedValue(Object value, Format formatter);
}
