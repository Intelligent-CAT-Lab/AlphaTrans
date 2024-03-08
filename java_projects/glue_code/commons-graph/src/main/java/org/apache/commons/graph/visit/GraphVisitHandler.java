package org.apache.commons.graph.visit;

import org.apache.commons.graph.Graph;

public interface GraphVisitHandler<V, E, G extends Graph<V, E>, O> {
  O onCompleted();

  VisitState finishVertex(V vertex);

  void finishGraph(G graph);

  VisitState finishEdge(V head, E edge, V tail);

  VisitState discoverVertex(V vertex);

  void discoverGraph(G graph);

  VisitState discoverEdge(V head, E edge, V tail);
}
