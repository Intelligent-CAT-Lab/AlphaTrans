package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class ISBN10CheckDigit extends ModulusCheckDigit {
  public static final CheckDigit ISBN10_CHECK_DIGIT = new ISBN10CheckDigit();
  private static final long serialVersionUID = 8000855044504864964L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/ISBN10CheckDigit.py", "ISBN10CheckDigit");
  private Value obj;

  public ISBN10CheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected String toCheckDigit(int charValue) throws CheckDigitException {
    try {
      //
      // if (charValue == 10) { // CHECKSTYLE IGNORE MagicNumber
      // return "X";
      // }
      // return super.toCheckDigit(charValue);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toCheckDigit", charValue).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ISBN10CheckDigit.toCheckDigit");
    }
  }

  protected int toInt(char character, int leftPos, int rightPos) throws CheckDigitException {
    try {
      //
      // if (rightPos == 1 && character == 'X') {
      // return 10; // CHECKSTYLE IGNORE MagicNumber
      // }
      // return super.toInt(character, leftPos, rightPos);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toInt", character, leftPos, rightPos).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ISBN10CheckDigit.toInt");
    }
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // return charValue * rightPos;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  public ISBN10CheckDigit() {
    //
    // super(11); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
