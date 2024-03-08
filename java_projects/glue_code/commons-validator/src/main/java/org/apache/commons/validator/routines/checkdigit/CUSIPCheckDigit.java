package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class CUSIPCheckDigit extends ModulusCheckDigit {
  public static final CheckDigit CUSIP_CHECK_DIGIT = new CUSIPCheckDigit();
  private static final int[] POSITION_WEIGHT = new int[] {2, 1};
  private static final long serialVersionUID = 666941918490152456L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/CUSIPCheckDigit.py", "CUSIPCheckDigit");
  private Value obj;

  public CUSIPCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // int weight = POSITION_WEIGHT[rightPos % 2];
    // int weightedValue = (charValue * weight);
    // return ModulusCheckDigit.sumDigits(weightedValue);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  protected int toInt(char character, int leftPos, int rightPos) throws CheckDigitException {
    try {
      //
      // int charValue = Character.getNumericValue(character);
      // final int charMax = rightPos == 1 ? 9 : 35; // CHECKSTYLE IGNORE MagicNumber
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
      throw (CheckDigitException) ExceptionHandler.handle(e, "CUSIPCheckDigit.toInt");
    }
  }

  public CUSIPCheckDigit() {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
