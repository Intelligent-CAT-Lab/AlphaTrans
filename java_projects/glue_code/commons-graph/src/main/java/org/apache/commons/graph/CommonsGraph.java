package org.apache.commons.graph;

import org.apache.commons.graph.builder.GraphConnection;
import org.apache.commons.graph.builder.LinkedConnectionBuilder;
import org.apache.commons.graph.coloring.ColorsBuilder;
import org.apache.commons.graph.connectivity.ConnectivityBuilder;
import org.apache.commons.graph.elo.GameResult;
import org.apache.commons.graph.elo.RankingSelector;
import org.apache.commons.graph.export.NamedExportSelector;
import org.apache.commons.graph.flow.FlowWeightedEdgesBuilder;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.scc.SccAlgorithmSelector;
import org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder;
import org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder;
import org.apache.commons.graph.visit.VisitSourceSelector;
import org.graalvm.polyglot.Value;

public final class CommonsGraph {
  private static Value clz = ContextInitializer.getPythonClass("/CommonsGraph.py", "CommonsGraph");
  private Value obj;

  public CommonsGraph(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static <V, E, G extends Graph<V, E>> VisitSourceSelector<V, E, G> visit(G graph) {
    //
    // graph = checkNotNull(graph, "No algorithm can be applied on null graph!");
    // return new DefaultVisitSourceSelector<V, E, G>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("visit", graph).as(VisitSourceSelector.class);
  }

  public static <V, E> Graph<V, E> synchronize3(UndirectedGraph<V, E> graph) {
    //
    // return new SynchronizedUndirectedGraph<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("synchronize3", graph).as(Graph.class);
  }

  public static <V, E> Graph<V, E> synchronize2(MutableGraph<V, E> graph) {
    //
    // return new SynchronizedMutableGraph<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("synchronize2", graph).as(Graph.class);
  }

  public static <V, E> Graph<V, E> synchronize1(Graph<V, E> graph) {
    //
    // return new SynchronizedGraph<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("synchronize1", graph).as(Graph.class);
  }

  public static <V, E> Graph<V, E> synchronize0(DirectedGraph<V, E> graph) {
    //
    // return new SynchronizedDirectedGraph<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("synchronize0", graph).as(Graph.class);
  }

  public static <V, E, G extends MutableGraph<V, E>> LinkedConnectionBuilder<V, E, G> populate(
      G graph) {
    //
    // return new DefaultLinkedConnectionBuilder<V, E, G>(
    // checkNotNull(graph, "Impossible to configure null graph!"));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("populate", graph).as(LinkedConnectionBuilder.class);
  }

  public static <V, E> UndirectedMutableGraph<V, E> newUndirectedMutableGraph(
      GraphConnection<V, E> graphConnection) {
    //
    // return populate(new UndirectedMutableGraph<V, E>()).withConnections(graphConnection);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newUndirectedMutableGraph", graphConnection)
        .as(UndirectedMutableGraph.class);
  }

  public static <V, E> DirectedMutableGraph<V, E> newDirectedMutableGraph(
      GraphConnection<V, E> graphConnection) {
    //
    // return populate(new DirectedMutableGraph<V, E>()).withConnections(graphConnection);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newDirectedMutableGraph", graphConnection)
        .as(DirectedMutableGraph.class);
  }

  SpanningWeightedEdgeMapperBuilder<V, WE> minimumSpanningTree(G graph) {
    //
    // graph = checkNotNull(graph, "Minimum spanning tree can not be calculated on null graph");
    // return new DefaultSpanningWeightedEdgeMapperBuilder<V, WE>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("minimumSpanningTree", graph)
        .as(SpanningWeightedEdgeMapperBuilder.class);
  }

  SccAlgorithmSelector<V, E> findStronglyConnectedComponent(G graph) {
    //
    // graph =
    // checkNotNull(
    // graph,
    // "Strongly Connected Component cannot be calculated from a null graph");
    // return new DefaultSccAlgorithmSelector<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("findStronglyConnectedComponent", graph).as(SccAlgorithmSelector.class);
  }

  public static <V, WE, G extends Graph<V, WE>> PathWeightedEdgesBuilder<V, WE> findShortestPath(
      G graph) {
    //
    // graph = checkNotNull(graph, "Shortest path can not be calculated on null graph");
    // return new DefaultWeightedEdgesSelector<V, WE>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("findShortestPath", graph).as(PathWeightedEdgesBuilder.class);
  }

  FlowWeightedEdgesBuilder<V, WE> findMaxFlow(G graph) {
    //
    // graph = checkNotNull(graph, "Max flow can not be calculated on null graph");
    // return new DefaultFlowWeightedEdgesBuilder<V, WE>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("findMaxFlow", graph).as(FlowWeightedEdgesBuilder.class);
  }

  public static <V, E, G extends Graph<V, E>> ConnectivityBuilder<V, E> findConnectedComponent(
      G graph) {
    //
    // graph = checkNotNull(graph, "Connected Component cannot be calculated from a null graph");
    // return new DefaultConnectivityBuilder<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("findConnectedComponent", graph).as(ConnectivityBuilder.class);
  }

  public static <V, E, G extends Graph<V, E>> NamedExportSelector<V, E> export(G graph) {
    //
    // graph = checkNotNull(graph, "Null graph can not be exported");
    // return new DefaultExportSelector<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("export", graph).as(NamedExportSelector.class);
  }

  public static <P, TG extends DirectedGraph<P, GameResult>> RankingSelector<P> eloRate(
      TG tournamentGraph) {
    //
    // tournamentGraph =
    // checkNotNull(tournamentGraph, "ELO ranking can not be applied on null graph!");
    // return new DefaultRankingSelector<P>(tournamentGraph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("eloRate", tournamentGraph).as(RankingSelector.class);
  }

  public static <V, E, G extends UndirectedGraph<V, E>> ColorsBuilder<V, E> coloring(G graph) {
    //
    // graph = checkNotNull(graph, "Coloring can not be calculated on null graph");
    // return new DefaultColorsBuilder<V, E>(graph);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("coloring", graph).as(ColorsBuilder.class);
  }

  private CommonsGraph() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
