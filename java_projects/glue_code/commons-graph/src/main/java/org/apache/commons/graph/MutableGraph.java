package org.apache.commons.graph;


public interface MutableGraph<V, E> extends Graph<V, E> {
  void removeVertex(V v);

  void removeEdge(E e);

  void addVertex(V v);

  void addEdge(V head, E e, V tail);
}
