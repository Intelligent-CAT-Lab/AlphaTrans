package org.apache.commons.validator.routines;

import java.io.Serializable;
import java.text.Format;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public abstract class AbstractFormatValidator implements Serializable {
  private static final long serialVersionUID = -4690687565200568258L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/AbstractFormatValidator.py", "AbstractFormatValidator");
  private Value obj;

  public AbstractFormatValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected Object parse(String value, Format formatter) {
    //
    //
    // ParsePosition pos = new ParsePosition(0);
    // Object parsedValue = formatter.parseObject(value, pos);
    // if (pos.getErrorIndex() > -1) {
    // return null;
    // }
    //
    // if (isStrict() && pos.getIndex() < value.length()) {
    // return null;
    // }
    //
    // if (parsedValue != null) {
    // parsedValue = processParsedValue(parsedValue, formatter);
    // }
    //
    // return parsedValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parse", value, formatter).as(Object.class);
  }

  protected String format4(Object value, Format formatter) {
    //
    // return formatter.format(value);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format4", value, formatter).as(String.class);
  }

  public String format3(Object value, String pattern, Locale locale) {
    //
    // Format formatter = getFormat(pattern, locale);
    // return format4(value, formatter);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format3", value, pattern, locale).as(String.class);
  }

  public String format2(Object value, Locale locale) {
    //
    // return format3(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format2", value, locale).as(String.class);
  }

  public String format1(Object value, String pattern) {
    //
    // return format3(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format1", value, pattern).as(String.class);
  }

  public String format0(Object value) {
    //
    // return format3(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("format0", value).as(String.class);
  }

  public boolean isValid2(String value, Locale locale) {
    //
    // return isValid3(value, (String) null, locale);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid2", value, locale).as(boolean.class);
  }

  public boolean isValid1(String value, String pattern) {
    //
    // return isValid3(value, pattern, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid1", value, pattern).as(boolean.class);
  }

  public boolean isValid0(String value) {
    //
    // return isValid3(value, (String) null, (Locale) null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid0", value).as(boolean.class);
  }

  public boolean isStrict() {
    //
    // return strict;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrict").as(boolean.class);
  }

  public AbstractFormatValidator(boolean strict) {
    //
    // this.strict = strict;
    //

    this.obj = clz.invokeMember("__init__", strict);
  }

  protected abstract Format getFormat(String pattern, Locale locale);

  protected abstract Object processParsedValue(Object value, Format formatter);

  public abstract boolean isValid3(String value, String pattern, Locale locale);
}
