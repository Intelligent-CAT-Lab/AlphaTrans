package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;

public class Util {
  private static Value clz = ContextInitializer.getPythonClass("Util.py", "Util");
  private Value obj;

  public Util(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
