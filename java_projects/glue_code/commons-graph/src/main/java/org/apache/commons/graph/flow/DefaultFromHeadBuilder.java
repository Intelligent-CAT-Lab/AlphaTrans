package org.apache.commons.graph.flow;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Mapper;
import org.graalvm.polyglot.Value;

final class DefaultFromHeadBuilder<V, WE, W> implements FromHeadBuilder<V, WE, W> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/flow/DefaultFromHeadBuilder.py", "DefaultFromHeadBuilder");
  private Value obj;

  public DefaultFromHeadBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <H extends V> ToTailBuilder<V, WE, W> from(H head) {
    //
    // head = checkNotNull(head, "head vertex has to be specifies when looking for the max flow");
    // return new DefaultToTailBuilder<V, WE, W>(graph, weightedEdges, head);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("from", head).as(ToTailBuilder.class);
  }

  public DefaultFromHeadBuilder(DirectedGraph<V, WE> graph, Mapper<WE, W> weightedEdges) {
    //
    // this.graph = graph;
    // this.weightedEdges = weightedEdges;
    //

    this.obj = clz.invokeMember("__init__", graph, weightedEdges);
  }
}
