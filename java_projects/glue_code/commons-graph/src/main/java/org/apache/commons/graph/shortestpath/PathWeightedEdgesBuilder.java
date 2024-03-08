package org.apache.commons.graph.shortestpath;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Mapper;
public interface PathWeightedEdgesBuilder<V, WE> {
    <W, M extends Mapper<WE, W>> PathSourceSelector<V, WE, W> whereEdgesHaveWeights(
;}
