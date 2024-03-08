package org.apache.commons.graph;

import org.apache.commons.graph.model.BaseLabeledVertex;
import org.graalvm.polyglot.Value;

public final class VertexLabelMapper implements Mapper<BaseLabeledVertex, String> {
  private static final long serialVersionUID = 20120728L;
  private static Value clz =
      ContextInitializer.getPythonClass("/VertexLabelMapper.py", "VertexLabelMapper");
  private Value obj;

  public VertexLabelMapper(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String map(BaseLabeledVertex input) {
    //
    // return input.getLabel();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("map", input).as(String.class);
  }
}
