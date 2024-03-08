package org.apache.commons.graph;

import java.io.Serializable;

public interface Graph<V, E> extends Serializable {
  VertexPair<V> getVertices1(E e);

  Iterable<V> getVertices0();

  int getSize();

  int getOrder();

  Iterable<E> getEdges();

  E getEdge(V source, V target);

  int getDegree(V v);

  Iterable<V> getConnectedVertices(V v);

  boolean containsVertex(V v);

  boolean containsEdge(E e);
}
