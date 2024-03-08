package org.apache.commons.graph.collections;

import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

final class FibonacciHeapNode<E> {
  private FibonacciHeapNode<E> right = this;
  private FibonacciHeapNode<E> left = this;
  private static Value clz =
      ContextInitializer.getPythonClass("/collections/FibonacciHeapNode.py", "FibonacciHeapNode");
  private Value obj;

  public FibonacciHeapNode(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return element.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public void setRight(FibonacciHeapNode<E> right) {
    //
    // this.right = right;
    //

    obj.invokeMember("setRight", right);
  }

  public void setParent(FibonacciHeapNode<E> parent) {
    //
    // this.parent = parent;
    //

    obj.invokeMember("setParent", parent);
  }

  public void setMarked(boolean marked) {
    //
    // this.marked = marked;
    //

    obj.invokeMember("setMarked", marked);
  }

  public void setLeft(FibonacciHeapNode<E> left) {
    //
    // this.left = left;
    //

    obj.invokeMember("setLeft", left);
  }

  public void setChild(FibonacciHeapNode<E> child) {
    //
    // this.child = child;
    //

    obj.invokeMember("setChild", child);
  }

  public boolean isMarked() {
    //
    // return marked;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isMarked").as(boolean.class);
  }

  public void incraeseDegree() {
    //
    // degree++;
    //

    obj.invokeMember("incraeseDegree");
  }

  public FibonacciHeapNode<E> getRight() {
    //
    // return right;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRight").as(FibonacciHeapNode.class);
  }

  public FibonacciHeapNode<E> getParent() {
    //
    // return parent;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParent").as(FibonacciHeapNode.class);
  }

  public FibonacciHeapNode<E> getLeft() {
    //
    // return left;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLeft").as(FibonacciHeapNode.class);
  }

  public E getElement() {
    //
    // return element;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getElement").as(E.class);
  }

  public int getDegree() {
    //
    // return degree;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDegree").as(int.class);
  }

  public FibonacciHeapNode<E> getChild() {
    //
    // return child;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getChild").as(FibonacciHeapNode.class);
  }

  public void decraeseDegree() {
    //
    // degree--;
    //

    obj.invokeMember("decraeseDegree");
  }

  public FibonacciHeapNode(E element) {
    //
    // degree = 0;
    // setParent(null);
    // setChild(null);
    // setLeft(this);
    // setRight(this);
    // setMarked(false);
    //
    // this.element = element;
    //

    this.obj = clz.invokeMember("__init__", element);
  }
}
