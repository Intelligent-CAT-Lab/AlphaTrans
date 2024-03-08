package org.apache.commons.validator.routines;

import java.math.BigDecimal;
import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class BigDecimalValidator extends AbstractNumberValidator {
  private static final BigDecimalValidator VALIDATOR = BigDecimalValidator.BigDecimalValidator2();
  private static final long serialVersionUID = -670320911490506772L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/BigDecimalValidator.py", "BigDecimalValidator");
  private Value obj;

  public BigDecimalValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    // BigDecimal decimal = null;
    // if (value instanceof Long) {
    // decimal = BigDecimal.valueOf(((Long) value).longValue());
    // } else {
    // decimal = new BigDecimal(value.toString());
    // }
    //
    // int scale = determineScale((NumberFormat) formatter);
    // if (scale >= 0) {
    // decimal = decimal.setScale(scale, BigDecimal.ROUND_DOWN);
    // }
    //
    // return decimal;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue(BigDecimal value, double max) {
    //
    // return (value.doubleValue() <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue", value, max).as(boolean.class);
  }

  public boolean minValue(BigDecimal value, double min) {
    //
    // return (value.doubleValue() >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue", value, min).as(boolean.class);
  }

  public boolean isInRange(BigDecimal value, double min, double max) {
    //
    // return (value.doubleValue() >= min && value.doubleValue() <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange", value, min, max).as(boolean.class);
  }

  public BigDecimal validate3(String value, String pattern, Locale locale) {
    //
    // return (BigDecimal) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(BigDecimal.class);
  }

  public BigDecimal validate2(String value, Locale locale) {
    //
    // return (BigDecimal) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(BigDecimal.class);
  }

  public BigDecimal validate1(String value, String pattern) {
    //
    // return (BigDecimal) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(BigDecimal.class);
  }

  public BigDecimal validate0(String value) {
    //
    // return (BigDecimal) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(BigDecimal.class);
  }

  public static BigDecimalValidator BigDecimalValidator2() {
    //
    // return BigDecimalValidator1(true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("BigDecimalValidator2").as(BigDecimalValidator.class);
  }

  public static BigDecimalValidator BigDecimalValidator1(boolean strict) {
    //
    // return new BigDecimalValidator(strict, STANDARD_FORMAT, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("BigDecimalValidator1", strict).as(BigDecimalValidator.class);
  }

  protected BigDecimalValidator(boolean strict, int formatType, boolean allowFractions) {
    //
    // super(strict, formatType, allowFractions);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType, allowFractions);
  }

  public static BigDecimalValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(BigDecimalValidator.class);
  }
}
