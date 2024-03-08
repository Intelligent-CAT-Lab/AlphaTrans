package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class ModulusTenCheckDigit extends ModulusCheckDigit {
  private static final long serialVersionUID = -3752929983453368497L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/ModulusTenCheckDigit.py", "ModulusTenCheckDigit");
  private Value obj;

  public ModulusTenCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return getClass().getSimpleName()
    // + "[postitionWeight="
    // + Arrays.toString(postitionWeight)
    // + ", useRightPos="
    // + useRightPos
    // + ", sumWeightedDigits="
    // + sumWeightedDigits
    // + "]";
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // int pos = useRightPos ? rightPos : leftPos;
    // int weight = postitionWeight[(pos - 1) % postitionWeight.length];
    // int weightedValue = charValue * weight;
    // if (sumWeightedDigits) {
    // weightedValue = ModulusCheckDigit.sumDigits(weightedValue);
    // }
    // return weightedValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  protected int toInt(char character, int leftPos, int rightPos) throws CheckDigitException {
    try {
      //
      // int num = Character.getNumericValue(character);
      // if (num < 0) {
      // throw CheckDigitException.CheckDigitException1(
      // "Invalid Character[" + leftPos + "] = '" + character + "'");
      // }
      // return num;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toInt", character, leftPos, rightPos).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle CheckDigitException
      throw (CheckDigitException) ExceptionHandler.handle(e, "ModulusTenCheckDigit.toInt");
    }
  }

  public boolean isValid(String code) {
    //
    // if (code == null || code.length() == 0) {
    // return false;
    // }
    // if (!Character.isDigit(code.charAt(code.length() - 1))) {
    // return false;
    // }
    //
    // return super.isValid(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public static ModulusTenCheckDigit ModulusTenCheckDigit2(int[] postitionWeight) {
    //
    // return new ModulusTenCheckDigit(postitionWeight, false, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ModulusTenCheckDigit2", postitionWeight)
        .as(ModulusTenCheckDigit.class);
  }

  public static ModulusTenCheckDigit ModulusTenCheckDigit1(
      int[] postitionWeight, boolean useRightPos) {
    //
    // return new ModulusTenCheckDigit(postitionWeight, useRightPos, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ModulusTenCheckDigit1", postitionWeight, useRightPos)
        .as(ModulusTenCheckDigit.class);
  }

  public ModulusTenCheckDigit(
      int[] postitionWeight, boolean useRightPos, boolean sumWeightedDigits) {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    // this.postitionWeight = Arrays.copyOf(postitionWeight, postitionWeight.length);
    // this.useRightPos = useRightPos;
    // this.sumWeightedDigits = sumWeightedDigits;
    //

    this.obj = clz.invokeMember("__init__", postitionWeight, useRightPos, sumWeightedDigits);
  }
}
