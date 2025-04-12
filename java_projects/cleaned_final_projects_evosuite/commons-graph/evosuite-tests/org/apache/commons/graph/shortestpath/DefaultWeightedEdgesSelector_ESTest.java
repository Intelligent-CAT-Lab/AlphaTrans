
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
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector;
import org.apache.commons.graph.shortestpath.PathSourceSelector;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultWeightedEdgesSelector_ESTest extends DefaultWeightedEdgesSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Integer integer0 = Integer.valueOf(350);
      InMemoryPath<Integer, Integer> inMemoryPath0 = new InMemoryPath<Integer, Integer>(integer0, integer0);
      DefaultWeightedEdgesSelector<Integer, Integer> defaultWeightedEdgesSelector0 = new DefaultWeightedEdgesSelector<Integer, Integer>(inMemoryPath0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      PathSourceSelector<Integer, Integer, Integer> pathSourceSelector0 = defaultWeightedEdgesSelector0.whereEdgesHaveWeights(mapper0);
      assertNotNull(pathSourceSelector0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DefaultWeightedEdgesSelector<Integer, Integer> defaultWeightedEdgesSelector0 = new DefaultWeightedEdgesSelector<Integer, Integer>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultWeightedEdgesSelector0.whereEdgesHaveWeights((Mapper<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Function to calculate edges weight can not be null.
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
