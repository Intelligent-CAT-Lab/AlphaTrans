package org.apache.commons.graph;


public interface Path<V, E> extends Graph<V, E> {
  V getTarget();

  V getSource();
}
