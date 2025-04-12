
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


package org.apache.commons.graph.spanning;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.math.BigInteger;
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector;
import org.apache.commons.graph.spanning.ReverseDeleteGraph;
import org.apache.commons.graph.spanning.SuperVertex;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations;
import org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultSpanningTreeAlgorithmSelector_ESTest extends DefaultSpanningTreeAlgorithmSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<BigInteger, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, BigInteger>();
      byte[] byteArray0 = new byte[3];
      BigInteger bigInteger0 = new BigInteger(byteArray0);
      BigInteger bigInteger1 = new BigInteger(byteArray0);
      directedMutableGraph0.addVertex(bigInteger0);
      directedMutableGraph0.addEdge(bigInteger1, bigInteger1, bigInteger1);
      Mapper<BigInteger, FloatWeightBaseOperations> mapper0 = (Mapper<BigInteger, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(directedMutableGraph0, mapper0, bigInteger0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(orderedMonoid0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.FibonacciHeap", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      InMemoryPath<OrderedMonoid<BigInteger>, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<OrderedMonoid<BigInteger>, FloatWeightBaseOperations>(bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations0);
      DefaultSpanningTreeAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, FloatWeightBaseOperations>(inMemoryPath0, (Mapper<FloatWeightBaseOperations, BigInteger>) null, bigIntegerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<BigInteger, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, BigInteger>();
      BigInteger bigInteger0 = BigInteger.ZERO;
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(directedMutableGraph0, (Mapper<BigInteger, FloatWeightBaseOperations>) null, bigInteger0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm((OrderedMonoid<FloatWeightBaseOperations>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // The Prim algorithm cannot be calculated with null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      Monoid<SuperVertex<BigInteger, FloatWeightBaseOperations, BigInteger>> monoid0 = (Monoid<SuperVertex<BigInteger, FloatWeightBaseOperations, BigInteger>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations1 = new BigIntegerWeightBaseOperations();
      Mapper<FloatWeightBaseOperations, SuperVertex<BigInteger, FloatWeightBaseOperations, BigInteger>> mapper0 = (Mapper<FloatWeightBaseOperations, SuperVertex<BigInteger, FloatWeightBaseOperations, BigInteger>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<OrderedMonoid<BigInteger>, FloatWeightBaseOperations, SuperVertex<BigInteger, FloatWeightBaseOperations, BigInteger>> inMemoryWeightedPath0 = new InMemoryWeightedPath<OrderedMonoid<BigInteger>, FloatWeightBaseOperations, SuperVertex<BigInteger, FloatWeightBaseOperations, BigInteger>>(bigIntegerWeightBaseOperations0, bigIntegerWeightBaseOperations1, monoid0, mapper0);
      Mapper<FloatWeightBaseOperations, BigInteger> mapper1 = (Mapper<FloatWeightBaseOperations, BigInteger>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultSpanningTreeAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, FloatWeightBaseOperations>(inMemoryWeightedPath0, mapper1, bigIntegerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations@1 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BigInteger bigInteger0 = BigInteger.ONE;
      LinkedList<BigInteger> linkedList0 = new LinkedList<BigInteger>();
      InMemoryPath<BigInteger, BigInteger> inMemoryPath0 = new InMemoryPath<BigInteger, BigInteger>(bigInteger0, bigInteger0);
      ReverseDeleteGraph<BigInteger, BigInteger> reverseDeleteGraph0 = new ReverseDeleteGraph<BigInteger, BigInteger>(inMemoryPath0, linkedList0, linkedList0);
      inMemoryPath0.addConnectionInTail(bigInteger0, bigInteger0, bigInteger0);
      Mapper<BigInteger, FloatWeightBaseOperations> mapper0 = (Mapper<BigInteger, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(reverseDeleteGraph0, mapper0, bigInteger0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm(orderedMonoid0);
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
      DirectedMutableGraph<BigInteger, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, BigInteger>();
      BigInteger bigInteger0 = BigInteger.ZERO;
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(directedMutableGraph0, (Mapper<BigInteger, FloatWeightBaseOperations>) null, bigInteger0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm((OrderedMonoid<FloatWeightBaseOperations>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // The Kruskal algorithm cannot be calculated with null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Mapper<Object, Object> mapper0 = (Mapper<Object, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultSpanningTreeAlgorithmSelector<Object, Object, Object> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<Object, Object, Object>((Graph<Object, Object>) null, mapper0, (Object) null);
      OrderedMonoid<Object> orderedMonoid0 = (OrderedMonoid<Object>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(orderedMonoid0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(undirectedMutableGraph0, (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) null, floatWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm((OrderedMonoid<FloatWeightBaseOperations>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // The Boruvka algorithm cannot be calculated with null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      undirectedMutableGraph0.addVertex(floatWeightBaseOperations0);
      DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(undirectedMutableGraph0, mapper0, floatWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      SpanningTree<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm(orderedMonoid0);
      assertNotNull(spanningTree0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      DirectedMutableGraph<OrderedMonoid<BigInteger>, FloatWeightBaseOperations> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<BigInteger>, FloatWeightBaseOperations>();
      RevertedGraph<OrderedMonoid<BigInteger>, FloatWeightBaseOperations> revertedGraph0 = new RevertedGraph<OrderedMonoid<BigInteger>, FloatWeightBaseOperations>(directedMutableGraph0);
      DefaultSpanningTreeAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<OrderedMonoid<BigInteger>, BigInteger, FloatWeightBaseOperations>(revertedGraph0, (Mapper<FloatWeightBaseOperations, BigInteger>) null, bigIntegerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingPrimAlgorithm((OrderedMonoid<BigInteger>) bigIntegerWeightBaseOperations0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedMutableGraph<BigInteger, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, BigInteger>();
      BigInteger bigInteger0 = BigInteger.ZERO;
      directedMutableGraph0.addVertex(bigInteger0);
      directedMutableGraph0.addEdge(bigInteger0, bigInteger0, bigInteger0);
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(directedMutableGraph0, (Mapper<BigInteger, FloatWeightBaseOperations>) null, bigInteger0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      SpanningTree<BigInteger, BigInteger, FloatWeightBaseOperations> spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm(orderedMonoid0);
      assertNotNull(spanningTree0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<BigInteger, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, BigInteger>();
      BigInteger bigInteger0 = BigInteger.ONE;
      List<BigInteger> list0 = List.of(bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0);
      LinkedList<BigInteger> linkedList0 = new LinkedList<BigInteger>();
      ReverseDeleteGraph<BigInteger, BigInteger> reverseDeleteGraph0 = new ReverseDeleteGraph<BigInteger, BigInteger>(directedMutableGraph0, list0, linkedList0);
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Mapper<BigInteger, FloatWeightBaseOperations> mapper0 = (Mapper<BigInteger, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0).when(mapper0).map(any(java.math.BigInteger.class));
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(reverseDeleteGraph0, mapper0, bigInteger0);
      directedMutableGraph0.addVertex(bigInteger0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(0, 4, 0, 4, 1).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn(floatWeightBaseOperations0).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm(orderedMonoid0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DirectedMutableGraph<BigInteger, BigInteger> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, BigInteger>();
      BigInteger bigInteger0 = BigInteger.ONE;
      List<BigInteger> list0 = List.of(bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0, bigInteger0);
      LinkedList<BigInteger> linkedList0 = new LinkedList<BigInteger>();
      ReverseDeleteGraph<BigInteger, BigInteger> reverseDeleteGraph0 = new ReverseDeleteGraph<BigInteger, BigInteger>(directedMutableGraph0, list0, linkedList0);
      Mapper<BigInteger, FloatWeightBaseOperations> mapper0 = (Mapper<BigInteger, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null, (Object) null, (Object) null, (Object) null).when(mapper0).map(any(java.math.BigInteger.class));
      DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<BigInteger, FloatWeightBaseOperations, BigInteger>(reverseDeleteGraph0, mapper0, bigInteger0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(0, 0, 0, 0, 0).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn((Object) null).when(orderedMonoid0).identity();
      SpanningTree<BigInteger, BigInteger, FloatWeightBaseOperations> spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingKruskalAlgorithm(orderedMonoid0);
      assertNotNull(spanningTree0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      FloatWeightBaseOperations floatWeightBaseOperations1 = new FloatWeightBaseOperations();
      undirectedMutableGraph0.addVertex(floatWeightBaseOperations1);
      undirectedMutableGraph0.addVertex(floatWeightBaseOperations0);
      DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(undirectedMutableGraph0, mapper0, floatWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(orderedMonoid0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // unconnected graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      undirectedMutableGraph0.addVertex(floatWeightBaseOperations0);
      DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeAlgorithmSelector0 = new DefaultSpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(undirectedMutableGraph0, mapper0, floatWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      SpanningTree<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> spanningTree0 = defaultSpanningTreeAlgorithmSelector0.applyingBoruvkaAlgorithm(orderedMonoid0);
      assertNotNull(spanningTree0);
  }
}
