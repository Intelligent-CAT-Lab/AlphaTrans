

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



package org.apache.commons.validator.routines.checkdigit;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ABANumberCheckDigit_ESTest extends ABANumberCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      int int0 = aBANumberCheckDigit0.weightedValue(0, 5, 98);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      int int0 = aBANumberCheckDigit0.weightedValue(10, 10, 21);
      assertEquals(30, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      int int0 = aBANumberCheckDigit0.weightedValue((-237), (-237), (-237));
      assertEquals((-711), int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = (ABANumberCheckDigit)ABANumberCheckDigit.ABAN_CHECK_DIGIT;
      // Undeclared exception!
      try { 
        aBANumberCheckDigit0.weightedValue(0, 1, (-911));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2 out of bounds for length 3
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit", e);
      }
  }
}
