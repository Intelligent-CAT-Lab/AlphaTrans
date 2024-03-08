package org.apache.commons.graph;

import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.graalvm.polyglot.Value;

public final class EdgeWeightMapper implements Mapper<BaseLabeledWeightedEdge<Double>, Double> {
  private static final long serialVersionUID = 20120728L;
  private static Value clz =
      ContextInitializer.getPythonClass("/EdgeWeightMapper.py", "EdgeWeightMapper");
  private Value obj;

  public EdgeWeightMapper(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Double map(BaseLabeledWeightedEdge<Double> input) {
    //
    // return input.getWeight();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("map", input).as(Double.class);
  }
}
