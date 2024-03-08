package org.apache.commons.graph.shortestpath;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.GraphException;
import org.graalvm.polyglot.Value;

public final class NegativeWeightedCycleException extends GraphException {
  private static final long serialVersionUID = 3196711750285223435L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/NegativeWeightedCycleException.py", "NegativeWeightedCycleException");
  private Value obj;

  public NegativeWeightedCycleException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public NegativeWeightedCycleException(
      String messagePattern, Throwable cause, Object... arguments) {
    //
    // super(messagePattern, cause, arguments);
    //

    this.obj = clz.invokeMember("__init__", messagePattern, cause, arguments);
  }
}
