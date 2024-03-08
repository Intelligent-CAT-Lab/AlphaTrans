package org.apache.commons.validator.routines;

import java.math.BigDecimal;
import java.text.Format;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class PercentValidator extends BigDecimalValidator {
  private static final BigDecimal POINT_ZERO_ONE = new BigDecimal("0.01");
  private static final char PERCENT_SYMBOL = '%';
  private static final PercentValidator VALIDATOR = PercentValidator.PercentValidator1();
  private static final long serialVersionUID = -3508241924961535772L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/PercentValidator.py", "PercentValidator");
  private Value obj;

  public PercentValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object parse(String value, Format formatter) {
    //
    //
    // BigDecimal parsedValue = (BigDecimal) super.parse(value, formatter);
    // if (parsedValue != null || !(formatter instanceof DecimalFormat)) {
    // return parsedValue;
    // }
    //
    // DecimalFormat decimalFormat = (DecimalFormat) formatter;
    // String pattern = decimalFormat.toPattern();
    // if (pattern.indexOf(PERCENT_SYMBOL) >= 0) {
    // StringBuilder buffer = new StringBuilder(pattern.length());
    // for (int i = 0; i < pattern.length(); i++) {
    // if (pattern.charAt(i) != PERCENT_SYMBOL) {
    // buffer.append(pattern.charAt(i));
    // }
    // }
    // decimalFormat.applyPattern(buffer.toString());
    // parsedValue = (BigDecimal) super.parse(value, decimalFormat);
    //
    // if (parsedValue != null) {
    // parsedValue = parsedValue.multiply(POINT_ZERO_ONE);
    // }
    // }
    // return parsedValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse", value, formatter).as(Object.class);
  }

  public static PercentValidator PercentValidator1() {
    //
    // return new PercentValidator(true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("PercentValidator1").as(PercentValidator.class);
  }

  public PercentValidator(boolean strict) {
    //
    // super(strict, PERCENT_FORMAT, true);
    //

    this.obj = clz.invokeMember("__init__", strict);
  }

  public static BigDecimalValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(BigDecimalValidator.class);
  }
}
