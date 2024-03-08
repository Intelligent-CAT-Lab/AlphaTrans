package org.apache.commons.graph.connectivity;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.graalvm.polyglot.Value;

public class DefaultConnectivityBuilder<V, E> implements ConnectivityBuilder<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/connectivity/DefaultConnectivityBuilder.py", "DefaultConnectivityBuilder");
  private Value obj;

  public DefaultConnectivityBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public ConnectivityAlgorithmsSelector<V, E> includingVertices(V... vertices) {
    //
    // vertices =
    // checkNotNull(
    // vertices,
    // "Graph connectivity cannote be applied on null vertices array, use no-args"
    // + " if you intend specify no vertices");
    // return new DefaultConnectivityAlgorithmsSelector<V, E>(graph, asList(vertices));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("includingVertices", vertices).as(ConnectivityAlgorithmsSelector.class);
  }

  public ConnectivityAlgorithmsSelector<V, E> includingAllVertices() {
    //
    // return new DefaultConnectivityAlgorithmsSelector<V, E>(graph, graph.getVertices0());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("includingAllVertices").as(ConnectivityAlgorithmsSelector.class);
  }

  public DefaultConnectivityBuilder(Graph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }
}
