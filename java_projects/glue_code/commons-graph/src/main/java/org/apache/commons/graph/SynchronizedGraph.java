package org.apache.commons.graph;

import org.graalvm.polyglot.Value;

class SynchronizedGraph<V, E> implements Graph<V, E> {
  private static final long serialVersionUID = 4472623111635514693L;
  private static Value clz =
      ContextInitializer.getPythonClass("/SynchronizedGraph.py", "SynchronizedGraph");
  private Value obj;

  public SynchronizedGraph(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return g.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // final int prime = 31;
    // int result = 1;
    // result = prime * result + ((g == null) ? 0 : g.hashCode());
    // result = prime * result + ((lock == null) ? 0 : lock.hashCode());
    // return result;
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
    // @SuppressWarnings("unchecked")
    // SynchronizedGraph<Object, Object> other = (SynchronizedGraph<Object, Object>) obj;
    // return eq(g, other.g);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public VertexPair<V> getVertices1(E e) {
    //
    // synchronized (lock) {
    // return g.getVertices1(e);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices1", e).as(VertexPair.class);
  }

  public Iterable<V> getVertices0() {
    //
    // synchronized (lock) {
    // return g.getVertices0();
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVertices0").as(Iterable.class);
  }

  public int getSize() {
    //
    // synchronized (lock) {
    // return g.getSize();
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSize").as(int.class);
  }

  public int getOrder() {
    //
    // synchronized (lock) {
    // return g.getOrder();
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOrder").as(int.class);
  }

  public Iterable<E> getEdges() {
    //
    // synchronized (lock) {
    // return g.getEdges();
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdges").as(Iterable.class);
  }

  public E getEdge(V source, V target) {
    //
    // synchronized (lock) {
    // return g.getEdge(source, target);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEdge", source, target).as(E.class);
  }

  public int getDegree(V v) {
    //
    // synchronized (lock) {
    // return g.getDegree(v);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDegree", v).as(int.class);
  }

  public Iterable<V> getConnectedVertices(V v) {
    //
    // synchronized (lock) {
    // return g.getConnectedVertices(v);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getConnectedVertices", v).as(Iterable.class);
  }

  public boolean containsVertex(V v) {
    //
    // synchronized (lock) {
    // return g.containsVertex(v);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsVertex", v).as(boolean.class);
  }

  public boolean containsEdge(E e) {
    //
    // synchronized (lock) {
    // return g.containsEdge(e);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsEdge", e).as(boolean.class);
  }

  public SynchronizedGraph(Graph<V, E> g) {
    //
    // this.g = g;
    // this.lock = this;
    //

    this.obj = clz.invokeMember("__init__", g);
  }
}
