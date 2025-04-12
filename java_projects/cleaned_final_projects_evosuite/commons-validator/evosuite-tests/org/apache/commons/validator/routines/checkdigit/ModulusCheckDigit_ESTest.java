

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
import org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISINCheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit;
import org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit;
import org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit;
import org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit;
import org.apache.commons.validator.routines.checkdigit.SedolCheckDigit;
import org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ModulusCheckDigit_ESTest extends ModulusCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[1] = (-3373);
      ModulusTenCheckDigit modulusTenCheckDigit0 = new ModulusTenCheckDigit(intArray0, true, true);
      int int0 = modulusTenCheckDigit0.weightedValue((-3373), (-965), 2630);
      assertEquals(31, int0);
      assertEquals(10, modulusTenCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = (CUSIPCheckDigit)CUSIPCheckDigit.CUSIP_CHECK_DIGIT;
      int int0 = cUSIPCheckDigit0.weightedValue((-318), (-1158), (-1158));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      String string0 = iSSNCheckDigit0.toCheckDigit(0);
      assertEquals("0", string0);
      assertEquals(11, iSSNCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      boolean boolean0 = luhnCheckDigit0.isValid("8");
      assertFalse(boolean0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      int int0 = luhnCheckDigit0.toInt('0', 1, 1);
      assertEquals(0, int0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      int int0 = luhnCheckDigit0.toInt('4', 55, (-208));
      assertEquals(4, int0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      String string0 = luhnCheckDigit0.toCheckDigit(9);
      assertEquals("9", string0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int int0 = ModulusCheckDigit.sumDigits(0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      SedolCheckDigit sedolCheckDigit0 = new SedolCheckDigit();
      int int0 = sedolCheckDigit0.calculateModulus("01fq", false);
      assertEquals(0, int0);
      assertEquals(10, sedolCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      int int0 = iSSNCheckDigit0.calculateModulus("9", true);
      assertEquals(6, int0);
      assertEquals(11, iSSNCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = 592;
      intArray0[2] = (-3243);
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, true);
      int int0 = modulusTenCheckDigit0.calculateModulus("zuC", false);
      assertEquals((-6), int0);
      assertEquals(10, modulusTenCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      try { 
        luhnCheckDigit0.toInt('P', 'P', 'P');
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[80] = 'P'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      VerhoeffCheckDigit verhoeffCheckDigit0 = (VerhoeffCheckDigit)VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT;
      // Undeclared exception!
      try { 
        verhoeffCheckDigit0.isValid("");
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = new ISBN10CheckDigit();
      try { 
        iSBN10CheckDigit0.calculateModulus("?5amv8m.>mzR", false);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[1] = '?'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ISINCheckDigit iSINCheckDigit0 = new ISINCheckDigit();
      // Undeclared exception!
      try { 
        iSINCheckDigit0.calculateModulus("", true);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      // Undeclared exception!
      try { 
        aBANumberCheckDigit0.calculateModulus((String) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[0];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0);
      // Undeclared exception!
      try { 
        modulusTenCheckDigit0.calculateModulus("uxpYyvc*qUY[w(K%35S", true);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[0];
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, false);
      // Undeclared exception!
      try { 
        modulusTenCheckDigit0.calculate("431");
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int int0 = ModulusCheckDigit.sumDigits(9);
      assertEquals(9, int0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      try { 
        luhnCheckDigit0.toCheckDigit(775);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Check Digit Value =775
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ISSNCheckDigit iSSNCheckDigit0 = new ISSNCheckDigit();
      try { 
        iSSNCheckDigit0.toCheckDigit((-857));
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Check Digit Value =-857
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      boolean boolean0 = luhnCheckDigit0.isValid("Invalid Character[");
      assertFalse(boolean0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      boolean boolean0 = luhnCheckDigit0.isValid("00");
      assertEquals(10, luhnCheckDigit0.getModulus());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      try { 
        luhnCheckDigit0.calculate("");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Code is missing
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      String string0 = luhnCheckDigit0.calculate("1");
      assertEquals("8", string0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      try { 
        luhnCheckDigit0.calculate((String) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Code is missing
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[0] = (-5);
      ModulusTenCheckDigit modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(intArray0, true);
      boolean boolean0 = modulusTenCheckDigit0.isValid("9");
      assertFalse(boolean0);
      assertEquals(10, modulusTenCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      boolean boolean0 = luhnCheckDigit0.isValid("");
      assertEquals(10, luhnCheckDigit0.getModulus());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      boolean boolean0 = luhnCheckDigit0.isValid("2931");
      assertTrue(boolean0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = new LuhnCheckDigit();
      boolean boolean0 = luhnCheckDigit0.isValid((String) null);
      assertFalse(boolean0);
      assertEquals(10, luhnCheckDigit0.getModulus());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      int int0 = aBANumberCheckDigit0.getModulus();
      assertEquals(10, int0);
  }
}
