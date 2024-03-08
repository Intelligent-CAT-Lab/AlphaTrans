package org.apache.commons.graph.utils;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class Assertions {
  private static Value clz =
      ContextInitializer.getPythonClass("/utils/Assertions.py", "Assertions");
  private Value obj;

  public Assertions(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static void checkState(
      boolean expression, String errorMessageTemplate, Object... errorMessageArgs) {
    //
    // if (!expression) {
    // throw new IllegalStateException(format(errorMessageTemplate, errorMessageArgs));
    // }
    //

    clz.invokeMember("checkState", expression, errorMessageTemplate, errorMessageArgs);
  }

  public static <T> T checkNotNull(
      T reference, String errorMessageTemplate, Object... errorMessageArgs) {
    //
    // if (reference == null) {
    // throw new NullPointerException(format(errorMessageTemplate, errorMessageArgs));
    // }
    // return reference;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("checkNotNull", reference, errorMessageTemplate, errorMessageArgs)
        .as(T.class);
  }

  public static void checkArgument(
      boolean expression, String errorMessageTemplate, Object... errorMessageArgs) {
    //
    // if (!expression) {
    // throw new IllegalArgumentException(format(errorMessageTemplate, errorMessageArgs));
    // }
    //

    clz.invokeMember("checkArgument", expression, errorMessageTemplate, errorMessageArgs);
  }

  private Assertions() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
