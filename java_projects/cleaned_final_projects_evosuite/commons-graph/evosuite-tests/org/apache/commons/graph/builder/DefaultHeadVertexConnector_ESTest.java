
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
import org.apache.commons.graph.builder.DefaultHeadVertexConnector;
import org.apache.commons.graph.builder.TailVertexConnector;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultHeadVertexConnector_ESTest extends DefaultHeadVertexConnector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      DefaultHeadVertexConnector<Integer, Integer> defaultHeadVertexConnector0 = new DefaultHeadVertexConnector<Integer, Integer>(mutableSpanningTree0, (Integer) null);
      Integer integer0 = new Integer((-1535));
      TailVertexConnector<Integer, Integer> tailVertexConnector0 = defaultHeadVertexConnector0.from(integer0);
      assertNotNull(tailVertexConnector0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DefaultHeadVertexConnector<Integer, Integer> defaultHeadVertexConnector0 = new DefaultHeadVertexConnector<Integer, Integer>(directedMutableGraph0, (Integer) null);
      // Undeclared exception!
      try { 
        defaultHeadVertexConnector0.from((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null head vertex not admitted
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
