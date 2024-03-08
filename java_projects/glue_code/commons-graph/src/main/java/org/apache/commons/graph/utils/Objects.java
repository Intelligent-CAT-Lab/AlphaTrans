package org.apache.commons.graph.utils;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class Objects {
  private static Value clz = ContextInitializer.getPythonClass("/utils/Objects.py", "Objects");
  private Value obj;

  public Objects(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static int hash(
      int initialNonZeroOddNumber, int multiplierNonZeroOddNumber, Object... objs) {
    //
    // int result = initialNonZeroOddNumber;
    // for (Object obj : objs) {
    // result = multiplierNonZeroOddNumber * result + (obj != null ? obj.hashCode() : 0);
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash", initialNonZeroOddNumber, multiplierNonZeroOddNumber, objs)
        .as(int.class);
  }

  public static <O> boolean eq(O o1, O o2) {
    //
    // return o1 != null ? o1.equals(o2) : o2 == null;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("eq", o1, o2).as(boolean.class);
  }

  private Objects() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
