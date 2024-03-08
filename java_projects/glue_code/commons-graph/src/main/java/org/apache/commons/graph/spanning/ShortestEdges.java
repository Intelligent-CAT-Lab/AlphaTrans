package org.apache.commons.graph.spanning;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.graalvm.polyglot.Value;

final class ShortestEdges<V, WE, W> implements Comparator<V> {
  private final Map<V, WE> predecessors = new HashMap<V, WE>();
  private static Value clz =
      ContextInitializer.getPythonClass("/spanning/ShortestEdges.py", "ShortestEdges");
  private Value obj;

  public ShortestEdges(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return predecessors.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public boolean isEmpty() {
    //
    // return predecessors.isEmpty();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEmpty").as(boolean.class);
  }

  public boolean hasWeight(V vertex) {
    //
    // return predecessors.containsKey(vertex);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasWeight", vertex).as(boolean.class);
  }

  public W getWeight(V vertex) {
    //
    // if (source.equals(vertex)) {
    // return weightOperations.identity();
    // }
    //
    // WE edge = predecessors.get(vertex);
    //
    // if (edge == null) {
    // return null;
    // }
    //
    // return weightedEdges.map(edge);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getWeight", vertex).as(W.class);
  }

  public SpanningTree<V, WE, W> createSpanningTree() {
    //
    // MutableSpanningTree<V, WE, W> spanningTree =
    // new MutableSpanningTree<V, WE, W>(weightOperations, weightedEdges);
    //
    // for (WE edge : this.predecessors.values()) {
    // VertexPair<V> vertices = graph.getVertices1(edge);
    //
    // V head = vertices.getHead();
    // V tail = vertices.getTail();
    //
    // addEdgeIgnoringExceptions(head, spanningTree);
    // addEdgeIgnoringExceptions(tail, spanningTree);
    //
    // spanningTree.addEdge(head, graph.getEdge(head, tail), tail);
    // }
    //
    // return spanningTree;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("createSpanningTree").as(SpanningTree.class);
  }

  public int compare(V left, V right) {
    //
    // if (!hasWeight(left) && !hasWeight(right)) {
    // return 0;
    // } else if (!hasWeight(left)) {
    // return 1;
    // } else if (!hasWeight(right)) {
    // return -1;
    // }
    // return weightOperations.compare(getWeight(left), getWeight(right));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", left, right).as(int.class);
  }

  public void addPredecessor(V tail, WE head) {
    //
    // predecessors.put(tail, head);
    //

    obj.invokeMember("addPredecessor", tail, head);
  }

  public ShortestEdges(
      Graph<V, WE> graph,
      V source,
      OrderedMonoid<W> weightOperations,
      Mapper<WE, W> weightedEdges) {
    //
    // this.graph = graph;
    // this.source = source;
    // this.weightOperations = weightOperations;
    // this.weightedEdges = weightedEdges;
    //

    this.obj = clz.invokeMember("__init__", graph, source, weightOperations, weightedEdges);
  }

  private static <V, WE, W> void addEdgeIgnoringExceptions(
      V vertex, MutableSpanningTree<V, WE, W> spanningTree) {
    //
    // try {
    // spanningTree.addVertex(vertex);
    // } catch (GraphException e) {
    // }
    //

    clz.invokeMember("addEdgeIgnoringExceptions", vertex, spanningTree);
  }
}
