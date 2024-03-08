package org.apache.commons.graph.spanning;

import java.util.Collection;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.VertexPair;
import org.graalvm.polyglot.Value;

final class ReverseDeleteGraph<V, WE> implements Graph<V, WE> {
  private static final long serialVersionUID = -543197749473412325L;
  private static Value clz =
      ContextInitializer.getPythonClass("/spanning/ReverseDeleteGraph.py", "ReverseDeleteGraph");
  private Value obj;

  public ReverseDeleteGraph(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public VertexPair<V> getVertices1(WE e) {
    //
    // for (WE edge : sortedEdge) {
    // if (edge.equals(e)) {
    // return graph.getVertices1(e);
    // }
    // }
    //
    // if (sortedEdge.contains(e)) {
    // return graph.getVertices1(e);
    // }
    //
    // if (visitedEdge.contains(e)) {
    // return graph.getVertices1(e);
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices1", e).as(VertexPair.class);
  }

  public Iterable<V> getVertices0() {
    //
    // return graph.getVertices0();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices0").as(Iterable.class);
  }

  public int getSize() {
    //
    // return sortedEdge.size() + visitedEdge.size();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSize").as(int.class);
  }

  public int getOrder() {
    //
    // return graph.getOrder();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOrder").as(int.class);
  }

  public Iterable<WE> getEdges() {
    //
    // List<WE> e = new ArrayList<WE>();
    // e.addAll(sortedEdge);
    // e.addAll(visitedEdge);
    // return e;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdges").as(Iterable.class);
  }

  public WE getEdge(V source, V target) {
    //
    // WE edge = graph.getEdge(source, target);
    // if (sortedEdge.contains(edge)) {
    // return edge;
    // }
    //
    // if (visitedEdge.contains(edge)) {
    // return edge;
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdge", source, target).as(WE.class);
  }

  public int getDegree(V v) {
    //
    // throw new GraphException("Unused Method", null, null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDegree", v).as(int.class);
  }

  public Iterable<V> getConnectedVertices(V v) {
    //
    //
    // List<V> tmp = new ArrayList<V>();
    // for (V originalVertex : graph.getConnectedVertices(v)) {
    // if (getEdge(v, originalVertex) != null) {
    // tmp.add(originalVertex);
    // }
    // }
    //
    // return tmp;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getConnectedVertices", v).as(Iterable.class);
  }

  public boolean containsVertex(V v) {
    //
    // return graph.containsVertex(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsVertex", v).as(boolean.class);
  }

  public boolean containsEdge(WE e) {
    //
    // return graph.containsEdge(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsEdge", e).as(boolean.class);
  }

  public ReverseDeleteGraph(
      Graph<V, WE> graph, Collection<WE> sortedEdge, Collection<WE> visitedEdge) {
    //
    // this.graph = graph;
    // this.sortedEdge = sortedEdge;
    // this.visitedEdge = visitedEdge;
    //

    this.obj = clz.invokeMember("__init__", graph, sortedEdge, visitedEdge);
  }
}
