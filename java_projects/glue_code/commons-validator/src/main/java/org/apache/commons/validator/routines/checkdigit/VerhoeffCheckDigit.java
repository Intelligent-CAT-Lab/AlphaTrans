package org.apache.commons.validator.routines.checkdigit;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class VerhoeffCheckDigit implements CheckDigit, Serializable {
  public static final CheckDigit VERHOEFF_CHECK_DIGIT = new VerhoeffCheckDigit();
  private static final int[] INV_TABLE = new int[] {0, 4, 3, 2, 1, 5, 6, 7, 8, 9};
  private static final int[][] P_TABLE =
      new int[][] {
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
        {1, 5, 7, 6, 2, 8, 3, 0, 9, 4},
        {5, 8, 0, 3, 7, 9, 6, 1, 4, 2},
        {8, 9, 1, 6, 0, 4, 3, 5, 2, 7},
        {9, 4, 5, 3, 1, 2, 6, 8, 7, 0},
        {4, 2, 8, 6, 5, 7, 3, 9, 0, 1},
        {2, 7, 9, 3, 8, 0, 6, 4, 1, 5},
        {7, 0, 4, 6, 9, 1, 3, 2, 5, 8}
      };
  private static final int[][] D_TABLE =
      new int[][] {
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
        {1, 2, 3, 4, 0, 6, 7, 8, 9, 5},
        {2, 3, 4, 0, 1, 7, 8, 9, 5, 6},
        {3, 4, 0, 1, 2, 8, 9, 5, 6, 7},
        {4, 0, 1, 2, 3, 9, 5, 6, 7, 8},
        {5, 9, 8, 7, 6, 0, 4, 3, 2, 1},
        {6, 5, 9, 8, 7, 1, 0, 4, 3, 2},
        {7, 6, 5, 9, 8, 2, 1, 0, 4, 3},
        {8, 7, 6, 5, 9, 3, 2, 1, 0, 4},
        {9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
      };
  private static final long serialVersionUID = 4138993995483695178L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/VerhoeffCheckDigit.py", "VerhoeffCheckDigit");
  private Value obj;

  public VerhoeffCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String calculate(String code) throws CheckDigitException {
    try {
      //
      // if (code == null || code.length() == 0) {
      // throw CheckDigitException.CheckDigitException1("Code is missing");
      // }
      // int checksum = calculateChecksum(code, false);
      // return Integer.toString(INV_TABLE[checksum]);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculate", code).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "VerhoeffCheckDigit.calculate");
    }
  }

  public boolean isValid(String code) {
    //
    // if (code == null || code.length() == 0) {
    // return false;
    // }
    // try {
    // return (calculateChecksum(code, true) == 0);
    // } catch (CheckDigitException e) {
    // return false;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  private int calculateChecksum(String code, boolean includesCheckDigit)
      throws CheckDigitException {
    try {
      //
      // int checksum = 0;
      // for (int i = 0; i < code.length(); i++) {
      // int idx = code.length() - (i + 1);
      // int num = Character.getNumericValue(code.charAt(idx));
      // if (num < 0 || num > 9) { // CHECKSTYLE IGNORE MagicNumber
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Character[" + i + "] = '" + ((int) code.charAt(idx)) + "'");
      // }
      // int pos = includesCheckDigit ? i : i + 1;
      // checksum = D_TABLE[checksum][P_TABLE[pos % 8][num]]; // CHECKSTYLE IGNORE MagicNumber
      // }
      // return checksum;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculateChecksum", code, includesCheckDigit).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException)
          ExceptionHandler.handle(e, "VerhoeffCheckDigit.calculateChecksum");
    }
  }
}
