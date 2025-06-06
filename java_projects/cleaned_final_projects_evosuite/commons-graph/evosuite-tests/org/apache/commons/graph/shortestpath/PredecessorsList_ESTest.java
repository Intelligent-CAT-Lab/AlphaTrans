
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
import org.apache.commons.graph.WeightedPath;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.shortestpath.PredecessorsList;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PredecessorsList_ESTest extends PredecessorsList_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      Integer integer1 = new Integer(1);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      predecessorsList0.addPredecessor(integer1, integer0);
      WeightedPath<Integer, Integer, Integer> weightedPath0 = predecessorsList0.buildPath1(integer1, integer1, integer0, predecessorsList0);
      assertNotNull(weightedPath0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Integer integer1 = new Integer(1);
      predecessorsList0.addPredecessor(integer1, integer0);
      Mapper<Integer, Integer> mapper1 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      PredecessorsList<Integer, Integer, Integer> predecessorsList1 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper1);
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath1(integer0, integer1, integer0, predecessorsList1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.PredecessorsList", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(2);
      Integer integer1 = new Integer(2);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer1, integer1, integer1, integer1, integer0).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      predecessorsList0.addPredecessor(integer0, integer1);
      Integer integer2 = new Integer(1);
      // Undeclared exception!
      predecessorsList0.buildPath1(integer1, integer0, integer2, predecessorsList0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(2);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Mapper<Integer, Integer> mapper1 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      PredecessorsList<Integer, Integer, Integer> predecessorsList1 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper1);
      Integer integer1 = new Integer(1);
      // Undeclared exception!
      try { 
        predecessorsList1.buildPath1(integer0, integer0, integer1, predecessorsList0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.PredecessorsList", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Integer integer1 = new Integer(1);
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath1(integer0, integer1, integer0, (PredecessorsList<Integer, Integer, Integer>) null);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.PredecessorsList", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0, (Object) null, (Object) null, (Object) null, (Object) null).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Integer integer1 = new Integer((-2));
      predecessorsList0.addPredecessor(integer0, integer0);
      Integer integer2 = new Integer(2);
      // Undeclared exception!
      predecessorsList0.buildPath1(integer2, integer1, integer1, predecessorsList0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0, (Object) null, (Object) null, (Object) null, (Object) null).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Integer integer1 = new Integer((-2));
      predecessorsList0.addPredecessor(integer1, integer0);
      Integer integer2 = Integer.valueOf((-3));
      // Undeclared exception!
      predecessorsList0.buildPath0(integer2, integer1);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Integer integer1 = new Integer(1);
      Integer integer2 = new Integer(1);
      predecessorsList0.addPredecessor(integer2, integer0);
      Integer integer3 = Integer.valueOf((-3));
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath0(integer3, integer1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.PredecessorsList", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer((-2));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0).when(mapper0).map(anyInt());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, mapper0);
      Integer integer1 = new Integer(1);
      predecessorsList0.addPredecessor(integer1, integer0);
      WeightedPath<Integer, Integer, Integer> weightedPath0 = predecessorsList0.buildPath0(integer0, integer1);
      assertNotNull(weightedPath0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      predecessorsList0.addPredecessor(integer0, integer0);
      Integer integer1 = integerWeightBaseOperations0.append(integer0, integer0);
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath1(integer0, integer0, integer1, predecessorsList0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Integer integer0 = new Integer(2427);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper0);
      Mapper<Integer, Integer> mapper1 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryWeightedPath0, integerWeightBaseOperations0, mapper1);
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath1((Integer) null, (Integer) null, integer0, predecessorsList0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Path source cannot be null
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Integer integer0 = Integer.valueOf((-1));
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(inMemoryPath0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      predecessorsList0.addPredecessor(integer0, integer0);
      Integer integer1 = integerWeightBaseOperations0.append(integer0, integer0);
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath0(integer1, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>((Graph<Integer, Integer>) null, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath0((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Path source cannot be null
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(undirectedMutableGraph0, (Monoid<Integer>) null, (Mapper<Integer, Integer>) null);
      boolean boolean0 = predecessorsList0.isEmpty();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = integerWeightBaseOperations0.identity();
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(undirectedMutableGraph0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      assertTrue(predecessorsList0.isEmpty());
      
      predecessorsList0.addPredecessor(integer0, integer0);
      boolean boolean0 = predecessorsList0.isEmpty();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = integerWeightBaseOperations0.identity();
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(undirectedMutableGraph0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      predecessorsList0.addPredecessor(integer0, integer0);
      Integer integer1 = new Integer((-1));
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath1(integer1, integer0, integer0, predecessorsList0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = integerWeightBaseOperations0.identity();
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(undirectedMutableGraph0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      Integer integer1 = new Integer((-1));
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath1(integer1, integer0, integer0, predecessorsList0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.PredecessorsList", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = integerWeightBaseOperations0.identity();
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      PredecessorsList<Integer, Integer, Integer> predecessorsList0 = new PredecessorsList<Integer, Integer, Integer>(undirectedMutableGraph0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      predecessorsList0.addPredecessor(integer0, integer0);
      Integer integer1 = new Integer((-1));
      // Undeclared exception!
      try { 
        predecessorsList0.buildPath0(integer1, integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }
}
