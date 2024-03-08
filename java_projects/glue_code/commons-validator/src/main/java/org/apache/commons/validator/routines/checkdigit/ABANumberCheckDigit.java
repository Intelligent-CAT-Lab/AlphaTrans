package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class ABANumberCheckDigit extends ModulusCheckDigit {
  public static final CheckDigit ABAN_CHECK_DIGIT = new ABANumberCheckDigit();
  private static final int[] POSITION_WEIGHT = new int[] {3, 1, 7};
  private static final long serialVersionUID = -8255937433810380145L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/ABANumberCheckDigit.py", "ABANumberCheckDigit");
  private Value obj;

  public ABANumberCheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // int weight = POSITION_WEIGHT[rightPos % 3]; // CHECKSTYLE IGNORE MagicNumber
    // return charValue * weight;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  public ABANumberCheckDigit() {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
