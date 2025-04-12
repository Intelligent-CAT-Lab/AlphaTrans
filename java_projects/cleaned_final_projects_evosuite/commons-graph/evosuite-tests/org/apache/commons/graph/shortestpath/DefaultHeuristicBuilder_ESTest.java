
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
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder;
import org.apache.commons.graph.shortestpath.Heuristic;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultHeuristicBuilder_ESTest extends DefaultHeuristicBuilder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      UndirectedMutableGraph<Object, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Object, Integer>();
      Mapper<Integer, Object> mapper0 = (Mapper<Integer, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(mapper0).toString();
      OrderedMonoid<Object> orderedMonoid0 = (OrderedMonoid<Object>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      DefaultHeuristicBuilder<Object, Integer, Object> defaultHeuristicBuilder0 = new DefaultHeuristicBuilder<Object, Integer, Object>(undirectedMutableGraph0, mapper0, mapper0, undirectedMutableGraph0, orderedMonoid0);
      Heuristic<Object, Object> heuristic0 = (Heuristic<Object, Object>) mock(Heuristic.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(heuristic0).applyHeuristic(any() , any());
      // Undeclared exception!
      try { 
        defaultHeuristicBuilder0.withHeuristic(heuristic0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      UndirectedMutableGraph<Object, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Object, Integer>();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      DefaultHeuristicBuilder<Object, Integer, Integer> defaultHeuristicBuilder0 = new DefaultHeuristicBuilder<Object, Integer, Integer>(undirectedMutableGraph0, mapper0, undirectedMutableGraph0, mapper0, integerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultHeuristicBuilder0.withHeuristic((Heuristic<Object, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // A* algorithm can not be applied using a null heuristic
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Object object0 = new Object();
      InMemoryPath<Object, Heuristic<Integer, Object>> inMemoryPath0 = new InMemoryPath<Object, Heuristic<Integer, Object>>(object0, object0);
      Mapper<Heuristic<Integer, Object>, Heuristic<Object, Integer>> mapper0 = (Mapper<Heuristic<Integer, Object>, Heuristic<Object, Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      Object object1 = new Object();
      OrderedMonoid<Heuristic<Object, Integer>> orderedMonoid0 = (OrderedMonoid<Heuristic<Object, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      DefaultHeuristicBuilder<Object, Heuristic<Integer, Object>, Heuristic<Object, Integer>> defaultHeuristicBuilder0 = new DefaultHeuristicBuilder<Object, Heuristic<Integer, Object>, Heuristic<Object, Integer>>(inMemoryPath0, mapper0, object1, inMemoryPath0, orderedMonoid0);
      Heuristic<Object, Heuristic<Object, Integer>> heuristic0 = (Heuristic<Object, Heuristic<Object, Integer>>) mock(Heuristic.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(heuristic0).applyHeuristic(any() , any());
      // Undeclared exception!
      try { 
        defaultHeuristicBuilder0.withHeuristic(heuristic0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; java.lang.Object@67c32512 not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      Mapper<Object, Object> mapper0 = (Mapper<Object, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      Object object0 = new Object();
      directedMutableGraph0.addVertex(object0);
      OrderedMonoid<Object> orderedMonoid0 = (OrderedMonoid<Object>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(object0).when(orderedMonoid0).identity();
      directedMutableGraph0.addEdge(object0, object0, object0);
      DefaultHeuristicBuilder<Object, Object, Object> defaultHeuristicBuilder0 = new DefaultHeuristicBuilder<Object, Object, Object>(directedMutableGraph0, mapper0, object0, directedMutableGraph0, orderedMonoid0);
      Heuristic<Object, Object> heuristic0 = (Heuristic<Object, Object>) mock(Heuristic.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(heuristic0).applyHeuristic(any() , any());
      // Undeclared exception!
      try { 
        defaultHeuristicBuilder0.withHeuristic(heuristic0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Integer integer0 = new Integer(3);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Heuristic<Integer, Integer>, Integer> mapper0 = (Mapper<Heuristic<Integer, Integer>, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Heuristic<Integer, Integer>, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Heuristic<Integer, Integer>, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper0);
      Mapper<Heuristic<Integer, Integer>, Integer> mapper1 = (Mapper<Heuristic<Integer, Integer>, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      Integer integer1 = new Integer(0);
      DefaultHeuristicBuilder<Integer, Heuristic<Integer, Integer>, Integer> defaultHeuristicBuilder0 = new DefaultHeuristicBuilder<Integer, Heuristic<Integer, Integer>, Integer>(inMemoryWeightedPath0, mapper1, integer0, integer1, integerWeightBaseOperations0);
      Heuristic<Integer, Integer> heuristic0 = (Heuristic<Integer, Integer>) mock(Heuristic.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(heuristic0).applyHeuristic(anyInt() , anyInt());
      // Undeclared exception!
      try { 
        defaultHeuristicBuilder0.withHeuristic(heuristic0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      DirectedMutableGraph<Object, Object> directedMutableGraph0 = new DirectedMutableGraph<Object, Object>();
      Mapper<Object, Object> mapper0 = (Mapper<Object, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      OrderedMonoid<Object> orderedMonoid0 = (OrderedMonoid<Object>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null).when(orderedMonoid0).identity();
      DefaultHeuristicBuilder<Object, Object, Object> defaultHeuristicBuilder0 = new DefaultHeuristicBuilder<Object, Object, Object>(directedMutableGraph0, mapper0, directedMutableGraph0, directedMutableGraph0, orderedMonoid0);
      Heuristic<Object, Object> heuristic0 = (Heuristic<Object, Object>) mock(Heuristic.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(heuristic0).applyHeuristic(any() , any());
      WeightedPath<Object, Object, Object> weightedPath0 = defaultHeuristicBuilder0.withHeuristic(heuristic0);
      assertNotNull(weightedPath0);
  }
}
