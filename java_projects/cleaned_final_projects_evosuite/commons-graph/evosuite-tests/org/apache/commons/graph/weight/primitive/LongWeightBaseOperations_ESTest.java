
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


package org.apache.commons.graph.weight.primitive;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.weight.primitive.LongWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongWeightBaseOperations_ESTest extends LongWeightBaseOperations_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(0L);
      Long long1 = longWeightBaseOperations0.inverse(long0);
      assertEquals(0L, (long)long1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(1L);
      Long long1 = longWeightBaseOperations0.inverse(long0);
      Long long2 = longWeightBaseOperations0.inverse(long1);
      assertTrue(long2.equals((Object)long0));
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(1L);
      Long long1 = longWeightBaseOperations0.inverse(long0);
      int int0 = longWeightBaseOperations0.compare(long0, long1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(1L);
      Long long1 = longWeightBaseOperations0.inverse(long0);
      int int0 = longWeightBaseOperations0.compare(long1, long0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(0L);
      Long long1 = longWeightBaseOperations0.append(long0, long0);
      assertTrue(long1.equals((Object)long0));
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(0L);
      Long long1 = new Long((-1532L));
      Long long2 = longWeightBaseOperations0.append(long1, long0);
      assertEquals((-1532L), (long)long2);
      assertNotNull(long2);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = Long.getLong("_%*N7rY(JGY");
      // Undeclared exception!
      try { 
        longWeightBaseOperations0.compare((Long) null, long0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.LongWeightBaseOperations", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(0L);
      Long long1 = longWeightBaseOperations0.append(long0, (Long) null);
      assertNull(long1);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(1L);
      Long long1 = longWeightBaseOperations0.append(long0, long0);
      assertNotNull(long1);
      assertEquals(2L, (long)long1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = longWeightBaseOperations0.append((Long) null, (Long) null);
      assertNull(long0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = new Long(1L);
      int int0 = longWeightBaseOperations0.compare(long0, long0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      Long long0 = longWeightBaseOperations0.identity();
      assertEquals(0L, (long)long0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      // Undeclared exception!
      try { 
        longWeightBaseOperations0.inverse((Long) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.LongWeightBaseOperations", e);
      }
  }
}
