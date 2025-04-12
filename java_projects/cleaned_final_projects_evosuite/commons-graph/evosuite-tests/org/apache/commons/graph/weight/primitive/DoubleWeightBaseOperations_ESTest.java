
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
import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DoubleWeightBaseOperations_ESTest extends DoubleWeightBaseOperations_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double((-3519.0));
      Double double1 = doubleWeightBaseOperations0.inverse(double0);
      assertEquals(3519.0, (double)double1, 0.01);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = doubleWeightBaseOperations0.identity();
      Double double1 = doubleWeightBaseOperations0.inverse(double0);
      assertEquals(-0.0, (double)double1, 0.01);
      
      int int0 = doubleWeightBaseOperations0.compare(double0, double1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double(50.34);
      Double double1 = doubleWeightBaseOperations0.inverse(double0);
      int int0 = doubleWeightBaseOperations0.compare(double1, double0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double(50.34);
      Double double1 = doubleWeightBaseOperations0.inverse(double0);
      Double double2 = doubleWeightBaseOperations0.append(double0, double1);
      assertEquals(0.0, (double)double2, 0.01);
      assertNotNull(double2);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double((-1839.848443836));
      Double double1 = doubleWeightBaseOperations0.append(double0, double0);
      assertEquals((-3679.696887672), (double)double1, 0.01);
      assertNotNull(double1);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double(50.34);
      Double double1 = doubleWeightBaseOperations0.append(double0, (Double) null);
      assertNull(double1);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double(50.34);
      Double double1 = doubleWeightBaseOperations0.append(double0, double0);
      assertNotNull(double1);
      assertEquals(100.68, (double)double1, 0.01);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = doubleWeightBaseOperations0.append((Double) null, (Double) null);
      assertNull(double0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = new Double(50.34);
      int int0 = doubleWeightBaseOperations0.compare(double0, double0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      Double double0 = doubleWeightBaseOperations0.identity();
      // Undeclared exception!
      try { 
        doubleWeightBaseOperations0.compare(double0, (Double) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.Double", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DoubleWeightBaseOperations doubleWeightBaseOperations0 = new DoubleWeightBaseOperations();
      // Undeclared exception!
      try { 
        doubleWeightBaseOperations0.inverse((Double) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations", e);
      }
  }
}
