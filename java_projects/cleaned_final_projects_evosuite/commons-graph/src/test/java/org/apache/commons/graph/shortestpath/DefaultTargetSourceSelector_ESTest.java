
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
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath;
import org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector;
import org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultTargetSourceSelector_ESTest extends DefaultTargetSourceSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      inMemoryPath0.addConnectionInTail(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0).when(mapper0).map(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0, floatWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((-4666), 1734, 2).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0).when(orderedMonoid0).append(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn(floatWeightBaseOperations0).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> allVertexPairsShortestPath0 = defaultTargetSourceSelector0.applyingBelmannFord(orderedMonoid0);
      assertNotNull(allVertexPairsShortestPath0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      FloatWeightBaseOperations floatWeightBaseOperations1 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInTail(floatWeightBaseOperations0, floatWeightBaseOperations1, floatWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null, (Object) null).when(mapper0).map(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0, floatWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(0, 0, 0).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn((Object) null, (Object) null, (Object) null).when(orderedMonoid0).append(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn((Object) null).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> allVertexPairsShortestPath0 = defaultTargetSourceSelector0.applyingBelmannFord(orderedMonoid0);
      assertNotNull(allVertexPairsShortestPath0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      FloatWeightBaseOperations floatWeightBaseOperations1 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInTail(floatWeightBaseOperations1, floatWeightBaseOperations0, floatWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null, (Object) null, (Object) null).when(mapper0).map(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0, floatWeightBaseOperations1);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(0, 0).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn((Object) null, (Object) null, (Object) null, (Object) null).when(orderedMonoid0).append(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn((Object) null, (Object) null).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> allVertexPairsShortestPath0 = defaultTargetSourceSelector0.applyingBelmannFord(orderedMonoid0);
      assertNotNull(allVertexPairsShortestPath0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Double double0 = new Double(1739.0191174009544);
      InMemoryPath<Double, Double> inMemoryPath0 = new InMemoryPath<Double, Double>(double0, double0);
      DefaultTargetSourceSelector<Double, Double, OrderedMonoid<Double>> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<Double, Double, OrderedMonoid<Double>>(inMemoryPath0, (Mapper<Double, OrderedMonoid<Double>>) null, double0);
      // Undeclared exception!
      try { 
        defaultTargetSourceSelector0.to((Double) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Shortest path can not be calculated to a null target
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Float float0 = new Float(0.0);
      DefaultTargetSourceSelector<Float, OrderedMonoid<Float>, Float> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<Float, OrderedMonoid<Float>, Float>((Graph<Float, OrderedMonoid<Float>>) null, (Mapper<OrderedMonoid<Float>, Float>) null, float0);
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      // Undeclared exception!
      try { 
        defaultTargetSourceSelector0.applyingBelmannFord((OrderedMonoid<Float>) floatWeightBaseOperations0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) null, floatWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultTargetSourceSelector0.applyingBelmannFord((OrderedMonoid<FloatWeightBaseOperations>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Belmann-Ford algorithm can not be applied using null weight operations
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      inMemoryPath0.addConnectionInTail(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations0);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(floatWeightBaseOperations0, (Object) null, (Object) null).when(mapper0).map(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0, floatWeightBaseOperations0);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((-2), 0, 0).when(orderedMonoid0).compare(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn(floatWeightBaseOperations0, (Object) null, (Object) null).when(orderedMonoid0).append(any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class) , any(org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations.class));
      doReturn(floatWeightBaseOperations0).when(orderedMonoid0).identity();
      defaultTargetSourceSelector0.applyingBelmannFord(orderedMonoid0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations> inMemoryPath0 = new InMemoryPath<FloatWeightBaseOperations, FloatWeightBaseOperations>(floatWeightBaseOperations0, floatWeightBaseOperations0);
      FloatWeightBaseOperations floatWeightBaseOperations1 = new FloatWeightBaseOperations();
      inMemoryPath0.addConnectionInTail(floatWeightBaseOperations0, floatWeightBaseOperations0, floatWeightBaseOperations1);
      Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations> mapper0 = (Mapper<FloatWeightBaseOperations, FloatWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations>(inMemoryPath0, mapper0, floatWeightBaseOperations1);
      OrderedMonoid<FloatWeightBaseOperations> orderedMonoid0 = (OrderedMonoid<FloatWeightBaseOperations>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null, (Object) null).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<FloatWeightBaseOperations, FloatWeightBaseOperations, FloatWeightBaseOperations> allVertexPairsShortestPath0 = defaultTargetSourceSelector0.applyingBelmannFord(orderedMonoid0);
      assertNotNull(allVertexPairsShortestPath0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Mapper<DoubleWeightBaseOperations, DoubleWeightBaseOperations> mapper0 = (Mapper<DoubleWeightBaseOperations, DoubleWeightBaseOperations>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultTargetSourceSelector<DoubleWeightBaseOperations, DoubleWeightBaseOperations, DoubleWeightBaseOperations> defaultTargetSourceSelector0 = new DefaultTargetSourceSelector<DoubleWeightBaseOperations, DoubleWeightBaseOperations, DoubleWeightBaseOperations>((Graph<DoubleWeightBaseOperations, DoubleWeightBaseOperations>) null, mapper0, doubleWeightBaseOperations0);
      ShortestPathAlgorithmSelector<DoubleWeightBaseOperations, DoubleWeightBaseOperations, DoubleWeightBaseOperations> shortestPathAlgorithmSelector0 = defaultTargetSourceSelector0.to(doubleWeightBaseOperations0);
      assertNotNull(shortestPathAlgorithmSelector0);
  }
}
