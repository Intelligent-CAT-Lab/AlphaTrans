
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


package org.apache.commons.graph.model;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.RevertedGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class RevertedGraph_ESTest extends RevertedGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> directedMutableGraph1 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(directedMutableGraph1);
      RevertedGraph<Integer, Integer> revertedGraph2 = new RevertedGraph<Integer, Integer>(revertedGraph0);
      // Undeclared exception!
      try { 
        revertedGraph1.getEdge(revertedGraph0, revertedGraph2);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(1);
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      directedMutableGraph0.addEdge(revertedGraph0, integer0, revertedGraph0);
      int int0 = revertedGraph1.getSize();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.decorateAddVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(directedMutableGraph0);
      int int0 = revertedGraph1.getOutDegree(revertedGraph0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      int int0 = revertedGraph1.getOrder();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      int int0 = revertedGraph1.getInDegree(revertedGraph0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(1);
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      directedMutableGraph0.addEdge(revertedGraph0, integer0, revertedGraph0);
      int int0 = revertedGraph1.getInDegree(revertedGraph0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      Integer integer0 = revertedGraph1.getEdge(revertedGraph0, revertedGraph0);
      assertNull(integer0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> directedMutableGraph1 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      directedMutableGraph1.addVertex(revertedGraph0);
      directedMutableGraph1.addEdge(revertedGraph0, revertedGraph0, revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(directedMutableGraph1);
      RevertedGraph<Integer, Integer> revertedGraph2 = revertedGraph1.getEdge(revertedGraph0, revertedGraph0);
      assertSame(revertedGraph0, revertedGraph2);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      int int0 = revertedGraph1.getDegree(revertedGraph0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      directedMutableGraph0.addVertex(revertedGraph0);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      boolean boolean0 = revertedGraph1.containsVertex(revertedGraph0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> revertedGraph0 = null;
      try {
        revertedGraph0 = new RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>((DirectedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Adapted DirectedGraph must be not null
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>();
      RevertedGraph<Integer, RevertedGraph<Integer, Integer>> revertedGraph0 = new RevertedGraph<Integer, RevertedGraph<Integer, Integer>>(directedMutableGraph0);
      int int0 = revertedGraph0.getOrder();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(0);
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      Iterable<Integer> iterable0 = revertedGraph0.getOutbound(integer0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        revertedGraph1.getInDegree(revertedGraph0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      boolean boolean0 = revertedGraph1.containsVertex(revertedGraph0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      Integer integer0 = new Integer(2);
      // Undeclared exception!
      try { 
        revertedGraph0.getVertices1(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.RevertedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph0 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      Iterable<RevertedGraph<Integer, Integer>> iterable0 = revertedGraph0.getVertices0();
      assertNotNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph0 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph1 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      // Undeclared exception!
      try { 
        revertedGraph0.getConnectedVertices(revertedGraph1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      Iterable<Integer> iterable0 = revertedGraph0.getEdges();
      assertNotNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      int int0 = revertedGraph0.getSize();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(directedMutableGraph0);
      Iterable<RevertedGraph<Integer, Integer>> iterable0 = revertedGraph1.getInbound(revertedGraph0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        revertedGraph1.getOutDegree(revertedGraph0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      boolean boolean0 = revertedGraph0.containsEdge((Integer) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph1);
      RevertedGraph<RevertedGraph<Integer, Integer>, Integer> revertedGraph1 = new RevertedGraph<RevertedGraph<Integer, Integer>, Integer>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        revertedGraph1.getDegree(revertedGraph0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }
}
