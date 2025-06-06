
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
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath;
import org.apache.commons.graph.shortestpath.DefaultPathSourceSelector;
import org.apache.commons.graph.shortestpath.TargetSourceSelector;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.apache.commons.graph.weight.primitive.LongWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultPathSourceSelector_ESTest extends DefaultPathSourceSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>();
      DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations> defaultPathSourceSelector0 = new DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations>(undirectedMutableGraph0, (Mapper<LongWeightBaseOperations, LongWeightBaseOperations>) null);
      Monoid<DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations>> monoid0 = (Monoid<DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn(defaultPathSourceSelector0).when(monoid0).identity();
      MutableSpanningTree<VertexPair<LongWeightBaseOperations>, LongWeightBaseOperations, DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations>> mutableSpanningTree0 = new MutableSpanningTree<VertexPair<LongWeightBaseOperations>, LongWeightBaseOperations, DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations>>(monoid0, (Mapper<LongWeightBaseOperations, DefaultPathSourceSelector<LongWeightBaseOperations, LongWeightBaseOperations, LongWeightBaseOperations>>) null);
      Mapper<LongWeightBaseOperations, UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>> mapper0 = (Mapper<LongWeightBaseOperations, UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultPathSourceSelector<VertexPair<LongWeightBaseOperations>, LongWeightBaseOperations, UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>> defaultPathSourceSelector1 = new DefaultPathSourceSelector<VertexPair<LongWeightBaseOperations>, LongWeightBaseOperations, UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>>(mutableSpanningTree0, mapper0);
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      VertexPair<LongWeightBaseOperations> vertexPair0 = new VertexPair<LongWeightBaseOperations>(longWeightBaseOperations0, longWeightBaseOperations0);
      mutableSpanningTree0.addVertex(vertexPair0);
      Monoid<Object> monoid1 = (Monoid<Object>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid1).identity();
      Mapper<LongWeightBaseOperations, Object> mapper1 = (Mapper<LongWeightBaseOperations, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<LongWeightBaseOperations, LongWeightBaseOperations, Object> mutableSpanningTree1 = new MutableSpanningTree<LongWeightBaseOperations, LongWeightBaseOperations, Object>(monoid1, mapper1);
      OrderedMonoid<UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>> orderedMonoid0 = (OrderedMonoid<UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(orderedMonoid0).compare(any(org.apache.commons.graph.model.UndirectedMutableGraph.class) , any(org.apache.commons.graph.model.UndirectedMutableGraph.class));
      doReturn((Object) null).when(orderedMonoid0).append(any(org.apache.commons.graph.model.UndirectedMutableGraph.class) , any(org.apache.commons.graph.model.UndirectedMutableGraph.class));
      doReturn((Object) null, (Object) null, (Object) null).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<VertexPair<LongWeightBaseOperations>, LongWeightBaseOperations, UndirectedMutableGraph<LongWeightBaseOperations, LongWeightBaseOperations>> allVertexPairsShortestPath0 = defaultPathSourceSelector1.applyingFloydWarshall(orderedMonoid0);
      assertNotNull(allVertexPairsShortestPath0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Mapper<UndirectedMutableGraph<Object, Object>, OrderedMonoid<Object>> mapper0 = (Mapper<UndirectedMutableGraph<Object, Object>, OrderedMonoid<Object>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultPathSourceSelector<Object, UndirectedMutableGraph<Object, Object>, OrderedMonoid<Object>> defaultPathSourceSelector0 = new DefaultPathSourceSelector<Object, UndirectedMutableGraph<Object, Object>, OrderedMonoid<Object>>((Graph<Object, UndirectedMutableGraph<Object, Object>>) null, mapper0);
      // Undeclared exception!
      try { 
        defaultPathSourceSelector0.from((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Shortest path can not be calculated from a null source
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Mapper<FloatWeightBaseOperations, VertexPair<FloatWeightBaseOperations>> mapper0 = (Mapper<FloatWeightBaseOperations, VertexPair<FloatWeightBaseOperations>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultPathSourceSelector<UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>, FloatWeightBaseOperations, VertexPair<FloatWeightBaseOperations>> defaultPathSourceSelector0 = new DefaultPathSourceSelector<UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>, FloatWeightBaseOperations, VertexPair<FloatWeightBaseOperations>>((Graph<UndirectedMutableGraph<FloatWeightBaseOperations, FloatWeightBaseOperations>, FloatWeightBaseOperations>) null, mapper0);
      OrderedMonoid<VertexPair<FloatWeightBaseOperations>> orderedMonoid0 = (OrderedMonoid<VertexPair<FloatWeightBaseOperations>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      // Undeclared exception!
      try { 
        defaultPathSourceSelector0.applyingFloydWarshall(orderedMonoid0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultPathSourceSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DirectedMutableGraph<DefaultPathSourceSelector<IntegerWeightBaseOperations, IntegerWeightBaseOperations, IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>> directedMutableGraph0 = new DirectedMutableGraph<DefaultPathSourceSelector<IntegerWeightBaseOperations, IntegerWeightBaseOperations, IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>>();
      UndirectedMutableGraph<IntegerWeightBaseOperations, IntegerWeightBaseOperations> undirectedMutableGraph0 = new UndirectedMutableGraph<IntegerWeightBaseOperations, IntegerWeightBaseOperations>();
      Mapper<IntegerWeightBaseOperations, IntegerWeightBaseOperations> mapper0 = (Mapper<IntegerWeightBaseOperations, IntegerWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultPathSourceSelector<IntegerWeightBaseOperations, IntegerWeightBaseOperations, IntegerWeightBaseOperations> defaultPathSourceSelector0 = new DefaultPathSourceSelector<IntegerWeightBaseOperations, IntegerWeightBaseOperations, IntegerWeightBaseOperations>(undirectedMutableGraph0, mapper0);
      directedMutableGraph0.addVertex(defaultPathSourceSelector0);
      DefaultPathSourceSelector<DefaultPathSourceSelector<IntegerWeightBaseOperations, IntegerWeightBaseOperations, IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>> defaultPathSourceSelector1 = new DefaultPathSourceSelector<DefaultPathSourceSelector<IntegerWeightBaseOperations, IntegerWeightBaseOperations, IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>>(directedMutableGraph0, (Mapper<OrderedMonoid<IntegerWeightBaseOperations>, OrderedMonoid<IntegerWeightBaseOperations>>) null);
      OrderedMonoid<OrderedMonoid<IntegerWeightBaseOperations>> orderedMonoid0 = (OrderedMonoid<OrderedMonoid<IntegerWeightBaseOperations>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.OrderedMonoid.class) , any(org.apache.commons.graph.weight.OrderedMonoid.class));
      doReturn((Object) null).when(orderedMonoid0).append(any(org.apache.commons.graph.weight.OrderedMonoid.class) , any(org.apache.commons.graph.weight.OrderedMonoid.class));
      doReturn((Object) null, (Object) null, (Object) null).when(orderedMonoid0).identity();
      defaultPathSourceSelector1.applyingFloydWarshall(orderedMonoid0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      OrderedMonoid<LongWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<LongWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      InMemoryPath<OrderedMonoid<LongWeightBaseOperations>, LongWeightBaseOperations> inMemoryPath0 = new InMemoryPath<OrderedMonoid<LongWeightBaseOperations>, LongWeightBaseOperations>(orderedMonoid0, orderedMonoid0);
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      OrderedMonoid<LongWeightBaseOperations> orderedMonoid1 = (OrderedMonoid<LongWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      inMemoryPath0.addConnectionInTail(orderedMonoid1, longWeightBaseOperations0, orderedMonoid1);
      OrderedMonoid<LongWeightBaseOperations> orderedMonoid2 = (OrderedMonoid<LongWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      Mapper<LongWeightBaseOperations, OrderedMonoid<LongWeightBaseOperations>> mapper0 = (Mapper<LongWeightBaseOperations, OrderedMonoid<LongWeightBaseOperations>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(any(org.apache.commons.graph.weight.primitive.LongWeightBaseOperations.class));
      DefaultPathSourceSelector<OrderedMonoid<LongWeightBaseOperations>, LongWeightBaseOperations, OrderedMonoid<LongWeightBaseOperations>> defaultPathSourceSelector0 = new DefaultPathSourceSelector<OrderedMonoid<LongWeightBaseOperations>, LongWeightBaseOperations, OrderedMonoid<LongWeightBaseOperations>>(inMemoryPath0, mapper0);
      OrderedMonoid<LongWeightBaseOperations> orderedMonoid3 = (OrderedMonoid<LongWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      inMemoryPath0.addConnectionInTail(orderedMonoid3, longWeightBaseOperations0, orderedMonoid3);
      OrderedMonoid<OrderedMonoid<LongWeightBaseOperations>> orderedMonoid4 = (OrderedMonoid<OrderedMonoid<LongWeightBaseOperations>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      // Undeclared exception!
      try { 
        defaultPathSourceSelector0.applyingFloydWarshall(orderedMonoid4);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to add a shortest distance with a null distance
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultPathSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultPathSourceSelector0 = new DefaultPathSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0);
      TargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> targetSourceSelector0 = defaultPathSourceSelector0.from(floatWeightBaseOperations0);
      assertNotNull(targetSourceSelector0);
  }
}
