package org.apache.commons.graph.shortestpath;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.weight.OrderedMonoid;
public interface PathSourceSelector<V, WE, W> {
    <H extends V> TargetSourceSelector<V, WE, W> from(H source);
    <WO extends OrderedMonoid<W>> AllVertexPairsShortestPath<V, WE, W> applyingFloydWarshall(
;}
