

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
import org.apache.commons.validator.routines.checkdigit.SedolCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SedolCheckDigit_ESTest extends SedolCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = (SedolCheckDigit)SedolCheckDigit.SEDOL_CHECK_DIGIT;
      int int0 = sedolCheckDigit0.weightedValue(4, 4, 4);
      assertEquals(28, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      int int0 = sedolCheckDigit0.weightedValue((-1489), 6, (-1688));
      assertEquals((-13401), int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      int int0 = sedolCheckDigit0.toInt('0', (-2334), 1383);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = (SedolCheckDigit)SedolCheckDigit.SEDOL_CHECK_DIGIT;
      int int0 = sedolCheckDigit0.toInt('Z', 'Z', 'Z');
      assertEquals(35, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      int int0 = sedolCheckDigit0.calculateModulus("a", false);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      int int0 = sedolCheckDigit0.calculateModulus("NA0", true);
      assertEquals(3, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      // Undeclared exception!
      try { 
        sedolCheckDigit0.weightedValue(17, 17, 17);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 7
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.SedolCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      try { 
        sedolCheckDigit0.toInt('-', '-', '-');
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[45,45] = '-1' out of range 0 to 35
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = (CUSIPCheckDigit)CUSIPCheckDigit.CUSIP_CHECK_DIGIT;
      // Undeclared exception!
      try { 
        cUSIPCheckDigit0.toInt('S', 35, 35);
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      // Undeclared exception!
      try { 
        sedolCheckDigit0.calculateModulus((String) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.SedolCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      try { 
        sedolCheckDigit0.calculateModulus("I", true);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[1,1] = '18' out of range 0 to 9
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      try { 
        sedolCheckDigit0.calculate("y-F\"Eco");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[2,7] = '-1' out of range 0 to 35
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      try { 
        sedolCheckDigit0.calculateModulus("7u[Z'O}_CdPT]", true);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Code Length = 13
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = (SedolCheckDigit)SedolCheckDigit.SEDOL_CHECK_DIGIT;
      int int0 = sedolCheckDigit0.weightedValue(0, 7, 5);
      assertEquals(0, int0);
  }
}
