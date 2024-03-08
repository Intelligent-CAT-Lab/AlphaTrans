package org.apache.commons.graph.builder;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.MutableGraph;
import org.graalvm.polyglot.Value;

final class DefaultHeadVertexConnector<V, E> implements HeadVertexConnector<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/builder/DefaultHeadVertexConnector.py", "DefaultHeadVertexConnector");
  private Value obj;

  public DefaultHeadVertexConnector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <H extends V> TailVertexConnector<V, E> from(H head) {
    //
    // head = checkNotNull(head, "Null head vertex not admitted");
    // return new DefaultTailVertexConnector<V, E>(graph, edge, head);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("from", head).as(TailVertexConnector.class);
  }

  public DefaultHeadVertexConnector(MutableGraph<V, E> graph, E edge) {
    //
    // this.graph = graph;
    // this.edge = edge;
    //

    this.obj = clz.invokeMember("__init__", graph, edge);
  }
}
