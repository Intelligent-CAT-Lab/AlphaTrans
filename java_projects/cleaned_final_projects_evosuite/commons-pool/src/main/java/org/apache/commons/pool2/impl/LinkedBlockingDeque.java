
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

package org.apache.commons.pool2.impl;

import java.io.Serializable;
import java.time.Duration;
import java.util.AbstractQueue;
import java.util.Collection;
import java.util.Deque;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Objects;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Condition;

/**
 * An optionally-bounded {@linkplain java.util.concurrent.BlockingDeque blocking deque} based on
 * linked nodes.
 *
 * <p>The optional capacity bound constructor argument serves as a way to prevent excessive
 * expansion. The capacity, if unspecified, is equal to {@link Integer#MAX_VALUE}. Linked nodes are
 * dynamically created upon each insertion unless this would bring the deque above capacity.
 *
 * <p>Most operations run in constant time (ignoring time spent blocking). Exceptions include {@link
 * #remove(Object) remove}, {@link #removeFirstOccurrence removeFirstOccurrence}, {@link
 * #removeLastOccurrence removeLastOccurrence}, {@link #contains contains}, {@link #iterator
 * iterator.remove()}, and the bulk operations, all of which run in linear time.
 *
 * <p>This class and its iterator implement all of the <em>optional</em> methods of the {@link
 * Collection} and {@link Iterator} interfaces.
 *
 * <p>This class is a member of the <a href="{@docRoot}/../technotes/guides/collections/index.html">
 * Java Collections Framework</a>.
 *
 * @param <E> the type of elements held in this collection
 *     <p>Note: This was copied from Apache Harmony and modified to suit the needs of Commons Pool.
 * @since 2.0
 */
class LinkedBlockingDeque<E> extends AbstractQueue<E> implements Deque<E>, Serializable {

    /*
     * Implemented as a simple doubly-linked list protected by a
     * single lock and using conditions to manage blocking.
     *
     * To implement weakly consistent iterators, it appears we need to
     * keep all Nodes GC-reachable from a predecessor dequeued Node.
     * That would cause two problems:
     * - allow a rogue Iterator to cause unbounded memory retention
     * - cause cross-generational linking of old Nodes to new Nodes if
     *   a Node was tenured while live, which generational GCs have a
     *   hard time dealing with, causing repeated major collections.
     * However, only non-deleted Nodes need to be reachable from
     * dequeued Nodes, and reachability does not necessarily have to
     * be of the kind understood by the GC.  We use the trick of
     * linking a Node that has just been dequeued to itself.  Such a
     * self-link implicitly means to jump to "first" (for next links)
     * or "last" (for prev links).
     */

    /*
     * We have "diamond" multiple interface/abstract class inheritance
     * here, and that introduces ambiguities. Often we want the
     * BlockingDeque javadoc combined with the AbstractQueue
     * implementation, so a lot of method specs are duplicated here.
     */

    /** Base class for Iterators for LinkedBlockingDeque */
    private abstract class AbstractItr implements Iterator<E> {
        /** The next node to return in next() */
        Node<E> next;

        /**
         * nextItem holds on to item fields because once we claim that an element exists in
         * hasNext(), we must return item read under lock (in advance()) even if it was in the
         * process of being removed when hasNext() was called.
         */
        E nextItem;

        /**
         * Node returned by most recent call to next. Needed by remove. Reset to null if this
         * element is deleted by a call to remove.
         */
        private Node<E> lastRet;

        /** Constructs a new iterator. Sets the initial position. */
        AbstractItr() {
            lock.lock();
            try {
                next = firstNode();
                nextItem = next == null ? null : next.item;
            } finally {
                lock.unlock();
            }
        }

        /** Advances next. */
        void advance() {
            lock.lock();
            try {
                next = succ(next);
                nextItem = next == null ? null : next.item;
            } finally {
                lock.unlock();
            }
        }

        /**
         * Obtain the first node to be returned by the iterator.
         *
         * @return first node
         */
        abstract Node<E> firstNode();

        @Override
        public boolean hasNext() {
            return next != null;
        }

        @Override
        public E next() {
            if (next == null) {
                throw new NoSuchElementException();
            }
            lastRet = next;
            final E x = nextItem;
            advance();
            return x;
        }

        /**
         * For a given node, obtain the next node to be returned by the iterator.
         *
         * @param n given node
         * @return next node
         */
        abstract Node<E> nextNode(Node<E> n);

        @Override
        public void remove() {
            final Node<E> n = lastRet;
            if (n == null) {
                throw new IllegalStateException();
            }
            lastRet = null;
            lock.lock();
            try {
                if (n.item != null) {
                    unlink(n);
                }
            } finally {
                lock.unlock();
            }
        }

        /**
         * Returns the successor node of the given non-null, but possibly previously deleted, node.
         *
         * @param n node whose successor is sought
         * @return successor node
         */
        private Node<E> succ(Node<E> n) {
            for (; ; ) {
                final Node<E> s = nextNode(n);
                if (s == null) {
                    return null;
                }
                if (s.item != null) {
                    return s;
                }
                if (s == n) {
                    return firstNode();
                }
                n = s;
            }
        }
    }

    /** Descending iterator */
    private class DescendingItr extends AbstractItr {
        @Override
        Node<E> firstNode() {
            return last;
        }

        @Override
        Node<E> nextNode(final Node<E> n) {
            return n.prev;
        }
    }

    /** Forward iterator */
    private class Itr extends AbstractItr {
        @Override
        Node<E> firstNode() {
            return first;
        }

        @Override
        Node<E> nextNode(final Node<E> n) {
            return n.next;
        }
    }

    /**
     * Doubly-linked list node class.
     *
     * @param <E> node item type
     */
    private static final class Node<E> {
        /** The item, or null if this node has been removed. */
        E item;

        /**
         * One of: - the real predecessor Node - this Node, meaning the predecessor is tail - null,
         * meaning there is no predecessor
         */
        Node<E> prev;

        /**
         * One of: - the real successor Node - this Node, meaning the successor is head - null,
         * meaning there is no successor
         */
        Node<E> next;

        /**
         * Constructs a new list node.
         *
         * @param x The list item
         * @param p Previous item
         * @param n Next item
         */
        Node(final E x, final Node<E> p, final Node<E> n) {
            item = x;
            prev = p;
            next = n;
        }
    }

    private static final long serialVersionUID = -387911632671998426L;

    /**
     * Pointer to first node. Invariant: (first == null && last == null) || (first.prev == null &&
     * first.item != null)
     */
    private transient Node<E> first; // @GuardedBy("lock")

    /**
     * Pointer to last node. Invariant: (first == null && last == null) || (last.next == null &&
     * last.item != null)
     */
    private transient Node<E> last; // @GuardedBy("lock")

    /** Number of items in the deque */
    private transient int count; // @GuardedBy("lock")

    /** Maximum number of items in the deque */
    private final int capacity;

    /** Main lock guarding all access */
    private final InterruptibleReentrantLock lock;

    /** Condition for waiting takes */
    private final Condition notEmpty;

    /** Condition for waiting puts */
    private final Condition notFull;

    /** Creates a {@code LinkedBlockingDeque} with a capacity of {@link Integer#MAX_VALUE}. */
    public static LinkedBlockingDeque LinkedBlockingDeque0() {
        return new LinkedBlockingDeque<>(0, Integer.MAX_VALUE, false, null);
    }

    /**
     * Creates a {@code LinkedBlockingDeque} with a capacity of {@link Integer#MAX_VALUE} and the
     * given fairness policy.
     *
     * @param fairness true means threads waiting on the deque should be served as if waiting in a
     *     FIFO request queue
     */
    public static LinkedBlockingDeque LinkedBlockingDeque1(final boolean fairness) {
        return new LinkedBlockingDeque<>(0, Integer.MAX_VALUE, fairness, null);
    }

    /**
     * Creates a {@code LinkedBlockingDeque} with a capacity of {@link Integer#MAX_VALUE}, initially
     * containing the elements of the given collection, added in traversal order of the collection's
     * iterator.
     *
     * @param c the collection of elements to initially contain
     * @throws NullPointerException if the specified collection or any of its elements are null
     */
    public static LinkedBlockingDeque LinkedBlockingDeque2(final Collection c) {
        return new LinkedBlockingDeque<>(0, Integer.MAX_VALUE, false, c);
    }

    /**
     * Creates a {@code LinkedBlockingDeque} with the given (fixed) capacity.
     *
     * @param capacity the capacity of this deque
     * @throws IllegalArgumentException if {@code capacity} is less than 1
     */
    public static LinkedBlockingDeque LinkedBlockingDeque3(final int capacity) {
        return new LinkedBlockingDeque<>(0, capacity, false, null);
    }

    /**
     * Creates a {@code LinkedBlockingDeque} with the given (fixed) capacity and fairness policy.
     *
     * @param capacity the capacity of this deque
     * @param fairness true means threads waiting on the deque should be served as if waiting in a
     *     FIFO request queue
     * @throws IllegalArgumentException if {@code capacity} is less than 1
     */
    public LinkedBlockingDeque(
            int constructorId,
            final int capacity,
            final boolean fairness,
            final Collection<? extends E> c) {
        if (constructorId == 0) {
            if (capacity <= 0) {
                throw new IllegalArgumentException();
            }
            this.capacity = capacity;
            lock = new InterruptibleReentrantLock(fairness);
            notEmpty = lock.newCondition();
            notFull = lock.newCondition();

            if (c != null) {
                lock.lock(); // Never contended, but necessary for visibility
                try {
                    for (final E e : c) {
                        Objects.requireNonNull(e);
                        if (!linkLast(e)) {
                            throw new IllegalStateException("Deque full");
                        }
                    }
                } finally {
                    lock.unlock();
                }
            }
        } else {
            this.capacity = capacity;
            lock = new InterruptibleReentrantLock(fairness);
            notEmpty = lock.newCondition();
            notFull = lock.newCondition();
        }
    }

    /** {@inheritDoc} */
    @Override
    public boolean add(final E e) {
        addLast(e);
        return true;
    }

    /** {@inheritDoc} */
    @Override
    public void addFirst(final E e) {
        if (!offerFirst0(e)) {
            throw new IllegalStateException("Deque full");
        }
    }

    /** {@inheritDoc} */
    @Override
    public void addLast(final E e) {
        if (!offerLast0(e)) {
            throw new IllegalStateException("Deque full");
        }
    }

    /**
     * Atomically removes all of the elements from this deque. The deque will be empty after this
     * call returns.
     */
    @Override
    public void clear() {
        lock.lock();
        try {
            for (Node<E> f = first; f != null; ) {
                f.item = null;
                final Node<E> n = f.next;
                f.prev = null;
                f.next = null;
                f = n;
            }
            first = last = null;
            count = 0;
            notFull.signalAll();
        } finally {
            lock.unlock();
        }
    }

    /**
     * Returns {@code true} if this deque contains the specified element. More formally, returns
     * {@code true} if and only if this deque contains at least one element {@code e} such that
     * {@code o.equals(e)}.
     *
     * @param o object to be checked for containment in this deque
     * @return {@code true} if this deque contains the specified element
     */
    @Override
    public boolean contains(final Object o) {
        if (o == null) {
            return false;
        }
        lock.lock();
        try {
            for (Node<E> p = first; p != null; p = p.next) {
                if (o.equals(p.item)) {
                    return true;
                }
            }
            return false;
        } finally {
            lock.unlock();
        }
    }

    /** {@inheritDoc} */
    @Override
    public Iterator<E> descendingIterator() {
        return new DescendingItr();
    }

    /**
     * Drains the queue to the specified collection.
     *
     * @param c The collection to add the elements to
     * @return number of elements added to the collection
     * @throws UnsupportedOperationException if the add operation is not supported by the specified
     *     collection
     * @throws ClassCastException if the class of the elements held by this collection prevents them
     *     from being added to the specified collection
     * @throws NullPointerException if c is null
     * @throws IllegalArgumentException if c is this instance
     */
    public int drainTo0(final Collection<? super E> c) {
        return drainTo1(c, Integer.MAX_VALUE);
    }

    /**
     * Drains no more than the specified number of elements from the queue to the specified
     * collection.
     *
     * @param c collection to add the elements to
     * @param maxElements maximum number of elements to remove from the queue
     * @return number of elements added to the collection
     * @throws UnsupportedOperationException if the add operation is not supported by the specified
     *     collection
     * @throws ClassCastException if the class of the elements held by this collection prevents them
     *     from being added to the specified collection
     * @throws NullPointerException if c is null
     * @throws IllegalArgumentException if c is this instance
     */
    public int drainTo1(final Collection<? super E> c, final int maxElements) {
        Objects.requireNonNull(c, "c");
        if (c == this) {
            throw new IllegalArgumentException();
        }
        lock.lock();
        try {
            final int n = Math.min(maxElements, count);
            for (int i = 0; i < n; i++) {
                c.add(first.item); // In this order, in case add() throws.
                unlinkFirst();
            }
            return n;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Retrieves, but does not remove, the head of the queue represented by this deque. This method
     * differs from {@link #peek peek} only in that it throws an exception if this deque is empty.
     *
     * <p>This method is equivalent to {@link #getFirst() getFirst}.
     *
     * @return the head of the queue represented by this deque
     * @throws NoSuchElementException if this deque is empty
     */
    @Override
    public E element() {
        return getFirst();
    }

    /** {@inheritDoc} */
    @Override
    public E getFirst() {
        final E x = peekFirst();
        if (x == null) {
            throw new NoSuchElementException();
        }
        return x;
    }

    /** {@inheritDoc} */
    @Override
    public E getLast() {
        final E x = peekLast();
        if (x == null) {
            throw new NoSuchElementException();
        }
        return x;
    }

    /**
     * Gets the length of the queue of threads waiting to take instances from this deque. See
     * disclaimer on accuracy in {@link
     * java.util.concurrent.locks.ReentrantLock#getWaitQueueLength(Condition)}.
     *
     * @return number of threads waiting on this deque's notEmpty condition.
     */
    public int getTakeQueueLength() {
        lock.lock();
        try {
            return lock.getWaitQueueLength(notEmpty);
        } finally {
            lock.unlock();
        }
    }

    /**
     * Returns true if there are threads waiting to take instances from this deque. See disclaimer
     * on accuracy in {@link java.util.concurrent.locks.ReentrantLock#hasWaiters(Condition)}.
     *
     * @return true if there is at least one thread waiting on this deque's notEmpty condition.
     */
    public boolean hasTakeWaiters() {
        lock.lock();
        try {
            return lock.hasWaiters(notEmpty);
        } finally {
            lock.unlock();
        }
    }

    /**
     * Interrupts the threads currently waiting to take an object from the pool. See disclaimer on
     * accuracy in {@link java.util.concurrent.locks.ReentrantLock#getWaitingThreads(Condition)}.
     */
    public void interuptTakeWaiters() {
        lock.lock();
        try {
            lock.interruptWaiters(notEmpty);
        } finally {
            lock.unlock();
        }
    }

    /**
     * Returns an iterator over the elements in this deque in proper sequence. The elements will be
     * returned in order from first (head) to last (tail). The returned {@code Iterator} is a
     * "weakly consistent" iterator that will never throw {@link
     * java.util.ConcurrentModificationException ConcurrentModificationException}, and guarantees to
     * traverse elements as they existed upon construction of the iterator, and may (but is not
     * guaranteed to) reflect any modifications subsequent to construction.
     *
     * @return an iterator over the elements in this deque in proper sequence
     */
    @Override
    public Iterator<E> iterator() {
        return new Itr();
    }

    /**
     * Links provided element as first element, or returns false if full.
     *
     * @param e The element to link as the first element.
     * @return {@code true} if successful, otherwise {@code false}
     */
    private boolean linkFirst(final E e) {
        if (count >= capacity) {
            return false;
        }
        final Node<E> f = first;
        final Node<E> x = new Node<>(e, null, f);
        first = x;
        if (last == null) {
            last = x;
        } else {
            f.prev = x;
        }
        ++count;
        notEmpty.signal();
        return true;
    }

    /**
     * Links provided element as last element, or returns false if full.
     *
     * @param e The element to link as the last element.
     * @return {@code true} if successful, otherwise {@code false}
     */
    private boolean linkLast(final E e) {
        if (count >= capacity) {
            return false;
        }
        final Node<E> l = last;
        final Node<E> x = new Node<>(e, l, null);
        last = x;
        if (first == null) {
            first = x;
        } else {
            l.next = x;
        }
        ++count;
        notEmpty.signal();
        return true;
    }

    @Override
    public boolean offer(final E e) {
        return offer0(e);
    }

    /** {@inheritDoc} */
    public boolean offer0(final E e) {
        return offerLast0(e);
    }

    /**
     * Links the provided element as the last in the queue, waiting up to the specified time to do
     * so if the queue is full.
     *
     * <p>This method is equivalent to {@link #offerLast(Object, long, TimeUnit)}
     *
     * @param e element to link
     * @param timeout length of time to wait
     * @return {@code true} if successful, otherwise {@code false}
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    boolean offer1(final E e, final Duration timeout) throws InterruptedException {
        return offerLast1(e, timeout);
    }

    /**
     * Links the provided element as the last in the queue, waiting up to the specified time to do
     * so if the queue is full.
     *
     * <p>This method is equivalent to {@link #offerLast(Object, long, TimeUnit)}
     *
     * @param e element to link
     * @param timeout length of time to wait
     * @param unit units that timeout is expressed in
     * @return {@code true} if successful, otherwise {@code false}
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    public boolean offer2(final E e, final long timeout, final TimeUnit unit)
            throws InterruptedException {
        return offerLast2(e, timeout, unit);
    }

    @Override
    public boolean offerFirst(final E e) {
        return offerFirst0(e);
    }

    /** {@inheritDoc} */
    public boolean offerFirst0(final E e) {
        Objects.requireNonNull(e, "e");
        lock.lock();
        try {
            return linkFirst(e);
        } finally {
            lock.unlock();
        }
    }

    /**
     * Links the provided element as the first in the queue, waiting up to the specified time to do
     * so if the queue is full.
     *
     * @param e element to link
     * @param timeout length of time to wait
     * @return {@code true} if successful, otherwise {@code false}
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    public boolean offerFirst1(final E e, final Duration timeout) throws InterruptedException {
        Objects.requireNonNull(e, "e");
        long nanos = timeout.toNanos();
        lock.lockInterruptibly();
        try {
            while (!linkFirst(e)) {
                if (nanos <= 0) {
                    return false;
                }
                nanos = notFull.awaitNanos(nanos);
            }
            return true;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Links the provided element as the first in the queue, waiting up to the specified time to do
     * so if the queue is full.
     *
     * @param e element to link
     * @param timeout length of time to wait
     * @param unit units that timeout is expressed in
     * @return {@code true} if successful, otherwise {@code false}
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    public boolean offerFirst2(final E e, final long timeout, final TimeUnit unit)
            throws InterruptedException {
        return offerFirst1(e, PoolImplUtils.toDuration(timeout, unit));
    }

    public boolean offerLast(final E e) {
        return offerLast0(e);
    }

    /** {@inheritDoc} */
    public boolean offerLast0(final E e) {
        Objects.requireNonNull(e, "e");
        lock.lock();
        try {
            return linkLast(e);
        } finally {
            lock.unlock();
        }
    }

    /**
     * Links the provided element as the last in the queue, waiting up to the specified time to do
     * so if the queue is full.
     *
     * @param e element to link
     * @param timeout length of time to wait
     * @return {@code true} if successful, otherwise {@code false}
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whist waiting for space
     */
    boolean offerLast1(final E e, final Duration timeout) throws InterruptedException {
        Objects.requireNonNull(e, "e");
        long nanos = timeout.toNanos();
        lock.lockInterruptibly();
        try {
            while (!linkLast(e)) {
                if (nanos <= 0) {
                    return false;
                }
                nanos = notFull.awaitNanos(nanos);
            }
            return true;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Links the provided element as the last in the queue, waiting up to the specified time to do
     * so if the queue is full.
     *
     * @param e element to link
     * @param timeout length of time to wait
     * @param unit units that timeout is expressed in
     * @return {@code true} if successful, otherwise {@code false}
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whist waiting for space
     */
    public boolean offerLast2(final E e, final long timeout, final TimeUnit unit)
            throws InterruptedException {
        return offerLast1(e, PoolImplUtils.toDuration(timeout, unit));
    }

    @Override
    public E peek() {
        return peekFirst();
    }

    @Override
    public E peekFirst() {
        lock.lock();
        try {
            return first == null ? null : first.item;
        } finally {
            lock.unlock();
        }
    }

    @Override
    public E peekLast() {
        lock.lock();
        try {
            return last == null ? null : last.item;
        } finally {
            lock.unlock();
        }
    }

    @Override
    public E poll() {
        return poll0();
    }

    public E poll0() {
        return pollFirst0();
    }

    /**
     * Unlinks the first element in the queue, waiting up to the specified time to do so if the
     * queue is empty.
     *
     * <p>This method is equivalent to {@link #pollFirst(long, TimeUnit)}.
     *
     * @param timeout length of time to wait
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    E poll1(final Duration timeout) throws InterruptedException {
        return pollFirst1(timeout);
    }

    /**
     * Unlinks the first element in the queue, waiting up to the specified time to do so if the
     * queue is empty.
     *
     * <p>This method is equivalent to {@link #pollFirst(long, TimeUnit)}.
     *
     * @param timeout length of time to wait
     * @param unit units that timeout is expressed in
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E poll2(final long timeout, final TimeUnit unit) throws InterruptedException {
        return pollFirst2(timeout, unit);
    }

    @Override
    public E pollFirst() {
        return pollFirst0();
    }

    public E pollFirst0() {
        lock.lock();
        try {
            return unlinkFirst();
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the first element in the queue, waiting up to the specified time to do so if the
     * queue is empty.
     *
     * @param timeout length of time to wait
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    E pollFirst1(final Duration timeout) throws InterruptedException {
        long nanos = timeout.toNanos();
        lock.lockInterruptibly();
        try {
            E x;
            while ((x = unlinkFirst()) == null) {
                if (nanos <= 0) {
                    return null;
                }
                nanos = notEmpty.awaitNanos(nanos);
            }
            return x;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the first element in the queue, waiting up to the specified time to do so if the
     * queue is empty.
     *
     * @param timeout length of time to wait
     * @param unit units that timeout is expressed in
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E pollFirst2(final long timeout, final TimeUnit unit) throws InterruptedException {
        return pollFirst1(PoolImplUtils.toDuration(timeout, unit));
    }

    @Override
    public E pollLast() {
        return pollLast0();
    }

    public E pollLast0() {
        lock.lock();
        try {
            return unlinkLast();
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the last element in the queue, waiting up to the specified time to do so if the queue
     * is empty.
     *
     * @param timeout length of time to wait
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E pollLast1(final Duration timeout) throws InterruptedException {
        long nanos = timeout.toNanos();
        lock.lockInterruptibly();
        try {
            E x;
            while ((x = unlinkLast()) == null) {
                if (nanos <= 0) {
                    return null;
                }
                nanos = notEmpty.awaitNanos(nanos);
            }
            return x;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the last element in the queue, waiting up to the specified time to do so if the queue
     * is empty.
     *
     * @param timeout length of time to wait
     * @param unit units that timeout is expressed in
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E pollLast2(final long timeout, final TimeUnit unit) throws InterruptedException {
        return pollLast1(PoolImplUtils.toDuration(timeout, unit));
    }

    /** {@inheritDoc} */
    @Override
    public E pop() {
        return removeFirst();
    }

    /** {@inheritDoc} */
    @Override
    public void push(final E e) {
        addFirst(e);
    }

    /**
     * Links the provided element as the last in the queue, waiting until there is space to do so if
     * the queue is full.
     *
     * <p>This method is equivalent to {@link #putLast(Object)}.
     *
     * @param e element to link
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    public void put(final E e) throws InterruptedException {
        putLast(e);
    }

    /**
     * Links the provided element as the first in the queue, waiting until there is space to do so
     * if the queue is full.
     *
     * @param e element to link
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    public void putFirst(final E e) throws InterruptedException {
        Objects.requireNonNull(e, "e");
        lock.lock();
        try {
            while (!linkFirst(e)) {
                notFull.await();
            }
        } finally {
            lock.unlock();
        }
    }

    /**
     * Links the provided element as the last in the queue, waiting until there is space to do so if
     * the queue is full.
     *
     * @param e element to link
     * @throws NullPointerException if e is null
     * @throws InterruptedException if the thread is interrupted whilst waiting for space
     */
    public void putLast(final E e) throws InterruptedException {
        Objects.requireNonNull(e, "e");
        lock.lock();
        try {
            while (!linkLast(e)) {
                notFull.await();
            }
        } finally {
            lock.unlock();
        }
    }

    /**
     * Reconstitutes this deque from a stream (that is, deserialize it).
     *
     * @param s the stream
     */
    private void readObject(final java.io.ObjectInputStream s)
            throws java.io.IOException, ClassNotFoundException {
        s.defaultReadObject();
        count = 0;
        first = null;
        last = null;
        for (; ; ) {
            @SuppressWarnings("unchecked")
            final E item = (E) s.readObject();
            if (item == null) {
                break;
            }
            add(item);
        }
    }

    /**
     * Returns the number of additional elements that this deque can ideally (in the absence of
     * memory or resource constraints) accept without blocking. This is always equal to the initial
     * capacity of this deque less the current {@code size} of this deque.
     *
     * <p>Note that you <em>cannot</em> always tell if an attempt to insert an element will succeed
     * by inspecting {@code remainingCapacity} because it may be the case that another thread is
     * about to insert or remove an element.
     *
     * @return The number of additional elements the queue is able to accept
     */
    public int remainingCapacity() {
        lock.lock();
        try {
            return capacity - count;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Retrieves and removes the head of the queue represented by this deque. This method differs
     * from {@link #poll poll} only in that it throws an exception if this deque is empty.
     *
     * <p>This method is equivalent to {@link #removeFirst() removeFirst}.
     *
     * @return the head of the queue represented by this deque
     * @throws NoSuchElementException if this deque is empty
     */
    public E remove0() {
        return removeFirst();
    }

    /**
     * Removes the first occurrence of the specified element from this deque. If the deque does not
     * contain the element, it is unchanged. More formally, removes the first element {@code e} such
     * that {@code o.equals(e)} (if such an element exists). Returns {@code true} if this deque
     * contained the specified element (or equivalently, if this deque changed as a result of the
     * call).
     *
     * <p>This method is equivalent to {@link #removeFirstOccurrence(Object) removeFirstOccurrence}.
     *
     * @param o element to be removed from this deque, if present
     * @return {@code true} if this deque changed as a result of the call
     */
    public boolean remove1(final Object o) {
        return removeFirstOccurrence(o);
    }

    /** {@inheritDoc} */
    @Override
    public E removeFirst() {
        final E x = pollFirst0();
        if (x == null) {
            throw new NoSuchElementException();
        }
        return x;
    }

    /*
     * TODO: Add support for more efficient bulk operations.
     *
     * We don't want to acquire the lock for every iteration, but we
     * also want other threads a chance to interact with the
     * collection, especially when count is close to capacity.
     */

    @Override
    public boolean removeFirstOccurrence(final Object o) {
        if (o == null) {
            return false;
        }
        lock.lock();
        try {
            for (Node<E> p = first; p != null; p = p.next) {
                if (o.equals(p.item)) {
                    unlink(p);
                    return true;
                }
            }
            return false;
        } finally {
            lock.unlock();
        }
    }

    /** {@inheritDoc} */
    @Override
    public E removeLast() {
        final E x = pollLast0();
        if (x == null) {
            throw new NoSuchElementException();
        }
        return x;
    }

    @Override
    public boolean removeLastOccurrence(final Object o) {
        if (o == null) {
            return false;
        }
        lock.lock();
        try {
            for (Node<E> p = last; p != null; p = p.prev) {
                if (o.equals(p.item)) {
                    unlink(p);
                    return true;
                }
            }
            return false;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Returns the number of elements in this deque.
     *
     * @return the number of elements in this deque
     */
    @Override
    public int size() {
        lock.lock();
        try {
            return count;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the first element in the queue, waiting until there is an element to unlink if the
     * queue is empty.
     *
     * <p>This method is equivalent to {@link #takeFirst()}.
     *
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E take() throws InterruptedException {
        return takeFirst();
    }

    /**
     * Unlinks the first element in the queue, waiting until there is an element to unlink if the
     * queue is empty.
     *
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E takeFirst() throws InterruptedException {
        lock.lock();
        try {
            E x;
            while ((x = unlinkFirst()) == null) {
                notEmpty.await();
            }
            return x;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the last element in the queue, waiting until there is an element to unlink if the
     * queue is empty.
     *
     * @return the unlinked element
     * @throws InterruptedException if the current thread is interrupted
     */
    public E takeLast() throws InterruptedException {
        lock.lock();
        try {
            E x;
            while ((x = unlinkLast()) == null) {
                notEmpty.await();
            }
            return x;
        } finally {
            lock.unlock();
        }
    }

    /**
     * Returns an array containing all of the elements in this deque, in proper sequence (from first
     * to last element).
     *
     * <p>The returned array will be "safe" in that no references to it are maintained by this
     * deque. (In other words, this method must allocate a new array). The caller is thus free to
     * modify the returned array.
     *
     * <p>This method acts as bridge between array-based and collection-based APIs.
     *
     * @return an array containing all of the elements in this deque
     */
    public Object[] toArray0() {
        lock.lock();
        try {
            final Object[] a = new Object[count];
            int k = 0;
            for (Node<E> p = first; p != null; p = p.next) {
                a[k++] = p.item;
            }
            return a;
        } finally {
            lock.unlock();
        }
    }

    /** {@inheritDoc} */
    @SuppressWarnings("unchecked")
    public <T> T[] toArray1(T[] a) {
        lock.lock();
        try {
            if (a.length < count) {
                a =
                        (T[])
                                java.lang.reflect.Array.newInstance(
                                        a.getClass().getComponentType(), count);
            }
            int k = 0;
            for (Node<E> p = first; p != null; p = p.next) {
                a[k++] = (T) p.item;
            }
            if (a.length > k) {
                a[k] = null;
            }
            return a;
        } finally {
            lock.unlock();
        }
    }

    @Override
    public String toString() {
        lock.lock();
        try {
            return super.toString();
        } finally {
            lock.unlock();
        }
    }

    /**
     * Unlinks the provided node.
     *
     * @param x The node to unlink
     */
    private void unlink(final Node<E> x) {
        final Node<E> p = x.prev;
        final Node<E> n = x.next;
        if (p == null) {
            unlinkFirst();
        } else if (n == null) {
            unlinkLast();
        } else {
            p.next = n;
            n.prev = p;
            x.item = null;
            --count;
            notFull.signal();
        }
    }

    /**
     * Removes and returns the first element, or null if empty.
     *
     * @return The first element or {@code null} if empty
     */
    private E unlinkFirst() {
        final Node<E> f = first;
        if (f == null) {
            return null;
        }
        final Node<E> n = f.next;
        final E item = f.item;
        f.item = null;
        f.next = f; // help GC
        first = n;
        if (n == null) {
            last = null;
        } else {
            n.prev = null;
        }
        --count;
        notFull.signal();
        return item;
    }

    /**
     * Removes and returns the last element, or null if empty.
     *
     * @return The first element or {@code null} if empty
     */
    private E unlinkLast() {
        final Node<E> l = last;
        if (l == null) {
            return null;
        }
        final Node<E> p = l.prev;
        final E item = l.item;
        l.item = null;
        l.prev = l; // help GC
        last = p;
        if (p == null) {
            first = null;
        } else {
            p.next = null;
        }
        --count;
        notFull.signal();
        return item;
    }

    /**
     * Saves the state of this deque to a stream (that is, serialize it).
     *
     * @serialData The capacity (int), followed by elements (each an {@code Object}) in the proper
     *     order, followed by a null
     * @param s the stream
     */
    private void writeObject(final java.io.ObjectOutputStream s) throws java.io.IOException {
        lock.lock();
        try {
            s.defaultWriteObject();
            for (Node<E> p = first; p != null; p = p.next) {
                s.writeObject(p.item);
            }
            s.writeObject(null);
        } finally {
            lock.unlock();
        }
    }
}
