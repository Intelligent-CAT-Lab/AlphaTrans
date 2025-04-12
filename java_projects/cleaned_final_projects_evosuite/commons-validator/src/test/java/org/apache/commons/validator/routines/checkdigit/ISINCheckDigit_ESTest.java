

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
import org.apache.commons.validator.routines.checkdigit.ISINCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ISINCheckDigit_ESTest extends ISINCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      try { 
        iSINCheckDigit0.calculate("00");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid code, sum is zero
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      int int0 = iSINCheckDigit0.weightedValue(0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = (ISINCheckDigit)ISINCheckDigit.ISIN_CHECK_DIGIT;
      int int0 = iSINCheckDigit0.weightedValue(546, (-1322), (-1352));
      assertEquals(12, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      int int0 = iSINCheckDigit0.calculateModulus("j", false);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      int int0 = iSINCheckDigit0.calculateModulus("Z", false);
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      // Undeclared exception!
      try { 
        iSINCheckDigit0.weightedValue(4760, 88, (-4127));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 2
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ISINCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      // Undeclared exception!
      try { 
        iSINCheckDigit0.calculateModulus("", true);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      // Undeclared exception!
      try { 
        iSINCheckDigit0.calculateModulus((String) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ISINCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      try { 
        iSINCheckDigit0.calculateModulus(",(9t", true);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid checkdigit[t] in ,(9t
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      try { 
        iSINCheckDigit0.calculateModulus("N94IBfDd;Jq]uk]9", true);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[9] = '-1'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }
}
