package org.apache.commons.graph.coloring;

import java.util.Set;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.GraphException;
import org.graalvm.polyglot.Value;

public class NotEnoughColorsException extends GraphException {
  private static final long serialVersionUID = -8782950517745777605L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/coloring/NotEnoughColorsException.py", "NotEnoughColorsException");
  private Value obj;

  public NotEnoughColorsException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public NotEnoughColorsException(Set<?> colors) {
    //
    // super(
    // format("Input color set %s has not enough colors to color the given graph", colors),
    // null,
    // null);
    //

    this.obj = clz.invokeMember("__init__", colors);
  }
}
