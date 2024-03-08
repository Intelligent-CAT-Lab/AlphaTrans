package org.apache.commons.graph.coloring;

import java.util.Set;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.UndirectedGraph;
import org.graalvm.polyglot.Value;

public final class DefaultColorsBuilder<V, E> implements ColorsBuilder<V, E> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/coloring/DefaultColorsBuilder.py", "DefaultColorsBuilder");
  private Value obj;

  public DefaultColorsBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <C> ColoringAlgorithmsSelector<V, E, C> withColors(Set<C> colors) {
    //
    // colors = checkNotNull(colors, "Colors set must be not null");
    // return new DefaultColoringAlgorithmsSelector<V, E, C>(graph, colors);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("withColors", colors).as(ColoringAlgorithmsSelector.class);
  }

  public DefaultColorsBuilder(UndirectedGraph<V, E> graph) {
    //
    // this.graph = graph;
    //

    this.obj = clz.invokeMember("__init__", graph);
  }
}
