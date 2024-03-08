package org.apache.commons.graph.coloring;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
public interface ColoringAlgorithmsSelector<V, E, C> {
    ColoredVertices<V, C> applyingGreedyAlgorithm();
    ColoredVertices<V, C> applyingBackTrackingAlgorithm1(
;    ColoredVertices<V, C> applyingBackTrackingAlgorithm0();
}
