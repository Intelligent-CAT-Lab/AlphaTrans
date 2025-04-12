
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
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.MutableGraph;
import org.apache.commons.graph.builder.DefaultTailVertexConnector;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultTailVertexConnector_ESTest extends DefaultTailVertexConnector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1471));
      Integer integer1 = new Integer(0);
      DefaultTailVertexConnector<Integer, Integer> defaultTailVertexConnector0 = new DefaultTailVertexConnector<Integer, Integer>(undirectedMutableGraph0, integer1, integer0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1471));
      undirectedMutableGraph0.addVertex(integer0);
      DefaultTailVertexConnector<Integer, Integer> defaultTailVertexConnector0 = new DefaultTailVertexConnector<Integer, Integer>(undirectedMutableGraph0, integer0, integer0);
      defaultTailVertexConnector0.to(integer0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      DefaultTailVertexConnector<Integer, Integer> defaultTailVertexConnector0 = new DefaultTailVertexConnector<Integer, Integer>((MutableGraph<Integer, Integer>) null, integer0, integer0);
      // Undeclared exception!
      try { 
        defaultTailVertexConnector0.to(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.builder.DefaultTailVertexConnector", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DefaultTailVertexConnector<Integer, Integer> defaultTailVertexConnector0 = new DefaultTailVertexConnector<Integer, Integer>(undirectedMutableGraph0, (Integer) null, (Integer) null);
      // Undeclared exception!
      try { 
        defaultTailVertexConnector0.to((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Null tail vertex not admitted
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1471));
      DefaultTailVertexConnector<Integer, Integer> defaultTailVertexConnector0 = new DefaultTailVertexConnector<Integer, Integer>(undirectedMutableGraph0, integer0, integer0);
      // Undeclared exception!
      try { 
        defaultTailVertexConnector0.to(integer0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }
}
