package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class FloatValidator extends AbstractNumberValidator {
  private static final FloatValidator VALIDATOR = FloatValidator.FloatValidator1();
  private static final long serialVersionUID = -4513245432806414267L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/FloatValidator.py", "FloatValidator");
  private Value obj;

  public FloatValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    //
    // double doubleValue = ((Number) value).doubleValue();
    //
    // if (doubleValue > 0) {
    // if (doubleValue < Float.MIN_VALUE) {
    // return null;
    // }
    // if (doubleValue > Float.MAX_VALUE) {
    // return null;
    // }
    // } else if (doubleValue < 0) {
    // double posDouble = doubleValue * -1;
    // if (posDouble < Float.MIN_VALUE) {
    // return null;
    // }
    // if (posDouble > Float.MAX_VALUE) {
    // return null;
    // }
    // }
    //
    // return Float.valueOf((float) doubleValue);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue1(Float value, float max) {
    //
    // return maxValue0(value.floatValue(), max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public boolean maxValue0(float value, float max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public boolean minValue1(Float value, float min) {
    //
    // return minValue0(value.floatValue(), min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public boolean minValue0(float value, float min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public boolean isInRange1(Float value, float min, float max) {
    //
    // return isInRange0(value.floatValue(), min, max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public boolean isInRange0(float value, float min, float max) {
    //
    // return (value >= min && value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public Float validate3(String value, String pattern, Locale locale) {
    //
    // return (Float) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(Float.class);
  }

  public Float validate2(String value, Locale locale) {
    //
    // return (Float) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(Float.class);
  }

  public Float validate1(String value, String pattern) {
    //
    // return (Float) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(Float.class);
  }

  public Float validate0(String value) {
    //
    // return (Float) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Float.class);
  }

  public static FloatValidator FloatValidator1() {
    //
    // return new FloatValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("FloatValidator1").as(FloatValidator.class);
  }

  public FloatValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, true);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static FloatValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(FloatValidator.class);
  }
}
