
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
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.collections.FibonacciHeapNode;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FibonacciHeapNode_ESTest extends FibonacciHeapNode_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer(0);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.toString();
      assertFalse(fibonacciHeapNode0.isMarked());
      assertEquals(0, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Integer integer0 = new Integer(0);
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(integer0);
      assertFalse(fibonacciHeapNode0.isMarked());
      
      fibonacciHeapNode0.setMarked(true);
      boolean boolean0 = fibonacciHeapNode0.isMarked();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      fibonacciHeapNode0.setRight((FibonacciHeapNode<Object>) null);
      FibonacciHeapNode<Object> fibonacciHeapNode1 = fibonacciHeapNode0.getRight();
      assertFalse(fibonacciHeapNode0.isMarked());
      assertNull(fibonacciHeapNode1);
      assertEquals(0, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Integer integer0 = new Integer(0);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      assertFalse(fibonacciHeapNode0.isMarked());
      
      fibonacciHeapNode0.setMarked(true);
      fibonacciHeapNode0.getRight();
      assertTrue(fibonacciHeapNode0.isMarked());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer((-613));
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.incraeseDegree();
      fibonacciHeapNode0.getRight();
      assertEquals(1, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Integer integer0 = new Integer((-24));
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.decraeseDegree();
      fibonacciHeapNode0.getRight();
      assertEquals((-1), fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Integer integer0 = new Integer(0);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      assertFalse(fibonacciHeapNode0.isMarked());
      
      fibonacciHeapNode0.setMarked(true);
      fibonacciHeapNode0.setParent(fibonacciHeapNode0);
      fibonacciHeapNode0.getParent();
      assertEquals(0, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer(0);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.setParent(fibonacciHeapNode0);
      FibonacciHeapNode<Integer> fibonacciHeapNode1 = fibonacciHeapNode0.getParent();
      assertFalse(fibonacciHeapNode1.isMarked());
      assertEquals(0, fibonacciHeapNode1.getDegree());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer(852);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.incraeseDegree();
      fibonacciHeapNode0.setParent(fibonacciHeapNode0);
      fibonacciHeapNode0.getParent();
      assertEquals(1, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      fibonacciHeapNode0.decraeseDegree();
      fibonacciHeapNode0.setParent(fibonacciHeapNode0);
      fibonacciHeapNode0.getParent();
      assertEquals((-1), fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      fibonacciHeapNode0.setLeft((FibonacciHeapNode<Object>) null);
      FibonacciHeapNode<Object> fibonacciHeapNode1 = fibonacciHeapNode0.getLeft();
      assertFalse(fibonacciHeapNode0.isMarked());
      assertNull(fibonacciHeapNode1);
      assertEquals(0, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Integer integer0 = new Integer(992);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      assertFalse(fibonacciHeapNode0.isMarked());
      
      fibonacciHeapNode0.setMarked(true);
      fibonacciHeapNode0.getLeft();
      assertTrue(fibonacciHeapNode0.isMarked());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Integer integer0 = new Integer(823);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.incraeseDegree();
      fibonacciHeapNode0.getLeft();
      assertEquals(1, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Integer integer0 = new Integer((-24));
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.decraeseDegree();
      fibonacciHeapNode0.getLeft();
      assertEquals((-1), fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>((Object) null);
      fibonacciHeapNode0.getElement();
      assertEquals(0, fibonacciHeapNode0.getDegree());
      assertFalse(fibonacciHeapNode0.isMarked());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Integer integer0 = new Integer(0);
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(integer0);
      fibonacciHeapNode0.incraeseDegree();
      int int0 = fibonacciHeapNode0.getDegree();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Integer integer0 = new Integer(1);
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(integer0);
      fibonacciHeapNode0.decraeseDegree();
      int int0 = fibonacciHeapNode0.getDegree();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Integer integer0 = new Integer(823);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.setChild(fibonacciHeapNode0);
      assertFalse(fibonacciHeapNode0.isMarked());
      
      fibonacciHeapNode0.setMarked(true);
      fibonacciHeapNode0.getChild();
      assertTrue(fibonacciHeapNode0.isMarked());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Integer integer0 = new Integer((-613));
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.setChild(fibonacciHeapNode0);
      FibonacciHeapNode<Integer> fibonacciHeapNode1 = fibonacciHeapNode0.getChild();
      assertFalse(fibonacciHeapNode1.isMarked());
      assertEquals(0, fibonacciHeapNode1.getDegree());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Integer integer0 = new Integer(823);
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.incraeseDegree();
      fibonacciHeapNode0.setChild(fibonacciHeapNode0);
      fibonacciHeapNode0.getChild();
      assertEquals(1, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      int int0 = fibonacciHeapNode0.getDegree();
      assertEquals(0, int0);
      assertFalse(fibonacciHeapNode0.isMarked());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      fibonacciHeapNode0.getElement();
      assertEquals(0, fibonacciHeapNode0.getDegree());
      assertFalse(fibonacciHeapNode0.isMarked());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Integer integer0 = new Integer((-24));
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      FibonacciHeapNode<Integer> fibonacciHeapNode1 = fibonacciHeapNode0.getChild();
      assertFalse(fibonacciHeapNode0.isMarked());
      assertNull(fibonacciHeapNode1);
      assertEquals(0, fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>((Object) null);
      // Undeclared exception!
      try { 
        fibonacciHeapNode0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      FibonacciHeapNode<Object> fibonacciHeapNode1 = fibonacciHeapNode0.getParent();
      assertFalse(fibonacciHeapNode0.isMarked());
      assertEquals(0, fibonacciHeapNode0.getDegree());
      assertNull(fibonacciHeapNode1);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Integer integer0 = new Integer((-24));
      FibonacciHeapNode<Integer> fibonacciHeapNode0 = new FibonacciHeapNode<Integer>(integer0);
      fibonacciHeapNode0.decraeseDegree();
      fibonacciHeapNode0.setChild(fibonacciHeapNode0);
      fibonacciHeapNode0.getChild();
      assertEquals((-1), fibonacciHeapNode0.getDegree());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Object object0 = new Object();
      FibonacciHeapNode<Object> fibonacciHeapNode0 = new FibonacciHeapNode<Object>(object0);
      boolean boolean0 = fibonacciHeapNode0.isMarked();
      assertEquals(0, fibonacciHeapNode0.getDegree());
      assertFalse(boolean0);
  }
}
