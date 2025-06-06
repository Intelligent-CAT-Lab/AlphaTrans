package org.apache.commons.graph.collections;


/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


import static org.apache.commons.graph.utils.Assertions.checkNotNull;

import static java.lang.Math.floor;
import static java.lang.Math.log;
import static java.lang.Math.sqrt;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

/**
 * A Fibonacci Heap implementation based on <a
 * href="https://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap21.htm">University of Science
 * and Technology of China</a> lesson.
 *
 * <p><b>Note 1</b>: this class is NOT thread safe!
 *
 * <p><b>Note 2</b>: this class doesn't support {@code null} values
 *
 * @param <E> the type of elements held in this collection.
 */
public final class FibonacciHeap<E> implements Queue<E> {

    /** The <i>Phi</i> constant value. */
    private static final double LOG_PHI = log((1 + sqrt(5)) / 2);

    /** A simple index of stored elements. */
    private final Set<E> elementsIndex = new HashSet<E>();

    /** The comparator, or null if priority queue uses elements' natural ordering. */
    private final Comparator<? super E> comparator;

    /** The number of nodes currently in {@code H} is kept in {@code n[H]}. */
    private int size = 0;

    /** {@code t(H)} the number of trees in the root list. */
    private int trees = 0;

    /** {@code m(H)} the number of marked nodes in {@code H}. */
    private int markedNodes = 0;

    /** The root of the tree containing a minimum key {@code min[H]}. */
    private FibonacciHeapNode<E> minimumNode;

    /**
     * Creates a {@link FibonacciHeap} that orders its elements according to their natural ordering.
     */
    public FibonacciHeap(/* @Nullable */ Comparator<? super E> comparator) {
        this.comparator = comparator;
    }

    public static FibonacciHeap FibonacciHeap1() {
        return new FibonacciHeap(null);
    }

    /**
     * Creates a {@link FibonacciHeap} that orders its elements according to the specified
     * comparator.
     *
     * @param comparator the comparator that will be used to order this queue. If null, the natural
     *     ordering of the elements will be used.
     */

    /**
     * {@inheritDoc}
     *
     * <pre>FIB-HEAP-INSERT(H, x)
     * 1  degree[x] &larr; 0
     * 2  p[x] &larr; NIL
     * 3  child[x] &larr; NIL
     * 4  left[x] &larr; x
     * 5  right[x] &larr; x
     * 6  mark[x] &larr; FALSE
     * 7  concatenate the root list containing x with root list H
     * 8  if min[H] = NIL or key[x] &lt; key[min[H]]
     * 9     then min[H] &larr; x
     * 10  n[H] &larr; n[H] + 1</pre>
     */
    public boolean add(E e) {
        checkNotNull(e, "Null elements not allowed in this FibonacciHeap implementation.");

        FibonacciHeapNode<E> node = new FibonacciHeapNode<E>(e);

        moveToRoot(node);

        size++;

        elementsIndex.add(e);

        return true;
    }

    /** {@inheritDoc} */
    public boolean addAll(Collection<? extends E> c) {
        for (E element : c) {
            add(element);
        }

        return true;
    }

    /**
     * Implements the {@code CASCADING-CUT(H,y)} function.
     *
     * <pre>CASCADING-CUT(H,y)
     * 1  z &larr; p[y]
     * 2  if z &ne; NIL
     * 3     then if mark[y] = FALSE
     * 4             then mark[y] &larr; TRUE
     * 5             else CUT(H,y,z)
     * 6                  CASCADING-CUT(H,z)</pre>
     *
     * @param y the target node to apply CASCADING-CUT
     */
    private void cascadingCut(FibonacciHeapNode<E> y) {
        FibonacciHeapNode<E> z = y.getParent();

        if (z != null) {
            if (!y.isMarked()) {
                y.setMarked(true);
                markedNodes++;
            } else {
                cut(y, z);
                cascadingCut(z);
            }
        }
    }

    /** {@inheritDoc} */
    public void clear() {
        minimumNode = null;
        size = 0;
        trees = 0;
        markedNodes = 0;
        elementsIndex.clear();
    }

    /**
     * Compare the given objects according to to the specified comparator if not null, according to
     * their natural ordering otherwise.
     *
     * @param o1 the first {@link FibonacciHeap} node to be compared
     * @param o2 the second {@link FibonacciHeap} node to be compared
     * @return a negative integer, zero, or a positive integer as the first argument is less than,
     *     equal to, or greater than the second
     */
    private int compare(FibonacciHeapNode<E> o1, FibonacciHeapNode<E> o2) {
        if (comparator != null) {
            return comparator.compare(o1.getElement(), o2.getElement());
        }
        @SuppressWarnings("unchecked") // it will throw a ClassCastException at runtime
        Comparable<? super E> o1Comparable = (Comparable<? super E>) o1.getElement();
        return o1Comparable.compareTo(o2.getElement());
    }

    /**
     * Implements the {@code CONSOLIDATE(H)} function.
     *
     * <pre>CONSOLIDATE(H)
     * 1 for i &larr; 0 to D(n[H])
     * 2      do A[i] &larr; NIL
     * 3 for each node w in the root list of H
     * 4      do x &larr; w
     * 5         d &larr; degree[x]
     * 6         while A[d] &ne; NIL
     * 7            do y &larr; A[d]
     * 8               if key[x] &gt; key[y]
     * 9                  then exchange x &harr; y
     * 10                FIB-HEAP-LINK(H,y,x)
     * 11                A[d] &larr; NIL
     * 12                d &larr; d + 1
     * 13         A[d] &larr; x
     * 14 min[H] &larr; NIL
     * 15 for i &larr; 0 to D(n[H])
     * 16      do if A[i] &ne; NIL
     * 17            then add A[i] to the root list of H
     * 18                 if min[H] = NIL or key[A[i]] &le; key[min[H]]
     * 19                    then min[H] &larr; A[i]</pre>
     */
    private void consolidate() {
        if (isEmpty()) {
            return;
        }

        int arraySize = ((int) floor(log(size) / LOG_PHI));

        List<FibonacciHeapNode<E>> nodeSequence = new ArrayList<FibonacciHeapNode<E>>(arraySize);
        for (int i = 0; i < arraySize; i++) {
            nodeSequence.add(i, null);
        }

        int numRoots = 0;

        FibonacciHeapNode<E> x = minimumNode;

        if (x != null) {
            numRoots++;
            x = x.getRight();

            while (x != minimumNode) {
                numRoots++;
                x = x.getRight();
            }
        }

        while (numRoots > 0) {
            int degree = x.getDegree();
            FibonacciHeapNode<E> next = x.getRight();

            while (nodeSequence.get(degree) != null) {
                FibonacciHeapNode<E> y = nodeSequence.get(degree);

                if (compare(x, y) > 0) {
                    FibonacciHeapNode<E> pointer = y;
                    y = x;
                    x = pointer;
                }

                link(y, x);

                nodeSequence.set(degree, null);

                degree++;
            }

            nodeSequence.set(degree, x);

            x = next;
            numRoots--;
        }

        minimumNode = null;

        for (FibonacciHeapNode<E> pointer : nodeSequence) {
            if (pointer == null) {
                continue;
            }
            if (minimumNode == null) {
                minimumNode = pointer;
            }

            if (minimumNode != null) {
                moveToRoot(pointer);
            }
        }
    }

    /** {@inheritDoc} */
    public boolean contains(Object o) {
        if (o == null) {
            return false;
        }

        return elementsIndex.contains(o);
    }

    /** {@inheritDoc} */
    public boolean containsAll(Collection<?> c) {
        if (c == null) {
            return false;
        }

        for (Object o : c) {
            if (!contains(o)) {
                return false;
            }
        }

        return true;
    }

    /**
     * Implements the {@code CUT(H,x,y)} function.
     *
     * <pre>CUT(H,x,y)
     * 1  remove x from the child list of y, decrementing degree[y]
     * 2  add x to the root list of H
     * 3  p[x] &larr; NIL
     * 4  mark[x] &larr; FALSE</pre>
     *
     * @param x the node has to be removed from {@code y} children
     * @param y the node has to be updated
     */
    private void cut(FibonacciHeapNode<E> x, FibonacciHeapNode<E> y) {
        moveToRoot(x);

        y.decraeseDegree();
        x.setParent(null);

        x.setMarked(false);
        markedNodes--;
    }

    /** {@inheritDoc} */
    public E element() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        return peek();
    }

    /** {@inheritDoc} */
    public boolean isEmpty() {
        return minimumNode == null;
    }

    /** {@inheritDoc} */
    public Iterator<E> iterator() {
        throw new UnsupportedOperationException();
    }

    /**
     * Implements the {@code FIB-HEAP-LINK(H, y, x)} function.
     *
     * <pre>FIB-HEAP-LINK(H, y, x)
     * 1  remove y from the root list of H
     * 2  make y a child of x, incrementing degree[x]
     * 3  mark[y]  FALSE</pre>
     *
     * @param y the node has to be removed from the root list
     * @param x the node has to to become fater of {@code y}
     */
    private void link(FibonacciHeapNode<E> y, FibonacciHeapNode<E> x) {
        y.getLeft().setRight(y.getRight());
        y.getRight().setLeft(y.getLeft());

        y.setParent(x);

        if (x.getChild() == null) {
            x.setChild(y);
            y.setRight(y);
            y.setLeft(y);
        } else {
            y.setLeft(x.getChild());
            y.setRight(x.getChild().getRight());
            x.getChild().setRight(y);
            y.getRight().setLeft(y);
        }

        x.incraeseDegree();

        y.setMarked(false);
        markedNodes++;
    }

    /**
     * Moves the target node in the {@code H} root nodes.
     *
     * @param node the node has to be moved in the {@code H} root nodes
     * @see #add(Object)
     * @see #consolidate()
     * @see #cut(FibonacciHeapNode, FibonacciHeapNode)
     */
    private void moveToRoot(FibonacciHeapNode<E> node) {
        if (isEmpty()) {
            minimumNode = node;
        } else {
            node.getLeft().setRight(node.getRight());
            node.getRight().setLeft(node.getLeft());

            node.setLeft(minimumNode);
            node.setRight(minimumNode.getRight());
            minimumNode.setRight(node);
            node.getRight().setLeft(node);

            if (compare(node, minimumNode) < 0) {
                minimumNode = node;
            }
        }
    }

    /** {@inheritDoc} */
    public boolean offer(E e) {
        return add(e);
    }

    /** {@inheritDoc} */
    public E peek() {
        if (isEmpty()) {
            return null;
        }

        return minimumNode.getElement();
    }

    /**
     * {@inheritDoc}
     *
     * <pre>FIB-HEAP-EXTRACT-MIN(H)
     * 1  z &larr; min[H]
     * 2  if z &ne; NIL
     * 3      then for each child x of z
     * 4               do add x to the root list of H
     * 5                  p[x] &larr; NIL
     * 6           remove z from the root list of H
     * 7           if z = right[z]
     * 8              then min[H] &larr; NIL
     * 9              else min[H] &larr; right[z]
     * 10                   CONSOLIDATE(H)
     * 11           n[H] &larr; n[H] - 1
     * 12  return z</pre>
     */
    public E poll() {
        if (isEmpty()) {
            return null;
        }

        FibonacciHeapNode<E> z = minimumNode;
        int numOfKids = z.getDegree();

        FibonacciHeapNode<E> x = z.getChild();
        FibonacciHeapNode<E> tempRight;

        while (numOfKids > 0) {
            tempRight = x.getRight();

            moveToRoot(x);

            x.setParent(null);

            x = tempRight;
            numOfKids--;
        }

        z.getLeft().setRight(z.getRight());
        z.getRight().setLeft(z.getLeft());

        if (z == z.getRight()) {
            minimumNode = null;
        } else {
            minimumNode = z.getRight();
            consolidate();
        }

        size--;

        E minimum = z.getElement();
        elementsIndex.remove(minimum);
        return minimum;
    }

    /**
     * The potential of Fibonacci heap {@code H} is then defined by {@code t(H) + 2m(H)}.
     *
     * @return The potential of this Fibonacci heap.
     */
    public int potential() {
        return trees + 2 * markedNodes;
    }

    public E remove() {
        return remove0();
    }

    /** {@inheritDoc} */
    public E remove0() {

        if (isEmpty()) {
            throw new NoSuchElementException();
        }

        return poll();
    }

    public boolean remove(Object o) {
        return remove1(o);
    }

    /** {@inheritDoc} */
    public boolean remove1(Object o) {
        throw new UnsupportedOperationException();
    }

    /** {@inheritDoc} */
    public boolean removeAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    /** {@inheritDoc} */
    public boolean retainAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    /** {@inheritDoc} */
    public int size() {
        return size;
    }

    public Object[] toArray() {
        return toArray0();
    }

    /** {@inheritDoc} */
    public Object[] toArray0() {
        throw new UnsupportedOperationException();
    }

    public <T> T[] toArray(T[] a) {
        return toArray1(a);
    }

    /** {@inheritDoc} */
    public <T> T[] toArray1(T[] a) {
        throw new UnsupportedOperationException();
    }

    /**
     * Creates a String representation of this Fibonacci heap.
     *
     * @return String of this.
     */
    public String toString() {
        if (minimumNode == null) {
            return "FibonacciHeap=[]";
        }

        Stack<FibonacciHeapNode<E>> stack = new Stack<FibonacciHeapNode<E>>();
        stack.push(minimumNode);

        StringBuilder buf = new StringBuilder("FibonacciHeap=[");

        while (!stack.empty()) {
            FibonacciHeapNode<E> curr = stack.pop();
            buf.append(curr);
            buf.append(", ");

            if (curr.getChild() != null) {
                stack.push(curr.getChild());
            }

            FibonacciHeapNode<E> start = curr;
            curr = curr.getRight();

            while (curr != start) {
                buf.append(curr);
                buf.append(", ");

                if (curr.getChild() != null) {
                    stack.push(curr.getChild());
                }

                curr = curr.getRight();
            }
        }

        buf.append(']');

        return buf.toString();
    }
}
