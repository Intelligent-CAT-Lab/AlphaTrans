package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class ShortValidator extends AbstractNumberValidator {
  private static final ShortValidator VALIDATOR = ShortValidator.ShortValidator1();
  private static final long serialVersionUID = -5227510699747787066L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/ShortValidator.py", "ShortValidator");
  private Value obj;

  public ShortValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    //
    // long longValue = ((Number) value).longValue();
    //
    // if (longValue < Short.MIN_VALUE || longValue > Short.MAX_VALUE) {
    // return null;
    // }
    // return Short.valueOf((short) longValue);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue1(Short value, short max) {
    //
    // return maxValue0(value.shortValue(), max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public boolean maxValue0(short value, short max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public boolean minValue1(Short value, short min) {
    //
    // return minValue0(value.shortValue(), min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public boolean minValue0(short value, short min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public boolean isInRange1(Short value, short min, short max) {
    //
    // return isInRange0(value.shortValue(), min, max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public boolean isInRange0(short value, short min, short max) {
    //
    // return (value >= min && value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public Short validate3(String value, String pattern, Locale locale) {
    //
    // return (Short) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(Short.class);
  }

  public Short validate2(String value, Locale locale) {
    //
    // return (Short) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(Short.class);
  }

  public Short validate1(String value, String pattern) {
    //
    // return (Short) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(Short.class);
  }

  public Short validate0(String value) {
    //
    // return (Short) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Short.class);
  }

  public static ShortValidator ShortValidator1() {
    //
    // return new ShortValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ShortValidator1").as(ShortValidator.class);
  }

  public ShortValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, false);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static ShortValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(ShortValidator.class);
  }
}
