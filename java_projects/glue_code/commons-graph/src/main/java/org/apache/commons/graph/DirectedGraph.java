package org.apache.commons.graph;


public interface DirectedGraph<V, E> extends Graph<V, E> {
  int getOutDegree(V v);

  Iterable<V> getOutbound(V v);

  int getInDegree(V v);

  Iterable<V> getInbound(V v);
}
