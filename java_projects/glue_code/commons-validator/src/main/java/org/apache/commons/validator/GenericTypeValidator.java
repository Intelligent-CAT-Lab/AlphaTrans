package org.apache.commons.validator;

import java.io.Serializable;
import java.util.Date;
import java.util.Locale;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.graalvm.polyglot.Value;

public class GenericTypeValidator implements Serializable {
  private static final Log LOG = LogFactory.getLog(GenericTypeValidator.class);
  private static final long serialVersionUID = 5487162314134261703L;
  private static Value clz =
      ContextInitializer.getPythonClass("/GenericTypeValidator.py", "GenericTypeValidator");
  private Value obj;

  public GenericTypeValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static Long formatCreditCard(String value) {
    //
    // return GenericValidator.isCreditCard(value) ? Long.valueOf(value) : null;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatCreditCard", value).as(Long.class);
  }

  public static Date formatDate1(String value, String datePattern, boolean strict) {
    //
    // Date date = null;
    //
    // if (value == null || datePattern == null || datePattern.length() == 0) {
    // return null;
    // }
    //
    // try {
    // SimpleDateFormat formatter = new SimpleDateFormat(datePattern);
    // formatter.setLenient(false);
    //
    // date = formatter.parse(value);
    //
    // if (strict && datePattern.length() != value.length()) {
    // date = null;
    // }
    // } catch (ParseException e) {
    // if (LOG.isDebugEnabled()) {
    // LOG.debug(
    // "Date parse failed value=["
    // + value
    // + "], "
    // + "pattern=["
    // + datePattern
    // + "], "
    // + "strict=["
    // + strict
    // + "] "
    // + e);
    // }
    // }
    //
    // return date;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatDate1", value, datePattern, strict).as(Date.class);
  }

  public static Date formatDate0(String value, Locale locale) {
    //
    // Date date = null;
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // DateFormat formatterShort = null;
    // DateFormat formatterDefault = null;
    // if (locale != null) {
    // formatterShort = DateFormat.getDateInstance(DateFormat.SHORT, locale);
    // formatterDefault = DateFormat.getDateInstance(DateFormat.DEFAULT, locale);
    // } else {
    // formatterShort = DateFormat.getDateInstance(DateFormat.SHORT, Locale.getDefault());
    // formatterDefault =
    // DateFormat.getDateInstance(DateFormat.DEFAULT, Locale.getDefault());
    // }
    //
    // formatterShort.setLenient(false);
    // formatterDefault.setLenient(false);
    //
    // try {
    // date = formatterShort.parse(value);
    // } catch (ParseException e) {
    // date = formatterDefault.parse(value);
    // }
    // } catch (ParseException e) {
    // if (LOG.isDebugEnabled()) {
    // LOG.debug(
    // "Date parse failed value=["
    // + value
    // + "], "
    // + "locale=["
    // + locale
    // + "] "
    // + e);
    // }
    // }
    //
    // return date;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatDate0", value, locale).as(Date.class);
  }

  public static Double formatDouble1(String value, Locale locale) {
    //
    // Double result = null;
    //
    // if (value != null) {
    // NumberFormat formatter = null;
    // if (locale != null) {
    // formatter = NumberFormat.getInstance(locale);
    // } else {
    // formatter = NumberFormat.getInstance(Locale.getDefault());
    // }
    // ParsePosition pos = new ParsePosition(0);
    // Number num = formatter.parse(value, pos);
    //
    // if (pos.getErrorIndex() == -1
    // && pos.getIndex() == value.length()
    // && num.doubleValue() >= (Double.MAX_VALUE * -1)
    // && num.doubleValue() <= Double.MAX_VALUE) {
    // result = Double.valueOf(num.doubleValue());
    // }
    // }
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatDouble1", value, locale).as(Double.class);
  }

  public static Double formatDouble0(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // return Double.valueOf(value);
    // } catch (NumberFormatException e) {
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatDouble0", value).as(Double.class);
  }

  public static Float formatFloat1(String value, Locale locale) {
    //
    // Float result = null;
    //
    // if (value != null) {
    // NumberFormat formatter = null;
    // if (locale != null) {
    // formatter = NumberFormat.getInstance(locale);
    // } else {
    // formatter = NumberFormat.getInstance(Locale.getDefault());
    // }
    // ParsePosition pos = new ParsePosition(0);
    // Number num = formatter.parse(value, pos);
    //
    // if (pos.getErrorIndex() == -1
    // && pos.getIndex() == value.length()
    // && num.doubleValue() >= (Float.MAX_VALUE * -1)
    // && num.doubleValue() <= Float.MAX_VALUE) {
    // result = Float.valueOf(num.floatValue());
    // }
    // }
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatFloat1", value, locale).as(Float.class);
  }

  public static Float formatFloat0(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // return Float.valueOf(value);
    // } catch (NumberFormatException e) {
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatFloat0", value).as(Float.class);
  }

  public static Long formatLong1(String value, Locale locale) {
    //
    // Long result = null;
    //
    // if (value != null) {
    // NumberFormat formatter = null;
    // if (locale != null) {
    // formatter = NumberFormat.getNumberInstance(locale);
    // } else {
    // formatter = NumberFormat.getNumberInstance(Locale.getDefault());
    // }
    // formatter.setParseIntegerOnly(true);
    // ParsePosition pos = new ParsePosition(0);
    // Number num = formatter.parse(value, pos);
    //
    // if (pos.getErrorIndex() == -1
    // && pos.getIndex() == value.length()
    // && num.doubleValue() >= Long.MIN_VALUE
    // && num.doubleValue() <= Long.MAX_VALUE) {
    // result = Long.valueOf(num.longValue());
    // }
    // }
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatLong1", value, locale).as(Long.class);
  }

  public static Long formatLong0(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // return Long.valueOf(value);
    // } catch (NumberFormatException e) {
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatLong0", value).as(Long.class);
  }

  public static Integer formatInt1(String value, Locale locale) {
    //
    // Integer result = null;
    //
    // if (value != null) {
    // NumberFormat formatter = null;
    // if (locale != null) {
    // formatter = NumberFormat.getNumberInstance(locale);
    // } else {
    // formatter = NumberFormat.getNumberInstance(Locale.getDefault());
    // }
    // formatter.setParseIntegerOnly(true);
    // ParsePosition pos = new ParsePosition(0);
    // Number num = formatter.parse(value, pos);
    //
    // if (pos.getErrorIndex() == -1
    // && pos.getIndex() == value.length()
    // && num.doubleValue() >= Integer.MIN_VALUE
    // && num.doubleValue() <= Integer.MAX_VALUE) {
    // result = Integer.valueOf(num.intValue());
    // }
    // }
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatInt1", value, locale).as(Integer.class);
  }

  public static Integer formatInt0(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // return Integer.valueOf(value);
    // } catch (NumberFormatException e) {
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatInt0", value).as(Integer.class);
  }

  public static Short formatShort1(String value, Locale locale) {
    //
    // Short result = null;
    //
    // if (value != null) {
    // NumberFormat formatter = null;
    // if (locale != null) {
    // formatter = NumberFormat.getNumberInstance(locale);
    // } else {
    // formatter = NumberFormat.getNumberInstance(Locale.getDefault());
    // }
    // formatter.setParseIntegerOnly(true);
    // ParsePosition pos = new ParsePosition(0);
    // Number num = formatter.parse(value, pos);
    //
    // if (pos.getErrorIndex() == -1
    // && pos.getIndex() == value.length()
    // && num.doubleValue() >= Short.MIN_VALUE
    // && num.doubleValue() <= Short.MAX_VALUE) {
    // result = Short.valueOf(num.shortValue());
    // }
    // }
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatShort1", value, locale).as(Short.class);
  }

  public static Short formatShort0(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // return Short.valueOf(value);
    // } catch (NumberFormatException e) {
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatShort0", value).as(Short.class);
  }

  public static Byte formatByte1(String value, Locale locale) {
    //
    // Byte result = null;
    //
    // if (value != null) {
    // NumberFormat formatter = null;
    // if (locale != null) {
    // formatter = NumberFormat.getNumberInstance(locale);
    // } else {
    // formatter = NumberFormat.getNumberInstance(Locale.getDefault());
    // }
    // formatter.setParseIntegerOnly(true);
    // ParsePosition pos = new ParsePosition(0);
    // Number num = formatter.parse(value, pos);
    //
    // if (pos.getErrorIndex() == -1
    // && pos.getIndex() == value.length()
    // && num.doubleValue() >= Byte.MIN_VALUE
    // && num.doubleValue() <= Byte.MAX_VALUE) {
    // result = Byte.valueOf(num.byteValue());
    // }
    // }
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatByte1", value, locale).as(Byte.class);
  }

  public static Byte formatByte0(String value) {
    //
    // if (value == null) {
    // return null;
    // }
    //
    // try {
    // return Byte.valueOf(value);
    // } catch (NumberFormatException e) {
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("formatByte0", value).as(Byte.class);
  }
}
