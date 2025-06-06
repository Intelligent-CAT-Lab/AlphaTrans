
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
import java.math.BigDecimal;
import java.math.MathContext;
import org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BigDecimalWeightBaseOperations_ESTest extends BigDecimalWeightBaseOperations_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = bigDecimalWeightBaseOperations0.identity();
      BigDecimal bigDecimal1 = new BigDecimal((-647L));
      BigDecimal bigDecimal2 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal1);
      assertEquals((short) (-647), bigDecimal2.shortValue());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = bigDecimalWeightBaseOperations0.identity();
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.inverse(bigDecimal0);
      assertEquals((byte)0, bigDecimal1.byteValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigDecimal bigDecimal1 = new BigDecimal((-1227L));
      MathContext mathContext0 = MathContext.DECIMAL128;
      BigDecimal bigDecimal2 = bigDecimal0.subtract(bigDecimal1, mathContext0);
      BigDecimal bigDecimal3 = bigDecimalWeightBaseOperations0.inverse(bigDecimal2);
      assertNotSame(bigDecimal1, bigDecimal3);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = new BigDecimal((-647L));
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.inverse(bigDecimal0);
      assertNotSame(bigDecimal1, bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = bigDecimalWeightBaseOperations0.identity();
      BigDecimal bigDecimal1 = new BigDecimal((-647L));
      int int0 = bigDecimalWeightBaseOperations0.compare(bigDecimal0, bigDecimal1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = new BigDecimal((-647L));
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0);
      assertEquals((short) (-1294), bigDecimal1.shortValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0);
      assertNotSame(bigDecimal1, bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      // Undeclared exception!
      try { 
        bigDecimalWeightBaseOperations0.compare((BigDecimal) null, (BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = new BigDecimal((-620));
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, (BigDecimal) null);
      assertNull(bigDecimal1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = new BigDecimal(4972);
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0);
      assertNotNull(bigDecimal1);
      
      int int0 = bigDecimalWeightBaseOperations0.compare(bigDecimal0, bigDecimal1);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = bigDecimalWeightBaseOperations0.append((BigDecimal) null, (BigDecimal) null);
      assertNull(bigDecimal0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = bigDecimalWeightBaseOperations0.identity();
      BigDecimal bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0);
      assertSame(bigDecimal0, bigDecimal1);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      // Undeclared exception!
      try { 
        bigDecimalWeightBaseOperations0.inverse((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BigDecimalWeightBaseOperations bigDecimalWeightBaseOperations0 = new BigDecimalWeightBaseOperations();
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      int int0 = bigDecimalWeightBaseOperations0.compare(bigDecimal0, bigDecimal0);
      assertEquals(0, int0);
  }
}
