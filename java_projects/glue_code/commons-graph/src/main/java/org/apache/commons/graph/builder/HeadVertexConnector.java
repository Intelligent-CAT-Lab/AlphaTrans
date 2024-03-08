package org.apache.commons.graph.builder;


public interface HeadVertexConnector<V, E> {
  <H extends V> TailVertexConnector<V, E> from(H head);
}
