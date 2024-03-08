package org.apache.commons.graph.flow;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Mapper;
import org.graalvm.polyglot.Value;

final class DefaultToTailBuilder<V, WE, W> implements ToTailBuilder<V, WE, W> {
  private static Value clz =
      ContextInitializer.getPythonClass("/flow/DefaultToTailBuilder.py", "DefaultToTailBuilder");
  private Value obj;

  public DefaultToTailBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <T extends V> MaxFlowAlgorithmSelector<V, WE, W> to(T tail) {
    //
    // tail = checkNotNull(tail, "tail vertex has to be specifies when looking for the max flow");
    // return new DefaultMaxFlowAlgorithmSelector<V, WE, W>(graph, weightedEdges, head, tail);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("to", tail).as(MaxFlowAlgorithmSelector.class);
  }

  public DefaultToTailBuilder(DirectedGraph<V, WE> graph, Mapper<WE, W> weightedEdges, V head) {
    //
    // this.graph = graph;
    // this.weightedEdges = weightedEdges;
    // this.head = head;
    //

    this.obj = clz.invokeMember("__init__", graph, weightedEdges, head);
  }
}
