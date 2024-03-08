package org.apache.commons.validator.routines;

import java.math.BigInteger;
import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class BigIntegerValidator extends AbstractNumberValidator {
  private static final BigIntegerValidator VALIDATOR = BigIntegerValidator.BigIntegerValidator1();
  private static final long serialVersionUID = 6713144356347139988L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/BigIntegerValidator.py", "BigIntegerValidator");
  private Value obj;

  public BigIntegerValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    // return BigInteger.valueOf(((Number) value).longValue());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue(BigInteger value, long max) {
    //
    // return (value.longValue() <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue", value, max).as(boolean.class);
  }

  public boolean minValue(BigInteger value, long min) {
    //
    // return (value.longValue() >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue", value, min).as(boolean.class);
  }

  public boolean isInRange(BigInteger value, long min, long max) {
    //
    // return (value.longValue() >= min && value.longValue() <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange", value, min, max).as(boolean.class);
  }

  public BigInteger validate3(String value, String pattern, Locale locale) {
    //
    // return (BigInteger) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(BigInteger.class);
  }

  public BigInteger validate2(String value, Locale locale) {
    //
    // return (BigInteger) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(BigInteger.class);
  }

  public BigInteger validate1(String value, String pattern) {
    //
    // return (BigInteger) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(BigInteger.class);
  }

  public BigInteger validate0(String value) {
    //
    // return (BigInteger) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(BigInteger.class);
  }

  public static BigIntegerValidator BigIntegerValidator1() {
    //
    // return new BigIntegerValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("BigIntegerValidator1").as(BigIntegerValidator.class);
  }

  public BigIntegerValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, false);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static BigIntegerValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(BigIntegerValidator.class);
  }
}
