
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
import java.lang.reflect.Array;
import java.util.Collection;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Locale;
import java.util.TreeSet;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.connectivity.DefaultConnectivityAlgorithmsSelector;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.weight.Monoid;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultConnectivityAlgorithmsSelector_ESTest extends DefaultConnectivityAlgorithmsSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      LinkedList<Object> linkedList1 = new LinkedList<Object>();
      List<LinkedList<Object>> list0 = List.of(linkedList0, linkedList0, linkedList0, linkedList1, linkedList1, linkedList1, linkedList1, linkedList0, linkedList0);
      Object object0 = new Object();
      linkedList1.add(object0);
      InMemoryPath<LinkedList<Object>, LinkedList<Object>> inMemoryPath0 = new InMemoryPath<LinkedList<Object>, LinkedList<Object>>(linkedList1, linkedList1);
      inMemoryPath0.addConnectionInTail(linkedList0, linkedList1, linkedList1);
      HashSet<LinkedList<Object>> hashSet0 = new HashSet<LinkedList<Object>>(list0);
      inMemoryPath0.addConnectionInTail(linkedList0, linkedList0, linkedList0);
      DefaultConnectivityAlgorithmsSelector<LinkedList<Object>, LinkedList<Object>> defaultConnectivityAlgorithmsSelector0 = new DefaultConnectivityAlgorithmsSelector<LinkedList<Object>, LinkedList<Object>>(inMemoryPath0, hashSet0);
      // Undeclared exception!
      try { 
        defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      List<LinkedList<Object>> list0 = List.of(linkedList0, linkedList0, linkedList0, linkedList0, linkedList0, linkedList0, linkedList0, linkedList0, linkedList0);
      InMemoryPath<LinkedList<Object>, LinkedList<Object>> inMemoryPath0 = new InMemoryPath<LinkedList<Object>, LinkedList<Object>>(linkedList0, linkedList0);
      HashSet<LinkedList<Object>> hashSet0 = new HashSet<LinkedList<Object>>(list0);
      linkedList0.offerFirst(hashSet0);
      DefaultConnectivityAlgorithmsSelector<LinkedList<Object>, LinkedList<Object>> defaultConnectivityAlgorithmsSelector0 = new DefaultConnectivityAlgorithmsSelector<LinkedList<Object>, LinkedList<Object>>(inMemoryPath0, hashSet0);
      // Undeclared exception!
      try { 
        defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm();
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      LinkedHashSet<Comparable<Locale.IsoCountryCode>> linkedHashSet0 = new LinkedHashSet<Comparable<Locale.IsoCountryCode>>(0);
      Monoid<Object> monoid0 = (Monoid<Object>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn(linkedHashSet0).when(monoid0).identity();
      Mapper<LinkedList<Object>, Object> mapper0 = (Mapper<LinkedList<Object>, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<LinkedList<Locale.IsoCountryCode>, LinkedList<Object>, Object> mutableSpanningTree0 = new MutableSpanningTree<LinkedList<Locale.IsoCountryCode>, LinkedList<Object>, Object>(monoid0, mapper0);
      LinkedList<Locale.IsoCountryCode>[] linkedListArray0 = (LinkedList<Locale.IsoCountryCode>[]) Array.newInstance(LinkedList.class, 8);
      LinkedList<Locale.IsoCountryCode> linkedList0 = new LinkedList<Locale.IsoCountryCode>();
      linkedListArray0[0] = linkedList0;
      linkedListArray0[1] = linkedListArray0[0];
      linkedListArray0[2] = linkedListArray0[1];
      linkedListArray0[3] = linkedList0;
      linkedListArray0[4] = linkedList0;
      linkedListArray0[5] = linkedListArray0[3];
      linkedListArray0[6] = linkedListArray0[0];
      linkedListArray0[7] = linkedList0;
      List<LinkedList<Locale.IsoCountryCode>> list0 = List.of(linkedListArray0);
      DefaultConnectivityAlgorithmsSelector<LinkedList<Locale.IsoCountryCode>, LinkedList<Object>> defaultConnectivityAlgorithmsSelector0 = new DefaultConnectivityAlgorithmsSelector<LinkedList<Locale.IsoCountryCode>, LinkedList<Object>>(mutableSpanningTree0, list0);
      // Undeclared exception!
      try { 
        defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm();
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex [] does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      LinkedList<Object> linkedList1 = new LinkedList<Object>();
      List<LinkedList<Object>> list0 = List.of(linkedList0, linkedList0, linkedList0, linkedList1, linkedList1, linkedList1, linkedList1, linkedList0, linkedList0);
      InMemoryPath<LinkedList<Object>, LinkedList<Object>> inMemoryPath0 = new InMemoryPath<LinkedList<Object>, LinkedList<Object>>(linkedList1, linkedList1);
      HashSet<LinkedList<Object>> hashSet0 = new HashSet<LinkedList<Object>>(list0);
      DefaultConnectivityAlgorithmsSelector<LinkedList<Object>, LinkedList<Object>> defaultConnectivityAlgorithmsSelector0 = new DefaultConnectivityAlgorithmsSelector<LinkedList<Object>, LinkedList<Object>>(inMemoryPath0, hashSet0);
      Monoid<Object> monoid0 = (Monoid<Object>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn(list0).when(monoid0).identity();
      inMemoryPath0.addConnectionInTail(linkedList0, linkedList1, linkedList0);
      MutableSpanningTree<Object, LinkedList<Locale.IsoCountryCode>, Object> mutableSpanningTree0 = new MutableSpanningTree<Object, LinkedList<Locale.IsoCountryCode>, Object>(monoid0, (Mapper<LinkedList<Locale.IsoCountryCode>, Object>) null);
      linkedList0.offer(mutableSpanningTree0);
      // Undeclared exception!
      try { 
        defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Impossible to get the degree of input vertex; [{}] not contained in this path
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      TreeSet<Locale.IsoCountryCode> treeSet0 = new TreeSet<Locale.IsoCountryCode>();
      DefaultConnectivityAlgorithmsSelector<Locale.IsoCountryCode, LinkedList<Object>> defaultConnectivityAlgorithmsSelector0 = new DefaultConnectivityAlgorithmsSelector<Locale.IsoCountryCode, LinkedList<Object>>((Graph<Locale.IsoCountryCode, LinkedList<Object>>) null, treeSet0);
      Collection<List<Locale.IsoCountryCode>> collection0 = defaultConnectivityAlgorithmsSelector0.applyingMinimumSpanningTreeAlgorithm();
      assertNotNull(collection0);
  }
}
