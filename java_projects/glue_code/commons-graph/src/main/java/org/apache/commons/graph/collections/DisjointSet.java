package org.apache.commons.graph.collections;

import java.util.HashMap;
import java.util.Map;
import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class DisjointSet<E> {
  private final Map<E, DisjointSetNode<E>> disjointSets = new HashMap<E, DisjointSetNode<E>>();
  private static Value clz =
      ContextInitializer.getPythonClass("/collections/DisjointSet.py", "DisjointSet");
  private Value obj;

  public DisjointSet(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void union(E e1, E e2) {
    //
    // DisjointSetNode<E> e1Root = find0(getNode(e1));
    // DisjointSetNode<E> e2Root = find0(getNode(e2));
    //
    // if (e1Root == e2Root) {
    // return;
    // }
    //
    // int comparison = e1Root.compareTo(e2Root);
    // if (comparison < 0) {
    // e1Root.setParent(e2Root);
    // } else if (comparison > 0) {
    // e2Root.setParent(e1Root);
    // } else {
    // e2Root.setParent(e1Root);
    // e1Root.increaseRank();
    // }
    //

    obj.invokeMember("union", e1, e2);
  }

  public E find1(E e) {
    //
    // DisjointSetNode<E> node = find0(getNode(e));
    //
    // if (node == node.getParent()) {
    // return node.getElement();
    // }
    //
    // node.setParent(find0(node.getParent()));
    //
    // return node.getParent().getElement();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("find1", e).as(E.class);
  }

  private DisjointSetNode<E> getNode(E e) {
    //
    // DisjointSetNode<E> node = disjointSets.get(e);
    //
    // if (node == null) {
    // node = new DisjointSetNode<E>(e);
    // disjointSets.put(e, node);
    // }
    //
    // return node;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getNode", e).as(DisjointSetNode.class);
  }

  private DisjointSetNode<E> find0(DisjointSetNode<E> node) {
    //
    // if (node == node.getParent()) {
    // return node;
    // }
    // return find0(node.getParent());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("find0", node).as(DisjointSetNode.class);
  }
}
