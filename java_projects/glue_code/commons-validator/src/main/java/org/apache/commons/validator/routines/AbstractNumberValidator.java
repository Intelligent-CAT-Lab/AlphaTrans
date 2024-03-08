package org.apache.commons.validator.routines;

import java.text.Format;
import java.text.NumberFormat;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public abstract class AbstractNumberValidator extends AbstractFormatValidator {
  public static final int PERCENT_FORMAT = 2;
  public static final int CURRENCY_FORMAT = 1;
  public static final int STANDARD_FORMAT = 0;
  private static final long serialVersionUID = -3088817875906765463L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/AbstractNumberValidator.py", "AbstractNumberValidator");
  private Value obj;

  public AbstractNumberValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Format getFormat(String pattern, Locale locale) {
    //
    // return getFormat0(pattern, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormat", pattern, locale).as(Format.class);
  }

  public boolean isValid3(String value, String pattern, Locale locale) {
    //
    // Object parsedValue = parse(value, pattern, locale);
    // return (parsedValue == null ? false : true);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid3", value, pattern, locale).as(boolean.class);
  }

  protected Format getFormat1(Locale locale) {
    //
    // NumberFormat formatter = null;
    // switch (formatType) {
    // case CURRENCY_FORMAT:
    // if (locale == null) {
    // formatter = NumberFormat.getCurrencyInstance();
    // } else {
    // formatter = NumberFormat.getCurrencyInstance(locale);
    // }
    // break;
    // case PERCENT_FORMAT:
    // if (locale == null) {
    // formatter = NumberFormat.getPercentInstance();
    // } else {
    // formatter = NumberFormat.getPercentInstance(locale);
    // }
    // break;
    // default:
    // if (locale == null) {
    // formatter = NumberFormat.getInstance();
    // } else {
    // formatter = NumberFormat.getInstance(locale);
    // }
    // if (!isAllowFractions()) {
    // formatter.setParseIntegerOnly(true);
    // }
    // break;
    // }
    // return formatter;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormat1", locale).as(Format.class);
  }

  protected int determineScale(NumberFormat format) {
    //
    // if (!isStrict()) {
    // return -1;
    // }
    // if (!isAllowFractions() || format.isParseIntegerOnly()) {
    // return 0;
    // }
    // int minimumFraction = format.getMinimumFractionDigits();
    // int maximumFraction = format.getMaximumFractionDigits();
    // if (minimumFraction != maximumFraction) {
    // return -1;
    // }
    // int scale = minimumFraction;
    // if (format instanceof DecimalFormat) {
    // int multiplier = ((DecimalFormat) format).getMultiplier();
    // if (multiplier == 100) { // CHECKSTYLE IGNORE MagicNumber
    // scale += 2; // CHECKSTYLE IGNORE MagicNumber
    // } else if (multiplier == 1000) { // CHECKSTYLE IGNORE MagicNumber
    // scale += 3; // CHECKSTYLE IGNORE MagicNumber
    // }
    // } else if (formatType == PERCENT_FORMAT) {
    // scale += 2; // CHECKSTYLE IGNORE MagicNumber
    // }
    // return scale;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("determineScale", format).as(int.class);
  }

  protected Format getFormat0(String pattern, Locale locale) {
    //
    //
    // NumberFormat formatter = null;
    // boolean usePattern = (pattern != null && pattern.length() > 0);
    // if (!usePattern) {
    // formatter = (NumberFormat) getFormat1(locale);
    // } else if (locale == null) {
    // formatter = new DecimalFormat(pattern);
    // } else {
    // DecimalFormatSymbols symbols = new DecimalFormatSymbols(locale);
    // formatter = new DecimalFormat(pattern, symbols);
    // }
    //
    // if (!isAllowFractions()) {
    // formatter.setParseIntegerOnly(true);
    // }
    // return formatter;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormat0", pattern, locale).as(Format.class);
  }

  protected Object parse(String value, String pattern, Locale locale) {
    //
    //
    // value = (value == null ? null : value.trim());
    // if (value == null || value.length() == 0) {
    // return null;
    // }
    // Format formatter = getFormat0(pattern, locale);
    // return parse(value, formatter);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse", value, pattern, locale).as(Object.class);
  }

  public boolean maxValue(Number value, Number max) {
    //
    // if (isAllowFractions()) {
    // return (value.doubleValue() <= max.doubleValue());
    // }
    // return (value.longValue() <= max.longValue());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("maxValue", value, max).as(boolean.class);
  }

  public boolean minValue(Number value, Number min) {
    //
    // if (isAllowFractions()) {
    // return (value.doubleValue() >= min.doubleValue());
    // }
    // return (value.longValue() >= min.longValue());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("minValue", value, min).as(boolean.class);
  }

  public boolean isInRange(Number value, Number min, Number max) {
    //
    // return (minValue(value, min) && maxValue(value, max));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInRange", value, min, max).as(boolean.class);
  }

  public int getFormatType() {
    //
    // return formatType;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormatType").as(int.class);
  }

  public boolean isAllowFractions() {
    //
    // return allowFractions;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isAllowFractions").as(boolean.class);
  }

  public AbstractNumberValidator(boolean strict, int formatType, boolean allowFractions) {
    //
    // super(strict);
    // this.allowFractions = allowFractions;
    // this.formatType = formatType;
    //

    this.obj = clz.invokeMember("__init__", strict, formatType, allowFractions);
  }

  protected abstract Object processParsedValue(Object value, Format formatter);
}
