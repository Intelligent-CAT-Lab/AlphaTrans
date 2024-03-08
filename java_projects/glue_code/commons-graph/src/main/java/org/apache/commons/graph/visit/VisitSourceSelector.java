package org.apache.commons.graph.visit;

import org.apache.commons.graph.Graph;

public interface VisitSourceSelector<V, E, G extends Graph<V, E>> {
  <S extends V> VisitAlgorithmsSelector<V, E, G> from(S source);
}
