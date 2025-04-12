

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
import org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ISSNCheckDigit_ESTest extends ISSNCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      try { 
        iSSNCheckDigit0.toCheckDigit(11);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Check Digit Value =11
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      int int0 = iSSNCheckDigit0.weightedValue(0, 2011, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = (ISSNCheckDigit)ISSNCheckDigit.ISSN_CHECK_DIGIT;
      int int0 = iSSNCheckDigit0.weightedValue(1, 1, 1);
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      int int0 = iSSNCheckDigit0.weightedValue((-490), (-490), (-490));
      assertEquals((-244510), int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = (ISSNCheckDigit)ISSNCheckDigit.ISSN_CHECK_DIGIT;
      int int0 = iSSNCheckDigit0.toInt('0', 0, 10);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      int int0 = iSSNCheckDigit0.toInt('X', 1, 1);
      assertEquals(10, int0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      try { 
        iSSNCheckDigit0.toInt('e', 9, 1);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[9] = 'e'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = (ISSNCheckDigit)ISSNCheckDigit.ISSN_CHECK_DIGIT;
      try { 
        iSSNCheckDigit0.toCheckDigit((-269));
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Check Digit Value =-269
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      boolean boolean0 = iSSNCheckDigit0.isValid("00");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      String string0 = iSSNCheckDigit0.toCheckDigit(10);
      assertEquals("X", string0);
  }
}
