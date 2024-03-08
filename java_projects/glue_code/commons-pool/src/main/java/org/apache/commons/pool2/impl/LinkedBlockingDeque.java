package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.io.Serializable;
import java.util.Collection;
import java.util.Iterator;
import java.util.concurrent.TimeUnit;
import java.time.Duration;
import java.util.AbstractQueue;
import java.util.Deque;
import java.util.NoSuchElementException;
import java.util.Objects;
import java.util.concurrent.locks.Condition;
    private abstract class AbstractItr implements Iterator<E> {
    private static Value clz = ContextInitializer.getPythonClass("/LinkedBlockingDeque.py", "AbstractItr");
    private Value obj;
    public AbstractItr(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public void remove() {
// 
// final Node<E> n = lastRet;
// if (n == null) {
// throw new IllegalStateException();
// }
// lastRet = null;
// lock.lock();
// try {
// if (n.item != null) {
// unlink(n);
// }
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("remove");
}
        public E next() {
// 
// if (next == null) {
// throw new NoSuchElementException();
// }
// lastRet = next;
// final E x = nextItem;
// advance();
// return x;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("next").as(E.class);
}
        public boolean hasNext() {
// 
// return next != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hasNext").as(boolean.class);
}
        private Node<E> succ(Node<E> n) {
// 
// for (; ; ) {
// final Node<E> s = nextNode(n);
// if (s == null) {
// return null;
// }
// if (s.item != null) {
// return s;
// }
// if (s == n) {
// return firstNode();
// }
// n = s;
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("succ", n).as(Node.class);
}
        void advance() {
// 
// lock.lock();
// try {
// next = succ(next);
// nextItem = next == null ? null : next.item;
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("advance");
}
        AbstractItr() {
// 
// lock.lock();
// try {
// next = firstNode();
// nextItem = next == null ? null : next.item;
// } finally {
// lock.unlock();
// }
// 

this.obj = clz.invokeMember("__init__");
}
        abstract Node<E> nextNode(Node<E> n);
        abstract Node<E> firstNode();
}
class LinkedBlockingDeque<E> extends AbstractQueue<E> implements Deque<E>, Serializable {
    private static final long serialVersionUID = -387911632671998426L;
    private static Value clz = ContextInitializer.getPythonClass("/LinkedBlockingDeque.py", "LinkedBlockingDeque");
    private Value obj;
    public LinkedBlockingDeque(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// lock.lock();
// try {
// return super.toString();
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    public <T> T[] toArray1(T[] a) {
// 
// lock.lock();
// try {
// if (a.length < count) {
// a =
// (T[])
// java.lang.reflect.Array.newInstance(
// a.getClass().getComponentType(), count);
// }
// int k = 0;
// for (Node<E> p = first; p != null; p = p.next) {
// a[k++] = (T) p.item;
// }
// if (a.length > k) {
// a[k] = null;
// }
// return a;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toArray1", a).as(T[].class);
}
    public int size() {
// 
// lock.lock();
// try {
// return count;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("size").as(int.class);
}
    public boolean removeLastOccurrence(final Object o) {
// 
// if (o == null) {
// return false;
// }
// lock.lock();
// try {
// for (Node<E> p = last; p != null; p = p.prev) {
// if (o.equals(p.item)) {
// unlink(p);
// return true;
// }
// }
// return false;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("removeLastOccurrence", o).as(boolean.class);
}
    public E removeLast() {
// 
// final E x = pollLast0();
// if (x == null) {
// throw new NoSuchElementException();
// }
// return x;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("removeLast").as(E.class);
}
    public boolean removeFirstOccurrence(final Object o) {
// 
// if (o == null) {
// return false;
// }
// lock.lock();
// try {
// for (Node<E> p = first; p != null; p = p.next) {
// if (o.equals(p.item)) {
// unlink(p);
// return true;
// }
// }
// return false;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("removeFirstOccurrence", o).as(boolean.class);
}
    public E removeFirst() {
// 
// final E x = pollFirst0();
// if (x == null) {
// throw new NoSuchElementException();
// }
// return x;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("removeFirst").as(E.class);
}
    public void push(final E e) {
// 
// addFirst(e);
// 

obj.invokeMember("push", e);
}
    public E pop() {
// 
// return removeFirst();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pop").as(E.class);
}
    public E pollLast() {
// 
// return pollLast0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollLast").as(E.class);
}
    public E pollFirst() {
// 
// return pollFirst0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollFirst").as(E.class);
}
    public E poll() {
// 
// return poll0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("poll").as(E.class);
}
    public E peekLast() {
// 
// lock.lock();
// try {
// return last == null ? null : last.item;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("peekLast").as(E.class);
}
    public E peekFirst() {
// 
// lock.lock();
// try {
// return first == null ? null : first.item;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("peekFirst").as(E.class);
}
    public E peek() {
// 
// return peekFirst();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("peek").as(E.class);
}
    public boolean offerFirst(final E e) {
// 
// return offerFirst0(e);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerFirst", e).as(boolean.class);
}
    public boolean offer(final E e) {
// 
// return offer0(e);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offer", e).as(boolean.class);
}
    public Iterator<E> iterator() {
// 
// return new Itr();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("iterator").as(Iterator.class);
}
    public E getLast() {
// 
// final E x = peekLast();
// if (x == null) {
// throw new NoSuchElementException();
// }
// return x;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLast").as(E.class);
}
    public E getFirst() {
// 
// final E x = peekFirst();
// if (x == null) {
// throw new NoSuchElementException();
// }
// return x;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getFirst").as(E.class);
}
    public E element() {
// 
// return getFirst();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("element").as(E.class);
}
    public Iterator<E> descendingIterator() {
// 
// return new DescendingItr();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("descendingIterator").as(Iterator.class);
}
    public boolean contains(final Object o) {
// 
// if (o == null) {
// return false;
// }
// lock.lock();
// try {
// for (Node<E> p = first; p != null; p = p.next) {
// if (o.equals(p.item)) {
// return true;
// }
// }
// return false;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("contains", o).as(boolean.class);
}
    public void clear() {
// 
// lock.lock();
// try {
// for (Node<E> f = first; f != null; ) {
// f.item = null;
// final Node<E> n = f.next;
// f.prev = null;
// f.next = null;
// f = n;
// }
// first = last = null;
// count = 0;
// notFull.signalAll();
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("clear");
}
    public void addLast(final E e) {
// 
// if (!offerLast0(e)) {
// throw new IllegalStateException("Deque full");
// }
// 

obj.invokeMember("addLast", e);
}
    public void addFirst(final E e) {
// 
// if (!offerFirst0(e)) {
// throw new IllegalStateException("Deque full");
// }
// 

obj.invokeMember("addFirst", e);
}
    public boolean add(final E e) {
// 
// addLast(e);
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("add", e).as(boolean.class);
}
    public Object[] toArray0() {
// 
// lock.lock();
// try {
// final Object[] a = new Object[count];
// int k = 0;
// for (Node<E> p = first; p != null; p = p.next) {
// a[k++] = p.item;
// }
// return a;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toArray0").as(Object[].class);
}
    public E takeLast() throws InterruptedException {
try {
// 
// lock.lock();
// try {
// E x;
// while ((x = unlinkLast()) == null) {
// notEmpty.await();
// }
// return x;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("takeLast").as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.takeLast");
}
}
    public E takeFirst() throws InterruptedException {
try {
// 
// lock.lock();
// try {
// E x;
// while ((x = unlinkFirst()) == null) {
// notEmpty.await();
// }
// return x;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("takeFirst").as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.takeFirst");
}
}
    public E take() throws InterruptedException {
try {
// 
// return takeFirst();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("take").as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.take");
}
}
    public boolean remove1(final Object o) {
// 
// return removeFirstOccurrence(o);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("remove1", o).as(boolean.class);
}
    public E remove0() {
// 
// return removeFirst();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("remove0").as(E.class);
}
    public int remainingCapacity() {
// 
// lock.lock();
// try {
// return capacity - count;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("remainingCapacity").as(int.class);
}
    public void putLast(final E e) throws InterruptedException {
try {
// 
// Objects.requireNonNull(e, "e");
// lock.lock();
// try {
// while (!linkLast(e)) {
// notFull.await();
// }
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("putLast", e);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.putLast");
}
}
    public void putFirst(final E e) throws InterruptedException {
try {
// 
// Objects.requireNonNull(e, "e");
// lock.lock();
// try {
// while (!linkFirst(e)) {
// notFull.await();
// }
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("putFirst", e);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.putFirst");
}
}
    public void put(final E e) throws InterruptedException {
try {
// 
// putLast(e);
// 

obj.invokeMember("put", e);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.put");
}
}
    public E pollLast2(final long timeout, final TimeUnit unit) throws InterruptedException {
try {
// 
// return pollLast1(PoolImplUtils.toDuration(timeout, unit));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollLast2", timeout, unit).as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.pollLast2");
}
}
    public E pollLast1(final Duration timeout) throws InterruptedException {
try {
// 
// long nanos = timeout.toNanos();
// lock.lockInterruptibly();
// try {
// E x;
// while ((x = unlinkLast()) == null) {
// if (nanos <= 0) {
// return null;
// }
// nanos = notEmpty.awaitNanos(nanos);
// }
// return x;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollLast1", timeout).as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.pollLast1");
}
}
    public E pollLast0() {
// 
// lock.lock();
// try {
// return unlinkLast();
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollLast0").as(E.class);
}
    public E pollFirst2(final long timeout, final TimeUnit unit) throws InterruptedException {
try {
// 
// return pollFirst1(PoolImplUtils.toDuration(timeout, unit));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollFirst2", timeout, unit).as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.pollFirst2");
}
}
    public E pollFirst0() {
// 
// lock.lock();
// try {
// return unlinkFirst();
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollFirst0").as(E.class);
}
    public E poll2(final long timeout, final TimeUnit unit) throws InterruptedException {
try {
// 
// return pollFirst2(timeout, unit);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("poll2", timeout, unit).as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.poll2");
}
}
    public E poll0() {
// 
// return pollFirst0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("poll0").as(E.class);
}
    public boolean offerLast2(final E e, final long timeout, final TimeUnit unit)
            throws InterruptedException {
try {
// 
// return offerLast1(e, PoolImplUtils.toDuration(timeout, unit));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerLast2", e, timeout, unit).as(boolean.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.offerLast2");
}
}
    public boolean offerLast0(final E e) {
// 
// Objects.requireNonNull(e, "e");
// lock.lock();
// try {
// return linkLast(e);
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerLast0", e).as(boolean.class);
}
    public boolean offerLast(final E e) {
// 
// return offerLast0(e);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerLast", e).as(boolean.class);
}
    public boolean offerFirst2(final E e, final long timeout, final TimeUnit unit)
            throws InterruptedException {
try {
// 
// return offerFirst1(e, PoolImplUtils.toDuration(timeout, unit));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerFirst2", e, timeout, unit).as(boolean.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.offerFirst2");
}
}
    public boolean offerFirst1(final E e, final Duration timeout) throws InterruptedException {
try {
// 
// Objects.requireNonNull(e, "e");
// long nanos = timeout.toNanos();
// lock.lockInterruptibly();
// try {
// while (!linkFirst(e)) {
// if (nanos <= 0) {
// return false;
// }
// nanos = notFull.awaitNanos(nanos);
// }
// return true;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerFirst1", e, timeout).as(boolean.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.offerFirst1");
}
}
    public boolean offerFirst0(final E e) {
// 
// Objects.requireNonNull(e, "e");
// lock.lock();
// try {
// return linkFirst(e);
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerFirst0", e).as(boolean.class);
}
    public boolean offer2(final E e, final long timeout, final TimeUnit unit)
            throws InterruptedException {
try {
// 
// return offerLast2(e, timeout, unit);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offer2", e, timeout, unit).as(boolean.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.offer2");
}
}
    public boolean offer0(final E e) {
// 
// return offerLast0(e);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offer0", e).as(boolean.class);
}
    public void interuptTakeWaiters() {
// 
// lock.lock();
// try {
// lock.interruptWaiters(notEmpty);
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("interuptTakeWaiters");
}
    public boolean hasTakeWaiters() {
// 
// lock.lock();
// try {
// return lock.hasWaiters(notEmpty);
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("hasTakeWaiters").as(boolean.class);
}
    public int getTakeQueueLength() {
// 
// lock.lock();
// try {
// return lock.getWaitQueueLength(notEmpty);
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getTakeQueueLength").as(int.class);
}
    public int drainTo1(final Collection<? super E> c, final int maxElements) {
try {
// 
// Objects.requireNonNull(c, "c");
// if (c == this) {
// throw new IllegalArgumentException();
// }
// lock.lock();
// try {
// final int n = Math.min(maxElements, count);
// for (int i = 0; i < n; i++) {
// c.add(first.item); // In this order, in case add() throws.
// unlinkFirst();
// }
// return n;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("drainTo1", c, maxElements).as(int.class);
} catch (PolyglotException e) {
    // TODO: Handle 
    throw () ExceptionHandler.handle(e, "LinkedBlockingDeque.drainTo1");
}
}
    public int drainTo0(final Collection<? super E> c) {
// 
// return drainTo1(c, Integer.MAX_VALUE);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("drainTo0", c).as(int.class);
}
    public LinkedBlockingDeque(
            int constructorId,
            final int capacity,
            final boolean fairness,
            final Collection<? extends E> c) {
// 
// if (constructorId == 0) {
// if (capacity <= 0) {
// throw new IllegalArgumentException();
// }
// this.capacity = capacity;
// lock = new InterruptibleReentrantLock(fairness);
// notEmpty = lock.newCondition();
// notFull = lock.newCondition();
// 
// if (c != null) {
// lock.lock(); // Never contended, but necessary for visibility
// try {
// for (final E e : c) {
// Objects.requireNonNull(e);
// if (!linkLast(e)) {
// throw new IllegalStateException("Deque full");
// }
// }
// } finally {
// lock.unlock();
// }
// }
// } else {
// this.capacity = capacity;
// lock = new InterruptibleReentrantLock(fairness);
// notEmpty = lock.newCondition();
// notFull = lock.newCondition();
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, capacity, fairness, c);
}
    public static LinkedBlockingDeque LinkedBlockingDeque3(final int capacity) {
// 
// return new LinkedBlockingDeque<>(0, capacity, false, null);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("LinkedBlockingDeque3", capacity).as(LinkedBlockingDeque.class);
}
    public static LinkedBlockingDeque LinkedBlockingDeque2(final Collection c) {
// 
// return new LinkedBlockingDeque<>(0, Integer.MAX_VALUE, false, c);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("LinkedBlockingDeque2", c).as(LinkedBlockingDeque.class);
}
    public static LinkedBlockingDeque LinkedBlockingDeque1(final boolean fairness) {
// 
// return new LinkedBlockingDeque<>(0, Integer.MAX_VALUE, fairness, null);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("LinkedBlockingDeque1", fairness).as(LinkedBlockingDeque.class);
}
    public static LinkedBlockingDeque LinkedBlockingDeque0() {
// 
// return new LinkedBlockingDeque<>(0, Integer.MAX_VALUE, false, null);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("LinkedBlockingDeque0").as(LinkedBlockingDeque.class);
}
    private void writeObject(final java.io.ObjectOutputStream s) throws java.io.IOException {
try {
// 
// lock.lock();
// try {
// s.defaultWriteObject();
// for (Node<E> p = first; p != null; p = p.next) {
// s.writeObject(p.item);
// }
// s.writeObject(null);
// } finally {
// lock.unlock();
// }
// 

obj.invokeMember("writeObject", s);
} catch (PolyglotException e) {
    // TODO: Handle java.io.IOException
    throw (java.io.IOException) ExceptionHandler.handle(e, "LinkedBlockingDeque.writeObject");
}
}
    private E unlinkLast() {
// 
// final Node<E> l = last;
// if (l == null) {
// return null;
// }
// final Node<E> p = l.prev;
// final E item = l.item;
// l.item = null;
// l.prev = l; // help GC
// last = p;
// if (p == null) {
// first = null;
// } else {
// p.next = null;
// }
// --count;
// notFull.signal();
// return item;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("unlinkLast").as(E.class);
}
    private E unlinkFirst() {
// 
// final Node<E> f = first;
// if (f == null) {
// return null;
// }
// final Node<E> n = f.next;
// final E item = f.item;
// f.item = null;
// f.next = f; // help GC
// first = n;
// if (n == null) {
// last = null;
// } else {
// n.prev = null;
// }
// --count;
// notFull.signal();
// return item;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("unlinkFirst").as(E.class);
}
    private void unlink(final Node<E> x) {
// 
// final Node<E> p = x.prev;
// final Node<E> n = x.next;
// if (p == null) {
// unlinkFirst();
// } else if (n == null) {
// unlinkLast();
// } else {
// p.next = n;
// n.prev = p;
// x.item = null;
// --count;
// notFull.signal();
// }
// 

obj.invokeMember("unlink", x);
}
    private void readObject(final java.io.ObjectInputStream s)
            throws java.io.IOException, ClassNotFoundException {
try {
// 
// s.defaultReadObject();
// count = 0;
// first = null;
// last = null;
// for (; ; ) {
// @SuppressWarnings("unchecked")
// final E item = (E) s.readObject();
// if (item == null) {
// break;
// }
// add(item);
// }
// 

obj.invokeMember("readObject", s);
} catch (PolyglotException e) {
    // TODO: Handle java.io.IOException, ClassNotFoundException
    throw (java.io.IOException, ClassNotFoundException) ExceptionHandler.handle(e, "LinkedBlockingDeque.readObject");
}
}
    private boolean linkLast(final E e) {
// 
// if (count >= capacity) {
// return false;
// }
// final Node<E> l = last;
// final Node<E> x = new Node<>(e, l, null);
// last = x;
// if (first == null) {
// first = x;
// } else {
// l.next = x;
// }
// ++count;
// notEmpty.signal();
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("linkLast", e).as(boolean.class);
}
    private boolean linkFirst(final E e) {
// 
// if (count >= capacity) {
// return false;
// }
// final Node<E> f = first;
// final Node<E> x = new Node<>(e, null, f);
// first = x;
// if (last == null) {
// last = x;
// } else {
// f.prev = x;
// }
// ++count;
// notEmpty.signal();
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("linkFirst", e).as(boolean.class);
}
    E pollFirst1(final Duration timeout) throws InterruptedException {
try {
// 
// long nanos = timeout.toNanos();
// lock.lockInterruptibly();
// try {
// E x;
// while ((x = unlinkFirst()) == null) {
// if (nanos <= 0) {
// return null;
// }
// nanos = notEmpty.awaitNanos(nanos);
// }
// return x;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("pollFirst1", timeout).as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.pollFirst1");
}
}
    E poll1(final Duration timeout) throws InterruptedException {
try {
// 
// return pollFirst1(timeout);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("poll1", timeout).as(E.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.poll1");
}
}
    boolean offerLast1(final E e, final Duration timeout) throws InterruptedException {
try {
// 
// Objects.requireNonNull(e, "e");
// long nanos = timeout.toNanos();
// lock.lockInterruptibly();
// try {
// while (!linkLast(e)) {
// if (nanos <= 0) {
// return false;
// }
// nanos = notFull.awaitNanos(nanos);
// }
// return true;
// } finally {
// lock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offerLast1", e, timeout).as(boolean.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.offerLast1");
}
}
    boolean offer1(final E e, final Duration timeout) throws InterruptedException {
try {
// 
// return offerLast1(e, timeout);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("offer1", e, timeout).as(boolean.class);
} catch (PolyglotException e) {
    // TODO: Handle InterruptedException
    throw (InterruptedException) ExceptionHandler.handle(e, "LinkedBlockingDeque.offer1");
}
}
    private class DescendingItr extends AbstractItr {
    private static Value clz = ContextInitializer.getPythonClass("/LinkedBlockingDeque.py", "DescendingItr");
    private Value obj;
    public DescendingItr(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        Node<E> nextNode(final Node<E> n) {
// 
// return n.prev;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("nextNode", n).as(Node.class);
}
        Node<E> firstNode() {
// 
// return last;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("firstNode").as(Node.class);
}
}
    private class Itr extends AbstractItr {
    private static Value clz = ContextInitializer.getPythonClass("/LinkedBlockingDeque.py", "Itr");
    private Value obj;
    public Itr(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        Node<E> nextNode(final Node<E> n) {
// 
// return n.next;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("nextNode", n).as(Node.class);
}
        Node<E> firstNode() {
// 
// return first;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("firstNode").as(Node.class);
}
}
    private static final class Node<E> {
    private static Value clz = ContextInitializer.getPythonClass("/LinkedBlockingDeque.py", "Node");
    private Value obj;
    public Node(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        Node(final E x, final Node<E> p, final Node<E> n) {
// 
// item = x;
// prev = p;
// next = n;
// 

this.obj = clz.invokeMember("__init__", x, p, n);
}
}
}
