
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


package org.apache.commons.graph;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.CommonsGraph;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.SynchronizedDirectedGraph;
import org.apache.commons.graph.SynchronizedMutableGraph;
import org.apache.commons.graph.SynchronizedUndirectedGraph;
import org.apache.commons.graph.UndirectedGraph;
import org.apache.commons.graph.builder.GraphConnection;
import org.apache.commons.graph.builder.LinkedConnectionBuilder;
import org.apache.commons.graph.coloring.ColorsBuilder;
import org.apache.commons.graph.connectivity.ConnectivityBuilder;
import org.apache.commons.graph.elo.GameResult;
import org.apache.commons.graph.elo.RankingSelector;
import org.apache.commons.graph.export.NamedExportSelector;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.scc.SccAlgorithmSelector;
import org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder;
import org.apache.commons.graph.visit.VisitSourceSelector;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CommonsGraph_ESTest extends CommonsGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      VisitSourceSelector<Object, Object, MutableGraph<Object, Object>> visitSourceSelector0 = CommonsGraph.visit((MutableGraph<Object, Object>) directedMutableGraph0);
      assertNotNull(visitSourceSelector0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      GraphConnection<Object, Object> graphConnection0 = (GraphConnection<Object, Object>) mock(GraphConnection.class, new ViolatedAssumptionAnswer());
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = CommonsGraph.newDirectedMutableGraph(graphConnection0);
      Object object0 = new Object();
      directedMutableGraph0.addVertex(object0);
      Graph<Object, Object> graph0 = CommonsGraph.synchronize1((Graph<Object, Object>) directedMutableGraph0);
      assertEquals(1, graph0.getOrder());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      GraphConnection<Object, Object> graphConnection0 = (GraphConnection<Object, Object>) mock(GraphConnection.class, new ViolatedAssumptionAnswer());
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = CommonsGraph.newDirectedMutableGraph(graphConnection0);
      Object object0 = new Object();
      directedMutableGraph0.addVertex(object0);
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedMutableGraph0);
      Graph<Object, Object> graph0 = CommonsGraph.synchronize0((DirectedGraph<Object, Object>) synchronizedDirectedGraph0);
      assertEquals(0, graph0.getSize());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      ConnectivityBuilder<Object, Object> connectivityBuilder0 = CommonsGraph.findConnectedComponent((DirectedGraph<Object, Object>) directedMutableGraph0);
      assertNotNull(connectivityBuilder0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      NamedExportSelector<Object, Object> namedExportSelector0 = CommonsGraph.export((DirectedGraph<Object, Object>) directedMutableGraph0);
      assertNotNull(namedExportSelector0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedMutableGraph<Object, MutableGraph<Object, Object>> directedMutableGraph0 = new DirectedMutableGraph<Object, MutableGraph<Object, Object>>();
      SynchronizedDirectedGraph<Object, MutableGraph<Object, Object>> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, MutableGraph<Object, Object>>(directedMutableGraph0);
      SynchronizedUndirectedGraph<Object, MutableGraph<Object, Object>> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, MutableGraph<Object, Object>>(synchronizedDirectedGraph0);
      ColorsBuilder<Object, MutableGraph<Object, Object>> colorsBuilder0 = CommonsGraph.coloring(synchronizedUndirectedGraph0);
      assertNotNull(colorsBuilder0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.populate((SynchronizedMutableGraph<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to configure null graph!
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.newUndirectedMutableGraph((GraphConnection<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Input graph cannot be configured with null connections
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.findStronglyConnectedComponent((DirectedGraph<DirectedGraph<DirectedGraph, Object>, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Strongly Connected Component cannot be calculated from a null graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.findShortestPath((SynchronizedUndirectedGraph<SynchronizedUndirectedGraph<Object, Object>, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Shortest path can not be calculated on null graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.eloRate((DirectedGraph<DirectedGraph<Object, Object>, GameResult>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // ELO ranking can not be applied on null graph!
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(directedMutableGraph0);
      LinkedConnectionBuilder<Object, Object, SynchronizedMutableGraph<Object, Object>> linkedConnectionBuilder0 = CommonsGraph.populate(synchronizedMutableGraph0);
      assertNotNull(linkedConnectionBuilder0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.visit((SynchronizedUndirectedGraph<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // No algorithm can be applied on null graph!
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      UndirectedMutableGraph<SynchronizedMutableGraph<Object, Object>, SynchronizedMutableGraph<Object, Object>> undirectedMutableGraph0 = new UndirectedMutableGraph<SynchronizedMutableGraph<Object, Object>, SynchronizedMutableGraph<Object, Object>>();
      Graph<SynchronizedMutableGraph<Object, Object>, SynchronizedMutableGraph<Object, Object>> graph0 = CommonsGraph.synchronize3((UndirectedGraph<SynchronizedMutableGraph<Object, Object>, SynchronizedMutableGraph<Object, Object>>) undirectedMutableGraph0);
      assertEquals(0, graph0.getOrder());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedMutableGraph0);
      SccAlgorithmSelector<Object, Object> sccAlgorithmSelector0 = CommonsGraph.findStronglyConnectedComponent(synchronizedDirectedGraph0);
      assertNotNull(sccAlgorithmSelector0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.export((Graph<Graph<Object, Graph>, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null graph can not be exported
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      Graph<Object, Object> graph0 = CommonsGraph.synchronize0((DirectedGraph<Object, Object>) directedMutableGraph0);
      assertEquals(0, graph0.getSize());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.minimumSpanningTree((DirectedGraph<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Minimum spanning tree can not be calculated on null graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      Graph<Object, Object> graph0 = CommonsGraph.synchronize1((Graph<Object, Object>) directedMutableGraph0);
      assertEquals(0, graph0.getOrder());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.findConnectedComponent((DirectedGraph<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Connected Component cannot be calculated from a null graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.coloring((UndirectedGraph<MutableGraph<MutableGraph, Object>, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Coloring can not be calculated on null graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.findMaxFlow((DirectedGraph<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Max flow can not be calculated on null graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      DirectedMutableGraph<Object, GameResult> directedMutableGraph0 = new DirectedMutableGraph<Object, GameResult>();
      RankingSelector<Object> rankingSelector0 = CommonsGraph.eloRate((DirectedGraph<Object, GameResult>) directedMutableGraph0);
      assertNotNull(rankingSelector0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(directedMutableGraph0);
      PathWeightedEdgesBuilder<Object, Object> pathWeightedEdgesBuilder0 = CommonsGraph.findShortestPath(synchronizedMutableGraph0);
      assertNotNull(pathWeightedEdgesBuilder0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommonsGraph.newDirectedMutableGraph((GraphConnection<SynchronizedUndirectedGraph<SynchronizedUndirectedGraph, Object>, SynchronizedUndirectedGraph<Object, Object>>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Input graph cannot be configured with null connections
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
