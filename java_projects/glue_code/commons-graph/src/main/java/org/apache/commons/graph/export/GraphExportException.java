package org.apache.commons.graph.export;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class GraphExportException extends Exception {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/export/GraphExportException.py", "GraphExportException");
  private Value obj;

  public GraphExportException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public GraphExportException(Throwable cause, String messagePattern, Object... messageArguments) {
    //
    // super(format(messagePattern, messageArguments), cause);
    //

    this.obj = clz.invokeMember("__init__", cause, messagePattern, messageArguments);
  }
}
