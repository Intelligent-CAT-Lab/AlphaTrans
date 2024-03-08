package org.apache.commons.graph.shortestpath;

import java.util.HashMap;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

public final class AllVertexPairsShortestPath<V, WE, W> {
  private final Map<VertexPair<V>, W> shortestDistances = new HashMap<VertexPair<V>, W>();
  private final Map<VertexPair<V>, WeightedPath<V, WE, W>> paths =
      new HashMap<VertexPair<V>, WeightedPath<V, WE, W>>();
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/shortestpath/AllVertexPairsShortestPath.py", "AllVertexPairsShortestPath");
  private Value obj;

  public AllVertexPairsShortestPath(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return shortestDistances.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public WeightedPath<V, WE, W> findShortestPath(V source, V target) {
    //
    // source = checkNotNull(source, "Impossible to add a shortest path from a null source");
    // target = checkNotNull(target, "Impossible to add a shortest path to a null target");
    //
    // WeightedPath<V, WE, W> path = paths.get(new VertexPair<V>(source, target));
    //
    // if (path == null) {
    // throw new PathNotFoundException("Path from '%s' to '%s' doesn't exist", source, target);
    // }
    //
    // return path;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("findShortestPath", source, target).as(WeightedPath.class);
  }

  boolean hasShortestDistance(V source, V target) {
    //
    // source = checkNotNull(source, "Impossible to add a shortest path from a null source");
    // target = checkNotNull(target, "Impossible to add a shortest path to a null target");
    //
    // if (source.equals(target)) {
    // return true;
    // }
    //
    // return shortestDistances.containsKey(new VertexPair<V>(source, target));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasShortestDistance", source, target).as(boolean.class);
  }

  W getShortestDistance(V source, V target) {
    //
    // source = checkNotNull(source, "Impossible to add a shortest path from a null source");
    // target = checkNotNull(target, "Impossible to add a shortest path to a null target");
    //
    // if (source.equals(target)) {
    // return weightOperations.identity();
    // }
    //
    // return shortestDistances.get(new VertexPair<V>(source, target));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getShortestDistance", source, target).as(W.class);
  }

  void addShortestPath(V source, V target, WeightedPath<V, WE, W> weightedPath) {
    //
    // source = checkNotNull(source, "Impossible to add a shortest path from a null source");
    // target = checkNotNull(target, "Impossible to add a shortest path to a null target");
    // weightedPath =
    // checkNotNull(
    // weightedPath,
    // "Impossible to add a null weightedPath path to a null target");
    //
    // paths.put(new VertexPair<V>(source, target), weightedPath);
    //

    obj.invokeMember("addShortestPath", source, target, weightedPath);
  }

  void addShortestDistance(V source, V target, W distance) {
    //
    // source = checkNotNull(source, "Impossible to add a shortest path from a null source");
    // target = checkNotNull(target, "Impossible to add a shortest path to a null target");
    // distance =
    // checkNotNull(
    // distance, "Impossible to add a shortest distance with a null distance");
    //
    // shortestDistances.put(new VertexPair<V>(source, target), distance);
    //

    obj.invokeMember("addShortestDistance", source, target, distance);
  }

  AllVertexPairsShortestPath(OrderedMonoid<W> weightOperations) {
    //
    // this.weightOperations = weightOperations;
    //

    this.obj = clz.invokeMember("__init__", weightOperations);
  }
}
