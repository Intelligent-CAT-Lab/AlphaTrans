package org.apache.commons.graph.export;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.graalvm.polyglot.Value;

public final class DefaultExportSelector<V, E> implements NamedExportSelector<V, E> {
  private String name = null;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/export/DefaultExportSelector.py", "DefaultExportSelector");
  private Value obj;

  public DefaultExportSelector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public ExportSelector<V, E> withName(String name) {
    //
    // this.name = checkNotNull(name, "Graph name cannot be null.");
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("withName", name).as(ExportSelector.class);
  }

  public DotExporter<V, E> usingDotNotation() {
    //
    // return new DotExporter<V, E>(graph, name);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("usingDotNotation").as(DotExporter.class);
  }

  public DefaultExportSelector(Graph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }
}
