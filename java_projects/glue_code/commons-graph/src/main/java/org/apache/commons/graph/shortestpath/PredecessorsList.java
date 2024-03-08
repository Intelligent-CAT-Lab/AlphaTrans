package org.apache.commons.graph.shortestpath;

import java.util.HashMap;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.weight.Monoid;
import org.graalvm.polyglot.Value;

public final class PredecessorsList<V, WE, W> {
  private final Map<V, V> predecessors = new HashMap<V, V>();
  private static Value clz =
      ContextInitializer.getPythonClass("/shortestpath/PredecessorsList.py", "PredecessorsList");
  private Value obj;

  public PredecessorsList(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isEmpty() {
    //
    // return predecessors.isEmpty();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEmpty").as(boolean.class);
  }

  public WeightedPath<V, WE, W> buildPath1(
      V source, V touch, V target, PredecessorsList<V, WE, W> backwardsList) {
    //
    // InMemoryWeightedPath<V, WE, W> path =
    // new InMemoryWeightedPath<V, WE, W>(source, target, weightOperations, weightedEdges);
    //
    // V vertex = touch;
    // while (!source.equals(vertex)) {
    // V predecessor = predecessors.get(vertex);
    // if (predecessor == null) {
    // throw new PathNotFoundException(
    // "Path from '%s' to '%s' doesn't exist", source, target);
    // }
    // WE edge = graph.getEdge(predecessor, vertex);
    //
    // path.addConnectionInHead(predecessor, edge, vertex);
    //
    // vertex = predecessor;
    // }
    //
    // vertex = touch;
    //
    // while (!target.equals(vertex)) {
    // V predecessor = backwardsList.predecessors.get(vertex);
    // if (predecessor == null) {
    // throw new PathNotFoundException(
    // "Path from '%s' to '%s' doesn't exist", source, target);
    // }
    // WE edge = graph.getEdge(vertex, predecessor);
    //
    // path.addConnectionInTail(vertex, edge, predecessor);
    //
    // vertex = predecessor;
    // }
    //
    // return path;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("buildPath1", source, touch, target, backwardsList)
        .as(WeightedPath.class);
  }

  public WeightedPath<V, WE, W> buildPath0(V source, V target) {
    //
    // InMemoryWeightedPath<V, WE, W> path =
    // new InMemoryWeightedPath<V, WE, W>(source, target, weightOperations, weightedEdges);
    //
    // V vertex = target;
    // while (!source.equals(vertex)) {
    // V predecessor = predecessors.get(vertex);
    // if (predecessor == null) {
    // throw new PathNotFoundException(
    // "Path from '%s' to '%s' doesn't exist", source, target);
    // }
    // WE edge = graph.getEdge(predecessor, vertex);
    //
    // path.addConnectionInHead(predecessor, edge, vertex);
    //
    // vertex = predecessor;
    // }
    //
    // return path;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("buildPath0", source, target).as(WeightedPath.class);
  }

  public void addPredecessor(V tail, V head) {
    //
    // predecessors.put(tail, head);
    //

    obj.invokeMember("addPredecessor", tail, head);
  }

  public PredecessorsList(
      Graph<V, WE> graph, Monoid<W> weightOperations, Mapper<WE, W> weightedEdges) {
    //
    // this.graph = graph;
    // this.weightOperations = weightOperations;
    // this.weightedEdges = weightedEdges;
    //

    this.obj = clz.invokeMember("__init__", graph, weightOperations, weightedEdges);
  }
}
