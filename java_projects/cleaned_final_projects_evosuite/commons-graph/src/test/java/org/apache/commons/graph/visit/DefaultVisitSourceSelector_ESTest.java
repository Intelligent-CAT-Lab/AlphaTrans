
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


package org.apache.commons.graph.visit;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.visit.DefaultVisitSourceSelector;
import org.apache.commons.graph.visit.VisitAlgorithmsSelector;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultVisitSourceSelector_ESTest extends DefaultVisitSourceSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      MutableSpanningTree<Integer, Object, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Object, Integer>(integerWeightBaseOperations0, (Mapper<Object, Integer>) null);
      Integer integer0 = new Integer(0);
      mutableSpanningTree0.addVertex(integer0);
      DefaultVisitSourceSelector<Integer, Object, MutableSpanningTree<Integer, Object, Integer>> defaultVisitSourceSelector0 = new DefaultVisitSourceSelector<Integer, Object, MutableSpanningTree<Integer, Object, Integer>>(mutableSpanningTree0);
      VisitAlgorithmsSelector<Integer, Object, MutableSpanningTree<Integer, Object, Integer>> visitAlgorithmsSelector0 = defaultVisitSourceSelector0.from(integer0);
      assertNotNull(visitAlgorithmsSelector0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultVisitSourceSelector<Object, Object, DirectedMutableGraph<Object, Object>> defaultVisitSourceSelector0 = new DefaultVisitSourceSelector<Object, Object, DirectedMutableGraph<Object, Object>>((DirectedMutableGraph<Object, Object>) null);
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        defaultVisitSourceSelector0.from(object0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.visit.DefaultVisitSourceSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Object>> directedMutableGraph0 = new DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Object>>();
      DefaultVisitSourceSelector<Object, DirectedMutableGraph<Integer, Object>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Object>>> defaultVisitSourceSelector0 = new DefaultVisitSourceSelector<Object, DirectedMutableGraph<Integer, Object>, DirectedMutableGraph<Object, DirectedMutableGraph<Integer, Object>>>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultVisitSourceSelector0.from((Object) directedMutableGraph0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex {} does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
