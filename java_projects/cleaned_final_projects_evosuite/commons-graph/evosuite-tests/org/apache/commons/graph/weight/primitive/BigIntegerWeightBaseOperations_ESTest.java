
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
import java.math.BigInteger;
import org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BigIntegerWeightBaseOperations_ESTest extends BigIntegerWeightBaseOperations_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = bigIntegerWeightBaseOperations0.identity();
      BigInteger bigInteger1 = bigIntegerWeightBaseOperations0.inverse(bigInteger0);
      BigInteger bigInteger2 = bigIntegerWeightBaseOperations0.append(bigInteger1, bigInteger0);
      assertNotNull(bigInteger2);
      assertNotSame(bigInteger2, bigInteger0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = bigIntegerWeightBaseOperations0.identity();
      BigInteger bigInteger1 = bigInteger0.pow(0);
      BigInteger bigInteger2 = bigIntegerWeightBaseOperations0.inverse(bigInteger1);
      BigInteger bigInteger3 = bigIntegerWeightBaseOperations0.inverse(bigInteger2);
      assertNotSame(bigInteger2, bigInteger3);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = bigIntegerWeightBaseOperations0.identity();
      int int0 = bigIntegerWeightBaseOperations0.compare(bigInteger0, bigInteger0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = BigInteger.valueOf(1293L);
      BigInteger bigInteger1 = BigInteger.TWO;
      int int0 = bigIntegerWeightBaseOperations0.compare(bigInteger0, bigInteger1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = BigInteger.TWO;
      BigInteger bigInteger1 = bigIntegerWeightBaseOperations0.inverse(bigInteger0);
      int int0 = bigIntegerWeightBaseOperations0.compare(bigInteger1, bigInteger0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = BigInteger.TWO;
      BigInteger bigInteger1 = bigIntegerWeightBaseOperations0.inverse(bigInteger0);
      BigInteger bigInteger2 = bigIntegerWeightBaseOperations0.append(bigInteger1, bigInteger1);
      assertEquals((byte) (-4), bigInteger2.byteValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = BigInteger.TEN;
      BigInteger bigInteger1 = bigIntegerWeightBaseOperations0.append(bigInteger0, bigInteger0);
      assertFalse(bigInteger1.equals((Object)bigInteger0));
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = BigInteger.TWO;
      BigInteger bigInteger1 = bigIntegerWeightBaseOperations0.append(bigInteger0, (BigInteger) null);
      assertNull(bigInteger1);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      BigInteger bigInteger0 = bigIntegerWeightBaseOperations0.append((BigInteger) null, (BigInteger) null);
      assertNull(bigInteger0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      // Undeclared exception!
      try { 
        bigIntegerWeightBaseOperations0.compare((BigInteger) null, (BigInteger) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BigIntegerWeightBaseOperations bigIntegerWeightBaseOperations0 = new BigIntegerWeightBaseOperations();
      // Undeclared exception!
      try { 
        bigIntegerWeightBaseOperations0.inverse((BigInteger) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations", e);
      }
  }
}
