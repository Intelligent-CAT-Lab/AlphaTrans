package org.apache.commons.graph.flow;


public interface ToTailBuilder<V, WE, W> {
  <T extends V> MaxFlowAlgorithmSelector<V, WE, W> to(T tail);
}
