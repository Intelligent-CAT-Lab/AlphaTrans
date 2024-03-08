package org.apache.commons.graph.spanning;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.weight.OrderedMonoid;
public interface SpanningTreeAlgorithmSelector<V, W, WE> {
    <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingPrimAlgorithm(WO weightOperations);
    <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingKruskalAlgorithm(
;    <WO extends OrderedMonoid<W>> SpanningTree<V, WE, W> applyingBoruvkaAlgorithm(
;}
