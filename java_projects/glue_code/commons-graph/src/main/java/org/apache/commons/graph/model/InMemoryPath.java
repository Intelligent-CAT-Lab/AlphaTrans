package org.apache.commons.graph.model;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.Path;
import org.apache.commons.graph.VertexPair;
import org.graalvm.polyglot.Value;

public class InMemoryPath<V, E> implements Path<V, E> {
  private final Map<E, VertexPair<V>> indexedVertices = new HashMap<E, VertexPair<V>>();
  private final Map<VertexPair<V>, E> indexedEdges = new HashMap<VertexPair<V>, E>();
  private final Map<V, V> successors = new HashMap<V, V>();
  private final LinkedList<E> edges = new LinkedList<E>();
  private final LinkedList<V> vertices = new LinkedList<V>();
  private static final long serialVersionUID = -7248626031673230570L;
  private static Value clz =
      ContextInitializer.getPythonClass("/model/InMemoryPath.py", "InMemoryPath");
  private Value obj;

  public InMemoryPath(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return format("InMemoryPath [vertices=%s, edges=%s]", vertices, edges);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // final int prime = 31;
    // return hash(1, prime, edges, source, target, vertices);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(Object obj) {
    //
    // if (this == obj) {
    // return true;
    // }
    //
    // if (obj == null || getClass() != obj.getClass()) {
    // return false;
    // }
    //
    // @SuppressWarnings("unchecked") // test against any Path typed instance
    // InMemoryPath<Object, Object> other = (InMemoryPath<Object, Object>) obj;
    // return eq(source, other.getSource())
    // && eq(target, other.getTarget())
    // && eq(vertices, other.getVertices0())
    // && eq(edges, other.getEdges());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public VertexPair<V> getVertices1(E e) {
    //
    // return indexedVertices.get(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices1", e).as(VertexPair.class);
  }

  public Iterable<V> getVertices0() {
    //
    // return unmodifiableList(vertices);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices0").as(Iterable.class);
  }

  public V getTarget() {
    //
    // return target;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTarget").as(V.class);
  }

  public V getSource() {
    //
    // return source;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSource").as(V.class);
  }

  public int getSize() {
    //
    // return edges.size();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSize").as(int.class);
  }

  public int getOrder() {
    //
    // return vertices.size();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOrder").as(int.class);
  }

  public Iterable<E> getEdges() {
    //
    // return unmodifiableList(edges);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdges").as(Iterable.class);
  }

  public E getEdge(V source, V target) {
    //
    // return indexedEdges.get(new VertexPair<V>(source, target));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdge", source, target).as(E.class);
  }

  public int getDegree(V v) {
    //
    // v = checkNotNull(v, "Impossible to get the degree of a null vertex");
    // checkArgument(
    // successors.containsKey(v),
    // "Impossible to get the degree of input vertex; %s not contained in this path",
    // v);
    //
    // if (source.equals(v) || target.equals(v)) {
    // return 1;
    // }
    //
    // return 2;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDegree", v).as(int.class);
  }

  public Iterable<V> getConnectedVertices(V v) {
    //
    // v = checkNotNull(v, "Impossible to get the degree of a null vertex");
    //
    // if (target.equals(v)) {
    // return null;
    // }
    //
    // checkArgument(
    // successors.containsKey(v),
    // "Impossible to get the degree of input vertex; %s not contained in this path",
    // v);
    //
    // @SuppressWarnings("unchecked") // type driven by input type
    // List<V> connected = asList(successors.get(v));
    // return connected;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getConnectedVertices", v).as(Iterable.class);
  }

  public boolean containsVertex(V v) {
    //
    // return vertices.contains(v);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsVertex", v).as(boolean.class);
  }

  public boolean containsEdge(E e) {
    //
    // return edges.contains(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsEdge", e).as(boolean.class);
  }

  public void addConnectionInTail(V head, E edge, V tail) {
    //
    // vertices.addLast(head);
    // edges.addLast(edge);
    //
    // if (target.equals(tail)) {
    // vertices.addLast(tail);
    // }
    //
    // addConnection(head, edge, tail);
    //

    obj.invokeMember("addConnectionInTail", head, edge, tail);
  }

  public void addConnectionInHead(V head, E edge, V tail) {
    //
    // if (target.equals(tail)) {
    // vertices.addFirst(tail);
    // }
    //
    // vertices.addFirst(head);
    // edges.addFirst(edge);
    //
    // addConnection(head, edge, tail);
    //

    obj.invokeMember("addConnectionInHead", head, edge, tail);
  }

  public InMemoryPath(V start, V target) {
    //
    // this.source = checkNotNull(start, "Path source cannot be null");
    // this.target = checkNotNull(target, "Path target cannot be null");
    //

    this.obj = clz.invokeMember("__init__", start, target);
  }

  private void addConnection(V head, E edge, V tail) {
    //
    // successors.put(head, tail);
    //
    // VertexPair<V> vertexPair = new VertexPair<V>(head, tail);
    // indexedEdges.put(vertexPair, edge);
    // indexedVertices.put(edge, vertexPair);
    //

    obj.invokeMember("addConnection", head, edge, tail);
  }
}
