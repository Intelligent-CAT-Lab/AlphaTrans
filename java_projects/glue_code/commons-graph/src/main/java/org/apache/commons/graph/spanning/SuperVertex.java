package org.apache.commons.graph.spanning;

import java.util.Iterator;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.graalvm.polyglot.Value;

final class SuperVertex<V, W, WE> implements Iterable<V> {
  private static Value clz =
      ContextInitializer.getPythonClass("/spanning/SuperVertex.py", "SuperVertex");
  private Value obj;

  public SuperVertex(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void merge(final SuperVertex<V, W, WE> other) {
    //
    // for (final V v : other.vertices) {
    // vertices.add(v);
    // }
    //
    // for (final WE edge : other.orderedEdges) {
    // final VertexPair<V> pair = graph.getVertices1(edge);
    // if (!vertices.contains(pair.getHead()) || !vertices.contains(pair.getTail())) {
    // orderedEdges.add(edge);
    // }
    // }
    //

    obj.invokeMember("merge", other);
  }

  public Iterator<V> iterator() {
    //
    // return vertices.iterator();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("iterator").as(Iterator.class);
  }

  public WE getMinimumWeightEdge() {
    //
    // boolean found = false;
    // WE edge = null;
    // while (!found && !orderedEdges.isEmpty()) {
    // edge = orderedEdges.pollFirst();
    // VertexPair<V> pair = graph.getVertices1(edge);
    // if (!vertices.contains(pair.getHead()) || !vertices.contains(pair.getTail())) {
    // found = true;
    // }
    // }
    // return edge;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinimumWeightEdge").as(WE.class);
  }

  public SuperVertex(
      final V source,
      final Graph<V, WE> graph,
      final WeightedEdgesComparator<W, WE> weightComparator) {
    //
    // this.graph = graph;
    //
    // vertices = new HashSet<V>();
    // vertices.add(source);
    //
    // orderedEdges = new TreeSet<WE>(weightComparator);
    //
    // for (final V w : graph.getConnectedVertices(source)) {
    // WE edge = graph.getEdge(source, w);
    // orderedEdges.add(edge);
    // }
    //

    this.obj = clz.invokeMember("__init__", source, graph, weightComparator);
  }
}
