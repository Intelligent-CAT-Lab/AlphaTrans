package org.apache.commons.graph.shortestpath;


public interface Heuristic<V, W> {
  W applyHeuristic(V current, V goal);
}
