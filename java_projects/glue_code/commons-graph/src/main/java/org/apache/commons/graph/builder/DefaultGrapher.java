package org.apache.commons.graph.builder;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.MutableGraph;
import org.graalvm.polyglot.Value;

final class DefaultGrapher<V, E> implements GraphConnector<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass("/builder/DefaultGrapher.py", "DefaultGrapher");
  private Value obj;

  public DefaultGrapher(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <N extends V> N addVertex(N node) {
    //
    // node = checkNotNull(node, "Null vertex not admitted");
    // graph.addVertex(node);
    // return node;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addVertex", node).as(N.class);
  }

  public <A extends E> HeadVertexConnector<V, E> addEdge(A arc) {
    //
    // arc = checkNotNull(arc, "Null edge not admitted");
    // return new DefaultHeadVertexConnector<V, E>(graph, arc);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addEdge", arc).as(HeadVertexConnector.class);
  }

  public DefaultGrapher(MutableGraph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }
}
