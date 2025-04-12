
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
import org.apache.commons.graph.collections.DisjointSet;
import org.apache.commons.graph.collections.DisjointSetNode;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DisjointSet_ESTest extends DisjointSet_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DisjointSet<Object> disjointSet0 = new DisjointSet<Object>();
      Object object0 = disjointSet0.find1((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Integer integer0 = new Integer(1477);
      DisjointSet<Integer> disjointSet0 = new DisjointSet<Integer>();
      Integer integer1 = new Integer(512);
      disjointSet0.union((Integer) null, integer1);
      disjointSet0.union(integer1, integer0);
      assertFalse(integer0.equals((Object)integer1));
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Integer integer0 = new Integer(2211);
      Integer integer1 = new Integer(0);
      Integer integer2 = new Integer((-1892));
      DisjointSet<Integer> disjointSet0 = new DisjointSet<Integer>();
      disjointSet0.union(integer0, integer1);
      disjointSet0.union(integer2, integer0);
      assertFalse(integer2.equals((Object)integer0));
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DisjointSet<Object> disjointSet0 = new DisjointSet<Object>();
      Object object0 = new Object();
      DisjointSetNode<Object> disjointSetNode0 = new DisjointSetNode<Object>(object0);
      disjointSet0.union(disjointSetNode0, disjointSetNode0);
      assertEquals(0, (int)disjointSetNode0.getRank());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      DisjointSet<Object> disjointSet0 = new DisjointSet<Object>();
      Object object0 = new Object();
      disjointSet0.union(disjointSet0, object0);
      Object object1 = disjointSet0.find1(object0);
      assertNotNull(object1);
  }
}
