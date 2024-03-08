package org.apache.commons.graph.shortestpath;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.weight.OrderedMonoid;
public interface ShortestPathAlgorithmSelector<V, WE, W> {
    <WO extends OrderedMonoid<W>> WeightedPath<V, WE, W> applyingDijkstra(WO weightOperations);
    <WO extends OrderedMonoid<W>> WeightedPath<V, WE, W> applyingBidirectionalDijkstra(
;    <WO extends OrderedMonoid<W>> HeuristicBuilder<V, WE, W> applyingAStar(WO weightOperations);
}
