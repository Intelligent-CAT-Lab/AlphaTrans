
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
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.SynchronizedDirectedGraph;
import org.apache.commons.graph.SynchronizedGraph;
import org.apache.commons.graph.SynchronizedMutableGraph;
import org.apache.commons.graph.SynchronizedUndirectedGraph;
import org.apache.commons.graph.VertexPair;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SynchronizedGraph_ESTest extends SynchronizedGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      VertexPair<SynchronizedGraph<Object, Object>> vertexPair0 = (VertexPair<SynchronizedGraph<Object, Object>>) mock(VertexPair.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(vertexPair0).toString();
      MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(vertexPair0).when(mutableGraph0).getVertices1(any(org.apache.commons.graph.SynchronizedGraph.class));
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>(mutableGraph0);
      MutableGraph<Object, Object> mutableGraph1 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph1 = new SynchronizedMutableGraph<Object, Object>(mutableGraph1);
      VertexPair<SynchronizedGraph<Object, Object>> vertexPair1 = synchronizedMutableGraph0.getVertices1(synchronizedMutableGraph1);
      assertSame(vertexPair1, vertexPair0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(mutableGraph0).getVertices0();
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      Iterable<Object> iterable0 = synchronizedMutableGraph0.getVertices0();
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      MutableGraph<Object, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<Object, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>>(mutableGraph0);
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(directedGraph0).getEdges();
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      Iterable<Object> iterable0 = synchronizedDirectedGraph0.getEdges();
      MutableGraph<Object, Object> mutableGraph1 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(iterable0).when(mutableGraph1).getVertices0();
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph1 = new SynchronizedMutableGraph<Object, Object>(mutableGraph1);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedMutableGraph1);
      Iterable<Object> iterable1 = synchronizedUndirectedGraph0.getVertices0();
      assertNull(iterable1);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(directedGraph0).getSize();
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      int int0 = synchronizedDirectedGraph0.getSize();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedGraph<Object, SynchronizedGraph<Object, Object>> directedGraph0 = (DirectedGraph<Object, SynchronizedGraph<Object, Object>>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((-1)).when(directedGraph0).getSize();
      SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>>(directedGraph0);
      int int0 = synchronizedDirectedGraph0.getSize();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(mutableGraph0).getOrder();
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>(mutableGraph0);
      int int0 = synchronizedMutableGraph0.getOrder();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedGraph<Object, SynchronizedGraph<Object, Object>> directedGraph0 = (DirectedGraph<Object, SynchronizedGraph<Object, Object>>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((-935)).when(directedGraph0).getOrder();
      SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>>(directedGraph0);
      SynchronizedUndirectedGraph<Object, SynchronizedGraph<Object, Object>> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, SynchronizedGraph<Object, Object>>(synchronizedDirectedGraph0);
      int int0 = synchronizedUndirectedGraph0.getOrder();
      assertEquals((-935), int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable<Object>) null).when(mutableGraph0).getEdges();
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      Iterable<Object> iterable0 = synchronizedMutableGraph0.getEdges();
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      MutableGraph<Object, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<Object, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>>(mutableGraph0);
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(directedGraph0).getEdges();
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      Iterable<Object> iterable0 = synchronizedDirectedGraph0.getEdges();
      MutableGraph<SynchronizedGraph<Object, Object>, Object> mutableGraph1 = (MutableGraph<SynchronizedGraph<Object, Object>, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(iterable0).when(mutableGraph1).getEdges();
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph1 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>(mutableGraph1);
      Iterable<Object> iterable1 = synchronizedMutableGraph1.getEdges();
      assertNull(iterable1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(directedGraph0).getEdge(any() , any());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      DirectedGraph<Object, SynchronizedGraph<Object, Object>> directedGraph1 = (DirectedGraph<Object, SynchronizedGraph<Object, Object>>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>> synchronizedDirectedGraph1 = new SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>>(directedGraph1);
      Object object0 = synchronizedDirectedGraph0.getEdge(synchronizedDirectedGraph1, synchronizedDirectedGraph1);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(directedGraph0).getDegree(any());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedDirectedGraph0);
      int int0 = synchronizedUndirectedGraph0.getDegree(synchronizedDirectedGraph0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((-935)).when(directedGraph0).getDegree(any());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedDirectedGraph0);
      int int0 = synchronizedUndirectedGraph0.getDegree(synchronizedDirectedGraph0);
      assertEquals((-935), int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(mutableGraph0).getConnectedVertices(any());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      Iterable<Object> iterable0 = synchronizedMutableGraph0.getConnectedVertices((Object) null);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(true).when(mutableGraph0).containsVertex(any());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedMutableGraph0);
      Object object0 = new Object();
      boolean boolean0 = synchronizedUndirectedGraph0.containsVertex(object0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(true).when(directedGraph0).containsEdge(any());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      boolean boolean0 = synchronizedDirectedGraph0.containsEdge(synchronizedMutableGraph0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>((MutableGraph<SynchronizedGraph<Object, Object>, Object>) null);
      // Undeclared exception!
      try { 
        synchronizedMutableGraph0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>((Graph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>) null);
      // Undeclared exception!
      try { 
        synchronizedUndirectedGraph0.getVertices1(synchronizedDirectedGraph0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>((MutableGraph<Object, Object>) null);
      // Undeclared exception!
      try { 
        synchronizedMutableGraph0.getVertices0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      SynchronizedGraph<Object, Object> synchronizedGraph0 = new SynchronizedGraph<Object, Object>((Graph<Object, Object>) null);
      // Undeclared exception!
      try { 
        synchronizedGraph0.getSize();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>((Graph<Object, Object>) null);
      // Undeclared exception!
      try { 
        synchronizedUndirectedGraph0.getOrder();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>>((DirectedGraph<Object, SynchronizedGraph<Object, Object>>) null);
      // Undeclared exception!
      try { 
        synchronizedDirectedGraph0.getEdges();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, Object>((Graph<SynchronizedGraph<Object, Object>, Object>) null);
      // Undeclared exception!
      try { 
        synchronizedUndirectedGraph0.getDegree((SynchronizedGraph<Object, Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>((Graph<Object, Object>) null);
      // Undeclared exception!
      try { 
        synchronizedUndirectedGraph0.getConnectedVertices((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>((MutableGraph<Object, Object>) null);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedMutableGraph0);
      // Undeclared exception!
      try { 
        synchronizedUndirectedGraph0.containsVertex(synchronizedUndirectedGraph0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      SynchronizedGraph<Object, Object> synchronizedGraph0 = new SynchronizedGraph<Object, Object>((Graph<Object, Object>) null);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedGraph0);
      // Undeclared exception!
      try { 
        synchronizedUndirectedGraph0.containsEdge((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>((MutableGraph<SynchronizedGraph<Object, Object>, Object>) null);
      synchronizedMutableGraph0.hashCode();
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      synchronizedDirectedGraph0.hashCode();
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      SynchronizedGraph<Object, Object> synchronizedGraph0 = new SynchronizedGraph<Object, Object>(synchronizedMutableGraph0);
      MutableGraph<SynchronizedGraph<Object, Object>, Object> mutableGraph1 = (MutableGraph<SynchronizedGraph<Object, Object>, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph1 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>(mutableGraph1);
      SynchronizedGraph<SynchronizedGraph<Object, Object>, Object> synchronizedGraph1 = new SynchronizedGraph<SynchronizedGraph<Object, Object>, Object>(synchronizedMutableGraph1);
      boolean boolean0 = synchronizedGraph1.equals(synchronizedGraph0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>((MutableGraph<SynchronizedGraph<Object, Object>, Object>) null);
      boolean boolean0 = synchronizedMutableGraph0.equals((Object) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedDirectedGraph0);
      boolean boolean0 = synchronizedUndirectedGraph0.equals(synchronizedUndirectedGraph0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>(mutableGraph0);
      SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>(synchronizedMutableGraph0);
      Object object0 = new Object();
      boolean boolean0 = synchronizedUndirectedGraph0.equals(object0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedDirectedGraph0);
      DirectedGraph<Object, SynchronizedGraph<Object, Object>> directedGraph1 = (DirectedGraph<Object, SynchronizedGraph<Object, Object>>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(synchronizedDirectedGraph0).when(directedGraph1).getEdge(any() , any());
      SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>> synchronizedDirectedGraph1 = new SynchronizedDirectedGraph<Object, SynchronizedGraph<Object, Object>>(directedGraph1);
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>((MutableGraph<Object, Object>) null);
      SynchronizedGraph<Object, Object> synchronizedGraph0 = synchronizedDirectedGraph1.getEdge(synchronizedMutableGraph0, synchronizedUndirectedGraph0);
      assertEquals(0, synchronizedGraph0.getSize());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      MutableGraph<Object, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<Object, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(mutableGraph0).containsEdge(any(org.apache.commons.graph.SynchronizedGraph.class));
      SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>>(mutableGraph0);
      MutableGraph<Object, Object> mutableGraph1 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph1 = new SynchronizedMutableGraph<Object, Object>(mutableGraph1);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedMutableGraph1);
      boolean boolean0 = synchronizedMutableGraph0.containsEdge(synchronizedUndirectedGraph0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      MutableGraph<Object, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<Object, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>>(mutableGraph0);
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((VertexPair) null).when(directedGraph0).getVertices1(any());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      VertexPair<Object> vertexPair0 = synchronizedDirectedGraph0.getVertices1(synchronizedMutableGraph0);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      SynchronizedUndirectedGraph<Object, Object> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<Object, Object>(synchronizedDirectedGraph0);
      MutableGraph<SynchronizedGraph<Object, Object>, Object> mutableGraph0 = (MutableGraph<SynchronizedGraph<Object, Object>, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(4432).when(mutableGraph0).getDegree(any(org.apache.commons.graph.SynchronizedGraph.class));
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>(mutableGraph0);
      int int0 = synchronizedMutableGraph0.getDegree(synchronizedUndirectedGraph0);
      assertEquals(4432, int0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(4432).when(mutableGraph0).getSize();
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>(mutableGraph0);
      SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>> synchronizedUndirectedGraph0 = new SynchronizedUndirectedGraph<SynchronizedGraph<Object, Object>, SynchronizedGraph<Object, Object>>(synchronizedMutableGraph0);
      int int0 = synchronizedUndirectedGraph0.getSize();
      assertEquals(4432, int0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      MutableGraph<Object, SynchronizedGraph<Object, Object>> mutableGraph0 = (MutableGraph<Object, SynchronizedGraph<Object, Object>>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, SynchronizedGraph<Object, Object>>(mutableGraph0);
      String string0 = synchronizedMutableGraph0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(mutableGraph0).containsVertex(any());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      boolean boolean0 = synchronizedMutableGraph0.containsVertex(synchronizedDirectedGraph0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      MutableGraph<SynchronizedGraph<Object, Object>, Object> mutableGraph0 = (MutableGraph<SynchronizedGraph<Object, Object>, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(1).when(mutableGraph0).getOrder();
      SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<SynchronizedGraph<Object, Object>, Object>(mutableGraph0);
      int int0 = synchronizedMutableGraph0.getOrder();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      DirectedGraph<Object, Object> directedGraph0 = (DirectedGraph<Object, Object>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(directedGraph0).getVertices0();
      SynchronizedDirectedGraph<Object, Object> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Object, Object>(directedGraph0);
      Iterable<Object> iterable0 = synchronizedDirectedGraph0.getVertices0();
      Object object0 = new Object();
      MutableGraph<Object, Object> mutableGraph0 = (MutableGraph<Object, Object>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      doReturn(iterable0).when(mutableGraph0).getConnectedVertices(any());
      SynchronizedMutableGraph<Object, Object> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Object, Object>(mutableGraph0);
      Iterable<Object> iterable1 = synchronizedMutableGraph0.getConnectedVertices(object0);
      assertNull(iterable1);
  }
}
