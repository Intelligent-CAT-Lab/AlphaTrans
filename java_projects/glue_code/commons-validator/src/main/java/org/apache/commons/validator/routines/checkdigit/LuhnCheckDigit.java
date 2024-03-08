package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class LuhnCheckDigit extends ModulusCheckDigit {
  public static final CheckDigit LUHN_CHECK_DIGIT = new LuhnCheckDigit();
  private static final int[] POSITION_WEIGHT = new int[] {2, 1};
  private static final long serialVersionUID = -2976900113942875999L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/checkdigit/LuhnCheckDigit.py", "LuhnCheckDigit");
  private Value obj;

  public LuhnCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // int weight = POSITION_WEIGHT[rightPos % 2]; // CHECKSTYLE IGNORE MagicNumber
    // int weightedValue = charValue * weight;
    // return weightedValue > 9
    // ? (weightedValue - 9)
    // : weightedValue; // CHECKSTYLE IGNORE MagicNumber
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  public LuhnCheckDigit() {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
