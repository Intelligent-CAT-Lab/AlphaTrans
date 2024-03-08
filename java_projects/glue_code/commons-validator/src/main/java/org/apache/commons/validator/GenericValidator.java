package org.apache.commons.validator;

import java.io.Serializable;
import java.util.Locale;
import org.apache.commons.validator.routines.CreditCardValidator;
import org.apache.commons.validator.routines.UrlValidator;
import org.graalvm.polyglot.Value;

public class GenericValidator implements Serializable {
  private static final CreditCardValidator CREDIT_CARD_VALIDATOR =
      CreditCardValidator.CreditCardValidator0();
  private static final UrlValidator URL_VALIDATOR = UrlValidator.UrlValidator6();
  private static final long serialVersionUID = -7212095066891517618L;
  private static Value clz =
      ContextInitializer.getPythonClass("/GenericValidator.py", "GenericValidator");
  private Value obj;

  public GenericValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static boolean maxValue3(float value, float max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("maxValue3", value, max).as(boolean.class);
  }

  public static boolean maxValue2(double value, double max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("maxValue2", value, max).as(boolean.class);
  }

  public static boolean maxValue1(long value, long max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("maxValue1", value, max).as(boolean.class);
  }

  public static boolean maxValue0(int value, int max) {
    //
    // return (value <= max);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("maxValue0", value, max).as(boolean.class);
  }

  public static boolean minValue3(float value, float min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minValue3", value, min).as(boolean.class);
  }

  public static boolean minValue2(double value, double min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minValue2", value, min).as(boolean.class);
  }

  public static boolean minValue1(long value, long min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minValue1", value, min).as(boolean.class);
  }

  public static boolean minValue0(int value, int min) {
    //
    // return (value >= min);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minValue0", value, min).as(boolean.class);
  }

  public static boolean minLength1(String value, int min, int lineEndLength) {
    //
    // int adjustAmount = adjustForLineEnding(value, lineEndLength);
    // return ((value.length() + adjustAmount) >= min);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minLength1", value, min, lineEndLength).as(boolean.class);
  }

  public static boolean minLength0(String value, int min) {
    //
    // return (value.length() >= min);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minLength0", value, min).as(boolean.class);
  }

  public static boolean maxLength1(String value, int max, int lineEndLength) {
    //
    // int adjustAmount = adjustForLineEnding(value, lineEndLength);
    // return ((value.length() + adjustAmount) <= max);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("maxLength1", value, max, lineEndLength).as(boolean.class);
  }

  public static boolean maxLength0(String value, int max) {
    //
    // return (value.length() <= max);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("maxLength0", value, max).as(boolean.class);
  }

  public static boolean isUrl(String value) {
    //
    // return URL_VALIDATOR.isValid(value);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isUrl", value).as(boolean.class);
  }

  public static boolean isEmail(String value) {
    //
    // return EmailValidator.getInstance0().isValid(value);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isEmail", value).as(boolean.class);
  }

  public static boolean isCreditCard(String value) {
    //
    // return CREDIT_CARD_VALIDATOR.isValid(value);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isCreditCard", value).as(boolean.class);
  }

  public static boolean isInRange5(double value, double min, double max) {
    //
    // return ((value >= min) && (value <= max));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInRange5", value, min, max).as(boolean.class);
  }

  public static boolean isInRange4(long value, long min, long max) {
    //
    // return ((value >= min) && (value <= max));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInRange4", value, min, max).as(boolean.class);
  }

  public static boolean isInRange3(short value, short min, short max) {
    //
    // return ((value >= min) && (value <= max));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInRange3", value, min, max).as(boolean.class);
  }

  public static boolean isInRange2(float value, float min, float max) {
    //
    // return ((value >= min) && (value <= max));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInRange2", value, min, max).as(boolean.class);
  }

  public static boolean isInRange1(int value, int min, int max) {
    //
    // return ((value >= min) && (value <= max));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInRange1", value, min, max).as(boolean.class);
  }

  public static boolean isInRange0(byte value, byte min, byte max) {
    //
    // return ((value >= min) && (value <= max));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInRange0", value, min, max).as(boolean.class);
  }

  public static boolean isDate1(String value, String datePattern, boolean strict) {
    //
    // return org.apache.commons.validator.DateValidator.getInstance()
    // .isValid0(value, datePattern, strict);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isDate1", value, datePattern, strict).as(boolean.class);
  }

  public static boolean isDate0(String value, Locale locale) {
    //
    // return DateValidator.getInstance().isValid2(value, locale);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isDate0", value, locale).as(boolean.class);
  }

  public static boolean isDouble(String value) {
    //
    // return (GenericTypeValidator.formatDouble0(value) != null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isDouble", value).as(boolean.class);
  }

  public static boolean isFloat(String value) {
    //
    // return (GenericTypeValidator.formatFloat0(value) != null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isFloat", value).as(boolean.class);
  }

  public static boolean isLong(String value) {
    //
    // return (GenericTypeValidator.formatLong0(value) != null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isLong", value).as(boolean.class);
  }

  public static boolean isInt(String value) {
    //
    // return (GenericTypeValidator.formatInt0(value) != null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isInt", value).as(boolean.class);
  }

  public static boolean isShort(String value) {
    //
    // return (GenericTypeValidator.formatShort0(value) != null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isShort", value).as(boolean.class);
  }

  public static boolean isByte(String value) {
    //
    // return (GenericTypeValidator.formatByte0(value) != null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isByte", value).as(boolean.class);
  }

  public static boolean matchRegexp(String value, String regexp) {
    //
    // if (regexp == null || regexp.length() <= 0) {
    // return false;
    // }
    //
    // return Pattern.matches(regexp, value);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("matchRegexp", value, regexp).as(boolean.class);
  }

  public static boolean isBlankOrNull(String value) {
    //
    // return ((value == null) || (value.trim().length() == 0));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isBlankOrNull", value).as(boolean.class);
  }

  private static int adjustForLineEnding(String value, int lineEndLength) {
    //
    // int nCount = 0;
    // int rCount = 0;
    // for (int i = 0; i < value.length(); i++) {
    // if (value.charAt(i) == '\n') {
    // nCount++;
    // }
    // if (value.charAt(i) == '\r') {
    // rCount++;
    // }
    // }
    // return ((nCount * lineEndLength) - (rCount + nCount));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("adjustForLineEnding", value, lineEndLength).as(int.class);
  }
}
