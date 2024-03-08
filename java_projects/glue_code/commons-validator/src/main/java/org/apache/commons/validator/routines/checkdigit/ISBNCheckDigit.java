package org.apache.commons.validator.routines.checkdigit;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class ISBNCheckDigit implements CheckDigit, Serializable {
  public static final CheckDigit ISBN_CHECK_DIGIT = new ISBNCheckDigit();
  public static final CheckDigit ISBN13_CHECK_DIGIT = EAN13CheckDigit.EAN13_CHECK_DIGIT;
  public static final CheckDigit ISBN10_CHECK_DIGIT = ISBN10CheckDigit.ISBN10_CHECK_DIGIT;
  private static final long serialVersionUID = 1391849166205184558L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/checkdigit/ISBNCheckDigit.py", "ISBNCheckDigit");
  private Value obj;

  public ISBNCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isValid(String code) {
    //
    // if (code == null) {
    // return false;
    // } else if (code.length() == 10) { // CHECKSTYLE IGNORE MagicNumber
    // return ISBN10_CHECK_DIGIT.isValid(code);
    // } else if (code.length() == 13) { // CHECKSTYLE IGNORE MagicNumber
    // return ISBN13_CHECK_DIGIT.isValid(code);
    // } else {
    // return false;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public String calculate(String code) throws CheckDigitException {
    try {
      //
      // if (code == null || code.length() == 0) {
      // throw CheckDigitException.CheckDigitException1("ISBN Code is missing");
      // } else if (code.length() == 9) { // CHECKSTYLE IGNORE MagicNumber
      // return ISBN10_CHECK_DIGIT.calculate(code);
      // } else if (code.length() == 12) { // CHECKSTYLE IGNORE MagicNumber
      // return ISBN13_CHECK_DIGIT.calculate(code);
      // } else {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid ISBN Length = " + code.length());
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculate", code).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ISBNCheckDigit.calculate");
    }
  }
}
