package org.apache.commons.graph.shortestpath;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

final class ShortestDistances<V, W> implements Comparator<V> {
  private final Map<V, W> distances = new HashMap<V, W>();
  private static Value clz =
      ContextInitializer.getPythonClass("/shortestpath/ShortestDistances.py", "ShortestDistances");
  private Value obj;

  public ShortestDistances(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setWeight(V vertex, W distance) {
    //
    // distances.put(vertex, distance);
    //

    obj.invokeMember("setWeight", vertex, distance);
  }

  public W getWeight(V vertex) {
    //
    // return distances.get(vertex);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getWeight", vertex).as(W.class);
  }

  public int compare(V left, V right) {
    //
    // if (!alreadyVisited(left) && !alreadyVisited(right)) {
    // return 0;
    // } else if (!alreadyVisited(left)) {
    // return 1;
    // } else if (!alreadyVisited(right)) {
    // return -1;
    // }
    // return weightOperations.compare(getWeight(left), getWeight(right));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", left, right).as(int.class);
  }

  public boolean alreadyVisited(V vertex) {
    //
    // return distances.containsKey(vertex);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("alreadyVisited", vertex).as(boolean.class);
  }

  public ShortestDistances(OrderedMonoid<W> weightOperations) {
    //
    // this.weightOperations = weightOperations;
    //

    this.obj = clz.invokeMember("__init__", weightOperations);
  }
}
