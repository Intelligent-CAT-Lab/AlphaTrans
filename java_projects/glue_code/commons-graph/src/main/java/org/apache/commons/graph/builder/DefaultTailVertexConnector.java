package org.apache.commons.graph.builder;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.MutableGraph;
import org.graalvm.polyglot.Value;

final class DefaultTailVertexConnector<V, E> implements TailVertexConnector<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/builder/DefaultTailVertexConnector.py", "DefaultTailVertexConnector");
  private Value obj;

  public DefaultTailVertexConnector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <T extends V> void to(T tail) {
    //
    // tail = checkNotNull(tail, "Null tail vertex not admitted");
    // graph.addEdge(head, edge, tail);
    //

    obj.invokeMember("to", tail);
  }

  public DefaultTailVertexConnector(MutableGraph<V, E> graph, E edge, V head) {
    //
    // this.graph = graph;
    // this.edge = edge;
    // this.head = head;
    //

    this.obj = clz.invokeMember("__init__", graph, edge, head);
  }
}
