/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.pool2.impl;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Timeout;

import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeUnit;

/** Tests for {@link LinkedBlockingDeque}. */
public class TestLinkedBlockingDeque {

    private static final Duration TIMEOUT_50_MILLIS = Duration.ofMillis(50);
    private static final Integer ONE = Integer.valueOf(1);
    private static final Integer TWO = Integer.valueOf(2);
    private static final Integer THREE = Integer.valueOf(3);

    LinkedBlockingDeque<Integer> deque;

    @BeforeEach
    public void setUp() {
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2);
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    /*
     * https://issues.apache.org/jira/browse/POOL-281
     *
     * Should complete almost instantly when the issue is fixed.
     */

    @Test
    public void testAdd_test0_decomposed()  {
        assertTrue(deque.add(ONE));
        assertTrue(deque.add(TWO));
        assertThrows(IllegalStateException.class, () -> deque.add(THREE));
        assertThrows(NullPointerException.class, () -> deque.add(null));
    }

    @Test
    public void testAddFirst_test0_decomposed()  {
        deque.addFirst(ONE);
        deque.addFirst(TWO);
    }

    @Test
    public void testAddFirst_test1_decomposed()  {
        deque.addFirst(ONE);
        deque.addFirst(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testAddFirst_test2_decomposed()  {
        deque.addFirst(ONE);
        deque.addFirst(TWO);
        assertEquals(2, deque.size());
        assertThrows(IllegalStateException.class, () -> deque.add(THREE));
    }

    @Test
    public void testAddFirst_test3_decomposed()  {
        deque.addFirst(ONE);
        deque.addFirst(TWO);
        assertEquals(2, deque.size());
        assertThrows(IllegalStateException.class, () -> deque.add(THREE));
        assertEquals(Integer.valueOf(2), deque.pop());
    }

    @Test
    public void testAddLast_test0_decomposed()  {
        deque.addLast(ONE);
        deque.addLast(TWO);
    }

    @Test
    public void testAddLast_test1_decomposed()  {
        deque.addLast(ONE);
        deque.addLast(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testAddLast_test2_decomposed()  {
        deque.addLast(ONE);
        deque.addLast(TWO);
        assertEquals(2, deque.size());
        assertThrows(IllegalStateException.class, () -> deque.add(THREE));
    }

    @Test
    public void testAddLast_test3_decomposed()  {
        deque.addLast(ONE);
        deque.addLast(TWO);
        assertEquals(2, deque.size());
        assertThrows(IllegalStateException.class, () -> deque.add(THREE));
        assertEquals(Integer.valueOf(1), deque.pop());
    }

    @Test
    public void testClear_test0_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testClear_test1_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        deque.clear();
    }

    @Test
    public void testClear_test2_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        deque.clear();
        deque.add(ONE);
    }

    @Test
    public void testClear_test3_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        deque.clear();
        deque.add(ONE);
        assertEquals(1, deque.size());
    }

    @Test
    public void testConstructors_test0_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
    }

    @Test
    public void testConstructors_test1_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        assertEquals(Integer.MAX_VALUE, deque.remainingCapacity());
    }

    @Test
    public void testConstructors_test2_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        assertEquals(Integer.MAX_VALUE, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2);
    }

    @Test
    public void testConstructors_test3_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        assertEquals(Integer.MAX_VALUE, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2);
        assertEquals(2, deque.remainingCapacity());
    }

    @Test
    public void testConstructors_test4_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        assertEquals(Integer.MAX_VALUE, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2);
        assertEquals(2, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque2(Arrays.asList(ONE, TWO));
    }

    @Test
    public void testConstructors_test5_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        assertEquals(Integer.MAX_VALUE, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2);
        assertEquals(2, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque2(Arrays.asList(ONE, TWO));
        assertEquals(2, deque.size());
    }

    @Test
    public void testConstructors_test6_decomposed()  {
        LinkedBlockingDeque<Integer> deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        assertEquals(Integer.MAX_VALUE, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2);
        assertEquals(2, deque.remainingCapacity());
        deque = LinkedBlockingDeque.LinkedBlockingDeque2(Arrays.asList(ONE, TWO));
        assertEquals(2, deque.size());
        assertThrows(
                NullPointerException.class,
                () -> LinkedBlockingDeque.LinkedBlockingDeque2(Arrays.asList(ONE, null)));
    }

    @Test
    public void testContains_test0_decomposed()  {
        deque.add(ONE);
    }

    @Test
    public void testContains_test1_decomposed()  {
        deque.add(ONE);
        assertTrue(deque.contains(ONE));
        assertFalse(deque.contains(TWO));
        assertFalse(deque.contains(null));
    }

    @Test
    public void testContains_test2_decomposed()  {
        deque.add(ONE);
        assertTrue(deque.contains(ONE));
        assertFalse(deque.contains(TWO));
        assertFalse(deque.contains(null));
        deque.add(TWO);
    }

    @Test
    public void testContains_test3_decomposed()  {
        deque.add(ONE);
        assertTrue(deque.contains(ONE));
        assertFalse(deque.contains(TWO));
        assertFalse(deque.contains(null));
        deque.add(TWO);
        assertTrue(deque.contains(TWO));
        assertFalse(deque.contains(THREE));
    }

    @Test
    public void testDescendingIterator_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.descendingIterator().next());
    }

    @Test
    public void testDescendingIterator_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.descendingIterator().next());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testDescendingIterator_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.descendingIterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.descendingIterator();
    }

    @Test
    public void testDescendingIterator_test3_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.descendingIterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.descendingIterator();
        assertEquals(Integer.valueOf(2), iter.next());
    }

    @Test
    public void testDescendingIterator_test4_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.descendingIterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.descendingIterator();
        assertEquals(Integer.valueOf(2), iter.next());
        iter.remove();
    }

    @Test
    public void testDescendingIterator_test5_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.descendingIterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.descendingIterator();
        assertEquals(Integer.valueOf(2), iter.next());
        iter.remove();
        assertEquals(Integer.valueOf(1), iter.next());
    }

    @Test
    public void testDrainTo_test0_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
    }

    @Test
    public void testDrainTo_test1_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testDrainTo_test2_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
    }

    @Test
    public void testDrainTo_test3_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
    }

    @Test
    public void testDrainTo_test4_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
    }

    @Test
    public void testDrainTo_test5_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testDrainTo_test6_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(1, deque.drainTo1(c, 1));
    }

    @Test
    public void testDrainTo_test7_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(1, deque.drainTo1(c, 1));
        assertEquals(1, deque.size());
        assertEquals(1, c.size());
    }

    @Test
    public void testDrainTo_test8_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(1, deque.drainTo1(c, 1));
        assertEquals(1, deque.size());
        assertEquals(1, c.size());
        c.iterator();
    }

    @Test
    public void testDrainTo_test9_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(1, deque.drainTo1(c, 1));
        assertEquals(1, deque.size());
        assertEquals(1, c.size());
        c.iterator();
        Integer.valueOf(1);
    }

    @Test
    public void testDrainTo_test10_decomposed()  {
        Collection<Integer> c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(2, deque.drainTo0(c));
        assertEquals(2, c.size());
        c = new ArrayList<>();
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(1, deque.drainTo1(c, 1));
        assertEquals(1, deque.size());
        assertEquals(1, c.size());
        c.iterator();
        Integer.valueOf(1);
        assertEquals(Integer.valueOf(1), c.iterator().next());
    }

    @Test
    public void testElement_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.element());
    }

    @Test
    public void testElement_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.element());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testElement_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.element());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.element());
    }

    @Test
    public void testGetFirst_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.getFirst());
    }

    @Test
    public void testGetFirst_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.getFirst());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testGetFirst_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.getFirst());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.getFirst());
    }

    @Test
    public void testGetLast_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.getLast());
    }

    @Test
    public void testGetLast_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.getLast());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testGetLast_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.getLast());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(2), deque.getLast());
    }

    @Test
    public void testIterator_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.iterator().next());
    }

    @Test
    public void testIterator_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.iterator().next());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testIterator_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.iterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.iterator();
    }

    @Test
    public void testIterator_test3_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.iterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.iterator();
        assertEquals(Integer.valueOf(1), iter.next());
    }

    @Test
    public void testIterator_test4_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.iterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.iterator();
        assertEquals(Integer.valueOf(1), iter.next());
        iter.remove();
    }

    @Test
    public void testIterator_test5_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.iterator().next());
        deque.add(ONE);
        deque.add(TWO);
        final Iterator<Integer> iter = deque.iterator();
        assertEquals(Integer.valueOf(1), iter.next());
        iter.remove();
        assertEquals(Integer.valueOf(2), iter.next());
    }

    @Test
    public void testOffer_test0_decomposed()  {
        assertTrue(deque.offer(ONE));
        assertTrue(deque.offer(TWO));
        assertFalse(deque.offer(THREE));
        assertThrows(NullPointerException.class, () -> deque.offer(null));
    }

    @Test
    public void testOfferFirst_test0_decomposed()  {
        deque.offerFirst(ONE);
        deque.offerFirst(TWO);
    }

    @Test
    public void testOfferFirst_test1_decomposed()  {
        deque.offerFirst(ONE);
        deque.offerFirst(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testOfferFirst_test2_decomposed()  {
        deque.offerFirst(ONE);
        deque.offerFirst(TWO);
        assertEquals(2, deque.size());
        assertThrows(NullPointerException.class, () -> deque.offerFirst(null));
    }

    @Test
    public void testOfferFirst_test3_decomposed()  {
        deque.offerFirst(ONE);
        deque.offerFirst(TWO);
        assertEquals(2, deque.size());
        assertThrows(NullPointerException.class, () -> deque.offerFirst(null));
        assertEquals(Integer.valueOf(2), deque.pop());
    }

    @Test
    public void testOfferFirstWithTimeout_test0_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.offerFirst1(null, TIMEOUT_50_MILLIS));
        assertTrue(deque.offerFirst1(ONE, TIMEOUT_50_MILLIS));
        assertTrue(deque.offerFirst1(TWO, TIMEOUT_50_MILLIS));
        assertFalse(deque.offerFirst1(THREE, TIMEOUT_50_MILLIS));
    }

    @Test
    public void testOfferLast_test0_decomposed()  {
        deque.offerLast(ONE);
        deque.offerLast(TWO);
    }

    @Test
    public void testOfferLast_test1_decomposed()  {
        deque.offerLast(ONE);
        deque.offerLast(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testOfferLast_test2_decomposed()  {
        deque.offerLast(ONE);
        deque.offerLast(TWO);
        assertEquals(2, deque.size());
        assertThrows(NullPointerException.class, () -> deque.offerLast(null));
    }

    @Test
    public void testOfferLast_test3_decomposed()  {
        deque.offerLast(ONE);
        deque.offerLast(TWO);
        assertEquals(2, deque.size());
        assertThrows(NullPointerException.class, () -> deque.offerLast(null));
        assertEquals(Integer.valueOf(1), deque.pop());
    }

    @Test
    public void testOfferLastWithTimeout_test0_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.offerLast1(null, TIMEOUT_50_MILLIS));
        assertTrue(deque.offerLast1(ONE, TIMEOUT_50_MILLIS));
        assertTrue(deque.offerLast1(TWO, TIMEOUT_50_MILLIS));
        assertFalse(deque.offerLast1(THREE, TIMEOUT_50_MILLIS));
    }

    @Test
    public void testOfferWithTimeout_test0_decomposed() throws InterruptedException {
        assertTrue(deque.offer1(ONE, TIMEOUT_50_MILLIS));
        assertTrue(deque.offer1(TWO, TIMEOUT_50_MILLIS));
        assertFalse(deque.offer1(THREE, TIMEOUT_50_MILLIS));
        assertThrows(NullPointerException.class, () -> deque.offer1(null, TIMEOUT_50_MILLIS));
    }

    @Test
    public void testPeek_test0_decomposed()  {
        assertNull(deque.peek());
    }

    @Test
    public void testPeek_test1_decomposed()  {
        assertNull(deque.peek());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testPeek_test2_decomposed()  {
        assertNull(deque.peek());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.peek());
    }

    @Test
    public void testPeekFirst_test0_decomposed()  {
        assertNull(deque.peekFirst());
    }

    @Test
    public void testPeekFirst_test1_decomposed()  {
        assertNull(deque.peekFirst());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testPeekFirst_test2_decomposed()  {
        assertNull(deque.peekFirst());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.peekFirst());
    }

    @Test
    public void testPeekLast_test0_decomposed()  {
        assertNull(deque.peekLast());
    }

    @Test
    public void testPeekLast_test1_decomposed()  {
        assertNull(deque.peekLast());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testPeekLast_test2_decomposed()  {
        assertNull(deque.peekLast());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(2), deque.peekLast());
    }

    @Test
    public void testPollFirst_test0_decomposed()  {
        assertNull(deque.pollFirst());
    }

    @Test
    public void testPollFirst_test1_decomposed()  {
        assertNull(deque.pollFirst());
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
    }

    @Test
    public void testPollFirst_test2_decomposed()  {
        assertNull(deque.pollFirst());
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
        assertEquals(Integer.valueOf(2), deque.pollFirst());
    }

    @Test
    public void testPollFirstWithTimeout_test0_decomposed() throws InterruptedException {
        assertNull(deque.pollFirst());
    }

    @Test
    public void testPollFirstWithTimeout_test1_decomposed() throws InterruptedException {
        assertNull(deque.pollFirst());
        assertNull(deque.pollFirst1(TIMEOUT_50_MILLIS));
    }

    @Test
    public void testPollLast_test0_decomposed()  {
        assertNull(deque.pollLast());
    }

    @Test
    public void testPollLast_test1_decomposed()  {
        assertNull(deque.pollLast());
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
    }

    @Test
    public void testPollLast_test2_decomposed()  {
        assertNull(deque.pollLast());
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
        assertEquals(Integer.valueOf(1), deque.pollLast());
    }

    @Test
    public void testPollLastWithTimeout_test0_decomposed() throws InterruptedException {
        assertNull(deque.pollLast());
    }

    @Test
    public void testPollLastWithTimeout_test1_decomposed() throws InterruptedException {
        assertNull(deque.pollLast());
        assertNull(deque.pollLast1(TIMEOUT_50_MILLIS));
    }

    @Test
    public void testPollWithTimeout_test0_decomposed() throws InterruptedException {
        assertNull(deque.poll1(TIMEOUT_50_MILLIS));
        assertNull(deque.poll1(TIMEOUT_50_MILLIS));
    }

    @Test
    public void testPop_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.pop());
    }

    @Test
    public void testPop_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.pop());
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testPop_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, () -> deque.pop());
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.pop());
        assertThrows(
                NoSuchElementException.class,
                () -> {
                    deque.pop();
                    deque.pop();
                });
    }

    @Test
    public void testPossibleBug_test0_decomposed()  {
        deque = LinkedBlockingDeque.LinkedBlockingDeque0();
    }

    @Test
    public void testPossibleBug_test1_decomposed()  {
        deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        for (int i = 0; i < 3; i++) {
            deque.add(Integer.valueOf(i));
        }
    }

    @Test
    public void testPossibleBug_test2_decomposed()  {
        deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        for (int i = 0; i < 3; i++) {
            deque.add(Integer.valueOf(i));
        }
        final Iterator<Integer> iter = deque.iterator();
    }

    @Test
    public void testPossibleBug_test3_decomposed()  {
        deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        for (int i = 0; i < 3; i++) {
            deque.add(Integer.valueOf(i));
        }
        final Iterator<Integer> iter = deque.iterator();
        iter.next();
    }

    @Test
    public void testPossibleBug_test4_decomposed()  {
        deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        for (int i = 0; i < 3; i++) {
            deque.add(Integer.valueOf(i));
        }
        final Iterator<Integer> iter = deque.iterator();
        iter.next();
        deque.remove(Integer.valueOf(1));
        deque.remove(Integer.valueOf(0));
        deque.remove(Integer.valueOf(2));
    }

    @Test
    public void testPossibleBug_test5_decomposed()  {
        deque = LinkedBlockingDeque.LinkedBlockingDeque0();
        for (int i = 0; i < 3; i++) {
            deque.add(Integer.valueOf(i));
        }
        final Iterator<Integer> iter = deque.iterator();
        iter.next();
        deque.remove(Integer.valueOf(1));
        deque.remove(Integer.valueOf(0));
        deque.remove(Integer.valueOf(2));
        iter.next();
    }

    @Test
    public void testPush_test0_decomposed()  {
        deque.push(ONE);
        deque.push(TWO);
    }

    @Test
    public void testPush_test1_decomposed()  {
        deque.push(ONE);
        deque.push(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testPush_test2_decomposed()  {
        deque.push(ONE);
        deque.push(TWO);
        assertEquals(2, deque.size());
        assertThrows(IllegalStateException.class, () -> deque.push(THREE));
    }

    @Test
    public void testPush_test3_decomposed()  {
        deque.push(ONE);
        deque.push(TWO);
        assertEquals(2, deque.size());
        assertThrows(IllegalStateException.class, () -> deque.push(THREE));
        assertEquals(Integer.valueOf(2), deque.pop());
    }

    @Test
    public void testPut_test0_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.put(null));
        deque.put(ONE);
        deque.put(TWO);
    }

    @Test
    public void testPutFirst_test0_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.putFirst(null));
        deque.putFirst(ONE);
        deque.putFirst(TWO);
    }

    @Test
    public void testPutFirst_test1_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.putFirst(null));
        deque.putFirst(ONE);
        deque.putFirst(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testPutFirst_test2_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.putFirst(null));
        deque.putFirst(ONE);
        deque.putFirst(TWO);
        assertEquals(2, deque.size());
        assertEquals(Integer.valueOf(2), deque.pop());
    }

    @Test
    public void testPutLast_test0_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.putLast(null));
        deque.putLast(ONE);
        deque.putLast(TWO);
    }

    @Test
    public void testPutLast_test1_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.putLast(null));
        deque.putLast(ONE);
        deque.putLast(TWO);
        assertEquals(2, deque.size());
    }

    @Test
    public void testPutLast_test2_decomposed() throws InterruptedException {
        assertThrows(NullPointerException.class, () -> deque.putLast(null));
        deque.putLast(ONE);
        deque.putLast(TWO);
        assertEquals(2, deque.size());
        assertEquals(Integer.valueOf(1), deque.pop());
    }

    @Test
    public void testRemove_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::remove);
        deque.add(ONE);
    }

    @Test
    public void testRemove_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::remove);
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testRemove_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::remove);
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.remove());
    }

    @Test
    public void testRemoveFirst_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::removeFirst);
        deque.add(ONE);
    }

    @Test
    public void testRemoveFirst_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::removeFirst);
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testRemoveFirst_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::removeFirst);
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(1), deque.removeFirst());
        assertThrows(
                NoSuchElementException.class,
                () -> {
                    deque.removeFirst();
                    deque.removeFirst();
                });
    }

    @Test
    public void testRemoveLast_test0_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::removeLast);
        deque.add(ONE);
    }

    @Test
    public void testRemoveLast_test1_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::removeLast);
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testRemoveLast_test2_decomposed()  {
        assertThrows(NoSuchElementException.class, deque::removeLast);
        deque.add(ONE);
        deque.add(TWO);
        assertEquals(Integer.valueOf(2), deque.removeLast());
        assertThrows(
                NoSuchElementException.class,
                () -> {
                    deque.removeLast();
                    deque.removeLast();
                });
    }

    @Test
    public void testRemoveLastOccurrence_test0_decomposed()  {
        assertFalse(deque.removeLastOccurrence(null));
        assertFalse(deque.removeLastOccurrence(ONE));
    }

    @Test
    public void testRemoveLastOccurrence_test1_decomposed()  {
        assertFalse(deque.removeLastOccurrence(null));
        assertFalse(deque.removeLastOccurrence(ONE));
        deque.add(ONE);
        deque.add(ONE);
    }

    @Test
    public void testRemoveLastOccurrence_test2_decomposed()  {
        assertFalse(deque.removeLastOccurrence(null));
        assertFalse(deque.removeLastOccurrence(ONE));
        deque.add(ONE);
        deque.add(ONE);
        assertTrue(deque.removeLastOccurrence(ONE));
    }

    @Test
    public void testRemoveLastOccurrence_test3_decomposed()  {
        assertFalse(deque.removeLastOccurrence(null));
        assertFalse(deque.removeLastOccurrence(ONE));
        deque.add(ONE);
        deque.add(ONE);
        assertTrue(deque.removeLastOccurrence(ONE));
        assertEquals(1, deque.size());
    }

    @Test
    public void testTake_test0_decomposed() throws InterruptedException {
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
    }

    @Test
    public void testTake_test1_decomposed() throws InterruptedException {
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
        assertEquals(Integer.valueOf(2), deque.take());
    }

    @Test
    public void testTakeFirst_test0_decomposed() throws InterruptedException {
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
    }

    @Test
    public void testTakeFirst_test1_decomposed() throws InterruptedException {
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
        assertEquals(Integer.valueOf(2), deque.takeFirst());
    }

    @Test
    public void testTakeLast_test0_decomposed() throws InterruptedException {
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
    }

    @Test
    public void testTakeLast_test1_decomposed() throws InterruptedException {
        assertTrue(deque.offerFirst(ONE));
        assertTrue(deque.offerFirst(TWO));
        assertEquals(Integer.valueOf(1), deque.takeLast());
    }

    @Test
    public void testToArray_test0_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
    }

    @Test
    public void testToArray_test1_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        Object[] arr = deque.toArray();
        assertEquals(Integer.valueOf(1), arr[0]);
    }

    @Test
    public void testToArray_test2_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        Object[] arr = deque.toArray();
        assertEquals(Integer.valueOf(1), arr[0]);
        assertEquals(Integer.valueOf(2), arr[1]);
        arr = deque.toArray(new Integer[0]);
        assertEquals(Integer.valueOf(1), arr[0]);
    }

    @Test
    public void testToArray_test3_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        Object[] arr = deque.toArray();
        assertEquals(Integer.valueOf(1), arr[0]);
        assertEquals(Integer.valueOf(2), arr[1]);
        arr = deque.toArray(new Integer[0]);
        assertEquals(Integer.valueOf(1), arr[0]);
        assertEquals(Integer.valueOf(2), arr[1]);
        arr = deque.toArray(new Integer[0]);
        assertEquals(Integer.valueOf(1), arr[0]);
    }

    @Test
    public void testToArray_test4_decomposed()  {
        deque.add(ONE);
        deque.add(TWO);
        Object[] arr = deque.toArray();
        assertEquals(Integer.valueOf(1), arr[0]);
        assertEquals(Integer.valueOf(2), arr[1]);
        arr = deque.toArray(new Integer[0]);
        assertEquals(Integer.valueOf(1), arr[0]);
        assertEquals(Integer.valueOf(2), arr[1]);
        arr = deque.toArray(new Integer[0]);
        assertEquals(Integer.valueOf(1), arr[0]);
        assertEquals(Integer.valueOf(2), arr[1]);
    }
}