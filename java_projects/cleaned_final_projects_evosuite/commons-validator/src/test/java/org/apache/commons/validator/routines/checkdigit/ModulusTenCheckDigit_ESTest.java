

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
import org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ModulusTenCheckDigit_ESTest extends ModulusTenCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[0] = (-4465);
      ModulusTenCheckDigit modulusTenCheckDigit0 = new ModulusTenCheckDigit(intArray0, true, true);
      int int0 = modulusTenCheckDigit0.weightedValue(21, (-1538), 1465);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[4];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      int int0 = modulusTenCheckDigit0.weightedValue(3301, 701, 9);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[1];
      intArray0[0] = 1;
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      int int0 = modulusTenCheckDigit0.weightedValue(1, 1, 1599);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = (-446);
      ModulusTenCheckDigit modulusTenCheckDigit0 = new ModulusTenCheckDigit(intArray0, true, false);
      int int0 = modulusTenCheckDigit0.weightedValue(1871, 4315, 1871);
      assertEquals((-834466), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[13];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      int int0 = modulusTenCheckDigit0.toInt('0', 10, (-600));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[4];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      int int0 = modulusTenCheckDigit0.toInt('r', 1, 118);
      assertEquals(27, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = 133;
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      boolean boolean0 = modulusTenCheckDigit0.isValid("k1");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[10];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      // Undeclared exception!
      try { 
        modulusTenCheckDigit0.weightedValue((-3218), (-3218), (-3218));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -9 out of bounds for length 10
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[0];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      // Undeclared exception!
      try { 
        modulusTenCheckDigit0.weightedValue(33, 33, 33);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[4];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      try { 
        modulusTenCheckDigit0.toInt('~', 118, (-1));
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[118] = '~'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[0];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      // Undeclared exception!
      try { 
        modulusTenCheckDigit0.isValid("eH;x%=j7qBnzBs7");
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        ModulusTenCheckDigit.ModulusTenCheckDigit2((int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        ModulusTenCheckDigit.ModulusTenCheckDigit1((int[]) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ModulusTenCheckDigit modulusTenCheckDigit0 = null;
      try {
        modulusTenCheckDigit0 = new ModulusTenCheckDigit((int[]) null, true, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[10];
      ModulusTenCheckDigit modulusTenCheckDigit0 = new ModulusTenCheckDigit(intArray0, true, true);
      boolean boolean0 = modulusTenCheckDigit0.isValid("37");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[5];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      boolean boolean0 = modulusTenCheckDigit0.isValid("11L'u%");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[1];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      boolean boolean0 = modulusTenCheckDigit0.isValid("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[17];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      boolean boolean0 = modulusTenCheckDigit0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[4];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      String string0 = modulusTenCheckDigit0.toString();
      assertEquals("ModulusTenCheckDigit[postitionWeight=[0, 0, 0, 0], useRightPos=false, sumWeightedDigits=false]", string0);
  }
}
