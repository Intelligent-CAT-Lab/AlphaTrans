

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
import org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ISBN10CheckDigit_ESTest extends ISBN10CheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      try { 
        iSBN10CheckDigit0.toCheckDigit(13);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Check Digit Value =13
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      try { 
        iSBN10CheckDigit0.toInt('g', 1, 1);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[1] = 'g'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      try { 
        iSBN10CheckDigit0.calculateModulus("0", false);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid code, sum is zero
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      int int0 = iSBN10CheckDigit0.weightedValue(0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      int int0 = iSBN10CheckDigit0.weightedValue((-101), (-101), (-101));
      assertEquals(10201, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = (ISBN10CheckDigit)ISBN10CheckDigit.ISBN10_CHECK_DIGIT;
      int int0 = iSBN10CheckDigit0.weightedValue(3, (-858), (-858));
      assertEquals((-2574), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      int int0 = iSBN10CheckDigit0.toInt('0', (-1087), 3573);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      int int0 = iSBN10CheckDigit0.toInt('5', 13, 0);
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      try { 
        iSBN10CheckDigit0.toCheckDigit((-17));
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Check Digit Value =-17
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      String string0 = iSBN10CheckDigit0.toCheckDigit(10);
      assertEquals("X", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      boolean boolean0 = iSBN10CheckDigit0.isValid("X");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      boolean boolean0 = iSBN10CheckDigit0.isValid("0");
      assertFalse(boolean0);
  }
}
