package org.apache.commons.graph.builder;


public interface GraphConnector<V, E> {
  <N extends V> N addVertex(N node);

  <A extends E> HeadVertexConnector<V, E> addEdge(A arc);
}
