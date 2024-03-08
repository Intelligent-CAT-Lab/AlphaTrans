package org.apache.commons.graph;

import java.io.Serializable;
import org.graalvm.polyglot.Value;

public final class VertexPair<V> implements Serializable {
  private static final long serialVersionUID = 2333503391707156055L;
  private static Value clz = ContextInitializer.getPythonClass("/VertexPair.py", "VertexPair");
  private Value obj;

  public VertexPair(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return format("[head=%s, tail=%s]", head, tail);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // final int prime = 31;
    // return hash(1, prime, head, tail);
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
    // @SuppressWarnings("unchecked") // equals() invoked against only same VertexPair type
    // VertexPair<V> other = (VertexPair<V>) obj;
    // return eq(head, other.getHead()) && eq(tail, other.getTail());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public V getTail() {
    //
    // return tail;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTail").as(V.class);
  }

  public V getHead() {
    //
    // return head;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHead").as(V.class);
  }

  public VertexPair(V head, V tail) {
    //
    // this.head = checkNotNull(head, "Impossible to construct a Vertex with a null head");
    // this.tail = checkNotNull(tail, "Impossible to construct a Vertex with a null tail");
    //

    this.obj = clz.invokeMember("__init__", head, tail);
  }
}
