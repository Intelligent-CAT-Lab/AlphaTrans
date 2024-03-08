package org.apache.commons.graph.collections;

import static java.lang.Math.log;
import static java.lang.Math.sqrt;

import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Queue;
import java.util.Set;
import org.apache.commons.graph.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class FibonacciHeap<E> implements Queue<E> {
  private int markedNodes = 0;
  private int trees = 0;
  private int size = 0;
  private final Set<E> elementsIndex = new HashSet<E>();
  private static final double LOG_PHI = log((1 + sqrt(5)) / 2);
  private static Value clz =
      ContextInitializer.getPythonClass("/collections/FibonacciHeap.py", "FibonacciHeap");
  private Value obj;

  public FibonacciHeap(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // if (minimumNode == null) {
    // return "FibonacciHeap=[]";
    // }
    //
    // Stack<FibonacciHeapNode<E>> stack = new Stack<FibonacciHeapNode<E>>();
    // stack.push(minimumNode);
    //
    // StringBuilder buf = new StringBuilder("FibonacciHeap=[");
    //
    // while (!stack.empty()) {
    // FibonacciHeapNode<E> curr = stack.pop();
    // buf.append(curr);
    // buf.append(", ");
    //
    // if (curr.getChild() != null) {
    // stack.push(curr.getChild());
    // }
    //
    // FibonacciHeapNode<E> start = curr;
    // curr = curr.getRight();
    //
    // while (curr != start) {
    // buf.append(curr);
    // buf.append(", ");
    //
    // if (curr.getChild() != null) {
    // stack.push(curr.getChild());
    // }
    //
    // curr = curr.getRight();
    // }
    // }
    //
    // buf.append(']');
    //
    // return buf.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public <T> T[] toArray1(T[] a) {
    //
    // throw new UnsupportedOperationException();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toArray1", a).as(T[].class);
  }

  public <T> T[] toArray(T[] a) {
    //
    // return toArray1(a);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toArray", a).as(T[].class);
  }

  public Object[] toArray0() {
    //
    // throw new UnsupportedOperationException();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toArray0").as(Object[].class);
  }

  public Object[] toArray() {
    //
    // return toArray0();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toArray").as(Object[].class);
  }

  public int size() {
    //
    // return size;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("size").as(int.class);
  }

  public boolean retainAll(Collection<?> c) {
    //
    // throw new UnsupportedOperationException();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("retainAll", c).as(boolean.class);
  }

  public boolean removeAll(Collection<?> c) {
    //
    // throw new UnsupportedOperationException();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("removeAll", c).as(boolean.class);
  }

  public boolean remove1(Object o) {
    //
    // throw new UnsupportedOperationException();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("remove1", o).as(boolean.class);
  }

  public boolean remove(Object o) {
    //
    // return remove1(o);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("remove", o).as(boolean.class);
  }

  public E remove0() {
    //
    //
    // if (isEmpty()) {
    // throw new NoSuchElementException();
    // }
    //
    // return poll();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("remove0").as(E.class);
  }

  public E remove() {
    //
    // return remove0();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("remove").as(E.class);
  }

  public int potential() {
    //
    // return trees + 2 * markedNodes;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("potential").as(int.class);
  }

  public E poll() {
    //
    // if (isEmpty()) {
    // return null;
    // }
    //
    // FibonacciHeapNode<E> z = minimumNode;
    // int numOfKids = z.getDegree();
    //
    // FibonacciHeapNode<E> x = z.getChild();
    // FibonacciHeapNode<E> tempRight;
    //
    // while (numOfKids > 0) {
    // tempRight = x.getRight();
    //
    // moveToRoot(x);
    //
    // x.setParent(null);
    //
    // x = tempRight;
    // numOfKids--;
    // }
    //
    // z.getLeft().setRight(z.getRight());
    // z.getRight().setLeft(z.getLeft());
    //
    // if (z == z.getRight()) {
    // minimumNode = null;
    // } else {
    // minimumNode = z.getRight();
    // consolidate();
    // }
    //
    // size--;
    //
    // E minimum = z.getElement();
    // elementsIndex.remove(minimum);
    // return minimum;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("poll").as(E.class);
  }

  public E peek() {
    //
    // if (isEmpty()) {
    // return null;
    // }
    //
    // return minimumNode.getElement();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("peek").as(E.class);
  }

  public boolean offer(E e) {
    //
    // return add(e);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("offer", e).as(boolean.class);
  }

  public Iterator<E> iterator() {
    //
    // throw new UnsupportedOperationException();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("iterator").as(Iterator.class);
  }

  public boolean isEmpty() {
    //
    // return minimumNode == null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEmpty").as(boolean.class);
  }

  public E element() {
    //
    // if (isEmpty()) {
    // throw new NoSuchElementException();
    // }
    // return peek();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("element").as(E.class);
  }

  public boolean containsAll(Collection<?> c) {
    //
    // if (c == null) {
    // return false;
    // }
    //
    // for (Object o : c) {
    // if (!contains(o)) {
    // return false;
    // }
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsAll", c).as(boolean.class);
  }

  public boolean contains(Object o) {
    //
    // if (o == null) {
    // return false;
    // }
    //
    // return elementsIndex.contains(o);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("contains", o).as(boolean.class);
  }

  public void clear() {
    //
    // minimumNode = null;
    // size = 0;
    // trees = 0;
    // markedNodes = 0;
    // elementsIndex.clear();
    //

    obj.invokeMember("clear");
  }

  public boolean addAll(Collection<? extends E> c) {
    //
    // for (E element : c) {
    // add(element);
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addAll", c).as(boolean.class);
  }

  public boolean add(E e) {
    //
    // checkNotNull(e, "Null elements not allowed in this FibonacciHeap implementation.");
    //
    // FibonacciHeapNode<E> node = new FibonacciHeapNode<E>(e);
    //
    // moveToRoot(node);
    //
    // size++;
    //
    // elementsIndex.add(e);
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("add", e).as(boolean.class);
  }

  public static FibonacciHeap FibonacciHeap1() {
    //
    // return new FibonacciHeap(null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("FibonacciHeap1").as(FibonacciHeap.class);
  }

  public FibonacciHeap(/* @Nullable */ Comparator<? super E> comparator) {
    //
    // this.comparator = comparator;
    //

    this.obj = clz.invokeMember("__init__", comparator);
  }

  private void moveToRoot(FibonacciHeapNode<E> node) {
    //
    // if (isEmpty()) {
    // minimumNode = node;
    // } else {
    // node.getLeft().setRight(node.getRight());
    // node.getRight().setLeft(node.getLeft());
    //
    // node.setLeft(minimumNode);
    // node.setRight(minimumNode.getRight());
    // minimumNode.setRight(node);
    // node.getRight().setLeft(node);
    //
    // if (compare(node, minimumNode) < 0) {
    // minimumNode = node;
    // }
    // }
    //

    obj.invokeMember("moveToRoot", node);
  }

  private void link(FibonacciHeapNode<E> y, FibonacciHeapNode<E> x) {
    //
    // y.getLeft().setRight(y.getRight());
    // y.getRight().setLeft(y.getLeft());
    //
    // y.setParent(x);
    //
    // if (x.getChild() == null) {
    // x.setChild(y);
    // y.setRight(y);
    // y.setLeft(y);
    // } else {
    // y.setLeft(x.getChild());
    // y.setRight(x.getChild().getRight());
    // x.getChild().setRight(y);
    // y.getRight().setLeft(y);
    // }
    //
    // x.incraeseDegree();
    //
    // y.setMarked(false);
    // markedNodes++;
    //

    obj.invokeMember("link", y, x);
  }

  private void cut(FibonacciHeapNode<E> x, FibonacciHeapNode<E> y) {
    //
    // moveToRoot(x);
    //
    // y.decraeseDegree();
    // x.setParent(null);
    //
    // x.setMarked(false);
    // markedNodes--;
    //

    obj.invokeMember("cut", x, y);
  }

  private void consolidate() {
    //
    // if (isEmpty()) {
    // return;
    // }
    //
    // int arraySize = ((int) floor(log(size) / LOG_PHI));
    //
    // List<FibonacciHeapNode<E>> nodeSequence = new ArrayList<FibonacciHeapNode<E>>(arraySize);
    // for (int i = 0; i < arraySize; i++) {
    // nodeSequence.add(i, null);
    // }
    //
    // int numRoots = 0;
    //
    // FibonacciHeapNode<E> x = minimumNode;
    //
    // if (x != null) {
    // numRoots++;
    // x = x.getRight();
    //
    // while (x != minimumNode) {
    // numRoots++;
    // x = x.getRight();
    // }
    // }
    //
    // while (numRoots > 0) {
    // int degree = x.getDegree();
    // FibonacciHeapNode<E> next = x.getRight();
    //
    // while (nodeSequence.get(degree) != null) {
    // FibonacciHeapNode<E> y = nodeSequence.get(degree);
    //
    // if (compare(x, y) > 0) {
    // FibonacciHeapNode<E> pointer = y;
    // y = x;
    // x = pointer;
    // }
    //
    // link(y, x);
    //
    // nodeSequence.set(degree, null);
    //
    // degree++;
    // }
    //
    // nodeSequence.set(degree, x);
    //
    // x = next;
    // numRoots--;
    // }
    //
    // minimumNode = null;
    //
    // for (FibonacciHeapNode<E> pointer : nodeSequence) {
    // if (pointer == null) {
    // continue;
    // }
    // if (minimumNode == null) {
    // minimumNode = pointer;
    // }
    //
    // if (minimumNode != null) {
    // moveToRoot(pointer);
    // }
    // }
    //

    obj.invokeMember("consolidate");
  }

  private int compare(FibonacciHeapNode<E> o1, FibonacciHeapNode<E> o2) {
    //
    // if (comparator != null) {
    // return comparator.compare(o1.getElement(), o2.getElement());
    // }
    // @SuppressWarnings("unchecked") // it will throw a ClassCastException at runtime
    // Comparable<? super E> o1Comparable = (Comparable<? super E>) o1.getElement();
    // return o1Comparable.compareTo(o2.getElement());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compare", o1, o2).as(int.class);
  }

  private void cascadingCut(FibonacciHeapNode<E> y) {
    //
    // FibonacciHeapNode<E> z = y.getParent();
    //
    // if (z != null) {
    // if (!y.isMarked()) {
    // y.setMarked(true);
    // markedNodes++;
    // } else {
    // cut(y, z);
    // cascadingCut(z);
    // }
    // }
    //

    obj.invokeMember("cascadingCut", y);
  }
}
