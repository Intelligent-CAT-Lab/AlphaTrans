package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class EAN13CheckDigit extends ModulusCheckDigit {
  public static final CheckDigit EAN13_CHECK_DIGIT = new EAN13CheckDigit();
  private static final int[] POSITION_WEIGHT = new int[] {3, 1};
  private static final long serialVersionUID = 1726347093230424107L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/EAN13CheckDigit.py", "EAN13CheckDigit");
  private Value obj;

  public EAN13CheckDigit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int weightedValue(int charValue, int leftPos, int rightPos) {
    //
    // int weight = POSITION_WEIGHT[rightPos % 2];
    // return charValue * weight;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("weightedValue", charValue, leftPos, rightPos).as(int.class);
  }

  public EAN13CheckDigit() {
    //
    // super(10); // CHECKSTYLE IGNORE MagicNumber
    //

    this.obj = clz.invokeMember("__init__");
  }
}
