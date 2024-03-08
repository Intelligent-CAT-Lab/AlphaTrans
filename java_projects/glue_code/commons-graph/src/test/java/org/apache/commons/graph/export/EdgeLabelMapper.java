package org.apache.commons.graph;

import org.apache.commons.graph.model.BaseLabeledWeightedEdge;
import org.graalvm.polyglot.Value;

public final class EdgeLabelMapper implements Mapper<BaseLabeledWeightedEdge<Double>, String> {
  private static final long serialVersionUID = 20120728L;
  private static Value clz =
      ContextInitializer.getPythonClass("/EdgeLabelMapper.py", "EdgeLabelMapper");
  private Value obj;

  public EdgeLabelMapper(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String map(BaseLabeledWeightedEdge<Double> input) {
    //
    // return input.getLabel();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("map", input).as(String.class);
  }
}
