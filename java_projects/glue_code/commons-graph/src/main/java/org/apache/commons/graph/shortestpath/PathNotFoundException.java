package org.apache.commons.graph.shortestpath;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.GraphException;
import org.graalvm.polyglot.Value;

public final class PathNotFoundException extends GraphException {
  private static final long serialVersionUID = 2919520319054603708L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/PathNotFoundException.py", "PathNotFoundException");
  private Value obj;

  public PathNotFoundException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public PathNotFoundException(String messagePattern, Object... arguments) {
    //
    // super(messagePattern, null, arguments);
    //

    this.obj = clz.invokeMember("__init__", messagePattern, arguments);
  }
}
