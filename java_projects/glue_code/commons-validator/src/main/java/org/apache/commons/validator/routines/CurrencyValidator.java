package org.apache.commons.validator.routines;

import java.text.Format;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class CurrencyValidator extends BigDecimalValidator {
  private static final char CURRENCY_SYMBOL = '\u00A4';
  private static final CurrencyValidator VALIDATOR = CurrencyValidator.CurrencyValidator1();
  private static final long serialVersionUID = -4201640771171486514L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/CurrencyValidator.py", "CurrencyValidator");
  private Value obj;

  public CurrencyValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object parse(String value, Format formatter) {
    //
    //
    // Object parsedValue = super.parse(value, formatter);
    // if (parsedValue != null || !(formatter instanceof DecimalFormat)) {
    // return parsedValue;
    // }
    //
    // DecimalFormat decimalFormat = (DecimalFormat) formatter;
    // String pattern = decimalFormat.toPattern();
    // if (pattern.indexOf(CURRENCY_SYMBOL) >= 0) {
    // StringBuilder buffer = new StringBuilder(pattern.length());
    // for (int i = 0; i < pattern.length(); i++) {
    // if (pattern.charAt(i) != CURRENCY_SYMBOL) {
    // buffer.append(pattern.charAt(i));
    // }
    // }
    // decimalFormat.applyPattern(buffer.toString());
    // parsedValue = super.parse(value, decimalFormat);
    // }
    // return parsedValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse", value, formatter).as(Object.class);
  }

  public static CurrencyValidator CurrencyValidator1() {
    //
    // return new CurrencyValidator(true, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CurrencyValidator1").as(CurrencyValidator.class);
  }

  public CurrencyValidator(boolean strict, boolean allowFractions) {
    //
    // super(strict, CURRENCY_FORMAT, allowFractions);
    //

    this.obj = clz.invokeMember("__init__", strict, allowFractions);
  }

  public static BigDecimalValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(BigDecimalValidator.class);
  }
}
