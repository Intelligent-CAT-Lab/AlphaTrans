
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


package org.apache.commons.graph.shortestpath;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.math.BigInteger;
import java.math.RoundingMode;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector;
import org.apache.commons.graph.shortestpath.HeuristicBuilder;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations;
import org.apache.commons.graph.weight.primitive.LongWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultShortestPathAlgorithmSelector_ESTest extends DefaultShortestPathAlgorithmSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<Object, RoundingMode> directedMutableGraph0 = new DirectedMutableGraph<Object, RoundingMode>();
      Mapper<RoundingMode, RoundingMode> mapper0 = (Mapper<RoundingMode, RoundingMode>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      DefaultShortestPathAlgorithmSelector<Object, RoundingMode, RoundingMode> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<Object, RoundingMode, RoundingMode>(directedMutableGraph0, mapper0, roundingMode0, directedMutableGraph0);
      OrderedMonoid<RoundingMode> orderedMonoid0 = (OrderedMonoid<RoundingMode>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingDijkstra(orderedMonoid0);
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
      DirectedMutableGraph<OrderedMonoid<BigInteger>, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<BigInteger>, BigInteger>();
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, BigInteger> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, BigInteger>(directedMutableGraph0, (Mapper<BigInteger, BigInteger>) null, bigIntegerWeightBaseOperations0, (OrderedMonoid<BigInteger>) null);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingDijkstra((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      UndirectedMutableGraph<RoundingMode, OrderedMonoid<RoundingMode>> undirectedMutableGraph0 = new UndirectedMutableGraph<RoundingMode, OrderedMonoid<RoundingMode>>();
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      DefaultShortestPathAlgorithmSelector<RoundingMode, OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<RoundingMode, OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>>(undirectedMutableGraph0, (Mapper<OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>>) null, roundingMode0, roundingMode0);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingDijkstra((OrderedMonoid<OrderedMonoid<RoundingMode>>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Dijkstra algorithm can not be applied using null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      InMemoryPath<OrderedMonoid<BigInteger>, BigInteger> inMemoryPath0 = new InMemoryPath<OrderedMonoid<BigInteger>, BigInteger>(bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0);
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations1 = new BigIntegerWeightBaseOperations();
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, BigInteger> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, BigInteger>(inMemoryPath0, (Mapper<BigInteger, BigInteger>) null, bigIntegerWeightBaseOperations1, bigIntegerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingDijkstra((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations@3 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      InMemoryPath<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>> inMemoryPath0 = new InMemoryPath<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>>(bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0);
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>, BigInteger> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>, BigInteger>(inMemoryPath0, (Mapper<OrderedMonoid<BigInteger>, BigInteger>) null, bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Object object0 = new Object();
      DefaultShortestPathAlgorithmSelector<Object, Object, Object> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<Object, Object, Object>((Graph<Object, Object>) null, (Mapper<Object, Object>) null, object0, object0);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra((OrderedMonoid<Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Bidirectional Dijkstra algorithm can not be applied using null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      InMemoryPath<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>> inMemoryPath0 = new InMemoryPath<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>>(bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0);
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations1 = new BigIntegerWeightBaseOperations();
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>, BigInteger> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<BigInteger>, OrderedMonoid<BigInteger>, BigInteger>(inMemoryPath0, (Mapper<OrderedMonoid<BigInteger>, BigInteger>) null, bigIntegerWeightBaseOperations1, bigIntegerWeightBaseOperations1);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations@3 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<LongWeightBaseOperations>, RevertedGraph<RoundingMode, RoundingMode>> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<LongWeightBaseOperations>, RevertedGraph<RoundingMode, RoundingMode>>();
      Mapper<RevertedGraph<RoundingMode, RoundingMode>, LongWeightBaseOperations> mapper0 = (Mapper<RevertedGraph<RoundingMode, RoundingMode>, LongWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<LongWeightBaseOperations>, RevertedGraph<RoundingMode, RoundingMode>, LongWeightBaseOperations> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<LongWeightBaseOperations>, RevertedGraph<RoundingMode, RoundingMode>, LongWeightBaseOperations>(directedMutableGraph0, mapper0, (OrderedMonoid<LongWeightBaseOperations>) null, (OrderedMonoid<LongWeightBaseOperations>) null);
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingAStar((OrderedMonoid<LongWeightBaseOperations>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // A* algorithm can not be applied using null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UndirectedMutableGraph<RoundingMode, OrderedMonoid<RoundingMode>> undirectedMutableGraph0 = new UndirectedMutableGraph<RoundingMode, OrderedMonoid<RoundingMode>>();
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      undirectedMutableGraph0.addVertex(roundingMode0);
      OrderedMonoid<RoundingMode> orderedMonoid0 = (OrderedMonoid<RoundingMode>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      undirectedMutableGraph0.addEdge(roundingMode0, orderedMonoid0, roundingMode0);
      RoundingMode roundingMode1 = RoundingMode.DOWN;
      DefaultShortestPathAlgorithmSelector<RoundingMode, OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<RoundingMode, OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>>(undirectedMutableGraph0, (Mapper<OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>>) null, roundingMode0, roundingMode1);
      OrderedMonoid<OrderedMonoid<RoundingMode>> orderedMonoid1 = (OrderedMonoid<OrderedMonoid<RoundingMode>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid1).identity();
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingDijkstra(orderedMonoid1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      UndirectedMutableGraph<RoundingMode, OrderedMonoid<RoundingMode>> undirectedMutableGraph0 = new UndirectedMutableGraph<RoundingMode, OrderedMonoid<RoundingMode>>();
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      undirectedMutableGraph0.addVertex(roundingMode0);
      OrderedMonoid<RoundingMode> orderedMonoid0 = (OrderedMonoid<RoundingMode>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      undirectedMutableGraph0.addEdge(roundingMode0, orderedMonoid0, roundingMode0);
      DefaultShortestPathAlgorithmSelector<RoundingMode, OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<RoundingMode, OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>>(undirectedMutableGraph0, (Mapper<OrderedMonoid<RoundingMode>, OrderedMonoid<RoundingMode>>) null, roundingMode0, roundingMode0);
      OrderedMonoid<OrderedMonoid<RoundingMode>> orderedMonoid1 = (OrderedMonoid<OrderedMonoid<RoundingMode>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null).when(orderedMonoid1).identity();
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra(orderedMonoid1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      directedMutableGraph0.addVertex(revertedGraph0);
      Mapper<Object, Object> mapper0 = (Mapper<Object, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultShortestPathAlgorithmSelector<Object, Object, Object> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<Object, Object, Object>(revertedGraph0, mapper0, revertedGraph0, revertedGraph0);
      OrderedMonoid<Object> orderedMonoid0 = (OrderedMonoid<Object>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(revertedGraph0, revertedGraph0).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra(orderedMonoid0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      RevertedGraph<Object, Object> revertedGraph0 = new RevertedGraph<Object, Object>(directedMutableGraph0);
      Mapper<Object, Object> mapper0 = (Mapper<Object, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultShortestPathAlgorithmSelector<Object, Object, Object> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<Object, Object, Object>(revertedGraph0, mapper0, revertedGraph0, revertedGraph0);
      OrderedMonoid<Object> orderedMonoid0 = (OrderedMonoid<Object>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(revertedGraph0, revertedGraph0).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultShortestPathAlgorithmSelector0.applyingBidirectionalDijkstra(orderedMonoid0);
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
      UndirectedMutableGraph<OrderedMonoid<RoundingMode>, RoundingMode> undirectedMutableGraph0 = new UndirectedMutableGraph<OrderedMonoid<RoundingMode>, RoundingMode>();
      Mapper<RoundingMode, RoundingMode> mapper0 = (Mapper<RoundingMode, RoundingMode>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      OrderedMonoid<RoundingMode> orderedMonoid0 = (OrderedMonoid<RoundingMode>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<RoundingMode>, RoundingMode, RoundingMode> defaultShortestPathAlgorithmSelector0 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<RoundingMode>, RoundingMode, RoundingMode>(undirectedMutableGraph0, mapper0, orderedMonoid0, orderedMonoid0);
      OrderedMonoid<RoundingMode> orderedMonoid1 = (OrderedMonoid<RoundingMode>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null).when(orderedMonoid1).identity();
      WeightedPath<OrderedMonoid<RoundingMode>, RoundingMode, RoundingMode> weightedPath0 = defaultShortestPathAlgorithmSelector0.applyingDijkstra(orderedMonoid1);
      Mapper<RoundingMode, OrderedMonoid<RoundingMode>> mapper1 = (Mapper<RoundingMode, OrderedMonoid<RoundingMode>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      OrderedMonoid<RoundingMode> orderedMonoid2 = (OrderedMonoid<RoundingMode>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      DefaultShortestPathAlgorithmSelector<OrderedMonoid<RoundingMode>, RoundingMode, OrderedMonoid<RoundingMode>> defaultShortestPathAlgorithmSelector1 = new DefaultShortestPathAlgorithmSelector<OrderedMonoid<RoundingMode>, RoundingMode, OrderedMonoid<RoundingMode>>(weightedPath0, mapper1, orderedMonoid2, orderedMonoid2);
      OrderedMonoid<OrderedMonoid<RoundingMode>> orderedMonoid3 = (OrderedMonoid<OrderedMonoid<RoundingMode>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      HeuristicBuilder<OrderedMonoid<RoundingMode>, RoundingMode, OrderedMonoid<RoundingMode>> heuristicBuilder0 = defaultShortestPathAlgorithmSelector1.applyingAStar(orderedMonoid3);
      assertNotNull(heuristicBuilder0);
  }
}
