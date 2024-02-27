package org.apache.commons.fileupload.servlet;

import org.apache.commons.fileupload.ContextInitializer;
import org.graalvm.polyglot.Value;

public class ServletRequestContext {
  private static Value clz =
      ContextInitializer.getPythonClass("/servleServletRequestContext.py", "ServletRequestContext");
  private Value obj;

  public ServletRequestContext(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
