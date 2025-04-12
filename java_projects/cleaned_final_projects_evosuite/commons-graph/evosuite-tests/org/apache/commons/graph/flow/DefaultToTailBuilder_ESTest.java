
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


package org.apache.commons.graph.flow;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.flow.DefaultToTailBuilder;
import org.apache.commons.graph.flow.MaxFlowAlgorithmSelector;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.RevertedGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultToTailBuilder_ESTest extends DefaultToTailBuilder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      Integer integer0 = new Integer(0);
      DefaultToTailBuilder<Integer, Integer, Integer> defaultToTailBuilder0 = new DefaultToTailBuilder<Integer, Integer, Integer>(revertedGraph0, mapper0, integer0);
      MaxFlowAlgorithmSelector<Integer, Integer, Integer> maxFlowAlgorithmSelector0 = defaultToTailBuilder0.to(integer0);
      assertNotNull(maxFlowAlgorithmSelector0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultToTailBuilder<Integer, Integer, Integer> defaultToTailBuilder0 = new DefaultToTailBuilder<Integer, Integer, Integer>((DirectedGraph<Integer, Integer>) null, (Mapper<Integer, Integer>) null, (Integer) null);
      // Undeclared exception!
      try { 
        defaultToTailBuilder0.to((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // tail vertex has to be specifies when looking for the max flow
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
