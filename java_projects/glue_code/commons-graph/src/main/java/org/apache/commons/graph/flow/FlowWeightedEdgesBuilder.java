package org.apache.commons.graph.flow;

import org.apache.commons.graph.Mapper;

public interface FlowWeightedEdgesBuilder<V, WE> {
  <W, M extends Mapper<WE, W>> FromHeadBuilder<V, WE, W> whereEdgesHaveWeights(M weightedEdges);
}
