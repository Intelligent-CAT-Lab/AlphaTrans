
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


package org.apache.commons.graph.scc;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedHashSet;
import java.util.Set;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.scc.KosarajuSharirAlgorithm;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class KosarajuSharirAlgorithm_ESTest extends KosarajuSharirAlgorithm_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Integer integer0 = new Integer((-99));
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      directedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer((-1428));
      directedMutableGraph0.addVertex(integer1);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addEdge(integer0, linkedHashSet0, integer1);
      KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      directedMutableGraph0.addEdge(integer1, linkedHashSet0, integer0);
      Set<Integer> set0 = kosarajuSharirAlgorithm0.perform1(integer0);
      assertTrue(set0.contains((-1428)));
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      KosarajuSharirAlgorithm<Integer, Integer> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, Integer>(revertedGraph0);
      Set<Set<Integer>> set0 = kosarajuSharirAlgorithm0.perform0();
      assertEquals(0, set0.size());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      directedMutableGraph0.addVertex(integer0);
      KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      Set<Set<Integer>> set0 = kosarajuSharirAlgorithm0.perform();
      assertFalse(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      KosarajuSharirAlgorithm<LinkedHashSet<Integer>, Integer> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<LinkedHashSet<Integer>, Integer>((DirectedGraph<LinkedHashSet<Integer>, Integer>) null);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      // Undeclared exception!
      try { 
        kosarajuSharirAlgorithm0.perform1(linkedHashSet0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      KosarajuSharirAlgorithm<Integer, Integer> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, Integer>((DirectedGraph<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        kosarajuSharirAlgorithm0.perform1((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Kosaraju Sharir algorithm cannot be calculated without expressing the source vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>>((DirectedGraph<Integer, LinkedHashSet<Integer>>) null);
      // Undeclared exception!
      try { 
        kosarajuSharirAlgorithm0.perform0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      KosarajuSharirAlgorithm<LinkedHashSet<Integer>, Integer> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<LinkedHashSet<Integer>, Integer>((DirectedGraph<LinkedHashSet<Integer>, Integer>) null);
      // Undeclared exception!
      try { 
        kosarajuSharirAlgorithm0.perform();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Integer integer0 = new Integer((-99));
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      directedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer((-1428));
      directedMutableGraph0.addVertex(integer1);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addEdge(integer0, linkedHashSet0, integer1);
      KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      Set<Set<Integer>> set0 = kosarajuSharirAlgorithm0.perform0();
      assertEquals(2, set0.size());
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      Integer integer0 = new Integer((-99));
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        kosarajuSharirAlgorithm0.perform1(integer0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex -99 does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>> kosarajuSharirAlgorithm0 = new KosarajuSharirAlgorithm<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      Set<Set<Integer>> set0 = kosarajuSharirAlgorithm0.perform();
      assertTrue(set0.isEmpty());
  }
}
