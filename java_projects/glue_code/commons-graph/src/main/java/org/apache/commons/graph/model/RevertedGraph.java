package org.apache.commons.graph.model;

import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.VertexPair;
import org.graalvm.polyglot.Value;

public final class RevertedGraph<V, E> implements DirectedGraph<V, E> {
  private static final long serialVersionUID = 5867643705350331891L;
  private static Value clz =
      ContextInitializer.getPythonClass("/model/RevertedGraph.py", "RevertedGraph");
  private Value obj;

  public RevertedGraph(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public VertexPair<V> getVertices1(E e) {
    //
    // VertexPair<V> directedVertexPair = directedGraph.getVertices1(e);
    // return new VertexPair<V>(directedVertexPair.getTail(), directedVertexPair.getHead());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices1", e).as(VertexPair.class);
  }

  public Iterable<V> getVertices0() {
    //
    // return directedGraph.getVertices0();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices0").as(Iterable.class);
  }

  public int getSize() {
    //
    // return directedGraph.getSize();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSize").as(int.class);
  }

  public int getOutDegree(V v) {
    //
    // return directedGraph.getOutDegree(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOutDegree", v).as(int.class);
  }

  public Iterable<V> getOutbound(V v) {
    //
    // return directedGraph.getInbound(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOutbound", v).as(Iterable.class);
  }

  public int getOrder() {
    //
    // return directedGraph.getOrder();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOrder").as(int.class);
  }

  public int getInDegree(V v) {
    //
    // return directedGraph.getOutDegree(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getInDegree", v).as(int.class);
  }

  public Iterable<V> getInbound(V v) {
    //
    // return directedGraph.getOutbound(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getInbound", v).as(Iterable.class);
  }

  public Iterable<E> getEdges() {
    //
    // return directedGraph.getEdges();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdges").as(Iterable.class);
  }

  public E getEdge(V source, V target) {
    //
    // return directedGraph.getEdge(target, source);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdge", source, target).as(E.class);
  }

  public int getDegree(V v) {
    //
    // return directedGraph.getDegree(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDegree", v).as(int.class);
  }

  public Iterable<V> getConnectedVertices(V v) {
    //
    // return directedGraph.getConnectedVertices(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getConnectedVertices", v).as(Iterable.class);
  }

  public boolean containsVertex(V v) {
    //
    // return directedGraph.containsVertex(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsVertex", v).as(boolean.class);
  }

  public boolean containsEdge(E e) {
    //
    // return directedGraph.containsEdge(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsEdge", e).as(boolean.class);
  }

  public RevertedGraph(DirectedGraph<V, E> directedGraph) {
    //
    // directedGraph = checkNotNull(directedGraph, "Adapted DirectedGraph must be not null");
    // this.directedGraph = directedGraph;
    //

    this.obj = clz.invokeMember("__init__", directedGraph);
  }
}
