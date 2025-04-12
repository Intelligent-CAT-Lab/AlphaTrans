
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


package org.apache.commons.graph.scc;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedHashSet;
import java.util.Set;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CheriyanMehlhornGabowAlgorithm_ESTest extends CheriyanMehlhornGabowAlgorithm_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, Integer>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      Integer integer0 = new Integer((-3629));
      LinkedHashSet<Integer> linkedHashSet1 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addEdge(linkedHashSet1, integer0, linkedHashSet1);
      CheriyanMehlhornGabowAlgorithm<LinkedHashSet<Integer>, Integer> cheriyanMehlhornGabowAlgorithm0 = new CheriyanMehlhornGabowAlgorithm<LinkedHashSet<Integer>, Integer>(directedMutableGraph0);
      Set<Set<LinkedHashSet<Integer>>> set0 = cheriyanMehlhornGabowAlgorithm0.perform();
      assertEquals(1, set0.size());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      CheriyanMehlhornGabowAlgorithm<Integer, Integer> cheriyanMehlhornGabowAlgorithm0 = new CheriyanMehlhornGabowAlgorithm<Integer, Integer>(revertedGraph0);
      Set<Set<Integer>> set0 = cheriyanMehlhornGabowAlgorithm0.perform();
      assertEquals(0, set0.size());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      CheriyanMehlhornGabowAlgorithm<Integer, Integer> cheriyanMehlhornGabowAlgorithm0 = new CheriyanMehlhornGabowAlgorithm<Integer, Integer>((DirectedGraph<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        cheriyanMehlhornGabowAlgorithm0.perform();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, Integer>();
      CheriyanMehlhornGabowAlgorithm<LinkedHashSet<Integer>, Integer> cheriyanMehlhornGabowAlgorithm0 = new CheriyanMehlhornGabowAlgorithm<LinkedHashSet<Integer>, Integer>(directedMutableGraph0);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      cheriyanMehlhornGabowAlgorithm0.perform();
      Set<Set<LinkedHashSet<Integer>>> set0 = cheriyanMehlhornGabowAlgorithm0.perform();
      assertEquals(1, set0.size());
  }
}
