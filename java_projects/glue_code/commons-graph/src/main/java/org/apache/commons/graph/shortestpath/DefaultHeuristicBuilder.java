package org.apache.commons.graph.shortestpath;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

final class DefaultHeuristicBuilder<V, WE, W> implements HeuristicBuilder<V, WE, W> {
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/DefaultHeuristicBuilder.py", "DefaultHeuristicBuilder");
  private Value obj;

  public DefaultHeuristicBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public <H extends Heuristic<V, W>> WeightedPath<V, WE, W> withHeuristic(H heuristic) {
    //
    // heuristic =
    // checkNotNull(heuristic, "A* algorithm can not be applied using a null heuristic");
    //
    // final ShortestDistances<V, W> gScores = new ShortestDistances<V, W>(weightOperations);
    // gScores.setWeight(start, weightOperations.identity());
    //
    // final ShortestDistances<V, W> fScores = new ShortestDistances<V, W>(weightOperations);
    // W hScore = heuristic.applyHeuristic(start, goal);
    // fScores.setWeight(start, hScore);
    //
    // final Set<V> closedSet = new HashSet<V>();
    //
    // final Queue<V> openSet = new FibonacciHeap<V>(fScores);
    // openSet.add(start);
    //
    // final PredecessorsList<V, WE, W> predecessors =
    // new PredecessorsList<V, WE, W>(graph, weightOperations, weightedEdges);
    //
    // while (!openSet.isEmpty()) {
    // V current = openSet.remove();
    //
    // if (goal.equals(current)) {
    // return predecessors.buildPath0(start, goal);
    // }
    //
    // closedSet.add(current);
    //
    // Iterable<V> connected =
    // (graph instanceof DirectedGraph)
    // ? ((DirectedGraph<V, WE>) graph).getOutbound(current)
    // : graph.getConnectedVertices(current);
    // for (V v : connected) {
    // if (!closedSet.contains(v)) {
    // WE edge = graph.getEdge(current, v);
    // W tentativeGScore =
    // weightOperations.append(
    // gScores.getWeight(current), weightedEdges.map(edge));
    //
    // if (openSet.add(v)
    // || weightOperations.compare(tentativeGScore, gScores.getWeight(v))
    // < 0) {
    // predecessors.addPredecessor(v, current);
    // gScores.setWeight(v, tentativeGScore);
    // hScore = heuristic.applyHeuristic(v, goal);
    // fScores.setWeight(v, weightOperations.append(gScores.getWeight(v), hScore));
    // }
    // }
    // }
    // }
    //
    // throw new PathNotFoundException(
    // "Path from '%s' to '%s' doesn't exist in Graph '%s'", start, goal, graph);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("withHeuristic", heuristic).as(WeightedPath.class);
  }

  public DefaultHeuristicBuilder(
      Graph<V, WE> graph,
      Mapper<WE, W> weightedEdges,
      V source,
      V target,
      OrderedMonoid<W> weightOperations) {
    //
    // this.graph = graph;
    // this.weightedEdges = weightedEdges;
    // this.start = source;
    // this.goal = target;
    // this.weightOperations = weightOperations;
    //

    this.obj = clz.invokeMember("__init__", graph, weightedEdges, source, target, weightOperations);
  }
}
