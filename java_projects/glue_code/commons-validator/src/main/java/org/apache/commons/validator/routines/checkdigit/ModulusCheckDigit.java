package org.apache.commons.validator.routines.checkdigit;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class ModulusCheckDigit implements CheckDigit, Serializable {
  private static final long serialVersionUID = 2948962251251528941L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/ModulusCheckDigit.py", "ModulusCheckDigit");
  private Value obj;

  public ModulusCheckDigit(Value obj) {
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
      // int modulusResult = calculateModulus(code, false);
      // int charValue = (modulus - modulusResult) % modulus;
      // return toCheckDigit(charValue);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculate", code).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ModulusCheckDigit.calculate");
    }
  }

  public boolean isValid(String code) {
    //
    // if (code == null || code.length() == 0) {
    // return false;
    // }
    // try {
    // int modulusResult = calculateModulus(code, true);
    // return (modulusResult == 0);
    // } catch (CheckDigitException ex) {
    // return false;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public static int sumDigits(int number) {
    //
    // int total = 0;
    // int todo = number;
    // while (todo > 0) {
    // total += todo % 10; // CHECKSTYLE IGNORE MagicNumber
    // todo = todo / 10; // CHECKSTYLE IGNORE MagicNumber
    // }
    // return total;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("sumDigits", number).as(int.class);
  }

  protected String toCheckDigit(int charValue) throws CheckDigitException {
    try {
      //
      // if (charValue >= 0 && charValue <= 9) { // CHECKSTYLE IGNORE MagicNumber
      // return Integer.toString(charValue);
      // }
      // throw CheckDigitException.CheckDigitException1("Invalid Check Digit Value =" + +charValue);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toCheckDigit", charValue).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ModulusCheckDigit.toCheckDigit");
    }
  }

  protected int toInt(char character, int leftPos, int rightPos) throws CheckDigitException {
    try {
      //
      // if (Character.isDigit(character)) {
      // return Character.getNumericValue(character);
      // }
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Character[" + leftPos + "] = '" + character + "'");
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toInt", character, leftPos, rightPos).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ModulusCheckDigit.toInt");
    }
  }

  protected int calculateModulus(String code, boolean includesCheckDigit)
      throws CheckDigitException {
    try {
      //
      // int total = 0;
      // for (int i = 0; i < code.length(); i++) {
      // int lth = code.length() + (includesCheckDigit ? 0 : 1);
      // int leftPos = i + 1;
      // int rightPos = lth - i;
      // int charValue = toInt(code.charAt(i), leftPos, rightPos);
      // total += weightedValue(charValue, leftPos, rightPos);
      // }
      // if (total == 0) {
      // throw CheckDigitException.CheckDigitException1("Invalid code, sum is zero");
      // }
      // return total % modulus;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("calculateModulus", code, includesCheckDigit).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ModulusCheckDigit.calculateModulus");
    }
  }

  public int getModulus() {
    //
    // return modulus;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getModulus").as(int.class);
  }

  public ModulusCheckDigit(int modulus) {
    //
    // this.modulus = modulus;
    //

    this.obj = clz.invokeMember("__init__", modulus);
  }

  protected abstract int weightedValue(int charValue, int leftPos, int rightPos);
}
