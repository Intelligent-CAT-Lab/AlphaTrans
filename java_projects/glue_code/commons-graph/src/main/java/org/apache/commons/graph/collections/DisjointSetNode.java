package org.apache.commons.graph.collections;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

final class DisjointSetNode<E> implements Comparable<DisjointSetNode<E>> {
  private Integer rank = 0;
  private DisjointSetNode<E> parent = this;
  private static Value clz =
      ContextInitializer.getPythonClass("/collections/DisjointSetNode.py", "DisjointSetNode");
  private Value obj;

  public DisjointSetNode(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setRank(int rank) {
    //
    // this.rank = rank;
    //

    obj.invokeMember("setRank", rank);
  }

  public void setParent(DisjointSetNode<E> parent) {
    //
    // this.parent = parent;
    //

    obj.invokeMember("setParent", parent);
  }

  public void increaseRank() {
    //
    // rank++;
    //

    obj.invokeMember("increaseRank");
  }

  public Integer getRank() {
    //
    // return rank;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRank").as(Integer.class);
  }

  public DisjointSetNode<E> getParent() {
    //
    // return parent;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParent").as(DisjointSetNode.class);
  }

  public E getElement() {
    //
    // return element;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getElement").as(E.class);
  }

  public int compareTo(DisjointSetNode<E> o) {
    //
    // return rank.compareTo(o.getRank());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareTo", o).as(int.class);
  }

  public DisjointSetNode(E element) {
    //
    // this.element = element;
    //

    this.obj = clz.invokeMember("__init__", element);
  }
}
