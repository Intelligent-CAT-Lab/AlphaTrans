package org.apache.commons.validator.routines.checkdigit;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class IBANCheckDigit implements CheckDigit, Serializable {
  public static final CheckDigit IBAN_CHECK_DIGIT = new IBANCheckDigit();
  private static final long MODULUS = 97;
  private static final long MAX = 999999999;
  private static final int MAX_ALPHANUMERIC_VALUE = 35; // Character.getNumericValue('Z')
  private static final long serialVersionUID = -3600191725934382801L;
  private static final int MIN_CODE_LEN = 5;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/checkdigit/IBANCheckDigit.py", "IBANCheckDigit");
  private Value obj;

  public IBANCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String calculate(String code) throws CheckDigitException {
    try {
      //
      // if (code == null || code.length() < MIN_CODE_LEN) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Code length=" + (code == null ? 0 : code.length()));
      // }
      // code = code.substring(0, 2) + "00" + code.substring(4); // CHECKSTYLE IGNORE MagicNumber
      // int modulusResult = calculateModulus(code);
      // int charValue = (98 - modulusResult); // CHECKSTYLE IGNORE MagicNumber
      // String checkDigit = Integer.toString(charValue);
      // return (charValue > 9 ? checkDigit : "0" + checkDigit); // CHECKSTYLE IGNORE MagicNumber
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculate", code).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "IBANCheckDigit.calculate");
    }
  }

  public boolean isValid(String code) {
    //
    // if (code == null || code.length() < MIN_CODE_LEN) {
    // return false;
    // }
    // String check = code.substring(2, 4); // CHECKSTYLE IGNORE MagicNumber
    // if ("00".equals(check) || "01".equals(check) || "99".equals(check)) {
    // return false;
    // }
    // try {
    // int modulusResult = calculateModulus(code);
    // return (modulusResult == 1);
    // } catch (CheckDigitException ex) {
    // return false;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public IBANCheckDigit() {
    //

    this.obj = clz.invokeMember("__init__");
  }

  private int calculateModulus(String code) throws CheckDigitException {
    try {
      //
      // String reformattedCode =
      // code.substring(4) + code.substring(0, 4); // CHECKSTYLE IGNORE MagicNumber
      // long total = 0;
      // for (int i = 0; i < reformattedCode.length(); i++) {
      // int charValue = Character.getNumericValue(reformattedCode.charAt(i));
      // if (charValue < 0 || charValue > MAX_ALPHANUMERIC_VALUE) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Character[" + i + "] = '" + charValue + "'");
      // }
      // total =
      // (charValue > 9 ? total * 100 : total * 10)
      // + charValue; // CHECKSTYLE IGNORE MagicNumber
      // if (total > MAX) {
      // total = total % MODULUS;
      // }
      // }
      // return (int) (total % MODULUS);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculateModulus", code).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "IBANCheckDigit.calculateModulus");
    }
  }
}
