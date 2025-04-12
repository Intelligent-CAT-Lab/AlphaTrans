
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


package org.apache.commons.graph.connectivity;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector;
import org.apache.commons.graph.connectivity.DefaultConnectivityBuilder;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultConnectivityBuilder_ESTest extends DefaultConnectivityBuilder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DefaultConnectivityBuilder<Integer, Integer> defaultConnectivityBuilder0 = new DefaultConnectivityBuilder<Integer, Integer>(undirectedMutableGraph0);
      ConnectivityAlgorithmsSelector<Integer, Integer> connectivityAlgorithmsSelector0 = defaultConnectivityBuilder0.includingAllVertices();
      assertNotNull(connectivityAlgorithmsSelector0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DefaultConnectivityBuilder<Integer, Integer> defaultConnectivityBuilder0 = new DefaultConnectivityBuilder<Integer, Integer>(undirectedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultConnectivityBuilder0.includingVertices((Integer[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Graph connectivity cannote be applied on null vertices array, use no-args if you intend specify no vertices
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DefaultConnectivityBuilder<Integer, Integer> defaultConnectivityBuilder0 = new DefaultConnectivityBuilder<Integer, Integer>(undirectedMutableGraph0);
      Integer[] integerArray0 = new Integer[6];
      ConnectivityAlgorithmsSelector<Integer, Integer> connectivityAlgorithmsSelector0 = defaultConnectivityBuilder0.includingVertices(integerArray0);
      assertNotNull(connectivityAlgorithmsSelector0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DefaultConnectivityBuilder<Integer, Integer> defaultConnectivityBuilder0 = new DefaultConnectivityBuilder<Integer, Integer>((Graph<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        defaultConnectivityBuilder0.includingAllVertices();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.connectivity.DefaultConnectivityBuilder", e);
      }
  }
}
