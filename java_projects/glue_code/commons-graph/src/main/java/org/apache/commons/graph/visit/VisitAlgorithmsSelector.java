package org.apache.commons.graph.visit;

import org.apache.commons.graph.Graph;

public interface VisitAlgorithmsSelector<V, E, G extends Graph<V, E>> {
  <O> O applyingDepthFirstSearch1(GraphVisitHandler<V, E, G, O> handler);

  Graph<V, E> applyingDepthFirstSearch0();

  <O> O applyingBreadthFirstSearch1(GraphVisitHandler<V, E, G, O> handler);

  Graph<V, E> applyingBreadthFirstSearch0();
}
