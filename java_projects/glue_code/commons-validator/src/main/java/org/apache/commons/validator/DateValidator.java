package org.apache.commons.validator;

import java.util.Locale;
import org.graalvm.polyglot.Value;

public class DateValidator {
  private static final DateValidator DATE_VALIDATOR = new DateValidator();
  private static Value clz =
      ContextInitializer.getPythonClass("/DateValidator.py", "DateValidator");
  private Value obj;

  public DateValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isValid1(String value, Locale locale) {
    //
    //
    // if (value == null) {
    // return false;
    // }
    //
    // DateFormat formatter = null;
    // if (locale != null) {
    // formatter = DateFormat.getDateInstance(DateFormat.SHORT, locale);
    // } else {
    // formatter = DateFormat.getDateInstance(DateFormat.SHORT, Locale.getDefault());
    // }
    //
    // formatter.setLenient(false);
    //
    // try {
    // formatter.parse(value);
    // } catch (ParseException e) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid1", value, locale).as(boolean.class);
  }

  public boolean isValid0(String value, String datePattern, boolean strict) {
    //
    //
    // if (value == null || datePattern == null || datePattern.length() <= 0) {
    //
    // return false;
    // }
    //
    // SimpleDateFormat formatter = new SimpleDateFormat(datePattern);
    // formatter.setLenient(false);
    //
    // try {
    // formatter.parse(value);
    // } catch (ParseException e) {
    // return false;
    // }
    //
    // if (strict && (datePattern.length() != value.length())) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid0", value, datePattern, strict).as(boolean.class);
  }

  protected DateValidator() {
    //
    // super();
    //

    this.obj = clz.invokeMember("__init__");
  }

  public static DateValidator getInstance() {
    //
    // return DATE_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(DateValidator.class);
  }
}
