
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


package org.apache.commons.graph.builder;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.builder.DefaultGrapher;
import org.apache.commons.graph.builder.HeadVertexConnector;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultGrapher_ESTest extends DefaultGrapher_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      DefaultGrapher<Integer, Integer> defaultGrapher0 = new DefaultGrapher<Integer, Integer>(mutableSpanningTree0);
      Integer integer0 = new Integer(2512);
      HeadVertexConnector<Integer, Integer> headVertexConnector0 = defaultGrapher0.addEdge(integer0);
      assertNotNull(headVertexConnector0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultGrapher<Integer, Integer> defaultGrapher0 = new DefaultGrapher<Integer, Integer>((MutableGraph<Integer, Integer>) null);
      Integer integer0 = new Integer(0);
      // Undeclared exception!
      try { 
        defaultGrapher0.addVertex(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.builder.DefaultGrapher", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DefaultGrapher<Integer, Integer> defaultGrapher0 = new DefaultGrapher<Integer, Integer>(undirectedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultGrapher0.addVertex((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null vertex not admitted
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      DefaultGrapher<Integer, Integer> defaultGrapher0 = new DefaultGrapher<Integer, Integer>(mutableSpanningTree0);
      Integer integer0 = new Integer(2512);
      Integer integer1 = defaultGrapher0.addVertex(integer0);
      // Undeclared exception!
      try { 
        defaultGrapher0.addVertex(integer1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DefaultGrapher<Integer, Integer> defaultGrapher0 = new DefaultGrapher<Integer, Integer>(undirectedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultGrapher0.addEdge((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null edge not admitted
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
