package org.apache.commons.validator.routines;

import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class DoubleValidator extends AbstractNumberValidator {
  private static final DoubleValidator VALIDATOR = DoubleValidator.DoubleValidator1();
  private static final long serialVersionUID = 5867946581318211330L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/DoubleValidator.py", "DoubleValidator");
  private Value obj;

  public DoubleValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object processParsedValue(Object value, Format formatter) {
    //
    //
    // if (value instanceof Double) {
    // return value;
    // }
    // return Double.valueOf(((Number) value).doubleValue());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("processParsedValue", value, formatter).as(Object.class);
  }

  public boolean maxValue1(Double value, double max) {
    //
    // return maxValue0(value.doubleValue(), max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public boolean maxValue0(double value, double max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public boolean minValue1(Double value, double min) {
    //
    // return minValue0(value.doubleValue(), min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public boolean minValue0(double value, double min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public boolean isInRange1(Double value, double min, double max) {
    //
    // return isInRange0(value.doubleValue(), min, max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public boolean isInRange0(double value, double min, double max) {
    //
    // return (value >= min && value <= max);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public Double validate3(String value, String pattern, Locale locale) {
    //
    // return (Double) parse(value, pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate3", value, pattern, locale).as(Double.class);
  }

  public Double validate2(String value, Locale locale) {
    //
    // return (Double) parse(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate2", value, locale).as(Double.class);
  }

  public Double validate1(String value, String pattern) {
    //
    // return (Double) parse(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate1", value, pattern).as(Double.class);
  }

  public Double validate0(String value) {
    //
    // return (Double) parse(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate0", value).as(Double.class);
  }

  public static DoubleValidator DoubleValidator1() {
    //
    // return new DoubleValidator(true, STANDARD_FORMAT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("DoubleValidator1").as(DoubleValidator.class);
  }

  public DoubleValidator(boolean strict, int formatType) {
    //
    // super(strict, formatType, true);
    //

    this.obj = clz.invokeMember("__init__", strict, formatType);
  }

  public static DoubleValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(DoubleValidator.class);
  }
}
