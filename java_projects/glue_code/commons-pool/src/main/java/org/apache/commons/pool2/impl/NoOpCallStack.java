package org.apache.commons.pool;

import java.io.PrintWriter;
import org.graalvm.polyglot.Value;

public class NoOpCallStack implements CallStack {
  public static final CallStack INSTANCE = new NoOpCallStack();
  private static Value clz =
      ContextInitializer.getPythonClass("/NoOpCallStack.py", "NoOpCallStack");
  private Value obj;

  public NoOpCallStack(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean printStackTrace(final PrintWriter writer) {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("printStackTrace", writer).as(boolean.class);
  }

  public void fillInStackTrace() {
    //

    obj.invokeMember("fillInStackTrace");
  }

  public void clear() {
    //

    obj.invokeMember("clear");
  }

  private NoOpCallStack() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
