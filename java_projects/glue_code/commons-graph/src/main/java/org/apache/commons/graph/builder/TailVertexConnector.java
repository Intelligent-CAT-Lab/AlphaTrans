package org.apache.commons.graph.builder;


public interface TailVertexConnector<V, E> {
  <T extends V> void to(T tail);
}
