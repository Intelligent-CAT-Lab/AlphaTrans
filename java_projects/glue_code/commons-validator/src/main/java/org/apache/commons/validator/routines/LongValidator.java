package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class LongValidator extends AbstractNumberValidator {
  private static final LongValidator VALIDATOR = LongValidator.LongValidator1();
  private static final long serialVersionUID = -5117231731027866098L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/LongValidator.py", "LongValidator");
  private Value obj;

  public LongValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    //
    // if (value instanceof Long) {
    // return value;
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue1(Long value, long max) {
    //
    // return maxValue0(value.longValue(), max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public boolean maxValue0(long value, long max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public boolean minValue1(Long value, long min) {
    //
    // return minValue0(value.longValue(), min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public boolean minValue0(long value, long min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public boolean isInRange1(Long value, long min, long max) {
    //
    // return isInRange0(value.longValue(), min, max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public boolean isInRange0(long value, long min, long max) {
    //
    // return (value >= min && value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public Long validate3(String value, String pattern, Locale locale) {
    //
    // return (Long) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(Long.class);
  }

  public Long validate2(String value, Locale locale) {
    //
    // return (Long) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(Long.class);
  }

  public Long validate1(String value, String pattern) {
    //
    // return (Long) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(Long.class);
  }

  public Long validate0(String value) {
    //
    // return (Long) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Long.class);
  }

  public static LongValidator LongValidator1() {
    //
    // return new LongValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("LongValidator1").as(LongValidator.class);
  }

  public LongValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, false);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static LongValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(LongValidator.class);
  }
}
