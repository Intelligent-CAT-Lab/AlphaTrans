package org.apache.commons.graph.flow;

import org.apache.commons.graph.weight.OrderedMonoid;

public interface MaxFlowAlgorithmSelector<V, WE, W> {
  <WO extends OrderedMonoid<W>> W applyingFordFulkerson(WO weightOperations);

  <WO extends OrderedMonoid<W>> W applyingEdmondsKarp(WO weightOperations);
}
