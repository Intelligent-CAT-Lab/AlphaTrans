
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


package org.apache.commons.graph.collections;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.lang.reflect.Array;
import java.util.Collection;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.stream.Stream;
import org.apache.commons.graph.collections.FibonacciHeap;
import org.apache.commons.graph.collections.FibonacciHeapNode;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FibonacciHeap_ESTest extends FibonacciHeap_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      FibonacciHeap fibonacciHeap0 = FibonacciHeap.FibonacciHeap1();
      Comparator<Object> comparator0 = (Comparator<Object>) mock(Comparator.class, new ViolatedAssumptionAnswer());
      FibonacciHeap<Object> fibonacciHeap1 = new FibonacciHeap<Object>(comparator0);
      fibonacciHeap1.offer(fibonacciHeap0);
      int int0 = fibonacciHeap1.size();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      List<String> list0 = List.of("", "", "org.apache.commons.graph.utils.Assertions", "", "", "", "", "");
      fibonacciHeap0.addAll(list0);
      fibonacciHeap0.poll();
      int int0 = fibonacciHeap0.potential();
      assertEquals(7, fibonacciHeap0.size());
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.offer((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null elements not allowed in this FibonacciHeap implementation.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.add(fibonacciHeap0);
      // Undeclared exception!
      try { 
        fibonacciHeap0.offer("FibonacciHeap=[org.apache.commons.graph.collections.FibonacciHeap@0000000001, ]");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      FibonacciHeap<Integer> fibonacciHeap1 = new FibonacciHeap<Integer>((Comparator<? super Integer>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap1.containsAll(fibonacciHeap0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.addAll((Collection<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.addAll(linkedList0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null elements not allowed in this FibonacciHeap implementation.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.add(fibonacciHeap0);
      List<String> list0 = List.of("{H#U6C}>dyurkgZEL&\"");
      // Undeclared exception!
      try { 
        fibonacciHeap0.addAll(list0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.add((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null elements not allowed in this FibonacciHeap implementation.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      Stream<Object> stream0 = fibonacciHeap0.parallelStream();
      fibonacciHeap0.add(fibonacciHeap0);
      // Undeclared exception!
      try { 
        fibonacciHeap0.add(stream0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.util.stream.ReferencePipeline$Head cannot be cast to class java.lang.Comparable (java.util.stream.ReferencePipeline$Head and java.lang.Comparable are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      FibonacciHeap<String> fibonacciHeap0 = new FibonacciHeap<String>((Comparator<? super String>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.remove0();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.add(fibonacciHeap0);
      fibonacciHeap0.poll();
      assertEquals(0, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      List<String> list0 = List.of(", ", "", "", "V<^gw/;,dyMJyC", "", "", "`1u/", "V<^gw/;,dyMJyC");
      fibonacciHeap0.addAll(list0);
      fibonacciHeap0.remove();
      fibonacciHeap0.poll();
      assertFalse(fibonacciHeap0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.add(fibonacciHeap0);
      fibonacciHeap0.peek();
      assertEquals(1, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FibonacciHeap<Integer> fibonacciHeap0 = new FibonacciHeap<Integer>((Comparator<? super Integer>) null);
      LinkedList<Integer> linkedList0 = new LinkedList<Integer>();
      Integer integer0 = new Integer(0);
      linkedList0.add(integer0);
      fibonacciHeap0.addAll(linkedList0);
      fibonacciHeap0.isEmpty();
      assertEquals(1, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Comparator<Object> comparator0 = (Comparator<Object>) mock(Comparator.class, new ViolatedAssumptionAnswer());
      FibonacciHeap<Integer> fibonacciHeap0 = new FibonacciHeap<Integer>(comparator0);
      fibonacciHeap0.isEmpty();
      assertEquals(0, fibonacciHeap0.potential());
      assertEquals(0, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      boolean boolean0 = fibonacciHeap0.contains(fibonacciHeap0);
      assertEquals(0, fibonacciHeap0.size());
      assertFalse(boolean0);
      assertEquals(0, fibonacciHeap0.potential());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.remove1((Object) null);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.toArray0();
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      FibonacciHeap<FibonacciHeap<String>> fibonacciHeap0 = new FibonacciHeap<FibonacciHeap<String>>((Comparator<? super FibonacciHeap<String>>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.iterator();
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      FibonacciHeapNode<Object>[] fibonacciHeapNodeArray0 = (FibonacciHeapNode<Object>[]) Array.newInstance(FibonacciHeapNode.class, 0);
      // Undeclared exception!
      try { 
        fibonacciHeap0.toArray1(fibonacciHeapNodeArray0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      String string0 = fibonacciHeap0.toString();
      assertEquals(0, fibonacciHeap0.size());
      assertEquals(0, fibonacciHeap0.potential());
      assertEquals("FibonacciHeap=[]", string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      List<String> list0 = List.of("", "FibonacciHeap=[", "FibonacciHeap=[", "", "", "", "U`'?k+", "org.apache.commons.graph.utils.Assertions");
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.addAll(list0);
      fibonacciHeap0.toString();
      assertEquals(8, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.add(fibonacciHeap0);
      fibonacciHeap0.remove0();
      assertEquals(0, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      FibonacciHeap<String> fibonacciHeap0 = new FibonacciHeap<String>((Comparator<? super String>) null);
      fibonacciHeap0.poll();
      assertEquals(0, fibonacciHeap0.size());
      assertEquals(0, fibonacciHeap0.potential());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.peek();
      assertEquals(0, fibonacciHeap0.size());
      assertEquals(0, fibonacciHeap0.potential());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.element();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      List<String> list0 = List.of("", "", ", ", "UX'V`.x|", "UX'V`.x|", "", "", "-?");
      fibonacciHeap0.addAll(list0);
      fibonacciHeap0.element();
      assertEquals(8, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      List<String> list0 = List.of("U`'?k+", "U`'?k+", "U`'?k+", "U`'?k+", "U`'?k+", "U`'?k+", "U`'?k+", "U`'?k+");
      fibonacciHeap0.addAll(list0);
      boolean boolean0 = fibonacciHeap0.containsAll(list0);
      assertFalse(fibonacciHeap0.isEmpty());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      boolean boolean0 = fibonacciHeap0.containsAll((Collection<?>) null);
      assertEquals(0, fibonacciHeap0.potential());
      assertFalse(boolean0);
      assertEquals(0, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      List<String> list0 = List.of("", "FibonacciHeap=[", "FibonacciHeap=[", "", "", "", "U`'?k+", "org.apache.commons.graph.utils.Assertions");
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.addAll(list0);
      boolean boolean0 = fibonacciHeap0.contains("U`'?k+");
      assertFalse(fibonacciHeap0.isEmpty());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      FibonacciHeap<String> fibonacciHeap0 = new FibonacciHeap<String>((Comparator<? super String>) null);
      boolean boolean0 = fibonacciHeap0.contains((Object) null);
      assertEquals(0, fibonacciHeap0.potential());
      assertEquals(0, fibonacciHeap0.size());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      List<String> list0 = List.of("", "FibonacciHeap=[", "FibonacciHeap=[", "", "", "", "U`'?k+", "org.apache.commons.graph.utils.Assertions");
      FibonacciHeap<FibonacciHeapNode<String>> fibonacciHeap0 = new FibonacciHeap<FibonacciHeapNode<String>>((Comparator<? super FibonacciHeapNode<String>>) null);
      boolean boolean0 = fibonacciHeap0.containsAll(list0);
      assertEquals(0, fibonacciHeap0.potential());
      assertFalse(boolean0);
      assertEquals(0, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      List<String> list0 = List.of("", "FibonacciHeap=[", "FibonacciHeap=[", "", "", "", "U`'?k+", "org.apache.commons.graph.utils.Assertions");
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.addAll(list0);
      fibonacciHeap0.poll();
      fibonacciHeap0.toString();
      assertTrue(fibonacciHeap0.contains("org.apache.commons.graph.utils.Assertions"));
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      FibonacciHeap<FibonacciHeapNode<String>> fibonacciHeap0 = new FibonacciHeap<FibonacciHeapNode<String>>((Comparator<? super FibonacciHeapNode<String>>) null);
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      // Undeclared exception!
      try { 
        fibonacciHeap0.retainAll(linkedList0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.clear();
      assertEquals(0, fibonacciHeap0.size());
      assertEquals(0, fibonacciHeap0.potential());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      FibonacciHeap fibonacciHeap0 = FibonacciHeap.FibonacciHeap1();
      Comparator<Object> comparator0 = (Comparator<Object>) mock(Comparator.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(comparator0).compare(any() , any());
      FibonacciHeap<Object> fibonacciHeap1 = new FibonacciHeap<Object>(comparator0);
      fibonacciHeap1.offer(fibonacciHeap0);
      boolean boolean0 = fibonacciHeap1.add(fibonacciHeap0);
      assertEquals(2, fibonacciHeap1.size());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.remove();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      FibonacciHeap<String> fibonacciHeap0 = new FibonacciHeap<String>((Comparator<? super String>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.toArray();
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      int int0 = fibonacciHeap0.size();
      assertEquals(0, fibonacciHeap0.potential());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.addAll(fibonacciHeap0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      FibonacciHeap<String> fibonacciHeap0 = new FibonacciHeap<String>((Comparator<? super String>) null);
      // Undeclared exception!
      try { 
        fibonacciHeap0.remove((Object) null);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      int int0 = fibonacciHeap0.potential();
      assertEquals(0, int0);
      assertEquals(0, fibonacciHeap0.size());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      FibonacciHeap<FibonacciHeap<Object>> fibonacciHeap0 = new FibonacciHeap<FibonacciHeap<Object>>((Comparator<? super FibonacciHeap<Object>>) null);
      Object[] objectArray0 = new Object[0];
      // Undeclared exception!
      try { 
        fibonacciHeap0.toArray(objectArray0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      fibonacciHeap0.offer("%^<[9a`RG/[|w!Vh1M");
      List<String> list0 = List.of("]nm[.`[1I ` 2FB+", "%^<[9a`RG/[|w!Vh1M", "%^<[9a`RG/[|w!Vh1M", "org.apache.commons.graph.collections.FibonacciHeapNode", "%^<[9a`RG/[|w!Vh1M", "%^<[9a`RG/[|w!Vh1M", "%^<[9a`RG/[|w!Vh1M", "org.apache.commons.graph.collections.FibonacciHeapNode");
      fibonacciHeap0.addAll(list0);
      fibonacciHeap0.poll();
      fibonacciHeap0.remove();
      assertFalse(fibonacciHeap0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      FibonacciHeap<Object> fibonacciHeap0 = new FibonacciHeap<Object>((Comparator<? super Object>) null);
      List<String> list0 = List.of("", "", "org.apache.commons.graph.utils.Assertions", "", "", "", "", "");
      // Undeclared exception!
      try { 
        fibonacciHeap0.removeAll(list0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }
}
