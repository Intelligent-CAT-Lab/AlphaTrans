package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class ByteValidator extends AbstractNumberValidator {
  private static final ByteValidator VALIDATOR = ByteValidator.ByteValidator1();
  private static final long serialVersionUID = 7001640945881854649L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/ByteValidator.py", "ByteValidator");
  private Value obj;

  public ByteValidator(Value obj) {
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
    // if (longValue >= Byte.MIN_VALUE && longValue <= Byte.MAX_VALUE) {
    // return Byte.valueOf((byte) longValue);
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue1(Byte value, byte max) {
    //
    // return maxValue0(value.byteValue(), max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public boolean maxValue0(byte value, byte max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public boolean minValue1(Byte value, byte min) {
    //
    // return minValue0(value.byteValue(), min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public boolean minValue0(byte value, byte min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public boolean isInRange1(Byte value, byte min, byte max) {
    //
    // return isInRange0(value.byteValue(), min, max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public boolean isInRange0(byte value, byte min, byte max) {
    //
    // return (value >= min && value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public Byte validate3(String value, String pattern, Locale locale) {
    //
    // return (Byte) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(Byte.class);
  }

  public Byte validate2(String value, Locale locale) {
    //
    // return (Byte) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(Byte.class);
  }

  public Byte validate1(String value, String pattern) {
    //
    // return (Byte) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(Byte.class);
  }

  public Byte validate0(String value) {
    //
    // return (Byte) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Byte.class);
  }

  public static ByteValidator ByteValidator1() {
    //
    // return new ByteValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ByteValidator1").as(ByteValidator.class);
  }

  public ByteValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, false);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static ByteValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(ByteValidator.class);
  }
}
