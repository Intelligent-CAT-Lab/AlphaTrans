
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
import org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FloatWeightBaseOperations_ESTest extends FloatWeightBaseOperations_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float((-1.0));
      Float float1 = floatWeightBaseOperations0.inverse(float0);
      assertEquals(1.0F, (float)float1, 0.01F);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float(2350.746606741365);
      Float float1 = floatWeightBaseOperations0.inverse(float0);
      assertEquals((-2350.7466F), (float)float1, 0.01F);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = floatWeightBaseOperations0.identity();
      assertEquals(0.0F, (float)float0, 0.01F);
      
      Float float1 = new Float(1.0);
      int int0 = floatWeightBaseOperations0.compare(float1, float0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float((-1.0F));
      Float float1 = floatWeightBaseOperations0.append(float0, float0);
      assertNotNull(float1);
      
      int int0 = floatWeightBaseOperations0.compare(float1, float0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float(1.0);
      Float float1 = floatWeightBaseOperations0.append(float0, float0);
      assertNotNull(float1);
      assertEquals(2.0F, (float)float1, 0.01F);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float(0.0);
      Float float1 = new Float((-1281.1265F));
      Float float2 = floatWeightBaseOperations0.append(float0, float1);
      assertEquals((-1281.1265F), (float)float2, 0.01F);
      assertNotNull(float2);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      // Undeclared exception!
      try { 
        floatWeightBaseOperations0.inverse((Float) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float((-1.0F));
      // Undeclared exception!
      try { 
        floatWeightBaseOperations0.compare(float0, (Float) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.Float", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = new Float(1509.5292578769947);
      Float float1 = floatWeightBaseOperations0.append(float0, (Float) null);
      assertNull(float1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = floatWeightBaseOperations0.identity();
      Float float1 = floatWeightBaseOperations0.append(float0, float0);
      assertEquals(0.0F, (float)float1, 0.01F);
      assertNotNull(float1);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = floatWeightBaseOperations0.append((Float) null, (Float) null);
      assertNull(float0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = floatWeightBaseOperations0.identity();
      Float float1 = floatWeightBaseOperations0.inverse(float0);
      assertEquals(-0.0F, (float)float1, 0.01F);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      FloatWeightBaseOperations floatWeightBaseOperations0 = new FloatWeightBaseOperations();
      Float float0 = floatWeightBaseOperations0.identity();
      assertEquals(0.0F, (float)float0, 0.01F);
      
      floatWeightBaseOperations0.compare(float0, float0);
      assertEquals(0.0F, floatWeightBaseOperations0.identity(), 0.01F);
  }
}
