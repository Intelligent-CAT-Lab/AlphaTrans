
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


package org.apache.commons.graph.spanning;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Iterator;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.spanning.SuperVertex;
import org.apache.commons.graph.spanning.WeightedEdgesComparator;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SuperVertex_ESTest extends SuperVertex_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      undirectedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer((-1));
      undirectedMutableGraph0.addEdge(integer0, integer1, integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = null;
      try {
        superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer1, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.TreeMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      undirectedMutableGraph0.addVertex(integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer0, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        superVertex0.merge((SuperVertex<Integer, Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.SuperVertex", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      SuperVertex<Integer, Integer, Integer> superVertex0 = null;
      try {
        superVertex0 = new SuperVertex<Integer, Integer, Integer>((Integer) null, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Integer integer0 = new Integer((-3413));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = null;
      try {
        superVertex0 = new SuperVertex<Integer, Integer, Integer>((Integer) null, inMemoryPath0, (WeightedEdgesComparator<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to get the degree of a null vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Integer integer0 = new Integer(2170);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer1 = integerWeightBaseOperations0.identity();
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer1);
      SuperVertex<Integer, Integer, Integer> superVertex0 = null;
      try {
        superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer0, inMemoryPath0, (WeightedEdgesComparator<Integer, Integer>) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; 2170 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      undirectedMutableGraph0.addVertex(integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer0, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
      undirectedMutableGraph0.addEdge(integer0, integer0, integer0);
      SuperVertex<Integer, Integer, Integer> superVertex1 = new SuperVertex<Integer, Integer, Integer>(integer0, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
      superVertex0.merge(superVertex1);
      assertNotSame(superVertex1, superVertex0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      undirectedMutableGraph0.addVertex(integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer0, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
      Integer integer1 = superVertex0.getMinimumWeightEdge();
      assertNull(integer1);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      undirectedMutableGraph0.addVertex(integer0);
      undirectedMutableGraph0.addEdge(integer0, integer0, integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer0, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
      Integer integer1 = superVertex0.getMinimumWeightEdge();
      assertEquals((-1), (int)integer1);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      undirectedMutableGraph0.addVertex(integer0);
      SuperVertex<Integer, Integer, Integer> superVertex0 = new SuperVertex<Integer, Integer, Integer>(integer0, undirectedMutableGraph0, (WeightedEdgesComparator<Integer, Integer>) null);
      Iterator<Integer> iterator0 = superVertex0.iterator();
      assertNotNull(iterator0);
  }
}
