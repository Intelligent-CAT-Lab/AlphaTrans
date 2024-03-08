package org.apache.commons.graph.shortestpath;

import org.apache.commons.graph.WeightedPath;

public interface HeuristicBuilder<V, WE, W> {
  <H extends Heuristic<V, W>> WeightedPath<V, WE, W> withHeuristic(H heuristic);
}
