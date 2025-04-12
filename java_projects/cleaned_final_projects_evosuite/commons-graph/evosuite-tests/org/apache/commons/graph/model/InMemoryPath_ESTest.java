
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
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.model.InMemoryPath;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class InMemoryPath_ESTest extends InMemoryPath_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer(1312);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      Integer integer1 = new Integer(1312);
      inMemoryPath0.addConnectionInHead(integer0, integer0, integer1);
      assertEquals(2, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      inMemoryPath0.addConnectionInHead(integer0, vertexPair0, integer0);
      inMemoryPath0.getVertices1(vertexPair0);
      assertEquals(2, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Integer integer0 = new Integer(0);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, VertexPair<Integer>>(vertexPair0, vertexPair0);
      VertexPair<Integer> vertexPair1 = inMemoryPath0.getTarget();
      assertSame(vertexPair1, vertexPair0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      inMemoryPath0.getSize();
      assertEquals(2, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      int int0 = inMemoryPath0.getOrder();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Integer integer0 = new Integer(2299);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, InMemoryPath<Integer, Integer>> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, InMemoryPath<Integer, Integer>>(vertexPair0, vertexPair0);
      InMemoryPath<Integer, Integer> inMemoryPath1 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath0.addConnectionInTail(vertexPair0, inMemoryPath1, vertexPair0);
      inMemoryPath0.getEdge(vertexPair0, vertexPair0);
      assertEquals(2, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Integer integer0 = new Integer(0);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, Integer> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, Integer>(vertexPair0, vertexPair0);
      inMemoryPath0.addConnectionInHead(vertexPair0, integer0, vertexPair0);
      inMemoryPath0.containsVertex(vertexPair0);
      assertEquals(2, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer((-1783));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.getEdge(integer0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer((-529));
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.getDegree((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to get the degree of a null vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Integer integer0 = new Integer((-533));
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.getConnectedVertices((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to get the degree of a null vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Integer integer0 = new Integer((-513));
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.addConnectionInHead(integer0, vertexPair0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      InMemoryPath<Integer, Integer> inMemoryPath0 = null;
      try {
        inMemoryPath0 = new InMemoryPath<Integer, Integer>((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Path source cannot be null
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Integer integer0 = new Integer((-18));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      boolean boolean0 = inMemoryPath0.equals(inMemoryPath0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Integer integer0 = new Integer(0);
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      Iterable<VertexPair<Integer>> iterable0 = inMemoryPath0.getEdges();
      assertNotNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Integer integer0 = new Integer(4762);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath0.hashCode();
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Integer integer0 = new Integer((-2145645046));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      Integer integer1 = new Integer((-296));
      InMemoryPath<Integer, InMemoryPath<Integer, Integer>> inMemoryPath1 = new InMemoryPath<Integer, InMemoryPath<Integer, Integer>>(integer1, integer1);
      inMemoryPath1.addConnectionInTail(integer0, inMemoryPath0, integer1);
      int int0 = inMemoryPath1.getDegree(integer0);
      assertEquals(2, inMemoryPath1.getOrder());
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Integer integer0 = new Integer(373);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      Integer integer1 = new Integer((-2147018722));
      VertexPair<Integer> vertexPair1 = new VertexPair<Integer>(integer1, integer0);
      InMemoryPath<VertexPair<Integer>, Integer> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, Integer>(vertexPair0, vertexPair1);
      inMemoryPath0.addConnectionInTail(vertexPair1, (Integer) null, vertexPair1);
      int int0 = inMemoryPath0.getDegree(vertexPair1);
      assertEquals(2, inMemoryPath0.getOrder());
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Integer integer0 = new Integer((-540));
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.getDegree(integer0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; -540 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Integer integer0 = new Integer((-2146245189));
      Integer integer1 = new Integer(1034);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer1, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.getConnectedVertices(integer1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; 1034 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Integer integer0 = new Integer(296);
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      inMemoryPath0.addConnectionInTail(integer0, vertexPair0, integer0);
      InMemoryPath<Integer, Integer> inMemoryPath1 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath1.addConnectionInTail(integer0, integer0, integer0);
      boolean boolean0 = inMemoryPath1.equals(inMemoryPath0);
      assertEquals(2, inMemoryPath1.getOrder());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Integer integer0 = new Integer(1);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      InMemoryPath<Integer, Integer> inMemoryPath1 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath1.addConnectionInHead(integer0, integer0, integer0);
      boolean boolean0 = inMemoryPath0.equals(inMemoryPath1);
      assertEquals(2, inMemoryPath1.getOrder());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Integer integer0 = new Integer(2881);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      Integer integer1 = new Integer(257);
      InMemoryPath<Integer, Integer> inMemoryPath1 = new InMemoryPath<Integer, Integer>(integer0, integer1);
      boolean boolean0 = inMemoryPath0.equals(inMemoryPath1);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Integer integer0 = new Integer((-2136799647));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      InMemoryPath<InMemoryPath<Integer, Integer>, Integer> inMemoryPath1 = new InMemoryPath<InMemoryPath<Integer, Integer>, Integer>(inMemoryPath0, inMemoryPath0);
      boolean boolean0 = inMemoryPath1.equals(inMemoryPath0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Integer integer0 = new Integer(373);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, VertexPair<Integer>>(vertexPair0, vertexPair0);
      InMemoryPath<VertexPair<Integer>, InMemoryPath<Integer, Integer>> inMemoryPath1 = new InMemoryPath<VertexPair<Integer>, InMemoryPath<Integer, Integer>>(vertexPair0, vertexPair0);
      Object object0 = inMemoryPath1.getSource();
      boolean boolean0 = inMemoryPath0.equals(object0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Integer integer0 = new Integer((-540));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      boolean boolean0 = inMemoryPath0.equals((Object) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Integer integer0 = new Integer(2299);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      InMemoryPath<InMemoryPath<Integer, Integer>, InMemoryPath<Integer, Integer>> inMemoryPath1 = new InMemoryPath<InMemoryPath<Integer, Integer>, InMemoryPath<Integer, Integer>>(inMemoryPath0, inMemoryPath0);
      Iterable<InMemoryPath<Integer, Integer>> iterable0 = inMemoryPath1.getConnectedVertices(inMemoryPath0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      // Undeclared exception!
      try { 
        inMemoryPath0.addConnectionInTail(integer0, integer0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, VertexPair<Integer>>(vertexPair0, vertexPair0);
      inMemoryPath0.addConnectionInHead(vertexPair0, vertexPair0, vertexPair0);
      inMemoryPath0.containsEdge(vertexPair0);
      assertEquals(2, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Integer integer0 = new Integer((-2146245189));
      Integer integer1 = new Integer(1034);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer1, integer0);
      inMemoryPath0.addConnectionInHead(integer1, integer1, integer1);
      inMemoryPath0.getConnectedVertices(integer1);
      assertEquals(1, inMemoryPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Integer integer0 = new Integer(2299);
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, InMemoryPath<Integer, Integer>> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, InMemoryPath<Integer, Integer>>(vertexPair0, vertexPair0);
      InMemoryPath<Integer, Integer> inMemoryPath1 = inMemoryPath0.getEdge(vertexPair0, vertexPair0);
      assertNull(inMemoryPath1);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      int int0 = inMemoryPath0.getOrder();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      InMemoryPath<VertexPair<Integer>, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<VertexPair<Integer>, VertexPair<Integer>>(vertexPair0, vertexPair0);
      boolean boolean0 = inMemoryPath0.containsEdge(vertexPair0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Integer integer0 = new Integer(0);
      InMemoryPath<Integer, VertexPair<Integer>> inMemoryPath0 = new InMemoryPath<Integer, VertexPair<Integer>>(integer0, integer0);
      int int0 = inMemoryPath0.getSize();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Integer integer0 = new Integer((-40));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      boolean boolean0 = inMemoryPath0.containsVertex(integer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Integer integer0 = new Integer((-540));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      VertexPair<Integer> vertexPair0 = inMemoryPath0.getVertices1(integer0);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      InMemoryPath<Integer, Integer> inMemoryPath1 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      boolean boolean0 = inMemoryPath1.equals(inMemoryPath0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Integer integer0 = new Integer((-2838));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      inMemoryPath0.addConnectionInTail(integer0, integer0, integer0);
      int int0 = inMemoryPath0.getDegree(integer0);
      assertEquals(2, inMemoryPath0.getOrder());
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      Integer integer0 = new Integer(2299);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      String string0 = inMemoryPath0.toString();
      assertEquals("InMemoryPath [vertices=[], edges=[]]", string0);
  }
}
