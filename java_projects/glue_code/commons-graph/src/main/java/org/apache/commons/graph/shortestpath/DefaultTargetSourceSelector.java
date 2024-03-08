package org.apache.commons.graph.shortestpath;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

final class DefaultTargetSourceSelector<V, WE, W> implements TargetSourceSelector<V, WE, W> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/DefaultTargetSourceSelector.py", "DefaultTargetSourceSelector");
  private Value obj;

  public DefaultTargetSourceSelector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <T extends V> ShortestPathAlgorithmSelector<V, WE, W> to(T target) {
    //
    // target = checkNotNull(target, "Shortest path can not be calculated to a null target");
    // return new DefaultShortestPathAlgorithmSelector<V, WE, W>(
    // graph, weightedEdges, source, target);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("to", target).as(ShortestPathAlgorithmSelector.class);
  }

  public <WO extends OrderedMonoid<W>> AllVertexPairsShortestPath<V, WE, W> applyingBelmannFord(
      WO weightOperations) {
    //
    // weightOperations =
    // checkNotNull(
    // weightOperations,
    // "Belmann-Ford algorithm can not be applied using null weight operations");
    //
    // final ShortestDistances<V, W> shortestDistances =
    // new ShortestDistances<V, W>(weightOperations);
    // shortestDistances.setWeight(source, weightOperations.identity());
    //
    // final PredecessorsList<V, WE, W> predecessors =
    // new PredecessorsList<V, WE, W>(graph, weightOperations, weightedEdges);
    //
    // for (int i = 0; i < graph.getOrder(); i++) {
    // for (WE edge : graph.getEdges()) {
    // VertexPair<V> vertexPair = graph.getVertices1(edge);
    // V u = vertexPair.getHead();
    // V v = vertexPair.getTail();
    //
    // if (shortestDistances.alreadyVisited(u)) {
    // W shortDist =
    // weightOperations.append(
    // shortestDistances.getWeight(u), weightedEdges.map(edge));
    //
    // if (!shortestDistances.alreadyVisited(v)
    // || weightOperations.compare(shortDist, shortestDistances.getWeight(v))
    // < 0) {
    // shortestDistances.setWeight(v, shortDist);
    //
    // predecessors.addPredecessor(v, u);
    // }
    // }
    // }
    // }
    //
    // for (WE edge : graph.getEdges()) {
    // VertexPair<V> vertexPair = graph.getVertices1(edge);
    // V u = vertexPair.getHead();
    // V v = vertexPair.getTail();
    //
    // if (shortestDistances.alreadyVisited(u)) {
    // W shortDist =
    // weightOperations.append(
    // shortestDistances.getWeight(u), weightedEdges.map(edge));
    //
    // if (!shortestDistances.alreadyVisited(v)
    // || weightOperations.compare(shortDist, shortestDistances.getWeight(v))
    // < 0) {
    // throw new NegativeWeightedCycleException(
    // "Graph contains a negative-weight cycle in vertex %s", null, v, graph);
    // }
    // }
    // }
    //
    // AllVertexPairsShortestPath<V, WE, W> allVertexPairsShortestPath =
    // new AllVertexPairsShortestPath<V, WE, W>(weightOperations);
    //
    // for (V target : graph.getVertices0()) {
    // if (!source.equals(target)) {
    // try {
    // WeightedPath<V, WE, W> weightedPath = predecessors.buildPath0(source, target);
    // allVertexPairsShortestPath.addShortestPath(source, target, weightedPath);
    // } catch (PathNotFoundException e) {
    // continue;
    // }
    // }
    // }
    //
    // return allVertexPairsShortestPath;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyingBelmannFord", weightOperations)
        .as(AllVertexPairsShortestPath.class);
  }

  public DefaultTargetSourceSelector(Graph<V, WE> graph, Mapper<WE, W> weightedEdges, V source) {
    //
    // this.graph = graph;
    // this.weightedEdges = weightedEdges;
    // this.source = source;
    //

    this.obj = clz.invokeMember("__init__", graph, weightedEdges, source);
  }
}
