package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class IntegerValidator extends AbstractNumberValidator {
  private static final IntegerValidator VALIDATOR = IntegerValidator.IntegerValidator1();
  private static final long serialVersionUID = 422081746310306596L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/IntegerValidator.py", "IntegerValidator");
  private Value obj;

  public IntegerValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    //
    // if (value instanceof Long) {
    // long longValue = ((Long) value).longValue();
    // if (longValue >= Integer.MIN_VALUE && longValue <= Integer.MAX_VALUE) {
    // return Integer.valueOf((int) longValue);
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue1(Integer value, int max) {
    //
    // return maxValue0(value.intValue(), max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public boolean maxValue0(int value, int max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public boolean minValue1(Integer value, int min) {
    //
    // return minValue0(value.intValue(), min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public boolean minValue0(int value, int min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public boolean isInRange1(Integer value, int min, int max) {
    //
    // return isInRange0(value.intValue(), min, max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public boolean isInRange0(int value, int min, int max) {
    //
    // return (value >= min && value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public Integer validate3(String value, String pattern, Locale locale) {
    //
    // return (Integer) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(Integer.class);
  }

  public Integer validate2(String value, Locale locale) {
    //
    // return (Integer) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(Integer.class);
  }

  public Integer validate1(String value, String pattern) {
    //
    // return (Integer) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(Integer.class);
  }

  public Integer validate0(String value) {
    //
    // return (Integer) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Integer.class);
  }

  public static IntegerValidator IntegerValidator1() {
    //
    // return new IntegerValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("IntegerValidator1").as(IntegerValidator.class);
  }

  public IntegerValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, false);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static IntegerValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(IntegerValidator.class);
  }
}
