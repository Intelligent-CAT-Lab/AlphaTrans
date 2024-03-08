package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public final class CallStackUtils {
  private static Value clz =
      ContextInitializer.getPythonClass("/CallStackUtils.py", "CallStackUtils");
  private Value obj;

  public CallStackUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  private CallStackUtils() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
