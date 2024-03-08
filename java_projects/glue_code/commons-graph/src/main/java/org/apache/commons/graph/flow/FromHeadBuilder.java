package org.apache.commons.graph.flow;


public interface FromHeadBuilder<V, WE, W> {
  <H extends V> ToTailBuilder<V, WE, W> from(H head);
}
