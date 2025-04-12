

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
import org.apache.commons.validator.routines.checkdigit.IBANCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IBANCheckDigit_ESTest extends IBANCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      String string0 = iBANCheckDigit0.calculate("ymJ36YtZJF");
      assertEquals("09", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      String string0 = iBANCheckDigit0.calculate("cgY]z");
      assertEquals("64", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid("] in ");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      String string0 = iBANCheckDigit0.calculate("ymJ36YtZJhF");
      assertEquals("08", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      try { 
        iBANCheckDigit0.calculate("-0");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Code length=2
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      try { 
        iBANCheckDigit0.calculate((String) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Code length=0
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = (IBANCheckDigit)IBANCheckDigit.IBAN_CHECK_DIGIT;
      boolean boolean0 = iBANCheckDigit0.isValid("D9ULRaW");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid("ymJ36YtZJhF");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid("f`99wfb~*:q4Mwj");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid("6X01ok#@p:P,");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid("6X00@+kJ@bp:P,");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid("60");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IBANCheckDigit iBANCheckDigit0 = new IBANCheckDigit();
      boolean boolean0 = iBANCheckDigit0.isValid((String) null);
      assertFalse(boolean0);
  }
}
