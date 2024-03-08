package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Calendar;
import java.util.Locale;
import java.util.TimeZone;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class TimeValidator extends AbstractCalendarValidator {
  private static final TimeValidator VALIDATOR = TimeValidator.TimeValidator1();
  private static final long serialVersionUID = 3494007492269691581L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/TimeValidator.py", "TimeValidator");
  private Value obj;

  public TimeValidator(Value obj) {
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

  public int compareHours(Calendar value, Calendar compare) {
    //
    // return compareTime(value, compare, Calendar.HOUR_OF_DAY);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareHours", value, compare).as(int.class);
  }

  public int compareMinutes(Calendar value, Calendar compare) {
    //
    // return compareTime(value, compare, Calendar.MINUTE);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareMinutes", value, compare).as(int.class);
  }

  public int compareSeconds(Calendar value, Calendar compare) {
    //
    // return compareTime(value, compare, Calendar.SECOND);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareSeconds", value, compare).as(int.class);
  }

  public int compareTime(Calendar value, Calendar compare) {
    //
    // return compareTime(value, compare, Calendar.MILLISECOND);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareTime", value, compare).as(int.class);
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

  public static TimeValidator TimeValidator1() {
    //
    // return new TimeValidator(true, DateFormat.SHORT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("TimeValidator1").as(TimeValidator.class);
  }

  public TimeValidator(boolean strict, int timeStyle) {
    //
    // super(strict, -1, timeStyle);
    //

    this.obj = clz.invokeMember("__init__", strict, timeStyle);
  }

  public static TimeValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(TimeValidator.class);
  }
}
