package org.apache.commons.graph.spanning;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.weight.OrderedMonoid;
public interface SpanningTreeSourceSelector<V, W, WE> {
    <S extends V> SpanningTreeAlgorithmSelector<V, W, WE> fromSource(S source);
    SpanningTreeAlgorithmSelector<V, W, WE> fromArbitrarySource();
    <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingReverseDeleteAlgorithm(
;}
