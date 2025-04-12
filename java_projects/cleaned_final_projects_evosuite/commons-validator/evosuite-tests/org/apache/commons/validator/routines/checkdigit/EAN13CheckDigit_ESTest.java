

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
import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class EAN13CheckDigit_ESTest extends EAN13CheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      EAN13CheckDigit eAN13CheckDigit0 = (EAN13CheckDigit)EAN13CheckDigit.EAN13_CHECK_DIGIT;
      int int0 = eAN13CheckDigit0.weightedValue(610, 0, 0);
      assertEquals(1830, int0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      EAN13CheckDigit eAN13CheckDigit0 = new EAN13CheckDigit();
      int int0 = eAN13CheckDigit0.weightedValue((-550), 0, 7);
      assertEquals((-550), int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      EAN13CheckDigit eAN13CheckDigit0 = new EAN13CheckDigit();
      // Undeclared exception!
      try { 
        eAN13CheckDigit0.weightedValue(4, 7, (-1563));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 2
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      EAN13CheckDigit eAN13CheckDigit0 = (EAN13CheckDigit)EAN13CheckDigit.EAN13_CHECK_DIGIT;
      int int0 = eAN13CheckDigit0.weightedValue(0, 0, 0);
      assertEquals(0, int0);
  }
}
