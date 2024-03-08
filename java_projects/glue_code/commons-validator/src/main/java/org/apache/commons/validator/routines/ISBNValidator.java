package org.apache.commons.validator.routines;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit;
import org.graalvm.polyglot.Value;

public class ISBNValidator implements Serializable {
  static final String ISBN13_REGEX =
      "^(978|979)(?:(\\d{10})|(?:"
          + SEP
          + GROUP
          + SEP
          + PUBLISHER
          + SEP
          + TITLE
          + SEP
          + "([0-9])))$";
  static final String ISBN10_REGEX =
      "^(?:(\\d{9}[0-9X])|(?:" + GROUP + SEP + PUBLISHER + SEP + TITLE + SEP + "([0-9X])))$";
  private final CodeValidator isbn13Validator =
      CodeValidator.CodeValidator4(ISBN13_REGEX, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT);
  private final CodeValidator isbn10Validator =
      CodeValidator.CodeValidator4(ISBN10_REGEX, 10, ISBN10CheckDigit.ISBN10_CHECK_DIGIT);
  private static final ISBNValidator ISBN_VALIDATOR_NO_CONVERT = new ISBNValidator(false);
  private static final ISBNValidator ISBN_VALIDATOR = ISBNValidator.ISBNValidator1();
  private static final String TITLE = "(\\d{1,6})";
  private static final String PUBLISHER = "(\\d{1,7})";
  private static final String GROUP = "(\\d{1,5})";
  private static final String SEP = "(?:\\-|\\s)";
  private static final long serialVersionUID = 4319515687976420405L;
  private static final int ISBN_10_LEN = 10;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/ISBNValidator.py", "ISBNValidator");
  private Value obj;

  public ISBNValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String convertToISBN13(String isbn10) {
    //
    //
    // if (isbn10 == null) {
    // return null;
    // }
    //
    // String input = isbn10.trim();
    // if (input.length() != ISBN_10_LEN) {
    // throw new IllegalArgumentException(
    // "Invalid length " + input.length() + " for '" + input + "'");
    // }
    //
    // String isbn13 = "978" + input.substring(0, ISBN_10_LEN - 1);
    // try {
    // String checkDigit = isbn13Validator.getCheckDigit().calculate(isbn13);
    // isbn13 += checkDigit;
    // return isbn13;
    // } catch (CheckDigitException e) {
    // throw new IllegalArgumentException(
    // "Check digit error for '" + input + "' - " + e.getMessage());
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("convertToISBN13", isbn10).as(String.class);
  }

  public String validateISBN13(String code) {
    //
    // Object result = isbn13Validator.validate(code);
    // return (result == null ? null : result.toString());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateISBN13", code).as(String.class);
  }

  public String validateISBN10(String code) {
    //
    // Object result = isbn10Validator.validate(code);
    // return (result == null ? null : result.toString());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateISBN10", code).as(String.class);
  }

  public String validate(String code) {
    //
    // String result = validateISBN13(code);
    // if (result == null) {
    // result = validateISBN10(code);
    // if (result != null && convert) {
    // result = convertToISBN13(result);
    // }
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate", code).as(String.class);
  }

  public boolean isValidISBN13(String code) {
    //
    // return isbn13Validator.isValid(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidISBN13", code).as(boolean.class);
  }

  public boolean isValidISBN10(String code) {
    //
    // return isbn10Validator.isValid(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidISBN10", code).as(boolean.class);
  }

  public boolean isValid(String code) {
    //
    // return (isValidISBN13(code) || isValidISBN10(code));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public static ISBNValidator ISBNValidator1() {
    //
    // return new ISBNValidator(true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ISBNValidator1").as(ISBNValidator.class);
  }

  public ISBNValidator(boolean convert) {
    //
    // this.convert = convert;
    //

    this.obj = clz.invokeMember("__init__", convert);
  }

  public static ISBNValidator getInstance1(boolean convert) {
    //
    // return (convert ? ISBN_VALIDATOR : ISBN_VALIDATOR_NO_CONVERT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance1", convert).as(ISBNValidator.class);
  }

  public static ISBNValidator getInstance0() {
    //
    // return ISBN_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance0").as(ISBNValidator.class);
  }
}
