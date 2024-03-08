package org.apache.commons.graph.shortestpath;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.graalvm.polyglot.Value;

public final class DefaultWeightedEdgesSelector<V, WE> implements PathWeightedEdgesBuilder<V, WE> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/DefaultWeightedEdgesSelector.py", "DefaultWeightedEdgesSelector");
  private Value obj;

  public DefaultWeightedEdgesSelector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <W, M extends Mapper<WE, W>> PathSourceSelector<V, WE, W> whereEdgesHaveWeights(
      M weightedEdges) {
    //
    // weightedEdges =
    // checkNotNull(weightedEdges, "Function to calculate edges weight can not be null.");
    // return new DefaultPathSourceSelector<V, WE, W>(graph, weightedEdges);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("whereEdgesHaveWeights", weightedEdges).as(PathSourceSelector.class);
  }

  public DefaultWeightedEdgesSelector(Graph<V, WE> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }
}
