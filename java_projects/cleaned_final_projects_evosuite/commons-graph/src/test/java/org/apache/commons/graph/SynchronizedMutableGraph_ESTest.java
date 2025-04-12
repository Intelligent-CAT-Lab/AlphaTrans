
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


package org.apache.commons.graph;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.SynchronizedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SynchronizedMutableGraph_ESTest extends SynchronizedMutableGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MutableGraph<Integer, Integer> mutableGraph0 = (MutableGraph<Integer, Integer>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Integer, Integer> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Integer, Integer>(mutableGraph0);
      Integer integer0 = new Integer((-1));
      Integer integer1 = new Integer(0);
      synchronizedMutableGraph0.addEdge((Integer) null, integer1, integer0);
      assertFalse(integer1.equals((Object)integer0));
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      SynchronizedMutableGraph<Integer, Integer> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Integer, Integer>((MutableGraph<Integer, Integer>) null);
      Integer integer0 = new Integer(3805);
      // Undeclared exception!
      try { 
        synchronizedMutableGraph0.removeEdge(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedMutableGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      MutableGraph<Integer, Integer> mutableGraph0 = (MutableGraph<Integer, Integer>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Integer, Integer> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Integer, Integer>(mutableGraph0);
      Integer integer0 = new Integer((-1));
      synchronizedMutableGraph0.addVertex(integer0);
      assertEquals(0, synchronizedMutableGraph0.getSize());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      MutableGraph<Integer, Integer> mutableGraph0 = (MutableGraph<Integer, Integer>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Integer, Integer> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Integer, Integer>(mutableGraph0);
      synchronizedMutableGraph0.removeEdge((Integer) null);
      assertEquals(0, synchronizedMutableGraph0.getSize());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      MutableGraph<Integer, Integer> mutableGraph0 = (MutableGraph<Integer, Integer>) mock(MutableGraph.class, new ViolatedAssumptionAnswer());
      SynchronizedMutableGraph<Integer, Integer> synchronizedMutableGraph0 = new SynchronizedMutableGraph<Integer, Integer>(mutableGraph0);
      Integer integer0 = new Integer((-1));
      synchronizedMutableGraph0.removeVertex(integer0);
      assertEquals(0, synchronizedMutableGraph0.getOrder());
  }
}
