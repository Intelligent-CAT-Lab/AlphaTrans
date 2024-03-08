package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class SedolCheckDigit extends ModulusCheckDigit {
  public static final CheckDigit SEDOL_CHECK_DIGIT = new SedolCheckDigit();
  private static final int[] POSITION_WEIGHT = new int[] {1, 3, 1, 7, 3, 9, 1};
  private static final int MAX_ALPHANUMERIC_VALUE = 35; // Character.getNumericValue('Z')
  private static final long serialVersionUID = -8976881621148878443L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/SedolCheckDigit.py", "SedolCheckDigit");
  private Value obj;

  public SedolCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int toInt(char character, int leftPos, int rightPos) throws CheckDigitException {
    try {
      //
      // int charValue = Character.getNumericValue(character);
      // final int charMax =
      // rightPos == 1 ? 9 : MAX_ALPHANUMERIC_VALUE; // CHECKSTYLE IGNORE MagicNumber
      // if (charValue < 0 || charValue > charMax) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Character["
      // + leftPos
      // + ","
      // + rightPos
      // + "] = '"
      // + charValue
      // + "' out of range 0 to "
      // + charMax);
      // }
      // return charValue;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toInt", character, leftPos, rightPos).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "SedolCheckDigit.toInt");
    }
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // return charValue * POSITION_WEIGHT[leftPos - 1];
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  protected int calculateModulus(String code, boolean includesCheckDigit)
      throws CheckDigitException {
    try {
      //
      // if (code.length() > POSITION_WEIGHT.length) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Code Length = " + code.length());
      // }
      // return super.calculateModulus(code, includesCheckDigit);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculateModulus", code, includesCheckDigit).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "SedolCheckDigit.calculateModulus");
    }
  }

  public SedolCheckDigit() {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
