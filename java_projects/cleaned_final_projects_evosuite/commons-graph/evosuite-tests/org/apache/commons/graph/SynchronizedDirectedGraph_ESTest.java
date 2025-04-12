
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
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.SynchronizedDirectedGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SynchronizedDirectedGraph_ESTest extends SynchronizedDirectedGraph_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable<Integer>) null).when(directedGraph0).getOutbound(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Iterable<Integer> iterable0 = synchronizedDirectedGraph0.getOutbound(integer0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(directedGraph0).getOutDegree(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-358));
      int int0 = synchronizedDirectedGraph0.getOutDegree(integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(1).when(directedGraph0).getOutDegree(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-1));
      int int0 = synchronizedDirectedGraph0.getOutDegree(integer0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(directedGraph0).getInbound(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-1));
      Iterable<Integer> iterable0 = synchronizedDirectedGraph0.getInbound(integer0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(directedGraph0).getInDegree(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-358));
      int int0 = synchronizedDirectedGraph0.getInDegree(integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn(1).when(directedGraph0).getInDegree(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-1));
      int int0 = synchronizedDirectedGraph0.getInDegree(integer0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>((DirectedGraph<Integer, Integer>) null);
      Integer integer0 = new Integer(854);
      // Undeclared exception!
      try { 
        synchronizedDirectedGraph0.getOutbound(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedDirectedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>((DirectedGraph<Integer, Integer>) null);
      Integer integer0 = new Integer(0);
      // Undeclared exception!
      try { 
        synchronizedDirectedGraph0.getOutDegree(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedDirectedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>((DirectedGraph<Integer, Integer>) null);
      Integer integer0 = new Integer((-2476));
      // Undeclared exception!
      try { 
        synchronizedDirectedGraph0.getInbound(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedDirectedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Integer integer0 = new Integer((-585));
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>((DirectedGraph<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        synchronizedDirectedGraph0.getInDegree(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.SynchronizedDirectedGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((Iterable) null).when(directedGraph0).getOutbound(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-3147));
      Iterable<Integer> iterable0 = synchronizedDirectedGraph0.getOutbound(integer0);
      assertNull(iterable0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((-1)).when(directedGraph0).getInDegree(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-3147));
      int int0 = synchronizedDirectedGraph0.getInDegree(integer0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DirectedGraph<Integer, Integer> directedGraph0 = (DirectedGraph<Integer, Integer>) mock(DirectedGraph.class, new ViolatedAssumptionAnswer());
      doReturn((-1)).when(directedGraph0).getOutDegree(anyInt());
      SynchronizedDirectedGraph<Integer, Integer> synchronizedDirectedGraph0 = new SynchronizedDirectedGraph<Integer, Integer>(directedGraph0);
      Integer integer0 = new Integer((-3147));
      int int0 = synchronizedDirectedGraph0.getOutDegree(integer0);
      assertEquals((-1), int0);
  }
}
