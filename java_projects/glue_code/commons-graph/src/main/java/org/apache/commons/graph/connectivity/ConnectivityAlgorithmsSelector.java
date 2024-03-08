package org.apache.commons.graph.connectivity;

import java.util.Collection;
import java.util.List;

public interface ConnectivityAlgorithmsSelector<V, E> {
  Collection<List<V>> applyingMinimumSpanningTreeAlgorithm();
}
