
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
import org.apache.commons.graph.VertexPair;
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AllVertexPairsShortestPath_ESTest extends AllVertexPairsShortestPath_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer(3102);
      Integer integer1 = new Integer(3102);
      OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>> orderedMonoid0 = (OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(orderedMonoid0);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.findShortestPath(integer1, integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Integer integer0 = new Integer(0);
      OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>> orderedMonoid0 = (OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(orderedMonoid0);
      Integer integer1 = new Integer(2946);
      Monoid<InMemoryWeightedPath<Integer, Integer, Integer>> monoid0 = (Monoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Integer, InMemoryWeightedPath<Integer, Integer, Integer>> mapper0 = (Mapper<Integer, InMemoryWeightedPath<Integer, Integer, Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(integer1, integer1, monoid0, mapper0);
      allVertexPairsShortestPath0.addShortestPath(integer0, integer1, inMemoryWeightedPath0);
      assertFalse(integer1.equals((Object)integer0));
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = (InMemoryWeightedPath<Integer, Integer, Integer>) mock(InMemoryWeightedPath.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(inMemoryWeightedPath0).toString();
      OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>> orderedMonoid0 = (OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(inMemoryWeightedPath0).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(orderedMonoid0);
      Integer integer0 = new Integer(0);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath1 = allVertexPairsShortestPath0.getShortestDistance(integer0, integer0);
      assertEquals(0, inMemoryWeightedPath1.getSize());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      AllVertexPairsShortestPath<Object, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Object, Integer, Integer>((OrderedMonoid<Integer>) null);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.hasShortestDistance((Object) null, (Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to add a shortest path from a null source
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      AllVertexPairsShortestPath<Integer, Comparable<Object>, VertexPair<Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Comparable<Object>, VertexPair<Integer>>((OrderedMonoid<VertexPair<Integer>>) null);
      Integer integer0 = Integer.valueOf(693);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.getShortestDistance(integer0, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      AllVertexPairsShortestPath<Object, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Object, Integer, Integer>(integerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.getShortestDistance((Object) null, (Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to add a shortest path from a null source
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      AllVertexPairsShortestPath<VertexPair<Integer>, Object, Object> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<VertexPair<Integer>, Object, Object>((OrderedMonoid<Object>) null);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.findShortestPath((VertexPair<Integer>) null, (VertexPair<Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to add a shortest path from a null source
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer(0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper0);
      AllVertexPairsShortestPath<Integer, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, Integer>(integerWeightBaseOperations0);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.addShortestPath((Integer) null, integer0, inMemoryWeightedPath0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to add a shortest path from a null source
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>> orderedMonoid0 = (OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      AllVertexPairsShortestPath<InMemoryWeightedPath<Integer, Integer, Integer>, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<InMemoryWeightedPath<Integer, Integer, Integer>, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(orderedMonoid0);
      // Undeclared exception!
      try { 
        allVertexPairsShortestPath0.addShortestDistance((InMemoryWeightedPath<Integer, Integer, Integer>) null, (InMemoryWeightedPath<Integer, Integer, Integer>) null, (InMemoryWeightedPath<Integer, Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to add a shortest path from a null source
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      AllVertexPairsShortestPath<Object, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Object, Integer, Integer>(integerWeightBaseOperations0);
      boolean boolean0 = allVertexPairsShortestPath0.hasShortestDistance(integerWeightBaseOperations0, integerWeightBaseOperations0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Integer integer0 = new Integer(0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      AllVertexPairsShortestPath<Integer, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, Integer>(integerWeightBaseOperations0);
      Integer integer1 = new Integer(2946);
      boolean boolean0 = allVertexPairsShortestPath0.hasShortestDistance(integer0, integer1);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>> orderedMonoid0 = (OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(orderedMonoid0);
      Integer integer0 = new Integer(0);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = allVertexPairsShortestPath0.getShortestDistance(integer0, integer0);
      assertNull(inMemoryWeightedPath0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Integer integer0 = new Integer(0);
      OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>> orderedMonoid0 = (OrderedMonoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(orderedMonoid0);
      Integer integer1 = new Integer(2946);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = allVertexPairsShortestPath0.getShortestDistance(integer1, integer0);
      assertNull(inMemoryWeightedPath0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      AllVertexPairsShortestPath<Object, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Object, Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer(1304);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Object, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Object, Integer, Integer>(integer0, integerWeightBaseOperations0, integerWeightBaseOperations0, mapper0);
      allVertexPairsShortestPath0.addShortestPath(integerWeightBaseOperations0, integerWeightBaseOperations0, inMemoryWeightedPath0);
      WeightedPath<Object, Integer, Integer> weightedPath0 = allVertexPairsShortestPath0.findShortestPath(integerWeightBaseOperations0, integerWeightBaseOperations0);
      assertEquals(0, weightedPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Object object0 = new Object();
      AllVertexPairsShortestPath<Object, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<Object, Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer((-1));
      allVertexPairsShortestPath0.addShortestDistance(integerWeightBaseOperations0, object0, integer0);
      boolean boolean0 = allVertexPairsShortestPath0.hasShortestDistance(integerWeightBaseOperations0, object0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      AllVertexPairsShortestPath<InMemoryWeightedPath<Integer, Integer, Integer>, Integer, Integer> allVertexPairsShortestPath0 = new AllVertexPairsShortestPath<InMemoryWeightedPath<Integer, Integer, Integer>, Integer, Integer>(integerWeightBaseOperations0);
      String string0 = allVertexPairsShortestPath0.toString();
      assertNotNull(string0);
  }
}
