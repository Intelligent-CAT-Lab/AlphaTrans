package org.apache.commons.graph.connectivity;


public interface ConnectivityBuilder<V, E> {
  ConnectivityAlgorithmsSelector<V, E> includingVertices(V... vertices);

  ConnectivityAlgorithmsSelector<V, E> includingAllVertices();
}
