
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


package org.apache.commons.graph.coloring;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.NoSuchElementException;
import java.util.function.Consumer;
import org.apache.commons.graph.coloring.UncoloredOrderedVertices;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class UncoloredOrderedVertices_ESTest extends UncoloredOrderedVertices_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      UncoloredOrderedVertices<Integer> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Integer>();
      Integer integer0 = new Integer((-1));
      uncoloredOrderedVertices0.addVertexDegree(integer0, integer0);
      int int0 = uncoloredOrderedVertices0.size();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      UncoloredOrderedVertices<Object> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Object>();
      Iterator<Object> iterator0 = uncoloredOrderedVertices0.iterator();
      assertNotNull(iterator0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Integer integer0 = new Integer(0);
      UncoloredOrderedVertices<LinkedHashSet<Object>> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<LinkedHashSet<Object>>();
      int int0 = uncoloredOrderedVertices0.compare(integer0, integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      UncoloredOrderedVertices<Integer> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Integer>();
      Integer integer0 = Integer.getInteger("H", (-2222));
      Integer integer1 = new Integer(0);
      int int0 = uncoloredOrderedVertices0.compare(integer0, integer1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      UncoloredOrderedVertices<Integer> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Integer>();
      Integer integer0 = new Integer((-93));
      Integer integer1 = new Integer((-653));
      int int0 = uncoloredOrderedVertices0.compare(integer0, integer1);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      UncoloredOrderedVertices<Object> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Object>();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        uncoloredOrderedVertices0.addVertexDegree(object0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.UncoloredOrderedVertices", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      UncoloredOrderedVertices<Object> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Object>();
      // Undeclared exception!
      try { 
        uncoloredOrderedVertices0.compare((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.UncoloredOrderedVertices", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer((-71));
      UncoloredOrderedVertices<Object> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Object>();
      uncoloredOrderedVertices0.addVertexDegree((Object) null, integer0);
      Consumer<Object> consumer0 = (Consumer<Object>) mock(Consumer.class, new ViolatedAssumptionAnswer());
      // Undeclared exception!
      try { 
        uncoloredOrderedVertices0.forEach(consumer0);
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.UncoloredOrderedVertices$1", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer((-759));
      UncoloredOrderedVertices<Object> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Object>();
      Object object0 = new Object();
      uncoloredOrderedVertices0.addVertexDegree(object0, integer0);
      Consumer<Object> consumer0 = (Consumer<Object>) mock(Consumer.class, new ViolatedAssumptionAnswer());
      uncoloredOrderedVertices0.forEach(consumer0);
      assertEquals(1, uncoloredOrderedVertices0.size());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      UncoloredOrderedVertices<Object> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<Object>();
      Object object0 = new Object();
      Integer integer0 = new Integer((-855));
      uncoloredOrderedVertices0.addVertexDegree(object0, integer0);
      uncoloredOrderedVertices0.addVertexDegree(object0, integer0);
      assertEquals(1, uncoloredOrderedVertices0.size());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      UncoloredOrderedVertices<LinkedHashSet<Object>> uncoloredOrderedVertices0 = new UncoloredOrderedVertices<LinkedHashSet<Object>>();
      int int0 = uncoloredOrderedVertices0.size();
      assertEquals(0, int0);
  }
}
