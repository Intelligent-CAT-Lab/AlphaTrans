
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
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MutableSpanningTree_ESTest extends MutableSpanningTree_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(0);
      Integer integer1 = new Integer(0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0).when(mapper0).map(anyInt());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      mutableSpanningTree0.addVertex(integer0);
      mutableSpanningTree0.decorateAddEdge(integer0, integer0, integer1);
      assertEquals(1, mutableSpanningTree0.getOrder());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(0);
      Integer integer1 = new Integer(0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0).when(mapper0).map(anyInt());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      mutableSpanningTree0.addVertex(integer1);
      mutableSpanningTree0.decorateAddEdge(integer1, integer0, integer0);
      assertTrue(integer0.equals((Object)integer1));
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      Integer integer1 = integerWeightBaseOperations0.append(integer0, integer0);
      // Undeclared exception!
      try { 
        mutableSpanningTree0.decorateAddEdge(integer1, integer0, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn(integer0).when(mapper0).map(anyInt());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      mutableSpanningTree0.decorateRemoveEdge(integer0);
      assertEquals(0, mutableSpanningTree0.getSize());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(anyInt());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      Integer integer0 = new Integer(0);
      mutableSpanningTree0.addVertex(integer0);
      mutableSpanningTree0.decorateAddEdge(integer0, integer0, integer0);
      Integer integer1 = mutableSpanningTree0.getWeight();
      assertNull(integer1);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = null;
      try {
        mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>((Monoid<Integer>) null, (Mapper<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.MutableSpanningTree", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(anyInt());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      Integer integer0 = new Integer(0);
      // Undeclared exception!
      try { 
        mutableSpanningTree0.decorateRemoveEdge(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations", e);
      }
  }
}
