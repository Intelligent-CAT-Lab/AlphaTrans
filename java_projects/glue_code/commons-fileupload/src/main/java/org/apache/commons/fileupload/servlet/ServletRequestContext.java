package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;

public class ServletRequestContext {
  private static Value clz =
      ContextInitializer.getPythonClass("<placeholder>", "ServletRequestContext");
  private Value obj;

  public ServletRequestContext(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
