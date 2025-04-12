
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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.connectivity.ConnectedComponentHandler;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.Monoid;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ConnectedComponentHandler_ESTest extends ConnectedComponentHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      LinkedList<InMemoryPath<Object, Object>> linkedList0 = new LinkedList<InMemoryPath<Object, Object>>();
      ConnectedComponentHandler<InMemoryPath<Object, Object>, MutableSpanningTree<Object, Object, Object>> connectedComponentHandler0 = new ConnectedComponentHandler<InMemoryPath<Object, Object>, MutableSpanningTree<Object, Object, Object>>(linkedList0);
      Object object0 = new Object();
      Monoid<Object> monoid0 = (Monoid<Object>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Object, Object> mapper0 = (Mapper<Object, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Object, Object, Object> inMemoryWeightedPath0 = new InMemoryWeightedPath<Object, Object, Object>(object0, connectedComponentHandler0, monoid0, mapper0);
      connectedComponentHandler0.finishVertex(inMemoryWeightedPath0);
      List<InMemoryPath<Object, Object>> list0 = connectedComponentHandler0.onCompleted();
      assertFalse(list0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      List<LinkedList<Object>> list0 = List.of(linkedList0, linkedList0);
      ConnectedComponentHandler<LinkedList<Object>, Comparable<Object>> connectedComponentHandler0 = new ConnectedComponentHandler<LinkedList<Object>, Comparable<Object>>(list0);
      // Undeclared exception!
      try { 
        connectedComponentHandler0.finishVertex(linkedList0);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.ImmutableCollections", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      ConnectedComponentHandler<Object, Object> connectedComponentHandler0 = new ConnectedComponentHandler<Object, Object>(linkedList0);
      List<LinkedList<Object>> list0 = List.of(linkedList0, linkedList0, linkedList0, linkedList0, linkedList0);
      linkedList0.push(list0);
      // Undeclared exception!
      try { 
        connectedComponentHandler0.finishVertex(linkedList0);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      LinkedList<InMemoryPath<Object, Object>> linkedList0 = new LinkedList<InMemoryPath<Object, Object>>();
      ConnectedComponentHandler<InMemoryPath<Object, Object>, InMemoryPath<Object, Object>> connectedComponentHandler0 = new ConnectedComponentHandler<InMemoryPath<Object, Object>, InMemoryPath<Object, Object>>(linkedList0);
      List<InMemoryPath<Object, Object>> list0 = connectedComponentHandler0.onCompleted();
      assertEquals(0, list0.size());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ConnectedComponentHandler<Object, LinkedList<Object>> connectedComponentHandler0 = new ConnectedComponentHandler<Object, LinkedList<Object>>((List<Object>) null);
      // Undeclared exception!
      try { 
        connectedComponentHandler0.finishVertex(connectedComponentHandler0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.connectivity.ConnectedComponentHandler", e);
      }
  }
}
