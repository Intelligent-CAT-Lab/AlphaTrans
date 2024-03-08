package org.apache.commons.graph.shortestpath;

import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

final class DefaultPathSourceSelector<V, WE, W> implements PathSourceSelector<V, WE, W> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/DefaultPathSourceSelector.py", "DefaultPathSourceSelector");
  private Value obj;

  public DefaultPathSourceSelector(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <H extends V> TargetSourceSelector<V, WE, W> from(H source) {
    //
    // source = checkNotNull(source, "Shortest path can not be calculated from a null source");
    // return new DefaultTargetSourceSelector<V, WE, W>(graph, weightedEdges, source);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("from", source).as(TargetSourceSelector.class);
  }

  public <WO extends OrderedMonoid<W>> AllVertexPairsShortestPath<V, WE, W> applyingFloydWarshall(
      WO weightOperations) {
    //
    // weightOperations =
    // checkNotNull(
    // weightOperations,
    // "Floyd-Warshall algorithm can not be applied using null weight operations");
    //
    // AllVertexPairsShortestPath<V, WE, W> shortestPaths =
    // new AllVertexPairsShortestPath<V, WE, W>(weightOperations);
    // Map<VertexPair<V>, V> next = new HashMap<VertexPair<V>, V>();
    //
    // for (WE we : graph.getEdges()) {
    // VertexPair<V> vertexPair = graph.getVertices1(we);
    // shortestPaths.addShortestDistance(
    // vertexPair.getHead(), vertexPair.getTail(), weightedEdges.map(we));
    //
    // if (graph instanceof UndirectedGraph) {
    // shortestPaths.addShortestDistance(
    // vertexPair.getTail(), vertexPair.getHead(), weightedEdges.map(we));
    // }
    // }
    //
    // for (V k : graph.getVertices0()) {
    // for (V i : graph.getVertices0()) {
    // for (V j : graph.getVertices0()) {
    // if (shortestPaths.hasShortestDistance(i, k)
    // && shortestPaths.hasShortestDistance(k, j)) {
    // W newDistance =
    // weightOperations.append(
    // shortestPaths.getShortestDistance(i, k),
    // shortestPaths.getShortestDistance(k, j));
    // if (!shortestPaths.hasShortestDistance(i, j)
    // || weightOperations.compare(
    // newDistance,
    // shortestPaths.getShortestDistance(i, j))
    // < 0) {
    // shortestPaths.addShortestDistance(i, j, newDistance);
    //
    // next.put(new VertexPair<V>(i, j), k);
    // }
    // }
    // }
    // }
    // }
    //
    // for (V source : graph.getVertices0()) {
    // for (V target : graph.getVertices0()) {
    // if (!source.equals(target)) {
    // PredecessorsList<V, WE, W> predecessorsList =
    // new PredecessorsList<V, WE, W>(graph, weightOperations, weightedEdges);
    //
    // pathReconstruction(predecessorsList, source, target, next);
    // if (!predecessorsList.isEmpty()) {
    // WeightedPath<V, WE, W> weightedPath =
    // predecessorsList.buildPath0(source, target);
    // if (weightedPath.getOrder() > 0) {
    // shortestPaths.addShortestPath(source, target, weightedPath);
    // }
    // }
    // }
    // }
    // }
    //
    // return shortestPaths;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyingFloydWarshall", weightOperations)
        .as(AllVertexPairsShortestPath.class);
  }

  public DefaultPathSourceSelector(Graph<V, WE> graph, Mapper<WE, W> weightedEdges) {
    //
    // this.graph = graph;
    // this.weightedEdges = weightedEdges;
    //

    this.obj = clz.invokeMember("__init__", graph, weightedEdges);
  }

  private void pathReconstruction(
      PredecessorsList<V, WE, W> path, V source, V target, Map<VertexPair<V>, V> next) {
    //
    // V k = next.get(new VertexPair<V>(source, target));
    // if (k == null) {
    // WE edge = graph.getEdge(source, target);
    // if (edge != null) {
    // path.addPredecessor(target, source);
    // }
    // } else {
    // pathReconstruction(path, source, k, next);
    // pathReconstruction(path, k, target, next);
    // }
    //

    obj.invokeMember("pathReconstruction", path, source, target, next);
  }
}
