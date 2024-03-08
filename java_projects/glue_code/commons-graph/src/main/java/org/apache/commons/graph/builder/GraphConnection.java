package org.apache.commons.graph.builder;


public interface GraphConnection<V, E> {
  void connect(GraphConnector<V, E> grapher);
}
