
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
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class UndirectedMutableGraph_ESTest extends UndirectedMutableGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      UndirectedMutableGraph<LinkedHashSet<Integer>, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<LinkedHashSet<Integer>, Integer>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer0 = new Integer(3920);
      // Undeclared exception!
      try { 
        undirectedMutableGraph0.decorateAddEdge(linkedHashSet0, integer0, linkedHashSet0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      UndirectedMutableGraph<Integer, LinkedHashSet<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      Integer integer0 = new Integer((-3966));
      undirectedMutableGraph0.decorateAddVertex(integer0);
      assertEquals(0, undirectedMutableGraph0.getOrder());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-2158));
      undirectedMutableGraph0.addVertex(integer0);
      int int0 = undirectedMutableGraph0.getDegree(integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      UndirectedMutableGraph<LinkedHashSet<Integer>, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<LinkedHashSet<Integer>, Integer>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      undirectedMutableGraph0.addVertex(linkedHashSet0);
      Integer integer0 = new Integer(3);
      undirectedMutableGraph0.internalAddEdge(linkedHashSet0, integer0, linkedHashSet0);
      int int0 = undirectedMutableGraph0.getDegree(linkedHashSet0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(0);
      undirectedMutableGraph0.addVertex(integer0);
      // Undeclared exception!
      try { 
        undirectedMutableGraph0.decorateAddEdge((Integer) null, (Integer) null, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      UndirectedMutableGraph<Integer, LinkedHashSet<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      Integer integer0 = new Integer((-1485));
      undirectedMutableGraph0.decorateRemoveVertex(integer0);
      assertEquals(0, undirectedMutableGraph0.getSize());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Integer integer0 = new Integer((-1923));
      UndirectedMutableGraph<Integer, LinkedHashSet<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      // Undeclared exception!
      try { 
        undirectedMutableGraph0.getDegree(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.UndirectedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      UndirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      undirectedMutableGraph0.addVertex(linkedHashSet0);
      undirectedMutableGraph0.decorateAddEdge(linkedHashSet0, linkedHashSet0, linkedHashSet0);
      undirectedMutableGraph0.decorateRemoveEdge(linkedHashSet0);
      assertTrue(linkedHashSet0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      UndirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      // Undeclared exception!
      try { 
        undirectedMutableGraph0.decorateRemoveEdge(linkedHashSet0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.UndirectedMutableGraph", e);
      }
  }
}
