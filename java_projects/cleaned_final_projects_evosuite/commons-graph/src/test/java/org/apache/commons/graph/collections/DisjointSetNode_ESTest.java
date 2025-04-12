
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


package org.apache.commons.graph.collections;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.collections.DisjointSetNode;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DisjointSetNode_ESTest extends DisjointSetNode_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Integer integer0 = new Integer((-2439));
      DisjointSetNode<Integer> disjointSetNode0 = new DisjointSetNode<Integer>(integer0);
      assertEquals(0, (int)disjointSetNode0.getRank());
      
      disjointSetNode0.setRank(1);
      Integer integer1 = disjointSetNode0.getRank();
      assertEquals(1, (int)integer1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DisjointSetNode<Object> disjointSetNode0 = new DisjointSetNode<Object>((Object) null);
      disjointSetNode0.setRank((-537));
      disjointSetNode0.getRank();
      assertEquals((-537), (int)disjointSetNode0.getRank());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Object object0 = new Object();
      DisjointSetNode<Object> disjointSetNode0 = new DisjointSetNode<Object>(object0);
      DisjointSetNode<DisjointSetNode<Object>> disjointSetNode1 = new DisjointSetNode<DisjointSetNode<Object>>(disjointSetNode0);
      disjointSetNode1.setParent((DisjointSetNode<DisjointSetNode<Object>>) null);
      DisjointSetNode<DisjointSetNode<Object>> disjointSetNode2 = disjointSetNode1.getParent();
      assertNull(disjointSetNode2);
      assertEquals(0, (int)disjointSetNode1.getRank());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DisjointSetNode<Object> disjointSetNode0 = new DisjointSetNode<Object>((Object) null);
      disjointSetNode0.getElement();
      assertEquals(0, (int)disjointSetNode0.getRank());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer(0);
      DisjointSetNode<Integer> disjointSetNode0 = new DisjointSetNode<Integer>(integer0);
      DisjointSetNode<Object> disjointSetNode1 = new DisjointSetNode<Object>(disjointSetNode0);
      DisjointSetNode<Object> disjointSetNode2 = new DisjointSetNode<Object>(integer0);
      disjointSetNode2.increaseRank();
      int int0 = disjointSetNode2.compareTo(disjointSetNode1);
      assertEquals(1, (int)disjointSetNode2.getRank());
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Object object0 = new Object();
      DisjointSetNode<Object> disjointSetNode0 = new DisjointSetNode<Object>(object0);
      DisjointSetNode<DisjointSetNode<Object>> disjointSetNode1 = new DisjointSetNode<DisjointSetNode<Object>>(disjointSetNode0);
      disjointSetNode1.setRank((-2439));
      DisjointSetNode<DisjointSetNode<Object>> disjointSetNode2 = new DisjointSetNode<DisjointSetNode<Object>>(disjointSetNode0);
      int int0 = disjointSetNode1.compareTo(disjointSetNode2);
      assertEquals((-2439), (int)disjointSetNode1.getRank());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DisjointSetNode<Integer> disjointSetNode0 = new DisjointSetNode<Integer>((Integer) null);
      // Undeclared exception!
      try { 
        disjointSetNode0.compareTo((DisjointSetNode<Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.collections.DisjointSetNode", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer(0);
      DisjointSetNode<Integer> disjointSetNode0 = new DisjointSetNode<Integer>(integer0);
      Integer integer1 = disjointSetNode0.getRank();
      assertEquals(0, (int)integer1);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer(0);
      DisjointSetNode<Integer> disjointSetNode0 = new DisjointSetNode<Integer>(integer0);
      DisjointSetNode<Object> disjointSetNode1 = new DisjointSetNode<Object>(disjointSetNode0);
      disjointSetNode1.compareTo(disjointSetNode1);
      assertEquals(0, (int)disjointSetNode1.getRank());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Object object0 = new Object();
      DisjointSetNode<Object> disjointSetNode0 = new DisjointSetNode<Object>(object0);
      disjointSetNode0.getElement();
      assertEquals(0, (int)disjointSetNode0.getRank());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DisjointSetNode<Integer> disjointSetNode0 = new DisjointSetNode<Integer>((Integer) null);
      DisjointSetNode<Integer> disjointSetNode1 = disjointSetNode0.getParent();
      assertEquals(0, (int)disjointSetNode1.getRank());
  }
}
