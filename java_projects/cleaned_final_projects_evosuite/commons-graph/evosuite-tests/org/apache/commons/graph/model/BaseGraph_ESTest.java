
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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.FormatFlagsConversionMismatchException;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.MissingFormatArgumentException;
import java.util.Set;
import java.util.UnknownFormatConversionException;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.model.BaseGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BaseGraph_ESTest extends BaseGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      UndirectedMutableGraph<Integer, Comparable<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Comparable<Integer>>();
      Integer integer0 = new Integer(1);
      undirectedMutableGraph0.addVertex(integer0);
      Integer integer1 = new Integer(1);
      undirectedMutableGraph0.addEdge(integer0, integer0, integer1);
      assertEquals(1, undirectedMutableGraph0.getOrder());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<VertexPair<Integer>, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<VertexPair<Integer>, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      Integer integer0 = new Integer((-2862));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      // Undeclared exception!
      try { 
        mutableSpanningTree0.getEdge(vertexPair0, (VertexPair<Integer>) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Object[] objectArray0 = new Object[5];
      BaseGraph.checkGraphCondition(true, "", objectArray0);
      assertEquals(5, objectArray0.length);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedMutableGraph<UndirectedMutableGraph<Integer, Integer>, MutableSpanningTree<Integer, Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<UndirectedMutableGraph<Integer, Integer>, MutableSpanningTree<Integer, Integer, Integer>>();
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      VertexPair<UndirectedMutableGraph<Integer, Integer>> vertexPair0 = directedMutableGraph0.getVertices1(mutableSpanningTree0);
      assertNull(vertexPair0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer(1630);
      undirectedMutableGraph0.addVertex(integer0);
      int int0 = undirectedMutableGraph0.getOrder();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      UndirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>>();
      Map<UndirectedMutableGraph<Integer, Integer>, VertexPair<Integer>> map0 = undirectedMutableGraph0.getIndexedVertices();
      assertTrue(map0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      UndirectedMutableGraph<UndirectedMutableGraph<Integer, Integer>, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<UndirectedMutableGraph<Integer, Integer>, Integer>();
      Map<VertexPair<UndirectedMutableGraph<Integer, Integer>>, Integer> map0 = undirectedMutableGraph0.getIndexedEdges();
      assertTrue(map0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      UndirectedMutableGraph<Integer, Comparable<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Comparable<Integer>>();
      Integer integer0 = new Integer(1);
      undirectedMutableGraph0.addVertex(integer0);
      Comparable<Integer> comparable0 = undirectedMutableGraph0.getEdge(integer0, integer0);
      assertNull(comparable0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UndirectedMutableGraph<VertexPair<Integer>, Object> undirectedMutableGraph0 = new UndirectedMutableGraph<VertexPair<Integer>, Object>();
      Set<Object> set0 = undirectedMutableGraph0.getAllEdges();
      assertEquals(0, set0.size());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<MutableSpanningTree<Integer, Integer, Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<MutableSpanningTree<Integer, Integer, Integer>, Integer>();
      Map<MutableSpanningTree<Integer, Integer, Integer>, Set<MutableSpanningTree<Integer, Integer, Integer>>> map0 = directedMutableGraph0.getAdjacencyList();
      assertEquals(0, map0.size());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DirectedMutableGraph<LinkedHashSet<Integer>, Object> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, Object>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      boolean boolean0 = directedMutableGraph0.containsVertex(linkedHashSet0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Integer integer0 = new Integer((-2862));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      UndirectedMutableGraph<VertexPair<Integer>, VertexPair<Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<VertexPair<Integer>, VertexPair<Integer>>();
      boolean boolean0 = undirectedMutableGraph0.containsVertex(vertexPair0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        BaseGraph.checkGraphCondition(false, "org.apache.commons.graph.model.MutableSpanningTree", (Object[]) null);
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
      Object[] objectArray0 = new Object[9];
      // Undeclared exception!
      try { 
        BaseGraph.checkGraphCondition(false, "HE%}R~;8I|2}vD", objectArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = '}'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Object[] objectArray0 = new Object[0];
      // Undeclared exception!
      try { 
        BaseGraph.checkGraphCondition(false, "Head Vertex '%s' not present in the Graph", objectArray0);
        fail("Expecting exception: MissingFormatArgumentException");
      
      } catch(MissingFormatArgumentException e) {
         //
         // Format specifier '%s'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Object[] objectArray0 = new Object[5];
      // Undeclared exception!
      try { 
        BaseGraph.checkGraphCondition(false, "Wt!vQ>x%04BJ+", objectArray0);
        fail("Expecting exception: FormatFlagsConversionMismatchException");
      
      } catch(FormatFlagsConversionMismatchException e) {
         //
         // Conversion = b, Flags = 0
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Object[] objectArray0 = new Object[0];
      // Undeclared exception!
      try { 
        BaseGraph.checkGraphCondition(false, (String) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      UndirectedMutableGraph<UndirectedMutableGraph<Integer, Integer>, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<UndirectedMutableGraph<Integer, Integer>, Integer>();
      undirectedMutableGraph0.hashCode();
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DirectedMutableGraph<Integer, Object> directedMutableGraph0 = new DirectedMutableGraph<Integer, Object>();
      String string0 = directedMutableGraph0.toString();
      assertEquals("{}", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>> directedMutableGraph1 = new DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>>();
      boolean boolean0 = directedMutableGraph1.equals(directedMutableGraph0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>>();
      boolean boolean0 = directedMutableGraph0.equals((Object) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>>();
      boolean boolean0 = directedMutableGraph0.equals(directedMutableGraph0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Object object0 = new Object();
      DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, UndirectedMutableGraph<Integer, Integer>>();
      boolean boolean0 = directedMutableGraph0.equals(object0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Monoid<Comparable<Integer>> monoid0 = (Monoid<Comparable<Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Comparable<Integer>) null).when(monoid0).identity();
      Mapper<Comparable<Integer>, Comparable<Integer>> mapper0 = (Mapper<Comparable<Integer>, Comparable<Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Comparable<Integer>, Comparable<Integer>> mutableSpanningTree0 = new MutableSpanningTree<Integer, Comparable<Integer>, Comparable<Integer>>(monoid0, mapper0);
      boolean boolean0 = mutableSpanningTree0.containsEdge((Comparable<Integer>) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      UndirectedMutableGraph<VertexPair<Integer>, VertexPair<Object>> undirectedMutableGraph0 = new UndirectedMutableGraph<VertexPair<Integer>, VertexPair<Object>>();
      int int0 = undirectedMutableGraph0.getSize();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Iterable<Integer> iterable0 = directedMutableGraph0.getEdges();
      assertNotNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DirectedMutableGraph<MutableSpanningTree<Object, Object, Integer>, VertexPair<Object>> directedMutableGraph0 = new DirectedMutableGraph<MutableSpanningTree<Object, Object, Integer>, VertexPair<Object>>();
      Iterable<MutableSpanningTree<Object, Object, Integer>> iterable0 = directedMutableGraph0.getVertices0();
      assertNotNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-2145857996));
      directedMutableGraph0.addVertex(integer0);
      Map<Integer, Set<Integer>> map0 = directedMutableGraph0.getAdjacencyList();
      assertFalse(map0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      int int0 = undirectedMutableGraph0.getOrder();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      DirectedMutableGraph<Integer, UndirectedMutableGraph<Object, Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, UndirectedMutableGraph<Object, Integer>>();
      Integer integer0 = new Integer(0);
      // Undeclared exception!
      try { 
        directedMutableGraph0.getConnectedVertices(integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }
}
