package org.apache.commons.graph.builder;

import org.apache.commons.graph.MutableGraph;

public interface LinkedConnectionBuilder<V, E, G extends MutableGraph<V, E>> {
  G withConnections(GraphConnection<V, E> graphConnection);
}
