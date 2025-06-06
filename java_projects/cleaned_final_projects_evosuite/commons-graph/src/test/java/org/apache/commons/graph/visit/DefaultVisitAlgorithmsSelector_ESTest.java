
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


package org.apache.commons.graph.visit;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.visit.BaseGraphVisitHandler;
import org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector;
import org.apache.commons.graph.visit.GraphVisitHandler;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultVisitAlgorithmsSelector_ESTest extends DefaultVisitAlgorithmsSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>();
      DefaultVisitAlgorithmsSelector<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>>(directedMutableGraph0, directedMutableGraph0);
      BaseGraphVisitHandler<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>, Object> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>, Object>();
      Integer integer0 = new Integer((-1809));
      DirectedMutableGraph<Integer, Integer> directedMutableGraph1 = new DirectedMutableGraph<Integer, Integer>();
      DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>> directedMutableGraph2 = (DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>) mock(DirectedMutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(directedMutableGraph2).getOutbound(anyInt());
      DefaultVisitAlgorithmsSelector<Integer, RevertedGraph<Integer, Integer>, DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>> defaultVisitAlgorithmsSelector1 = new DefaultVisitAlgorithmsSelector<Integer, RevertedGraph<Integer, Integer>, DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>>(directedMutableGraph2, integer0);
      BaseGraphVisitHandler<Integer, RevertedGraph<Integer, Integer>, DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>, Comparable<Object>> baseGraphVisitHandler1 = new BaseGraphVisitHandler<Integer, RevertedGraph<Integer, Integer>, DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>, Comparable<Object>>();
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector1.applyingDepthFirstSearch1((GraphVisitHandler<Integer, RevertedGraph<Integer, Integer>, DirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>, Comparable<Object>>) baseGraphVisitHandler1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      directedMutableGraph0.addVertex(revertedGraph0);
      DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>>(revertedGraph0, revertedGraph0);
      Graph<Object, Object> graph0 = defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch0();
      assertNotNull(graph0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      directedMutableGraph0.addVertex(revertedGraph0);
      DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>>(revertedGraph0, revertedGraph0);
      BaseGraphVisitHandler<Object, Object, RevertedGraph<Object, Object>, VertexPair<Integer>> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Object, Object, RevertedGraph<Object, Object>, VertexPair<Integer>>();
      VertexPair<Integer> vertexPair0 = defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1((GraphVisitHandler<Object, Object, RevertedGraph<Object, Object>, VertexPair<Integer>>) baseGraphVisitHandler0);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      UndirectedMutableGraph<Comparable<Integer>, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Comparable<Integer>, Integer>();
      Integer integer0 = Integer.getInteger((String) null, 0);
      DefaultVisitAlgorithmsSelector<Comparable<Integer>, Integer, UndirectedMutableGraph<Comparable<Integer>, Integer>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Comparable<Integer>, Integer, UndirectedMutableGraph<Comparable<Integer>, Integer>>(undirectedMutableGraph0, integer0);
      BaseGraphVisitHandler<Comparable<Integer>, Integer, UndirectedMutableGraph<Comparable<Integer>, Integer>, Integer> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Comparable<Integer>, Integer, UndirectedMutableGraph<Comparable<Integer>, Integer>, Integer>();
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch1((GraphVisitHandler<Comparable<Integer>, Integer, UndirectedMutableGraph<Comparable<Integer>, Integer>, Integer>) baseGraphVisitHandler0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>();
      DefaultVisitAlgorithmsSelector<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>>(directedMutableGraph0, directedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch1((GraphVisitHandler<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Graph visitor handler can not be null.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Object object0 = new Object();
      InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>> inMemoryPath0 = new InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>>(object0, object0);
      DefaultVisitAlgorithmsSelector<Object, MutableSpanningTree<Object, Integer, Object>, InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, MutableSpanningTree<Object, Integer, Object>, InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>>>(inMemoryPath0, inMemoryPath0);
      BaseGraphVisitHandler<Object, MutableSpanningTree<Object, Integer, Object>, InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>>, Integer> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Object, MutableSpanningTree<Object, Integer, Object>, InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>>, Integer>();
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch1((GraphVisitHandler<Object, MutableSpanningTree<Object, Integer, Object>, InMemoryPath<Object, MutableSpanningTree<Object, Integer, Object>>, Integer>) baseGraphVisitHandler0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; InMemoryPath [vertices=[], edges=[]] not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      UndirectedMutableGraph<Object, Comparable<Object>> undirectedMutableGraph0 = new UndirectedMutableGraph<Object, Comparable<Object>>();
      Object object0 = new Object();
      DefaultVisitAlgorithmsSelector<Object, Comparable<Object>, UndirectedMutableGraph<Object, Comparable<Object>>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, Comparable<Object>, UndirectedMutableGraph<Object, Comparable<Object>>>(undirectedMutableGraph0, object0);
      BaseGraphVisitHandler<Object, Comparable<Object>, UndirectedMutableGraph<Object, Comparable<Object>>, Object> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Object, Comparable<Object>, UndirectedMutableGraph<Object, Comparable<Object>>, Object>();
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1((GraphVisitHandler<Object, Comparable<Object>, UndirectedMutableGraph<Object, Comparable<Object>>, Object>) baseGraphVisitHandler0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BaseGraphVisitHandler<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>, Object> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>, Object>();
      DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>();
      DefaultVisitAlgorithmsSelector<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>>(directedMutableGraph0, directedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1((GraphVisitHandler<Object, DirectedMutableGraph<Integer, Integer>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Integer>>, Object>) baseGraphVisitHandler0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Comparable<Object> comparable0 = (Comparable<Object>) mock(Comparable.class, new ViolatedAssumptionAnswer());
      InMemoryPath<Comparable<Object>, Comparable<Integer>> inMemoryPath0 = new InMemoryPath<Comparable<Object>, Comparable<Integer>>(comparable0, comparable0);
      Comparable<Object> comparable1 = (Comparable<Object>) mock(Comparable.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(comparable1).toString();
      DefaultVisitAlgorithmsSelector<Comparable<Object>, Comparable<Integer>, InMemoryPath<Comparable<Object>, Comparable<Integer>>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Comparable<Object>, Comparable<Integer>, InMemoryPath<Comparable<Object>, Comparable<Integer>>>(inMemoryPath0, comparable1);
      BaseGraphVisitHandler<Comparable<Object>, Comparable<Integer>, InMemoryPath<Comparable<Object>, Comparable<Integer>>, Object> baseGraphVisitHandler0 = new BaseGraphVisitHandler<Comparable<Object>, Comparable<Integer>, InMemoryPath<Comparable<Object>, Comparable<Integer>>, Object>();
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1((GraphVisitHandler<Comparable<Object>, Comparable<Integer>, InMemoryPath<Comparable<Object>, Comparable<Integer>>, Object>) baseGraphVisitHandler0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; null not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      directedMutableGraph0.addVertex(revertedGraph0);
      DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>>(revertedGraph0, revertedGraph0);
      Graph<Object, Object> graph0 = defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch0();
      assertNotNull(graph0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>>(revertedGraph0, revertedGraph0);
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>> defaultVisitAlgorithmsSelector0 = new DefaultVisitAlgorithmsSelector<Object, Object, RevertedGraph<Object, Object>>(revertedGraph0, revertedGraph0);
      // Undeclared exception!
      try { 
        defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e);
      }
  }
}
