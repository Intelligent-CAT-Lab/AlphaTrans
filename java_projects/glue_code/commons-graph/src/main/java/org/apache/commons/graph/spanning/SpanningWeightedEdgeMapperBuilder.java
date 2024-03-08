package org.apache.commons.graph.spanning;

import org.apache.commons.graph.Mapper;

public interface SpanningWeightedEdgeMapperBuilder<V, WE> {
  <W> SpanningTreeSourceSelector<V, W, WE> whereEdgesHaveWeights(Mapper<WE, W> weightedEdges);
}
