package org.apache.commons.graph;

import org.graalvm.polyglot.Value;

public class GraphException extends RuntimeException {
  private static final long serialVersionUID = 6356965258279945475L;
  private static Value clz =
      ContextInitializer.getPythonClass("/GraphException.py", "GraphException");
  private Value obj;

  public GraphException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public GraphException(String messagePattern, Throwable cause, Object... arguments) {
    //
    // super((cause != null) ? format(messagePattern, arguments) : null, cause);
    //

    this.obj = clz.invokeMember("__init__", messagePattern, cause, arguments);
  }
}
