
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
import java.util.LinkedHashSet;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BaseMutableGraph_ESTest extends BaseMutableGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      directedMutableGraph0.addEdge(linkedHashSet0, linkedHashSet0, linkedHashSet0);
      LinkedHashSet<Integer> linkedHashSet1 = new LinkedHashSet<Integer>();
      directedMutableGraph0.removeVertex(linkedHashSet1);
      assertEquals(0, linkedHashSet1.size());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(3);
      directedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer(3);
      directedMutableGraph0.internalAddEdge(integer1, integer0, integer0);
      directedMutableGraph0.removeEdge(integer0);
      assertEquals(0, directedMutableGraph0.getSize());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1836));
      directedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer((-1836));
      directedMutableGraph0.addEdge(integer0, integer1, integer0);
      assertEquals(1, directedMutableGraph0.getSize());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-437));
      directedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer((-437));
      directedMutableGraph0.addEdge(integer0, integer1, integer1);
      assertEquals(1, directedMutableGraph0.getOrder());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-437));
      Integer integer1 = new Integer((-437));
      // Undeclared exception!
      try { 
        directedMutableGraph0.addEdge(integer0, integer1, integer1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      directedMutableGraph0.internalRemoveEdge(linkedHashSet0, linkedHashSet0, linkedHashSet0);
      assertTrue(linkedHashSet0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.internalRemoveEdge((Integer) null, (Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null head
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      // Undeclared exception!
      try { 
        undirectedMutableGraph0.internalAddEdge((Integer) null, (Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(0);
      directedMutableGraph0.addVertex(integer0);
      // Undeclared exception!
      try { 
        directedMutableGraph0.internalAddEdge(integer0, (Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-2142346125));
      directedMutableGraph0.addVertex(integer0);
      directedMutableGraph0.decorateRemoveVertex(integer0);
      // Undeclared exception!
      try { 
        directedMutableGraph0.addEdge(integer0, integer0, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-418));
      // Undeclared exception!
      try { 
        directedMutableGraph0.removeVertex(integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.removeVertex((Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(3);
      // Undeclared exception!
      try { 
        directedMutableGraph0.removeEdge(integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DirectedMutableGraph<Object, Integer> directedMutableGraph0 = new DirectedMutableGraph<Object, Integer>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.removeEdge((Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  // @Test(timeout = 4000)
  // public void test14()  throws Throwable  {
  //     DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
  //     Integer integer0 = new Integer((-418));
  //     directedMutableGraph0.addVertex(integer0);
  //     directedMutableGraph0.addEdge(integer0, integer0, integer0);
  //     Integer integer1 = new Integer((-418));
  //     directedMutableGraph0.addEdge(integer1, integer1, integer1);
  //     assertEquals(1, directedMutableGraph0.getOrder());
  // }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-418));
      directedMutableGraph0.addVertex(integer0);
      // Undeclared exception!
      try { 
        directedMutableGraph0.addVertex(integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.addVertex((Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1836));
      directedMutableGraph0.addVertex(integer0);
      directedMutableGraph0.addEdge(integer0, integer0, integer0);
      // Undeclared exception!
      try { 
        directedMutableGraph0.addEdge(integer0, integer0, integer0);
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
      Integer integer0 = new Integer((-2));
      // Undeclared exception!
      try { 
        directedMutableGraph0.addEdge(integer0, integer0, (Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(161);
      // Undeclared exception!
      try { 
        directedMutableGraph0.addEdge(integer0, (Integer) null, integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      // Undeclared exception!
      try { 
        directedMutableGraph0.addEdge((Integer) null, (Integer) null, (Integer) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DirectedMutableGraph<Object, Integer> directedMutableGraph1 = new DirectedMutableGraph<Object, Integer>();
      Integer integer0 = new Integer(2595);
      // Undeclared exception!
      try { 
        directedMutableGraph1.internalRemoveEdge(directedMutableGraph0, integer0, directedMutableGraph0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseMutableGraph", e);
      }
  }
}
