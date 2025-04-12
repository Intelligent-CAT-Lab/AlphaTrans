
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
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.SpanningTree;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector;
import org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations;
import org.apache.commons.graph.weight.primitive.LongWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultSpanningTreeSourceSelector_ESTest extends DefaultSpanningTreeSourceSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInHead(longWeightBaseOperations0, floatWeightBaseOperations0, longWeightBaseOperations0);
      SpanningTreeAlgorithmSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> spanningTreeAlgorithmSelector0 = defaultSpanningTreeSourceSelector0.fromSource(longWeightBaseOperations0);
      assertNotNull(spanningTreeAlgorithmSelector0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DefaultSpanningTreeSourceSelector<Long, Long, Long> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<Long, Long, Long>((Graph<Long, Long>) null, (Mapper<Long, Long>) null);
      Long long0 = new Long(1140L);
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.fromSource(long0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<BigInteger, OrderedMonoid<BigInteger>> directedMutableGraph0 = new DirectedMutableGraph<BigInteger, OrderedMonoid<BigInteger>>();
      DefaultSpanningTreeSourceSelector<BigInteger, RevertedGraph<BigInteger, BigInteger>, OrderedMonoid<BigInteger>> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<BigInteger, RevertedGraph<BigInteger, BigInteger>, OrderedMonoid<BigInteger>>(directedMutableGraph0, (Mapper<OrderedMonoid<BigInteger>, RevertedGraph<BigInteger, BigInteger>>) null);
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.fromSource((BigInteger) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Spanning tree cannot be calculated without expressing the source vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DefaultSpanningTreeSourceSelector<Long, Long, Long> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<Long, Long, Long>((Graph<Long, Long>) null, (Mapper<Long, Long>) null);
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.fromArbitrarySource();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      LongWeightBaseOperations longWeightBaseOperations1 = new LongWeightBaseOperations();
      inMemoryPath0.addConnectionInHead(longWeightBaseOperations0, floatWeightBaseOperations0, longWeightBaseOperations1);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(floatWeightBaseOperations0).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(orderedMonoid0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      inMemoryPath0.addConnectionInHead(longWeightBaseOperations0, floatWeightBaseOperations0, longWeightBaseOperations0);
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) null);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(orderedMonoid0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Function to calculate edges weight can not be null.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      undirectedMutableGraph0.addVertex(floatWeightBaseOperations0);
      DefaultSpanningTreeSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(undirectedMutableGraph0, (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) null);
      SpanningTreeAlgorithmSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> spanningTreeAlgorithmSelector0 = defaultSpanningTreeSourceSelector0.fromArbitrarySource();
      assertNotNull(spanningTreeAlgorithmSelector0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DirectedMutableGraph<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>> directedMutableGraph0 = new DirectedMutableGraph<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>>();
      RevertedGraph<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>> revertedGraph0 = new RevertedGraph<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>>(directedMutableGraph0);
      Mapper<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>> mapper0 = (Mapper<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultSpanningTreeSourceSelector<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>, Comparable<LongWeightBaseOperations>>(revertedGraph0, mapper0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.fromArbitrarySource();
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Spanning tree cannot be calculated on an empty graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      LongWeightBaseOperations longWeightBaseOperations1 = new LongWeightBaseOperations();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInHead(longWeightBaseOperations1, floatWeightBaseOperations0, longWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).append(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn((Object) null, (Object) null).when(orderedMonoid0).identity();
      SpanningTree<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> spanningTree0 = defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(orderedMonoid0);
      assertNotNull(spanningTree0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      LongWeightBaseOperations longWeightBaseOperations1 = new LongWeightBaseOperations();
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInHead(longWeightBaseOperations1, floatWeightBaseOperations0, longWeightBaseOperations1);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0).when(orderedMonoid0).identity();
      SpanningTree<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> spanningTree0 = defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(orderedMonoid0);
      assertNotNull(spanningTree0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInHead(longWeightBaseOperations0, floatWeightBaseOperations0, longWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(floatWeightBaseOperations0, (Object) null, (Object) null).when(orderedMonoid0).identity();
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.applyingReverseDeleteAlgorithm(orderedMonoid0);
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
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<LongWeightBaseOperations, FloatWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultSpanningTreeSourceSelector0 = new DefaultSpanningTreeSourceSelector<LongWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      // Undeclared exception!
      try { 
        defaultSpanningTreeSourceSelector0.fromSource(longWeightBaseOperations0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex org.apache.commons.graph.weight.primitive.LongWeightBaseOperations@1 does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
