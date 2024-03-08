package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class ISINCheckDigit extends ModulusCheckDigit {
  public static final CheckDigit ISIN_CHECK_DIGIT = new ISINCheckDigit();
  private static final int[] POSITION_WEIGHT = new int[] {2, 1};
  private static final int MAX_ALPHANUMERIC_VALUE = 35; // Character.getNumericValue('Z')
  private static final long serialVersionUID = -1239211208101323599L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/checkdigit/ISINCheckDigit.py", "ISINCheckDigit");
  private Value obj;

  public ISINCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // int weight = POSITION_WEIGHT[rightPos % 2]; // CHECKSTYLE IGNORE MagicNumber
    // int weightedValue = charValue * weight;
    // return ModulusCheckDigit.sumDigits(weightedValue);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  protected int calculateModulus(String code, boolean includesCheckDigit)
      throws CheckDigitException {
    try {
      //
      // StringBuilder transformed =
      // new StringBuilder(code.length() * 2); // CHECKSTYLE IGNORE MagicNumber
      // if (includesCheckDigit) {
      // char checkDigit = code.charAt(code.length() - 1); // fetch the last character
      // if (!Character.isDigit(checkDigit)) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid checkdigit[" + checkDigit + "] in " + code);
      // }
      // }
      // for (int i = 0; i < code.length(); i++) {
      // int charValue = Character.getNumericValue(code.charAt(i));
      // if (charValue < 0 || charValue > MAX_ALPHANUMERIC_VALUE) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Character[" + (i + 1) + "] = '" + charValue + "'");
      // }
      // transformed.append(charValue);
      // }
      // return super.calculateModulus(transformed.toString(), includesCheckDigit);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculateModulus", code, includesCheckDigit).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ISINCheckDigit.calculateModulus");
    }
  }

  public ISINCheckDigit() {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
