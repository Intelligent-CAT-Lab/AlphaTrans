

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
import org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CUSIPCheckDigit_ESTest extends CUSIPCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      int int0 = cUSIPCheckDigit0.weightedValue((-493), 2302, 14);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      int int0 = cUSIPCheckDigit0.weightedValue(2302, 2302, 578);
      assertEquals(14, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      int int0 = cUSIPCheckDigit0.toInt('0', 1503, 32);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      try { 
        cUSIPCheckDigit0.toInt('<', '<', '<');
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[60,60] = '-1' out of range 0 to 35
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = (CUSIPCheckDigit)CUSIPCheckDigit.CUSIP_CHECK_DIGIT;
      try { 
        cUSIPCheckDigit0.calculateModulus("yK2LZKyCL?LN6bQok2", true);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[10,9] = '-1' out of range 0 to 35
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      boolean boolean0 = cUSIPCheckDigit0.isValid("FZg");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      int int0 = cUSIPCheckDigit0.toInt('b', 0, 1721);
      assertEquals(11, int0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      // Undeclared exception!
      try { 
        cUSIPCheckDigit0.weightedValue((-1), (-1), (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 2
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit", e);
      }
  }
}
