package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class DateValidator extends AbstractCalendarValidator {
  private static final DateValidator VALIDATOR = DateValidator.DateValidator1();
  private static final long serialVersionUID = -3966328400469953190L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/DateValidator.py", "DateValidator");
  private Value obj;

  public DateValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    // return value;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public int compareYears(Date value, Date compare, TimeZone timeZone) {
    //
    // Calendar calendarValue = getCalendar(value, timeZone);
    // Calendar calendarCompare = getCalendar(compare, timeZone);
    // return compare(calendarValue, calendarCompare, Calendar.YEAR);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareYears", value, compare, timeZone).as(int.class);
  }

  public int compareQuarters1(
      Date value, Date compare, TimeZone timeZone, int monthOfFirstQuarter) {
    //
    // Calendar calendarValue = getCalendar(value, timeZone);
    // Calendar calendarCompare = getCalendar(compare, timeZone);
    // return super.compareQuarters(calendarValue, calendarCompare, monthOfFirstQuarter);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareQuarters1", value, compare, timeZone, monthOfFirstQuarter)
        .as(int.class);
  }

  public int compareQuarters0(Date value, Date compare, TimeZone timeZone) {
    //
    // return compareQuarters1(value, compare, timeZone, 1);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareQuarters0", value, compare, timeZone).as(int.class);
  }

  public int compareMonths(Date value, Date compare, TimeZone timeZone) {
    //
    // Calendar calendarValue = getCalendar(value, timeZone);
    // Calendar calendarCompare = getCalendar(compare, timeZone);
    // return compare(calendarValue, calendarCompare, Calendar.MONTH);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareMonths", value, compare, timeZone).as(int.class);
  }

  public int compareWeeks(Date value, Date compare, TimeZone timeZone) {
    //
    // Calendar calendarValue = getCalendar(value, timeZone);
    // Calendar calendarCompare = getCalendar(compare, timeZone);
    // return compare(calendarValue, calendarCompare, Calendar.WEEK_OF_YEAR);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareWeeks", value, compare, timeZone).as(int.class);
  }

  public int compareDates(Date value, Date compare, TimeZone timeZone) {
    //
    // Calendar calendarValue = getCalendar(value, timeZone);
    // Calendar calendarCompare = getCalendar(compare, timeZone);
    // return compare(calendarValue, calendarCompare, Calendar.DATE);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareDates", value, compare, timeZone).as(int.class);
  }

  public Date validate7(String value, String pattern, Locale locale, TimeZone timeZone) {
    //
    // return (Date) parse(value, pattern, locale, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate7", value, pattern, locale, timeZone).as(Date.class);
  }

  public Date validate6(String value, String pattern, Locale locale) {
    //
    // return (Date) parse(value, pattern, locale, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate6", value, pattern, locale).as(Date.class);
  }

  public Date validate5(String value, Locale locale, TimeZone timeZone) {
    //
    // return (Date) parse(value, (String) null, locale, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate5", value, locale, timeZone).as(Date.class);
  }

  public Date validate4(String value, Locale locale) {
    //
    // return (Date) parse(value, (String) null, locale, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate4", value, locale).as(Date.class);
  }

  public Date validate3(String value, String pattern, TimeZone timeZone) {
    //
    // return (Date) parse(value, pattern, (Locale) null, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, timeZone).as(Date.class);
  }

  public Date validate2(String value, String pattern) {
    //
    // return (Date) parse(value, pattern, (Locale) null, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, pattern).as(Date.class);
  }

  public Date validate1(String value, TimeZone timeZone) {
    //
    // return (Date) parse(value, (String) null, (Locale) null, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, timeZone).as(Date.class);
  }

  public Date validate0(String value) {
    //
    // return (Date) parse(value, (String) null, (Locale) null, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Date.class);
  }

  public static DateValidator DateValidator1() {
    //
    // return new DateValidator(true, DateFormat.SHORT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("DateValidator1").as(DateValidator.class);
  }

  public DateValidator(boolean strict, int dateStyle) {
    //
    // super(strict, dateStyle, -1);
    //

    this.obj = clz.invokeMember("__init__", strict, dateStyle);
  }

  public static DateValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(DateValidator.class);
  }

  private Calendar getCalendar(Date value, TimeZone timeZone) {
    //
    //
    // Calendar calendar = null;
    // if (timeZone != null) {
    // calendar = Calendar.getInstance(timeZone);
    // } else {
    // calendar = Calendar.getInstance();
    // }
    // calendar.setTime(value);
    // return calendar;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCalendar", value, timeZone).as(Calendar.class);
  }
}
