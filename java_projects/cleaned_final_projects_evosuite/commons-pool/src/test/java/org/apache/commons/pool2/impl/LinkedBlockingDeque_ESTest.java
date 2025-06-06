


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

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.time.Duration;
import java.time.temporal.ChronoUnit;
import java.time.temporal.UnsupportedTemporalTypeException;
import java.util.Collection;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Spliterator;
import java.util.concurrent.TimeUnit;
import java.util.stream.Stream;
import org.apache.commons.pool2.impl.LinkedBlockingDeque;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LinkedBlockingDeque_ESTest extends LinkedBlockingDeque_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, false, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(917, 917, false, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(linkedBlockingDeque1.contains(917));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer((-403));
      assertEquals((-403), (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedBlockingDeque1.add(integer0);
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(linkedBlockingDeque1.contains(917));
      assertTrue(linkedBlockingDeque1.contains(integer0));
      assertTrue(boolean0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Object[] objectArray0 = linkedBlockingDeque0.toArray0();
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, objectArray0.length);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(objectArray0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      
      Integer integer1 = new Integer((-403));
      assertEquals((-403), (int)integer1);
      assertNotNull(integer1);
      assertTrue(integer1.equals((Object)integer0));
      
      LinkedHashSet linkedHashSet1 = (LinkedHashSet)linkedHashSet0.clone();
      assertFalse(linkedHashSet0.contains(integer1));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertTrue(linkedHashSet1.isEmpty());
      assertEquals(0, linkedHashSet1.size());
      assertNotNull(linkedHashSet1);
      
      Integer integer2 = new Integer((-2083));
      assertEquals((-2083), (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)integer1));
      assertFalse(integer2.equals((Object)integer0));
      
      boolean boolean1 = linkedHashSet0.add(integer2);
      assertTrue(linkedHashSet0.contains((-2083)));
      assertFalse(linkedHashSet0.contains(integer1));
      assertTrue(boolean1);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(integer2.equals((Object)integer1));
      assertFalse(integer2.equals((Object)integer0));
      assertTrue(boolean1 == boolean0);
      
      TimeUnit timeUnit0 = TimeUnit.MICROSECONDS;
      boolean boolean2 = linkedBlockingDeque0.offer2(integer1, (-403), timeUnit0);
      assertTrue(linkedHashSet0.contains((-2083)));
      assertFalse(linkedHashSet0.contains(integer1));
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains((-2083)));
      assertTrue(boolean2);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertTrue(integer1.equals((Object)integer0));
      assertFalse(integer1.equals((Object)integer2));
      assertTrue(boolean2 == boolean0);
      assertTrue(boolean2 == boolean1);
      
      Integer integer3 = linkedBlockingDeque0.takeFirst();
      assertTrue(linkedHashSet0.contains((-2083)));
      assertFalse(linkedHashSet0.contains(integer3));
      assertFalse(linkedBlockingDeque0.contains(integer3));
      assertEquals((-403), (int)integer3);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(integer3);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertTrue(integer3.equals((Object)integer0));
      assertFalse(integer3.equals((Object)integer2));
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 7, false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(1));
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer(2155);
      assertEquals(2155, (int)integer0);
      assertNotNull(integer0);
      
      TimeUnit timeUnit0 = TimeUnit.DAYS;
      boolean boolean0 = linkedBlockingDeque0.offerLast2(integer0, 7, timeUnit0);
      assertFalse(linkedBlockingDeque0.contains(1));
      assertTrue(linkedBlockingDeque0.contains(2155));
      assertTrue(boolean0);
      
      int int0 = linkedBlockingDeque0.size();
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(2155));
      assertEquals(1, int0);
      
      Spliterator<Integer> spliterator0 = linkedBlockingDeque0.spliterator();
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(2155));
      assertNotNull(spliterator0);
      
      Duration duration0 = Duration.ofSeconds(1665L, 1885L);
      assertNotNull(duration0);
      
      Duration duration1 = duration0.plusMillis(2288L);
      assertNotSame(duration0, duration1);
      assertNotSame(duration1, duration0);
      assertNotNull(duration1);
      assertFalse(duration1.equals((Object)duration0));
      
      Duration duration2 = duration0.abs();
      assertSame(duration0, duration2);
      assertNotSame(duration0, duration1);
      assertSame(duration2, duration0);
      assertNotSame(duration2, duration1);
      assertNotNull(duration2);
      assertFalse(duration0.equals((Object)duration1));
      assertFalse(duration2.equals((Object)duration1));
      
      TimeUnit timeUnit1 = TimeUnit.NANOSECONDS;
      Integer integer1 = new Integer(0);
      assertEquals(0, (int)integer1);
      assertNotNull(integer1);
      assertFalse(integer1.equals((Object)int0));
      assertFalse(integer1.equals((Object)integer0));
      
      boolean boolean1 = linkedBlockingDeque0.offer(integer1);
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(0));
      assertTrue(boolean1);
      assertFalse(integer1.equals((Object)int0));
      assertFalse(integer1.equals((Object)integer0));
      assertTrue(boolean1 == boolean0);
      
      Integer integer2 = new Integer(0);
      assertEquals(0, (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer0));
      assertTrue(integer2.equals((Object)integer1));
      
      linkedBlockingDeque0.putFirst(integer2);
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(integer2));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer0));
      assertTrue(integer2.equals((Object)integer1));
      
      boolean boolean2 = linkedBlockingDeque0.offerFirst2(integer0, 0L, timeUnit1);
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(integer2));
      assertTrue(boolean2);
      assertNotSame(timeUnit1, timeUnit0);
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)integer2));
      assertFalse(integer0.equals((Object)integer1));
      assertFalse(timeUnit1.equals((Object)timeUnit0));
      assertTrue(boolean2 == boolean0);
      assertTrue(boolean2 == boolean1);
      
      linkedBlockingDeque0.interuptTakeWaiters();
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(integer2));
      
      linkedBlockingDeque0.putLast(integer1);
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(integer2));
      assertTrue(integer1.equals((Object)integer2));
      assertFalse(integer1.equals((Object)int0));
      assertFalse(integer1.equals((Object)integer0));
      
      Integer integer3 = linkedBlockingDeque0.removeLast();
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(integer2));
      assertEquals(0, (int)integer3);
      assertNotNull(integer3);
      assertFalse(integer3.equals((Object)int0));
      assertFalse(integer3.equals((Object)integer0));
      assertTrue(integer3.equals((Object)integer2));
      
      Integer[] integerArray0 = new Integer[4];
      integerArray0[0] = integer0;
      integerArray0[1] = integer0;
      integerArray0[2] = null;
      integerArray0[3] = integer3;
      String string0 = linkedBlockingDeque0.toString();
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertTrue(linkedBlockingDeque0.contains(integer2));
      assertEquals("[2155, 0, 2155, 0]", string0);
      assertNotNull(string0);
      
      Integer integer4 = linkedBlockingDeque0.takeLast();
      assertFalse(linkedBlockingDeque0.contains(7));
      assertTrue(linkedBlockingDeque0.contains(0));
      assertEquals(0, (int)integer4);
      assertNotNull(integer4);
      assertTrue(integer4.equals((Object)integer2));
      assertFalse(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)integer0));
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int int0 = 0;
      boolean boolean0 = true;
      int int1 = 2;
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertFalse(linkedList0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      List<Integer> list0 = List.copyOf((Collection<? extends Integer>) linkedList0);
      assertFalse(linkedList0.contains(int0));
      assertFalse(list0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertEquals(0, list0.size());
      assertTrue(list0.isEmpty());
      assertNotNull(list0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 2, true, list0);
      assertFalse(linkedList0.contains(1));
      assertFalse(list0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertEquals(0, linkedList0.size());
      assertEquals(0, list0.size());
      assertTrue(list0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-6730), 0, false, linkedBlockingDeque0);
      assertFalse(linkedList0.contains(0));
      assertFalse(list0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(0, linkedList0.size());
      assertEquals(0, list0.size());
      assertTrue(list0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      TimeUnit timeUnit0 = TimeUnit.HOURS;
      Integer integer0 = linkedBlockingDeque1.pollLast2(0, timeUnit0);
      assertFalse(linkedList0.contains(0));
      assertFalse(list0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(0, linkedList0.size());
      assertEquals(0, list0.size());
      assertTrue(list0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNull(integer0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Object object0 = new Object();
      assertNotNull(object0);
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.removeFirst();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Integer integer0 = new Integer((-118));
      assertEquals((-118), (int)integer0);
      assertNotNull(integer0);
      
      List<Integer> list0 = List.of(integer0);
      assertTrue(list0.contains(integer0));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotNull(list0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-118), (-245), true, list0);
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains((-245)));
      assertFalse(linkedBlockingDeque0.contains((-118)));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer1 = linkedBlockingDeque0.pollLast0();
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains((-245)));
      assertFalse(linkedBlockingDeque0.contains((-118)));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNull(integer1);
      
      int int0 = (-1);
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-1), (-118), true, list0);
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains(int0));
      assertFalse(linkedBlockingDeque1.contains((-118)));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(integer0.equals((Object)int0));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer2 = new Integer(1);
      assertEquals(1, (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer0));
      
      boolean boolean0 = linkedBlockingDeque1.offer(integer0);
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains(int0));
      assertFalse(linkedBlockingDeque1.contains((-118)));
      assertFalse(boolean0);
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)integer2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(0, Integer.MAX_VALUE, false, linkedBlockingDeque0);
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque2.contains(Integer.MAX_VALUE));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)integer2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      Object object0 = linkedBlockingDeque2.pollFirst();
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque2.contains(Integer.MAX_VALUE));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNull(object0);
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)integer2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertFalse(linkedHashSet0.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      boolean boolean1 = linkedHashSet0.remove(integer2);
      assertFalse(linkedHashSet0.contains(Integer.MAX_VALUE));
      assertFalse(boolean1);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer0));
      assertTrue(boolean1 == boolean0);
      
      LinkedBlockingDeque linkedBlockingDeque3 = LinkedBlockingDeque.LinkedBlockingDeque1(false);
      assertNotNull(linkedBlockingDeque3);
      
      int int1 = linkedBlockingDeque1.remainingCapacity();
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque1.contains(Integer.MAX_VALUE));
      assertEquals((-118), int1);
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)integer2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(int1 == int0);
      
      Integer integer3 = new Integer(1);
      assertEquals(1, (int)integer3);
      assertNotNull(integer3);
      assertFalse(integer3.equals((Object)integer0));
      assertFalse(integer3.equals((Object)int1));
      assertTrue(integer3.equals((Object)integer2));
      assertFalse(integer3.equals((Object)int0));
      
      Integer integer4 = new Integer((-245));
      assertEquals((-245), (int)integer4);
      assertNotNull(integer4);
      assertFalse(integer4.equals((Object)integer0));
      assertFalse(integer4.equals((Object)int1));
      assertFalse(integer4.equals((Object)integer2));
      assertFalse(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)integer3));
      
      linkedBlockingDeque2.putLast(integer4);
      assertTrue(list0.contains((-118)));
      assertFalse(list0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque2.contains(integer4));
      assertFalse(linkedBlockingDeque2.contains(Integer.MAX_VALUE));
      assertEquals(1, list0.size());
      assertFalse(list0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertTrue(integer0.equals((Object)int1));
      assertFalse(integer0.equals((Object)integer3));
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)integer4));
      assertFalse(integer0.equals((Object)integer2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(integer4.equals((Object)integer0));
      assertFalse(integer4.equals((Object)int1));
      assertFalse(integer4.equals((Object)integer2));
      assertFalse(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)integer3));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.removeLast();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 0, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer(1);
      assertEquals(1, (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedHashSet0.add(integer0);
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(linkedHashSet0.contains(1));
      assertTrue(boolean0);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      
      boolean boolean1 = linkedBlockingDeque0.offerFirst0(integer0);
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(boolean1);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(boolean1 == boolean0);
      
      boolean boolean2 = linkedBlockingDeque0.contains((Object) null);
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(boolean2);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(boolean2 == boolean0);
      assertTrue(boolean2 == boolean1);
      
      boolean boolean3 = linkedBlockingDeque0.hasTakeWaiters();
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(boolean3);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertTrue(boolean3 == boolean2);
      assertTrue(boolean3 == boolean1);
      assertFalse(boolean3 == boolean0);
      
      Duration duration0 = Duration.ZERO;
      assertNotNull(duration0);
      
      boolean boolean4 = linkedBlockingDeque0.offerLast1(integer0, duration0);
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(boolean4);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertTrue(boolean4 == boolean1);
      assertFalse(boolean4 == boolean0);
      assertTrue(boolean4 == boolean2);
      assertTrue(boolean4 == boolean3);
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.remove0();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedList0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      Integer integer0 = new Integer((-1800));
      assertEquals((-1800), (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedBlockingDeque0.offerLast(integer0);
      assertFalse(linkedList0.contains((-1800)));
      assertTrue(linkedBlockingDeque0.contains((-1800)));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertTrue(boolean0);
      assertEquals(0, linkedList0.size());
      
      Integer integer1 = linkedBlockingDeque0.pollLast2(371L, timeUnit0);
      assertFalse(linkedList0.contains((-1800)));
      assertFalse(linkedBlockingDeque0.contains((-1800)));
      assertEquals((-1800), (int)integer1);
      assertEquals(0, linkedList0.size());
      assertNotNull(integer1);
      
      linkedBlockingDeque0.push(integer1);
      assertFalse(linkedList0.contains((-1800)));
      assertTrue(linkedBlockingDeque0.contains((-1800)));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      
      Object object0 = new Object();
      assertNotNull(object0);
      
      boolean boolean1 = linkedBlockingDeque0.remove1(object0);
      assertFalse(linkedList0.contains((-1800)));
      assertTrue(linkedBlockingDeque0.contains((-1800)));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(boolean1);
      assertEquals(0, linkedList0.size());
      assertFalse(boolean1 == boolean0);
      
      Integer integer2 = linkedBlockingDeque0.removeFirst();
      assertFalse(linkedList0.contains(integer2));
      assertFalse(linkedBlockingDeque0.contains(integer2));
      assertEquals((-1800), (int)integer2);
      assertEquals(0, linkedList0.size());
      assertNotNull(integer2);
      
      Integer integer3 = new Integer(0);
      assertEquals(0, (int)integer3);
      assertNotNull(integer3);
      assertFalse(integer3.equals((Object)integer0));
      assertFalse(integer3.equals((Object)integer1));
      assertFalse(integer3.equals((Object)integer2));
      
      Object[] objectArray0 = linkedBlockingDeque0.toArray();
      assertFalse(linkedList0.contains(integer2));
      assertFalse(linkedBlockingDeque0.contains(integer2));
      assertEquals(0, objectArray0.length);
      assertEquals(0, linkedList0.size());
      assertNotNull(objectArray0);
      
      boolean boolean2 = linkedBlockingDeque0.offerLast0(integer3);
      assertFalse(linkedList0.contains(integer2));
      assertTrue(linkedBlockingDeque0.contains(integer3));
      assertFalse(linkedBlockingDeque0.contains(integer2));
      assertTrue(boolean2);
      assertEquals(0, linkedList0.size());
      assertFalse(integer3.equals((Object)integer0));
      assertFalse(integer3.equals((Object)integer1));
      assertFalse(integer3.equals((Object)integer2));
      assertTrue(boolean2 == boolean0);
      assertFalse(boolean2 == boolean1);
      
      // Undeclared exception!
      try { 
        LinkedBlockingDeque.LinkedBlockingDeque3(0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-166), 2, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-166)));
      assertFalse(linkedBlockingDeque0.contains((-166)));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque0);
      
      int int0 = Integer.MAX_VALUE;
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(2, Integer.MAX_VALUE, false, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(2));
      assertFalse(linkedBlockingDeque1.contains(2));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer((-1534));
      assertEquals((-1534), (int)integer0);
      assertNotNull(integer0);
      assertFalse(integer0.equals((Object)int0));
      
      boolean boolean0 = linkedBlockingDeque1.add(integer0);
      assertFalse(linkedHashSet0.contains(2));
      assertFalse(linkedBlockingDeque1.contains(2));
      assertTrue(linkedBlockingDeque1.contains(integer0));
      assertTrue(boolean0);
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(integer0.equals((Object)int0));
      
      int int1 = 903;
      Integer integer1 = new Integer(903);
      assertEquals(903, (int)integer1);
      assertNotNull(integer1);
      assertFalse(integer1.equals((Object)int0));
      assertTrue(integer1.equals((Object)int1));
      assertFalse(integer1.equals((Object)integer0));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(2, (-13), true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(int1));
      assertFalse(linkedBlockingDeque2.contains(int1));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      Integer integer2 = new Integer(1);
      assertEquals(1, (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      assertFalse(integer2.equals((Object)integer0));
      assertFalse(integer2.equals((Object)int1));
      
      ChronoUnit chronoUnit0 = ChronoUnit.DECADES;
      assertEquals(ChronoUnit.DECADES, chronoUnit0);
      
      // Undeclared exception!
      try { 
        Duration.of(Integer.MAX_VALUE, chronoUnit0);
        fail("Expecting exception: UnsupportedTemporalTypeException");
      
      } catch(UnsupportedTemporalTypeException e) {
         //
         // Unit must not have an estimated duration
         //
         verifyException("java.time.Duration", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int int0 = 183;
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1828, (-948), false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(1828));
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = linkedBlockingDeque0.pollLast0();
      assertFalse(linkedBlockingDeque0.contains(1828));
      assertNull(integer0);
      
      int int1 = 1103;
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(1103, 1, false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque1.contains(1));
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      int int2 = 4;
      Integer integer1 = new Integer(4);
      assertEquals(4, (int)integer1);
      assertNotNull(integer1);
      assertFalse(integer1.equals((Object)int0));
      assertFalse(integer1.equals((Object)int1));
      assertTrue(integer1.equals((Object)int2));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.offer((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int int0 = (-626);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertFalse(linkedHashSet0.contains(int0));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-626), 2302, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-626)));
      assertFalse(linkedBlockingDeque0.contains((-626)));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedHashSet<Integer> linkedHashSet1 = new LinkedHashSet<Integer>(linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains((-626)));
      assertFalse(linkedBlockingDeque0.contains((-626)));
      assertFalse(linkedHashSet1.contains((-626)));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertTrue(linkedHashSet1.isEmpty());
      assertEquals(0, linkedHashSet1.size());
      assertNotNull(linkedHashSet1);
      assertTrue(linkedHashSet1.equals((Object)linkedHashSet0));
      
      boolean boolean0 = linkedBlockingDeque0.containsAll(linkedHashSet1);
      assertFalse(linkedHashSet0.contains((-626)));
      assertFalse(linkedBlockingDeque0.contains((-626)));
      assertFalse(linkedHashSet1.contains((-626)));
      assertTrue(boolean0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertTrue(linkedHashSet1.isEmpty());
      assertEquals(0, linkedHashSet1.size());
      assertNotSame(linkedHashSet0, linkedHashSet1);
      assertNotSame(linkedHashSet1, linkedHashSet0);
      assertTrue(linkedHashSet0.equals((Object)linkedHashSet1));
      assertTrue(linkedHashSet1.equals((Object)linkedHashSet0));
      
      Integer integer0 = null;
      Duration duration0 = Duration.ofHours(2302);
      assertNotNull(duration0);
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.offerFirst1((Integer) null, duration0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LinkedBlockingDeque linkedBlockingDeque0 = LinkedBlockingDeque.LinkedBlockingDeque0();
      assertNotNull(linkedBlockingDeque0);
      
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedList0);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque1);
      
      Object[] objectArray0 = linkedBlockingDeque1.toArray0();
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertEquals(0, objectArray0.length);
      assertEquals(0, linkedList0.size());
      assertNotNull(objectArray0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedBlockingDeque1);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertFalse(linkedBlockingDeque2.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque3 = new LinkedBlockingDeque<Integer>((-603), 1119, false, linkedBlockingDeque2);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertFalse(linkedBlockingDeque2.contains(535));
      assertFalse(linkedBlockingDeque3.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque3);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque1));
      
      Duration duration0 = Duration.ZERO;
      assertNotNull(duration0);
      
      LinkedBlockingDeque linkedBlockingDeque4 = LinkedBlockingDeque.LinkedBlockingDeque2(linkedBlockingDeque1);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque4, linkedBlockingDeque0);
      assertNotNull(linkedBlockingDeque4);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque4.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = linkedBlockingDeque3.pollFirst1(duration0);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertFalse(linkedBlockingDeque2.contains(535));
      assertFalse(linkedBlockingDeque3.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque3, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque3, linkedBlockingDeque1);
      assertNull(integer0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque1));
      
      Integer integer1 = null;
      Integer integer2 = new Integer(0);
      assertEquals(0, (int)integer2);
      assertNotNull(integer2);
      
      boolean boolean0 = linkedList0.add(integer2);
      assertFalse(linkedList0.contains(535));
      assertTrue(linkedList0.contains(integer2));
      assertTrue(boolean0);
      assertEquals(1, linkedList0.size());
      
      Integer integer3 = linkedBlockingDeque1.pollFirst1(duration0);
      assertFalse(linkedList0.contains(535));
      assertTrue(linkedList0.contains(integer2));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertEquals(1, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNull(integer3);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.offerFirst2((Integer) null, (-1L), timeUnit0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(0, 290, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(290));
      assertFalse(linkedBlockingDeque0.contains(290));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(290, 3, true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = linkedBlockingDeque1.pollLast0();
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNull(integer0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(0, 1, true, linkedBlockingDeque1);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertFalse(linkedBlockingDeque2.contains(1));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      Integer integer1 = new Integer(0);
      assertEquals(0, (int)integer1);
      assertNotNull(integer1);
      
      boolean boolean0 = linkedBlockingDeque2.offer(integer1);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertTrue(linkedBlockingDeque2.contains(0));
      assertFalse(linkedBlockingDeque2.contains(1));
      assertTrue(boolean0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      Object object0 = linkedBlockingDeque2.pollFirst();
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertFalse(linkedBlockingDeque2.contains(0));
      assertEquals(0, object0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotNull(object0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      boolean boolean1 = linkedHashSet0.remove(object0);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertFalse(linkedBlockingDeque2.contains(0));
      assertFalse(boolean1);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(boolean1 == boolean0);
      
      LinkedBlockingDeque linkedBlockingDeque3 = LinkedBlockingDeque.LinkedBlockingDeque1(true);
      assertNotNull(linkedBlockingDeque3);
      
      int int0 = linkedBlockingDeque1.remainingCapacity();
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(3, int0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer2 = new Integer(290);
      assertEquals(290, (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)object0));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      
      linkedBlockingDeque0.putLast(integer2);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertTrue(linkedBlockingDeque0.contains(290));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer2.equals((Object)object0));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      
      Integer integer3 = linkedBlockingDeque0.removeLast();
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertEquals(290, (int)integer3);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(integer3);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer3.equals((Object)integer1));
      assertFalse(integer3.equals((Object)object0));
      assertFalse(integer3.equals((Object)int0));
      
      Integer[] integerArray0 = new Integer[4];
      integerArray0[0] = null;
      Integer integer4 = new Integer(3);
      assertEquals(3, (int)integer4);
      assertNotNull(integer4);
      assertFalse(integer4.equals((Object)object0));
      assertFalse(integer4.equals((Object)integer1));
      assertFalse(integer4.equals((Object)integer2));
      assertFalse(integer4.equals((Object)integer3));
      assertTrue(integer4.equals((Object)int0));
      
      integerArray0[1] = integer4;
      integerArray0[2] = integer3;
      integerArray0[3] = integer1;
      Integer[] integerArray1 = linkedBlockingDeque1.toArray1(integerArray0);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(4, integerArray1.length);
      assertEquals(4, integerArray0.length);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertSame(integerArray1, integerArray0);
      assertSame(integerArray0, integerArray1);
      assertNotNull(integerArray1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(4, 1286, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(4));
      assertFalse(linkedBlockingDeque0.contains(4));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(1286, 3, true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(4));
      assertFalse(linkedBlockingDeque0.contains(4));
      assertFalse(linkedBlockingDeque1.contains(4));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      int int0 = linkedBlockingDeque0.drainTo1(linkedBlockingDeque1, 0);
      assertFalse(linkedHashSet0.contains(3));
      assertFalse(linkedBlockingDeque0.contains(3));
      assertFalse(linkedBlockingDeque1.contains(3));
      assertEquals(0, int0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = linkedBlockingDeque1.peekFirst();
      assertFalse(linkedHashSet0.contains(3));
      assertFalse(linkedBlockingDeque0.contains(3));
      assertFalse(linkedBlockingDeque1.contains(3));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNull(integer0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LinkedBlockingDeque linkedBlockingDeque0 = LinkedBlockingDeque.LinkedBlockingDeque0();
      assertNotNull(linkedBlockingDeque0);
      
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedList0);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque1);
      
      Object[] objectArray0 = linkedBlockingDeque1.toArray0();
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertEquals(0, objectArray0.length);
      assertEquals(0, linkedList0.size());
      assertNotNull(objectArray0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedBlockingDeque1);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertFalse(linkedBlockingDeque2.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque3 = new LinkedBlockingDeque<Integer>((-603), 1119, false, linkedBlockingDeque2);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertFalse(linkedBlockingDeque2.contains((-603)));
      assertFalse(linkedBlockingDeque3.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque3);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque2));
      
      Duration duration0 = Duration.ZERO;
      assertNotNull(duration0);
      
      LinkedBlockingDeque linkedBlockingDeque4 = LinkedBlockingDeque.LinkedBlockingDeque2(linkedBlockingDeque1);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque4, linkedBlockingDeque0);
      assertNotNull(linkedBlockingDeque4);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque4.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = linkedBlockingDeque3.pollFirst1(duration0);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertFalse(linkedBlockingDeque2.contains((-603)));
      assertFalse(linkedBlockingDeque3.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque3, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque3, linkedBlockingDeque2);
      assertNull(integer0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque2));
      
      int int0 = linkedBlockingDeque2.getTakeQueueLength();
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertFalse(linkedBlockingDeque2.contains((-603)));
      assertEquals(0, int0);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque3);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque3));
      
      Integer integer1 = linkedBlockingDeque3.pollFirst0();
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertFalse(linkedBlockingDeque2.contains((-603)));
      assertFalse(linkedBlockingDeque3.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque3, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque3, linkedBlockingDeque2);
      assertNull(integer1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque2));
      
      int int1 = (-1);
      LinkedBlockingDeque<Integer> linkedBlockingDeque5 = new LinkedBlockingDeque<Integer>((-1), (-1), true, linkedBlockingDeque1);
      assertFalse(linkedList0.contains((-603)));
      assertFalse(linkedBlockingDeque1.contains((-603)));
      assertFalse(linkedBlockingDeque5.contains((-603)));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque5);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque5.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque5.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque5.equals((Object)linkedBlockingDeque2));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque5.element();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>(linkedList0);
      assertEquals(0, linkedList0.size());
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(399, (-2079), false, linkedHashSet0);
      assertFalse(linkedList0.contains(399));
      assertFalse(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque0.contains(399));
      assertEquals(0, linkedList0.size());
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      int int0 = linkedBlockingDeque0.remainingCapacity();
      assertFalse(linkedList0.contains(399));
      assertFalse(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque0.contains(399));
      assertEquals((-2079), int0);
      assertEquals(0, linkedList0.size());
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-948), (-262), true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-262)));
      assertFalse(linkedBlockingDeque0.contains((-262)));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(1, 1, true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer[] integerArray0 = new Integer[2];
      Integer integer0 = new Integer(0);
      assertEquals(0, (int)integer0);
      assertNotNull(integer0);
      
      integerArray0[0] = integer0;
      Integer integer1 = new Integer((-2340));
      assertEquals((-2340), (int)integer1);
      assertNotNull(integer1);
      assertFalse(integer1.equals((Object)integer0));
      
      integerArray0[1] = integer1;
      Integer[] integerArray1 = linkedHashSet0.toArray(integerArray0);
      assertFalse(linkedHashSet0.contains(1));
      assertEquals(2, integerArray0.length);
      assertEquals(2, integerArray1.length);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertSame(integerArray0, integerArray1);
      assertSame(integerArray1, integerArray0);
      assertNotNull(integerArray1);
      
      Integer integer2 = new Integer((-1729));
      assertEquals((-1729), (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)integer0));
      assertFalse(integer2.equals((Object)integer1));
      
      linkedBlockingDeque1.put(integer2);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertTrue(linkedBlockingDeque1.contains((-1729)));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(integer2.equals((Object)integer0));
      assertFalse(integer2.equals((Object)integer1));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.removeFirst();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedList0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      Integer integer0 = linkedBlockingDeque0.pollLast2(371L, timeUnit0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNull(integer0);
      
      Object object0 = new Object();
      assertNotNull(object0);
      
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertFalse(linkedHashSet0.contains(917));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      boolean boolean0 = linkedHashSet0.add((Integer) null);
      assertFalse(linkedHashSet0.contains(917));
      assertTrue(boolean0);
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(399, 399, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque1.contains(917));
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      linkedBlockingDeque1.clear();
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque1.contains(917));
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      linkedBlockingDeque0.clear();
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      
      Integer integer1 = new Integer((-6109));
      assertEquals((-6109), (int)integer1);
      assertNotNull(integer1);
      
      Integer integer2 = new Integer((-2795));
      assertEquals((-2795), (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)integer1));
      
      linkedBlockingDeque1.addLast(integer2);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedBlockingDeque1.contains((-2795)));
      assertFalse(linkedBlockingDeque1.contains((-6109)));
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(integer2.equals((Object)integer1));
      
      int int0 = linkedBlockingDeque1.getTakeQueueLength();
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedBlockingDeque1.contains((-2795)));
      assertFalse(linkedBlockingDeque1.contains((-6109)));
      assertEquals(0, int0);
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer3 = new Integer(669);
      assertEquals(669, (int)integer3);
      assertNotNull(integer3);
      assertFalse(integer3.equals((Object)integer1));
      assertFalse(integer3.equals((Object)int0));
      assertFalse(integer3.equals((Object)integer2));
      
      Integer integer4 = new Integer(399);
      assertEquals(399, (int)integer4);
      assertNotNull(integer4);
      assertFalse(integer4.equals((Object)integer1));
      assertFalse(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)integer2));
      assertFalse(integer4.equals((Object)integer3));
      
      boolean boolean1 = linkedHashSet0.add(integer4);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertTrue(boolean1);
      assertEquals(2, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertFalse(integer4.equals((Object)integer1));
      assertFalse(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)integer2));
      assertFalse(integer4.equals((Object)integer3));
      
      Integer integer5 = new Integer((-6109));
      assertEquals((-6109), (int)integer5);
      assertNotNull(integer5);
      assertFalse(integer5.equals((Object)integer2));
      assertFalse(integer5.equals((Object)int0));
      assertFalse(integer5.equals((Object)integer3));
      assertFalse(integer5.equals((Object)integer4));
      assertTrue(integer5.equals((Object)integer1));
      
      boolean boolean2 = linkedBlockingDeque1.removeLastOccurrence(integer5);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(integer4));
      assertTrue(linkedBlockingDeque1.contains((-2795)));
      assertFalse(linkedBlockingDeque1.contains((-6109)));
      assertFalse(boolean2);
      assertEquals(2, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(integer5.equals((Object)integer2));
      assertFalse(integer5.equals((Object)int0));
      assertFalse(integer5.equals((Object)integer3));
      assertFalse(integer5.equals((Object)integer4));
      assertTrue(integer5.equals((Object)integer1));
      assertFalse(boolean2 == boolean1);
      assertFalse(boolean2 == boolean0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer6 = new Integer((-2096));
      assertEquals((-2096), (int)integer6);
      assertNotNull(integer6);
      assertFalse(integer6.equals((Object)integer2));
      assertFalse(integer6.equals((Object)integer1));
      assertFalse(integer6.equals((Object)int0));
      assertFalse(integer6.equals((Object)integer5));
      assertFalse(integer6.equals((Object)integer3));
      assertFalse(integer6.equals((Object)integer4));
      
      linkedBlockingDeque0.addFirst(integer6);
      assertFalse(linkedList0.contains((-6109)));
      assertTrue(linkedBlockingDeque0.contains((-2096)));
      assertFalse(linkedBlockingDeque0.contains((-6109)));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer6.equals((Object)integer2));
      assertFalse(integer6.equals((Object)integer1));
      assertFalse(integer6.equals((Object)int0));
      assertFalse(integer6.equals((Object)integer5));
      assertFalse(integer6.equals((Object)integer3));
      assertFalse(integer6.equals((Object)integer4));
      
      Integer integer7 = linkedBlockingDeque1.removeFirst();
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(integer4));
      assertFalse(linkedBlockingDeque1.contains((-6109)));
      assertEquals((-2795), (int)integer7);
      assertEquals(2, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotNull(integer7);
      assertFalse(integer7.equals((Object)integer3));
      assertFalse(integer7.equals((Object)int0));
      assertFalse(integer7.equals((Object)integer1));
      assertFalse(integer7.equals((Object)integer4));
      assertFalse(integer7.equals((Object)integer6));
      assertFalse(integer7.equals((Object)integer5));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer8 = new Integer(399);
      assertEquals(399, (int)integer8);
      assertNotNull(integer8);
      assertFalse(integer8.equals((Object)integer2));
      assertFalse(integer8.equals((Object)integer1));
      assertFalse(integer8.equals((Object)integer3));
      assertTrue(integer8.equals((Object)integer4));
      assertFalse(integer8.equals((Object)int0));
      assertFalse(integer8.equals((Object)integer5));
      assertFalse(integer8.equals((Object)integer6));
      assertFalse(integer8.equals((Object)integer7));
      
      boolean boolean3 = linkedHashSet0.add(integer8);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertFalse(boolean3);
      assertEquals(2, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertFalse(integer8.equals((Object)integer2));
      assertFalse(integer8.equals((Object)integer1));
      assertFalse(integer8.equals((Object)integer3));
      assertTrue(integer8.equals((Object)integer4));
      assertFalse(integer8.equals((Object)int0));
      assertFalse(integer8.equals((Object)integer5));
      assertFalse(integer8.equals((Object)integer6));
      assertFalse(integer8.equals((Object)integer7));
      assertTrue(boolean3 == boolean2);
      assertFalse(boolean3 == boolean0);
      assertFalse(boolean3 == boolean1);
      
      Integer integer9 = linkedBlockingDeque1.peek();
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains((-6109)));
      assertEquals(2, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNull(integer9);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer10 = linkedBlockingDeque0.getLast();
      assertFalse(linkedList0.contains((-6109)));
      assertTrue(linkedBlockingDeque0.contains((-2096)));
      assertFalse(linkedBlockingDeque0.contains((-6109)));
      assertEquals((-2096), (int)integer10);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(integer10);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer10.equals((Object)int0));
      assertFalse(integer10.equals((Object)integer3));
      assertFalse(integer10.equals((Object)integer2));
      assertFalse(integer10.equals((Object)integer5));
      assertFalse(integer10.equals((Object)integer7));
      assertFalse(integer10.equals((Object)integer8));
      assertFalse(integer10.equals((Object)integer1));
      assertFalse(integer10.equals((Object)integer4));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>((-1177), 0, true, linkedBlockingDeque1);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains((-6109)));
      assertFalse(linkedBlockingDeque2.contains((-6109)));
      assertEquals(2, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque2.offerFirst0((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedList0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      Integer integer0 = linkedBlockingDeque0.pollLast2(371L, timeUnit0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNull(integer0);
      
      Object object0 = new Object();
      assertNotNull(object0);
      
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertFalse(linkedHashSet0.contains(917));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      boolean boolean0 = linkedHashSet0.add((Integer) null);
      assertFalse(linkedHashSet0.contains(917));
      assertTrue(boolean0);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      
      int int0 = 399;
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(399, 399, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains(399));
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      linkedBlockingDeque1.clear();
      assertFalse(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains(399));
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      linkedBlockingDeque0.clear();
      assertFalse(linkedList0.contains(399));
      assertFalse(linkedBlockingDeque0.contains(399));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      
      Integer integer1 = new Integer((-6109));
      assertEquals((-6109), (int)integer1);
      assertNotNull(integer1);
      assertFalse(integer1.equals((Object)int0));
      
      Integer integer2 = new Integer((-2795));
      assertEquals((-2795), (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      
      linkedBlockingDeque1.addLast(integer2);
      assertFalse(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains(399));
      assertTrue(linkedBlockingDeque1.contains(integer2));
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      
      int int1 = linkedBlockingDeque1.getTakeQueueLength();
      assertFalse(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains(399));
      assertTrue(linkedBlockingDeque1.contains(integer2));
      assertEquals(0, int1);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(int1 == int0);
      
      Integer integer3 = new Integer(669);
      assertEquals(669, (int)integer3);
      assertNotNull(integer3);
      assertFalse(integer3.equals((Object)integer1));
      assertFalse(integer3.equals((Object)int0));
      assertFalse(integer3.equals((Object)integer2));
      assertFalse(integer3.equals((Object)int1));
      
      Integer integer4 = new Integer(399);
      assertEquals(399, (int)integer4);
      assertNotNull(integer4);
      assertFalse(integer4.equals((Object)integer1));
      assertTrue(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)int1));
      assertFalse(integer4.equals((Object)integer3));
      assertFalse(integer4.equals((Object)integer2));
      
      linkedHashSet0.clear();
      assertFalse(linkedHashSet0.contains(399));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      
      boolean boolean1 = linkedHashSet0.add(integer4);
      assertFalse(linkedHashSet0.contains(integer3));
      assertTrue(linkedHashSet0.contains(399));
      assertTrue(boolean1);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(integer4.equals((Object)integer1));
      assertTrue(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)int1));
      assertFalse(integer4.equals((Object)integer3));
      assertFalse(integer4.equals((Object)integer2));
      
      Integer integer5 = new Integer((-6109));
      assertEquals((-6109), (int)integer5);
      assertNotNull(integer5);
      assertTrue(integer5.equals((Object)integer1));
      assertFalse(integer5.equals((Object)integer2));
      assertFalse(integer5.equals((Object)int1));
      assertFalse(integer5.equals((Object)int0));
      assertFalse(integer5.equals((Object)integer3));
      assertFalse(integer5.equals((Object)integer4));
      
      boolean boolean2 = linkedBlockingDeque1.removeLastOccurrence(integer5);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains(399));
      assertTrue(linkedBlockingDeque1.contains(integer2));
      assertFalse(boolean2);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertTrue(integer5.equals((Object)integer1));
      assertFalse(integer5.equals((Object)integer2));
      assertFalse(integer5.equals((Object)int1));
      assertFalse(integer5.equals((Object)int0));
      assertFalse(integer5.equals((Object)integer3));
      assertFalse(integer5.equals((Object)integer4));
      assertFalse(boolean2 == boolean1);
      assertFalse(boolean2 == boolean0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer6 = new Integer((-2096));
      assertEquals((-2096), (int)integer6);
      assertNotNull(integer6);
      assertFalse(integer6.equals((Object)int0));
      assertFalse(integer6.equals((Object)integer3));
      assertFalse(integer6.equals((Object)integer2));
      assertFalse(integer6.equals((Object)int1));
      assertFalse(integer6.equals((Object)integer1));
      assertFalse(integer6.equals((Object)integer4));
      assertFalse(integer6.equals((Object)integer5));
      
      linkedBlockingDeque0.addFirst(integer6);
      assertFalse(linkedList0.contains(399));
      assertFalse(linkedBlockingDeque0.contains(399));
      assertTrue(linkedBlockingDeque0.contains((-2096)));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer6.equals((Object)int0));
      assertFalse(integer6.equals((Object)integer3));
      assertFalse(integer6.equals((Object)integer2));
      assertFalse(integer6.equals((Object)int1));
      assertFalse(integer6.equals((Object)integer1));
      assertFalse(integer6.equals((Object)integer4));
      assertFalse(integer6.equals((Object)integer5));
      
      Integer integer7 = linkedBlockingDeque1.removeFirst();
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertFalse(linkedBlockingDeque1.contains(399));
      assertEquals((-2795), (int)integer7);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotNull(integer7);
      assertFalse(integer7.equals((Object)integer5));
      assertFalse(integer7.equals((Object)int1));
      assertFalse(integer7.equals((Object)integer6));
      assertFalse(integer7.equals((Object)integer3));
      assertFalse(integer7.equals((Object)int0));
      assertFalse(integer7.equals((Object)integer1));
      assertFalse(integer7.equals((Object)integer4));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer8 = new Integer(399);
      assertEquals(399, (int)integer8);
      assertNotNull(integer8);
      assertFalse(integer8.equals((Object)integer6));
      assertFalse(integer8.equals((Object)int1));
      assertFalse(integer8.equals((Object)integer3));
      assertFalse(integer8.equals((Object)integer2));
      assertTrue(integer8.equals((Object)int0));
      assertFalse(integer8.equals((Object)integer5));
      assertTrue(integer8.equals((Object)integer4));
      assertFalse(integer8.equals((Object)integer7));
      assertFalse(integer8.equals((Object)integer1));
      
      boolean boolean3 = linkedHashSet0.add(integer8);
      assertFalse(linkedHashSet0.contains((-6109)));
      assertTrue(linkedHashSet0.contains(399));
      assertFalse(boolean3);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(integer8.equals((Object)integer6));
      assertFalse(integer8.equals((Object)int1));
      assertFalse(integer8.equals((Object)integer3));
      assertFalse(integer8.equals((Object)integer2));
      assertTrue(integer8.equals((Object)int0));
      assertFalse(integer8.equals((Object)integer5));
      assertTrue(integer8.equals((Object)integer4));
      assertFalse(integer8.equals((Object)integer7));
      assertFalse(integer8.equals((Object)integer1));
      assertFalse(boolean3 == boolean0);
      assertTrue(boolean3 == boolean2);
      assertFalse(boolean3 == boolean1);
      
      Integer integer9 = linkedBlockingDeque0.peek();
      assertFalse(linkedList0.contains(399));
      assertFalse(linkedBlockingDeque0.contains(399));
      assertTrue(linkedBlockingDeque0.contains(integer9));
      assertEquals((-2096), (int)integer9);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(integer9);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer9.equals((Object)int1));
      assertFalse(integer9.equals((Object)integer5));
      assertFalse(integer9.equals((Object)integer2));
      assertFalse(integer9.equals((Object)integer3));
      assertFalse(integer9.equals((Object)integer1));
      assertFalse(integer9.equals((Object)integer8));
      assertFalse(integer9.equals((Object)integer4));
      assertFalse(integer9.equals((Object)int0));
      assertFalse(integer9.equals((Object)integer7));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.getLast();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int int0 = 2969;
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertFalse(linkedHashSet0.contains(int0));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(2969, 2969, false, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(2969));
      assertFalse(linkedBlockingDeque0.contains(2969));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer(1);
      assertEquals(1, (int)integer0);
      assertNotNull(integer0);
      assertFalse(integer0.equals((Object)int0));
      
      boolean boolean0 = linkedHashSet0.add(integer0);
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedHashSet0.contains(2969));
      assertTrue(boolean0);
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertFalse(integer0.equals((Object)int0));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.getLast();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-1), (-1), true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-1)));
      assertFalse(linkedBlockingDeque0.contains((-1)));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer((-1));
      assertEquals((-1), (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedHashSet0.add(integer0);
      assertTrue(linkedHashSet0.contains(integer0));
      assertTrue(boolean0);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      
      linkedBlockingDeque0.clear();
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedBlockingDeque0.contains(integer0));
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      
      linkedBlockingDeque0.clear();
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedBlockingDeque0.contains(integer0));
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      
      Integer integer1 = new Integer((-1));
      assertEquals((-1), (int)integer1);
      assertNotNull(integer1);
      assertTrue(integer1.equals((Object)integer0));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.addLast(integer1);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Deque full
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int int0 = 5;
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertFalse(linkedList0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(5, 5, false, linkedList0);
      assertFalse(linkedList0.contains(int0));
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      Duration duration0 = Duration.ofMinutes(0L);
      assertNotNull(duration0);
      
      int int1 = duration0.toSecondsPart();
      assertEquals(0, int1);
      assertFalse(int1 == int0);
      
      Integer integer0 = linkedBlockingDeque0.poll1(duration0);
      assertFalse(linkedList0.contains(int0));
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNull(integer0);
      
      Stream<Integer> stream0 = linkedBlockingDeque0.parallelStream();
      assertFalse(linkedList0.contains(int0));
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNotNull(stream0);
      
      int int2 = 2412;
      // Undeclared exception!
      try { 
        linkedList0.remove(2412);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // Index: 2412, Size: 0
         //
         verifyException("java.util.LinkedList", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(2359, 1, false, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      int int0 = 0;
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.removeLast();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int int0 = 1;
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 7, false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(1));
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer(2155);
      assertEquals(2155, (int)integer0);
      assertNotNull(integer0);
      assertFalse(integer0.equals((Object)int0));
      
      TimeUnit timeUnit0 = TimeUnit.DAYS;
      boolean boolean0 = linkedBlockingDeque0.offerLast2(integer0, 7, timeUnit0);
      assertTrue(linkedBlockingDeque0.contains(2155));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertTrue(boolean0);
      assertFalse(integer0.equals((Object)int0));
      
      int int1 = linkedBlockingDeque0.size();
      assertTrue(linkedBlockingDeque0.contains(2155));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertEquals(1, int1);
      assertTrue(int1 == int0);
      
      Spliterator<Integer> spliterator0 = linkedBlockingDeque0.spliterator();
      assertTrue(linkedBlockingDeque0.contains(2155));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertNotNull(spliterator0);
      
      Duration duration0 = Duration.ofDays(1665L);
      assertNotNull(duration0);
      
      Duration duration1 = Duration.ofSeconds(1665L, 1885L);
      assertNotSame(duration1, duration0);
      assertNotNull(duration1);
      assertFalse(duration1.equals((Object)duration0));
      
      Duration duration2 = duration1.plusMillis(2288L);
      assertNotSame(duration1, duration2);
      assertNotSame(duration1, duration0);
      assertNotSame(duration2, duration0);
      assertNotSame(duration2, duration1);
      assertNotNull(duration2);
      assertFalse(duration1.equals((Object)duration0));
      assertFalse(duration2.equals((Object)duration0));
      assertFalse(duration2.equals((Object)duration1));
      
      Duration duration3 = duration1.abs();
      assertNotSame(duration1, duration2);
      assertSame(duration1, duration3);
      assertNotSame(duration1, duration0);
      assertNotSame(duration3, duration0);
      assertSame(duration3, duration1);
      assertNotSame(duration3, duration2);
      assertNotNull(duration3);
      assertFalse(duration1.equals((Object)duration2));
      assertFalse(duration1.equals((Object)duration0));
      assertFalse(duration3.equals((Object)duration0));
      assertFalse(duration3.equals((Object)duration2));
      
      Duration duration4 = duration0.minus(duration1);
      assertNotSame(duration0, duration1);
      assertNotSame(duration0, duration4);
      assertNotSame(duration0, duration3);
      assertNotSame(duration0, duration2);
      assertNotSame(duration1, duration2);
      assertSame(duration1, duration3);
      assertNotSame(duration1, duration4);
      assertNotSame(duration1, duration0);
      assertNotSame(duration4, duration3);
      assertNotSame(duration4, duration0);
      assertNotSame(duration4, duration1);
      assertNotSame(duration4, duration2);
      assertNotNull(duration4);
      assertFalse(duration0.equals((Object)duration1));
      assertFalse(duration0.equals((Object)duration3));
      assertFalse(duration0.equals((Object)duration2));
      assertFalse(duration1.equals((Object)duration2));
      assertFalse(duration1.equals((Object)duration0));
      assertFalse(duration4.equals((Object)duration3));
      assertFalse(duration4.equals((Object)duration0));
      assertFalse(duration4.equals((Object)duration1));
      assertFalse(duration4.equals((Object)duration2));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.offer1((Integer) null, duration0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 7, false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(1));
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer(2155);
      assertEquals(2155, (int)integer0);
      assertNotNull(integer0);
      
      TimeUnit timeUnit0 = TimeUnit.DAYS;
      boolean boolean0 = linkedBlockingDeque0.offerLast2(integer0, 7, timeUnit0);
      assertTrue(linkedBlockingDeque0.contains(integer0));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertTrue(boolean0);
      
      int int0 = linkedBlockingDeque0.size();
      assertTrue(linkedBlockingDeque0.contains(integer0));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertEquals(1, int0);
      
      Spliterator<Integer> spliterator0 = linkedBlockingDeque0.spliterator();
      assertTrue(linkedBlockingDeque0.contains(integer0));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertNotNull(spliterator0);
      
      Duration duration0 = Duration.ofSeconds(1665L, 1885L);
      assertNotNull(duration0);
      
      Duration duration1 = duration0.plusMillis(2288L);
      assertNotSame(duration0, duration1);
      assertNotSame(duration1, duration0);
      assertNotNull(duration1);
      assertFalse(duration1.equals((Object)duration0));
      
      Duration duration2 = duration0.abs();
      assertNotSame(duration0, duration1);
      assertSame(duration0, duration2);
      assertSame(duration2, duration0);
      assertNotSame(duration2, duration1);
      assertNotNull(duration2);
      assertFalse(duration0.equals((Object)duration1));
      assertFalse(duration2.equals((Object)duration1));
      
      Integer integer1 = new Integer(1);
      assertEquals(1, (int)integer1);
      assertNotNull(integer1);
      assertTrue(integer1.equals((Object)int0));
      assertFalse(integer1.equals((Object)integer0));
      
      TimeUnit timeUnit1 = TimeUnit.NANOSECONDS;
      Integer integer2 = new Integer(0);
      assertEquals(0, (int)integer2);
      assertNotNull(integer2);
      assertFalse(integer2.equals((Object)integer0));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      
      boolean boolean1 = linkedBlockingDeque0.offer(integer2);
      assertTrue(linkedBlockingDeque0.contains(integer2));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertTrue(boolean1);
      assertFalse(integer2.equals((Object)integer0));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      assertTrue(boolean1 == boolean0);
      
      Integer integer3 = new Integer(0);
      assertEquals(0, (int)integer3);
      assertNotNull(integer3);
      assertFalse(integer3.equals((Object)integer0));
      assertFalse(integer3.equals((Object)int0));
      assertFalse(integer3.equals((Object)integer1));
      assertTrue(integer3.equals((Object)integer2));
      
      linkedBlockingDeque0.putFirst(integer3);
      assertTrue(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertFalse(integer3.equals((Object)integer0));
      assertFalse(integer3.equals((Object)int0));
      assertFalse(integer3.equals((Object)integer1));
      assertTrue(integer3.equals((Object)integer2));
      
      boolean boolean2 = linkedBlockingDeque0.offerFirst2(integer1, 0L, timeUnit1);
      assertTrue(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertTrue(boolean2);
      assertNotSame(timeUnit1, timeUnit0);
      assertTrue(integer1.equals((Object)int0));
      assertFalse(integer1.equals((Object)integer3));
      assertFalse(integer1.equals((Object)integer2));
      assertFalse(integer1.equals((Object)integer0));
      assertFalse(timeUnit1.equals((Object)timeUnit0));
      assertTrue(boolean2 == boolean1);
      assertTrue(boolean2 == boolean0);
      
      linkedBlockingDeque0.interuptTakeWaiters();
      assertTrue(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(7));
      
      linkedBlockingDeque0.putLast(integer2);
      assertTrue(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertTrue(integer2.equals((Object)integer3));
      assertFalse(integer2.equals((Object)integer0));
      assertFalse(integer2.equals((Object)int0));
      assertFalse(integer2.equals((Object)integer1));
      
      Integer integer4 = linkedBlockingDeque0.removeLast();
      assertTrue(linkedBlockingDeque0.contains(integer4));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertEquals(0, (int)integer4);
      assertNotNull(integer4);
      assertTrue(integer4.equals((Object)integer3));
      assertFalse(integer4.equals((Object)int0));
      assertFalse(integer4.equals((Object)integer1));
      assertFalse(integer4.equals((Object)integer0));
      
      Integer[] integerArray0 = new Integer[4];
      integerArray0[0] = integer0;
      integerArray0[1] = integer0;
      integerArray0[2] = null;
      integerArray0[3] = integer4;
      Integer[] integerArray1 = linkedBlockingDeque0.toArray1(integerArray0);
      assertTrue(linkedBlockingDeque0.contains(integer4));
      assertFalse(linkedBlockingDeque0.contains(7));
      assertEquals(4, integerArray0.length);
      assertEquals(4, integerArray1.length);
      assertSame(integerArray0, integerArray1);
      assertSame(integerArray1, integerArray0);
      assertNotNull(integerArray1);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int int0 = 1;
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 7, false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(1));
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = null;
      Integer integer1 = new Integer(2155);
      assertEquals(2155, (int)integer1);
      assertNotNull(integer1);
      assertFalse(integer1.equals((Object)int0));
      
      TimeUnit timeUnit0 = TimeUnit.DAYS;
      boolean boolean0 = linkedBlockingDeque0.offerLast2(integer1, 7, timeUnit0);
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertTrue(boolean0);
      assertFalse(integer1.equals((Object)int0));
      
      int int1 = linkedBlockingDeque0.size();
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertEquals(1, int1);
      assertTrue(int1 == int0);
      
      Spliterator<Integer> spliterator0 = linkedBlockingDeque0.spliterator();
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertNotNull(spliterator0);
      
      Duration duration0 = Duration.ofDays(1665L);
      assertNotNull(duration0);
      
      Duration duration1 = Duration.ofSeconds(1665L, 1885L);
      assertNotSame(duration1, duration0);
      assertNotNull(duration1);
      assertFalse(duration1.equals((Object)duration0));
      
      Duration duration2 = duration1.plusMillis(2288L);
      assertNotSame(duration1, duration0);
      assertNotSame(duration1, duration2);
      assertNotSame(duration2, duration0);
      assertNotSame(duration2, duration1);
      assertNotNull(duration2);
      assertFalse(duration1.equals((Object)duration0));
      assertFalse(duration2.equals((Object)duration0));
      assertFalse(duration2.equals((Object)duration1));
      
      Duration duration3 = duration1.abs();
      assertNotSame(duration1, duration0);
      assertSame(duration1, duration3);
      assertNotSame(duration1, duration2);
      assertNotSame(duration3, duration2);
      assertSame(duration3, duration1);
      assertNotSame(duration3, duration0);
      assertNotNull(duration3);
      assertFalse(duration1.equals((Object)duration0));
      assertFalse(duration1.equals((Object)duration2));
      assertFalse(duration3.equals((Object)duration2));
      assertFalse(duration3.equals((Object)duration0));
      
      Duration duration4 = duration0.minus(duration1);
      assertNotSame(duration0, duration2);
      assertNotSame(duration0, duration4);
      assertNotSame(duration0, duration3);
      assertNotSame(duration0, duration1);
      assertNotSame(duration1, duration0);
      assertSame(duration1, duration3);
      assertNotSame(duration1, duration2);
      assertNotSame(duration1, duration4);
      assertNotSame(duration4, duration2);
      assertNotSame(duration4, duration0);
      assertNotSame(duration4, duration1);
      assertNotSame(duration4, duration3);
      assertNotNull(duration4);
      assertFalse(duration0.equals((Object)duration2));
      assertFalse(duration0.equals((Object)duration3));
      assertFalse(duration0.equals((Object)duration1));
      assertFalse(duration1.equals((Object)duration0));
      assertFalse(duration1.equals((Object)duration2));
      assertFalse(duration4.equals((Object)duration2));
      assertFalse(duration4.equals((Object)duration0));
      assertFalse(duration4.equals((Object)duration1));
      assertFalse(duration4.equals((Object)duration3));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.offer1((Integer) null, duration0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>(4, 1827.0F);
      assertFalse(linkedHashSet0.contains(4));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-2539), (-1), false, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-2539)));
      assertFalse(linkedBlockingDeque0.contains((-2539)));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(4, 4, true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains((-2539)));
      assertFalse(linkedBlockingDeque0.contains((-2539)));
      assertFalse(linkedBlockingDeque1.contains((-2539)));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(4, 4, true, linkedBlockingDeque1);
      assertFalse(linkedHashSet0.contains(4));
      assertFalse(linkedBlockingDeque0.contains(4));
      assertFalse(linkedBlockingDeque1.contains(4));
      assertFalse(linkedBlockingDeque2.contains(4));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque2.offerLast0((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedList0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertFalse(linkedHashSet0.contains(917));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(917));
      assertFalse(linkedBlockingDeque1.contains(917));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer(917);
      assertEquals(917, (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedHashSet0.add(integer0);
      assertTrue(linkedHashSet0.contains(917));
      assertTrue(boolean0);
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      
      boolean boolean1 = linkedBlockingDeque0.hasTakeWaiters();
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(boolean1);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(boolean1 == boolean0);
      
      boolean boolean2 = linkedBlockingDeque0.contains(integer0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(boolean2);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertTrue(boolean2 == boolean1);
      assertFalse(boolean2 == boolean0);
      
      boolean boolean3 = linkedBlockingDeque0.hasTakeWaiters();
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(boolean3);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertTrue(boolean3 == boolean1);
      assertFalse(boolean3 == boolean0);
      assertTrue(boolean3 == boolean2);
      
      Duration duration0 = Duration.ZERO;
      assertNotNull(duration0);
      
      boolean boolean4 = linkedBlockingDeque1.offerLast1(integer0, duration0);
      assertTrue(linkedHashSet0.contains(917));
      assertTrue(linkedBlockingDeque1.contains(917));
      assertTrue(boolean4);
      assertEquals(1, linkedHashSet0.size());
      assertFalse(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(boolean4 == boolean1);
      assertFalse(boolean4 == boolean2);
      assertFalse(boolean4 == boolean3);
      assertTrue(boolean4 == boolean0);
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.remove0();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(4, 1286, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(4));
      assertFalse(linkedBlockingDeque0.contains(4));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(1286, 3, true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(1286));
      assertFalse(linkedBlockingDeque0.contains(1286));
      assertFalse(linkedBlockingDeque1.contains(1286));
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer(3);
      assertEquals(3, (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedBlockingDeque0.offerFirst(integer0);
      assertFalse(linkedHashSet0.contains(1286));
      assertTrue(linkedBlockingDeque0.contains(3));
      assertFalse(linkedBlockingDeque0.contains(1286));
      assertTrue(boolean0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      
      int int0 = linkedBlockingDeque0.drainTo1(linkedBlockingDeque1, 0);
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(linkedBlockingDeque0.contains(3));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertFalse(linkedBlockingDeque1.contains(0));
      assertEquals(0, int0);
      assertEquals(0, linkedHashSet0.size());
      assertTrue(linkedHashSet0.isEmpty());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      TimeUnit timeUnit0 = TimeUnit.DAYS;
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.pollFirst2(371000000L, timeUnit0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // long overflow
         //
         verifyException("java.lang.Math", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int int0 = 0;
      int int1 = 2;
      boolean boolean0 = false;
      int int2 = 25;
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(2, 25, true, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(int2));
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(25, 0, true, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertFalse(linkedBlockingDeque1.contains(int0));
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Stream<Integer> stream0 = linkedBlockingDeque1.stream();
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertFalse(linkedBlockingDeque1.contains(int0));
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotNull(stream0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer(1531);
      assertEquals(1531, (int)integer0);
      assertNotNull(integer0);
      assertFalse(integer0.equals((Object)int2));
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)int1));
      
      boolean boolean1 = linkedBlockingDeque0.contains(integer0);
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertFalse(boolean1);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(integer0.equals((Object)int2));
      assertFalse(integer0.equals((Object)int0));
      assertFalse(integer0.equals((Object)int1));
      assertTrue(boolean1 == boolean0);
      
      Integer integer1 = null;
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.offerFirst((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-343), (-343), true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-343)));
      assertFalse(linkedBlockingDeque0.contains((-343)));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-343), (-1), true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains((-343)));
      assertFalse(linkedBlockingDeque0.contains((-343)));
      assertFalse(linkedBlockingDeque1.contains((-343)));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      int int0 = linkedBlockingDeque1.drainTo1(linkedHashSet0, (-343));
      assertFalse(linkedHashSet0.contains((-343)));
      assertFalse(linkedBlockingDeque0.contains((-343)));
      assertFalse(linkedBlockingDeque1.contains((-343)));
      assertEquals((-343), int0);
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedList0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      Integer integer0 = linkedBlockingDeque0.pollLast2(371L, timeUnit0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertEquals(0, linkedList0.size());
      assertNull(integer0);
      
      Object object0 = new Object();
      assertNotNull(object0);
      
      boolean boolean0 = linkedBlockingDeque0.remove1(object0);
      assertFalse(linkedList0.contains(917));
      assertFalse(linkedBlockingDeque0.contains(917));
      assertFalse(boolean0);
      assertEquals(0, linkedList0.size());
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.removeFirst();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      LinkedBlockingDeque linkedBlockingDeque0 = LinkedBlockingDeque.LinkedBlockingDeque0();
      assertNotNull(linkedBlockingDeque0);
      
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedList0);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque1);
      
      Object[] objectArray0 = linkedBlockingDeque1.toArray0();
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertEquals(0, objectArray0.length);
      assertEquals(0, linkedList0.size());
      assertNotNull(objectArray0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedBlockingDeque1);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertFalse(linkedBlockingDeque2.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque3 = new LinkedBlockingDeque<Integer>((-603), 1119, false, linkedBlockingDeque2);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertFalse(linkedBlockingDeque2.contains(535));
      assertFalse(linkedBlockingDeque3.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque3);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque3.equals((Object)linkedBlockingDeque1));
      
      Duration duration0 = Duration.ZERO;
      assertNotNull(duration0);
      
      LinkedBlockingDeque linkedBlockingDeque4 = LinkedBlockingDeque.LinkedBlockingDeque2(linkedBlockingDeque1);
      assertFalse(linkedList0.contains(535));
      assertFalse(linkedBlockingDeque1.contains(535));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque3);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque4, linkedBlockingDeque0);
      assertNotNull(linkedBlockingDeque4);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque3));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque4.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer(0);
      assertEquals(0, (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedList0.add(integer0);
      assertTrue(linkedList0.contains(0));
      assertFalse(linkedList0.contains(535));
      assertTrue(boolean0);
      assertEquals(1, linkedList0.size());
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque3.putLast((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1359, (-6730), false, linkedHashSet0);
      assertFalse(linkedHashSet0.contains((-6730)));
      assertFalse(linkedBlockingDeque0.contains((-6730)));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(1934, 183, false, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(183));
      assertFalse(linkedBlockingDeque0.contains(183));
      assertFalse(linkedBlockingDeque1.contains(183));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = new Integer(1359);
      assertEquals(1359, (int)integer0);
      assertNotNull(integer0);
      
      linkedBlockingDeque1.putLast(integer0);
      assertFalse(linkedHashSet0.contains((-6730)));
      assertFalse(linkedBlockingDeque0.contains((-6730)));
      assertFalse(linkedBlockingDeque1.contains((-6730)));
      assertTrue(linkedBlockingDeque1.contains(1359));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-2902), Integer.MAX_VALUE, false, linkedList0);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = linkedBlockingDeque0.pollLast();
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      assertNull(integer0);
      
      Integer integer1 = new Integer((-2902));
      assertEquals((-2902), (int)integer1);
      assertNotNull(integer1);
      
      linkedBlockingDeque0.putFirst(integer1);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains((-2902)));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      
      linkedBlockingDeque0.addLast(integer1);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains((-2902)));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      
      linkedBlockingDeque0.addFirst(integer1);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains((-2902)));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(Integer.MAX_VALUE, 150, false, linkedList0);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque1.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Object object0 = linkedBlockingDeque1.pollLast0();
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque1.contains(Integer.MAX_VALUE));
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNull(object0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      boolean boolean0 = linkedBlockingDeque1.removeLastOccurrence((Object) null);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertFalse(linkedBlockingDeque1.contains(Integer.MAX_VALUE));
      assertFalse(boolean0);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      boolean boolean1 = linkedBlockingDeque0.contains((Object) null);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertFalse(boolean1);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertTrue(boolean1 == boolean0);
      
      LinkedBlockingDeque linkedBlockingDeque2 = LinkedBlockingDeque.LinkedBlockingDeque1(true);
      assertNotNull(linkedBlockingDeque2);
      
      Integer integer2 = linkedBlockingDeque0.poll();
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals((-2902), (int)integer2);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(integer2);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      
      Integer integer3 = linkedBlockingDeque0.removeFirst();
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertEquals((-2902), (int)integer3);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotNull(integer3);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      
      boolean boolean2 = linkedBlockingDeque0.offer(integer2);
      assertFalse(linkedList0.contains(Integer.MAX_VALUE));
      assertTrue(linkedBlockingDeque0.contains(integer1));
      assertFalse(linkedBlockingDeque0.contains(Integer.MAX_VALUE));
      assertTrue(boolean2);
      assertEquals(0, linkedList0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(boolean2 == boolean0);
      assertFalse(boolean2 == boolean1);
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.removeLast();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1, 0, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque0);
      
      Integer integer0 = new Integer(1);
      assertEquals(1, (int)integer0);
      assertNotNull(integer0);
      
      boolean boolean0 = linkedHashSet0.add(integer0);
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedHashSet0.contains(0));
      assertTrue(boolean0);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      
      boolean boolean1 = linkedBlockingDeque0.hasTakeWaiters();
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(integer0));
      assertFalse(boolean1);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(boolean1 == boolean0);
      
      boolean boolean2 = linkedBlockingDeque0.contains((Object) null);
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(integer0));
      assertFalse(boolean2);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertTrue(boolean2 == boolean1);
      assertFalse(boolean2 == boolean0);
      
      boolean boolean3 = linkedBlockingDeque0.hasTakeWaiters();
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(integer0));
      assertFalse(boolean3);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertTrue(boolean3 == boolean2);
      assertFalse(boolean3 == boolean0);
      assertTrue(boolean3 == boolean1);
      
      Duration duration0 = Duration.ZERO;
      assertNotNull(duration0);
      
      boolean boolean4 = linkedBlockingDeque0.offerLast1(integer0, duration0);
      assertTrue(linkedHashSet0.contains(integer0));
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(integer0));
      assertFalse(boolean4);
      assertFalse(linkedHashSet0.isEmpty());
      assertEquals(1, linkedHashSet0.size());
      assertFalse(boolean4 == boolean0);
      assertTrue(boolean4 == boolean1);
      assertTrue(boolean4 == boolean2);
      assertTrue(boolean4 == boolean3);
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.remove0();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedHashSet0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(0, 290, true, linkedHashSet0);
      assertFalse(linkedHashSet0.contains(0));
      assertFalse(linkedBlockingDeque0.contains(0));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(290, 3, true, linkedBlockingDeque0);
      assertFalse(linkedHashSet0.contains(290));
      assertFalse(linkedBlockingDeque0.contains(290));
      assertFalse(linkedBlockingDeque1.contains(290));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque1);
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      Integer integer0 = linkedBlockingDeque1.pollLast0();
      assertFalse(linkedHashSet0.contains(290));
      assertFalse(linkedBlockingDeque0.contains(290));
      assertFalse(linkedBlockingDeque1.contains(290));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNull(integer0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(0, 1, true, linkedBlockingDeque1);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertFalse(linkedBlockingDeque2.contains(1));
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotNull(linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      
      Integer integer1 = new Integer(0);
      assertEquals(0, (int)integer1);
      assertNotNull(integer1);
      
      boolean boolean0 = linkedBlockingDeque2.offer(integer1);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertFalse(linkedBlockingDeque2.contains(1));
      assertTrue(linkedBlockingDeque2.contains(0));
      assertTrue(boolean0);
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      
      Object object0 = linkedBlockingDeque2.pollFirst();
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertFalse(linkedBlockingDeque2.contains(1));
      assertEquals(0, object0);
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertNotNull(object0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      
      boolean boolean1 = linkedHashSet0.remove(object0);
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertFalse(linkedBlockingDeque2.contains(1));
      assertFalse(boolean1);
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque2, linkedBlockingDeque0);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque2.equals((Object)linkedBlockingDeque0));
      assertFalse(boolean1 == boolean0);
      
      LinkedBlockingDeque linkedBlockingDeque3 = LinkedBlockingDeque.LinkedBlockingDeque1(true);
      assertNotNull(linkedBlockingDeque3);
      
      int int0 = linkedBlockingDeque1.remainingCapacity();
      assertFalse(linkedHashSet0.contains(1));
      assertFalse(linkedBlockingDeque0.contains(1));
      assertFalse(linkedBlockingDeque1.contains(1));
      assertEquals(3, int0);
      assertTrue(linkedHashSet0.isEmpty());
      assertEquals(0, linkedHashSet0.size());
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque2);
      assertNotSame(linkedBlockingDeque0, linkedBlockingDeque1);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque0);
      assertNotSame(linkedBlockingDeque1, linkedBlockingDeque2);
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque2));
      assertFalse(linkedBlockingDeque0.equals((Object)linkedBlockingDeque1));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque0));
      assertFalse(linkedBlockingDeque1.equals((Object)linkedBlockingDeque2));
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.remove0();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      int int0 = 917;
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      assertFalse(linkedList0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedList0);
      
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(917, 917, true, linkedList0);
      assertFalse(linkedList0.contains(int0));
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNotNull(linkedBlockingDeque0);
      
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      Integer integer0 = linkedBlockingDeque0.pollLast2(371L, timeUnit0);
      assertFalse(linkedList0.contains(int0));
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertEquals(0, linkedList0.size());
      assertNull(integer0);
      
      Object object0 = new Object();
      assertNotNull(object0);
      
      boolean boolean0 = linkedBlockingDeque0.remove1(object0);
      assertFalse(linkedList0.contains(int0));
      assertFalse(linkedBlockingDeque0.contains(int0));
      assertFalse(boolean0);
      assertEquals(0, linkedList0.size());
      
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.removeFirst();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      int int0 = 3;
      Integer[] integerArray0 = new Integer[8];
      Integer integer0 = new Integer((-896));
      integerArray0[0] = integer0;
      Integer integer1 = new Integer(3);
      integerArray0[1] = integer1;
      Integer integer2 = new Integer((-3258));
      integerArray0[2] = integer2;
      Integer integer3 = new Integer(0);
      integerArray0[3] = integer3;
      Integer integer4 = new Integer(3);
      integerArray0[4] = integer4;
      Integer integer5 = new Integer(int0);
      integerArray0[5] = integer5;
      Integer integer6 = new Integer(0);
      integerArray0[6] = integer6;
      Integer integer7 = new Integer(0);
      integerArray0[7] = integer7;
      List<Integer> list0 = List.of(integerArray0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(3, 3, false, list0);
      linkedBlockingDeque0.poll0();
      TimeUnit timeUnit0 = TimeUnit.MINUTES;
      linkedBlockingDeque0.pollLast2((long) integerArray0[2], timeUnit0);
      linkedBlockingDeque0.putLast(integer1);
      assertTrue(linkedBlockingDeque0.contains(int0));
      
      linkedBlockingDeque0.remove0();
      Object[] objectArray0 = linkedBlockingDeque0.toArray0();
      assertEquals(0, objectArray0.length);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int int0 = 0;
      int int1 = 0;
      boolean boolean0 = false;
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = null;
      try {
        linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(0, 0, false, linkedHashSet0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      int int0 = 0;
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = null;
      try {
        linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(0, (-899), false, linkedHashSet0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(1029, 166, false, (Collection<? extends Integer>) null);
      assertFalse(linkedBlockingDeque0.contains(1029));
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      int int0 = 393;
      int int1 = (-1);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      Integer integer0 = new Integer(0);
      linkedList0.removeFirstOccurrence(integer0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(393, (-1), true, linkedList0);
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.pop();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-1678), (-1678), true, linkedHashSet0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(5, 0, true, linkedBlockingDeque0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(5, 1069, true, linkedBlockingDeque1);
      // Undeclared exception!
      try { 
        linkedBlockingDeque2.removeFirst();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-166), 2, true, linkedHashSet0);
      TimeUnit timeUnit0 = TimeUnit.HOURS;
      Integer integer0 = linkedBlockingDeque0.poll2((-639L), timeUnit0);
      assertNull(integer0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      LinkedBlockingDeque.LinkedBlockingDeque1(false);
      int int0 = 4;
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(4, 4, false, linkedHashSet0);
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.pop();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      LinkedBlockingDeque.LinkedBlockingDeque0();
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedList0);
      linkedBlockingDeque0.toArray0();
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-603), 535, false, linkedBlockingDeque0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>((-603), 1119, false, linkedBlockingDeque1);
      Duration duration0 = Duration.ZERO;
      LinkedBlockingDeque.LinkedBlockingDeque2(linkedBlockingDeque0);
      linkedBlockingDeque2.pollFirst1(duration0);
      Integer integer0 = new Integer(0);
      linkedList0.add(integer0);
      // Undeclared exception!
      try { 
        linkedBlockingDeque2.putLast((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(Integer.MAX_VALUE, 1, true, linkedList0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(0, 2293, true, linkedBlockingDeque0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque2 = null;
      try {
        linkedBlockingDeque2 = new LinkedBlockingDeque<Integer>(0, 0, true, linkedBlockingDeque1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Integer integer0 = new Integer(2407);
      Integer integer1 = new Integer(2);
      List<Integer> list0 = List.of(integer0, integer0, integer0, integer1, integer0, integer1, integer1, integer0, integer1);
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(4577, 0, false, list0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>(5, (-663), false, linkedBlockingDeque0);
      boolean boolean0 = linkedBlockingDeque1.offerLast(integer1);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = null;
      try {
        linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(0, 0, false, (Collection<? extends Integer>) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      int int0 = 103;
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>(0, 103, true, (Collection<? extends Integer>) null);
      // Undeclared exception!
      try { 
        linkedBlockingDeque0.offerLast((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // e
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      LinkedBlockingDeque<Integer> linkedBlockingDeque0 = new LinkedBlockingDeque<Integer>((-2323), 0, true, linkedHashSet0);
      LinkedBlockingDeque<Integer> linkedBlockingDeque1 = new LinkedBlockingDeque<Integer>((-3328), (-1225), true, linkedBlockingDeque0);
      Integer integer0 = new Integer((-1283));
      // Undeclared exception!
      try { 
        linkedBlockingDeque1.addLast(integer0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Deque full
         //
         verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e);
      }
  }
}
