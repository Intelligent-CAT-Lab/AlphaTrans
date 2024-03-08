package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Calendar;
import java.util.Locale;
import java.util.TimeZone;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class CalendarValidator extends AbstractCalendarValidator {
  private static final CalendarValidator VALIDATOR = CalendarValidator.CalendarValidator1();
  private static final long serialVersionUID = 9109652318762134167L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/CalendarValidator.py", "CalendarValidator");
  private Value obj;

  public CalendarValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    // return ((DateFormat) formatter).getCalendar();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public int compareYears(Calendar value, Calendar compare) {
    //
    // return compare(value, compare, Calendar.YEAR);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareYears", value, compare).as(int.class);
  }

  public int compareQuarters1(Calendar value, Calendar compare, int monthOfFirstQuarter) {
    //
    // return super.compareQuarters(value, compare, monthOfFirstQuarter);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareQuarters1", value, compare, monthOfFirstQuarter).as(int.class);
  }

  public int compareQuarters0(Calendar value, Calendar compare) {
    //
    // return compareQuarters1(value, compare, 1);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareQuarters0", value, compare).as(int.class);
  }

  public int compareMonths(Calendar value, Calendar compare) {
    //
    // return compare(value, compare, Calendar.MONTH);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareMonths", value, compare).as(int.class);
  }

  public int compareWeeks(Calendar value, Calendar compare) {
    //
    // return compare(value, compare, Calendar.WEEK_OF_YEAR);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareWeeks", value, compare).as(int.class);
  }

  public int compareDates(Calendar value, Calendar compare) {
    //
    // return compare(value, compare, Calendar.DATE);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareDates", value, compare).as(int.class);
  }

  public static void adjustToTimeZone(Calendar value, TimeZone timeZone) {
    //
    // if (value.getTimeZone().hasSameRules(timeZone)) {
    // value.setTimeZone(timeZone);
    // } else {
    // int year = value.get(Calendar.YEAR);
    // int month = value.get(Calendar.MONTH);
    // int date = value.get(Calendar.DATE);
    // int hour = value.get(Calendar.HOUR_OF_DAY);
    // int minute = value.get(Calendar.MINUTE);
    // value.setTimeZone(timeZone);
    // value.set(year, month, date, hour, minute);
    // }
    //

    clz.invokeMember("adjustToTimeZone", value, timeZone);
  }

  public Calendar validate7(String value, String pattern, Locale locale, TimeZone timeZone) {
    //
    // return (Calendar) parse(value, pattern, locale, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate7", value, pattern, locale, timeZone).as(Calendar.class);
  }

  public Calendar validate6(String value, String pattern, Locale locale) {
    //
    // return (Calendar) parse(value, pattern, locale, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate6", value, pattern, locale).as(Calendar.class);
  }

  public Calendar validate5(String value, Locale locale, TimeZone timeZone) {
    //
    // return (Calendar) parse(value, (String) null, locale, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate5", value, locale, timeZone).as(Calendar.class);
  }

  public Calendar validate4(String value, Locale locale) {
    //
    // return (Calendar) parse(value, (String) null, locale, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate4", value, locale).as(Calendar.class);
  }

  public Calendar validate3(String value, String pattern, TimeZone timeZone) {
    //
    // return (Calendar) parse(value, pattern, (Locale) null, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, timeZone).as(Calendar.class);
  }

  public Calendar validate2(String value, String pattern) {
    //
    // return (Calendar) parse(value, pattern, (Locale) null, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, pattern).as(Calendar.class);
  }

  public Calendar validate1(String value, TimeZone timeZone) {
    //
    // return (Calendar) parse(value, (String) null, (Locale) null, timeZone);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, timeZone).as(Calendar.class);
  }

  public Calendar validate0(String value) {
    //
    // return (Calendar) parse(value, (String) null, (Locale) null, (TimeZone) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Calendar.class);
  }

  public static CalendarValidator CalendarValidator1() {
    //
    // return new CalendarValidator(true, DateFormat.SHORT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CalendarValidator1").as(CalendarValidator.class);
  }

  public CalendarValidator(boolean strict, int dateStyle) {
    //
    // super(strict, dateStyle, -1);
    //

    this.obj = clz.invokeMember("__init__", strict, dateStyle);
  }

  public static CalendarValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(CalendarValidator.class);
  }
}
