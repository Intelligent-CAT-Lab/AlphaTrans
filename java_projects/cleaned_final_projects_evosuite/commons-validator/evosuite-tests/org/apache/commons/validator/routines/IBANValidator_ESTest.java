

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



package org.apache.commons.validator.routines;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.validator.routines.IBANValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IBANValidator_ESTest extends IBANValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.setValidator1("BH", (-1023), "HI='TR+yTK$E");
      assertNotNull(iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      // Undeclared exception!
      try { 
        iBANValidator0.setValidator1("h4t", 0, "h4t");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid country Code; must be exactly 2 upper-case characters
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      boolean boolean0 = iBANValidator0.isValid("LVd{2}[A-Z]{4}[A-Z0-9]{13}");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = new IBANValidator.Validator("FO", 9, "FOFO");
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      // Undeclared exception!
      try { 
        iBANValidator0.setValidator1("FO", 8, "DO");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // countryCode 'FO' does not agree with format: DO
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = null;
      try {
        iBANValidator_Validator0 = new IBANValidator.Validator("0", 250, "0");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid country Code; must be exactly 2 upper-case characters
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.setValidator1("FO", (-1), "FO");
      iBANValidator0.setValidator0(iBANValidator_Validator0);
      IBANValidator.Validator iBANValidator_Validator1 = iBANValidator0.setValidator0(iBANValidator_Validator0);
      assertSame(iBANValidator_Validator1, iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.DEFAULT_IBAN_VALIDATOR;
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.getValidator("SCSCd{2}[A-Z]{4}d{20}[A-Z]{3}");
      IBANValidator.Validator[] iBANValidator_ValidatorArray0 = new IBANValidator.Validator[1];
      iBANValidator_ValidatorArray0[0] = iBANValidator_Validator0;
      IBANValidator iBANValidator1 = new IBANValidator(iBANValidator_ValidatorArray0);
      assertFalse(iBANValidator1.equals((Object)iBANValidator0));
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      // Undeclared exception!
      try { 
        iBANValidator0.setValidator1((String) null, (-4212), (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.concurrent.ConcurrentHashMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      // Undeclared exception!
      try { 
        iBANValidator0.setValidator0((IBANValidator.Validator) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.DEFAULT_IBAN_VALIDATOR;
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.getValidator("z");
      assertNull(iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.getInstance();
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.getValidator("$%");
      assertNull(iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IBANValidator.Validator[] iBANValidator_ValidatorArray0 = new IBANValidator.Validator[1];
      IBANValidator iBANValidator0 = null;
      try {
        iBANValidator0 = new IBANValidator(iBANValidator_ValidatorArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.setValidator1("IEIEd{2}[A-Z]{4}d{14}", (-1), "IEIEd{2}[A-Z]{4}d{14}");
      assertNull(iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.getInstance();
      // Undeclared exception!
      try { 
        iBANValidator0.setValidator1("RegexValidator{", (-910), "$%");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // The singleton validator cannot be modified
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.DEFAULT_IBAN_VALIDATOR;
      // Undeclared exception!
      try { 
        iBANValidator0.setValidator0((IBANValidator.Validator) null);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // The singleton validator cannot be modified
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.getInstance();
      boolean boolean0 = iBANValidator0.isValid("}");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.getValidator((String) null);
      assertNull(iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      boolean boolean0 = iBANValidator0.hasValidator("QAQAd{2}[A-Z]{4}[A-Z0-9]{21}");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      boolean boolean0 = iBANValidator0.isValid("QAQAd{2}[A-Z]{4}[A-Z0-9]{21}");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = null;
      try {
        iBANValidator_Validator0 = new IBANValidator.Validator("RO", 9, "K'A<{ITI");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // countryCode 'RO' does not agree with format: K'A<{ITI
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = null;
      try {
        iBANValidator_Validator0 = new IBANValidator.Validator("SI", (-8), "SI");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid length parameter, must be in range 8 to 34 inclusive: -8
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = null;
      try {
        iBANValidator_Validator0 = new IBANValidator.Validator("UA", 2978, "UA");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid length parameter, must be in range 8 to 34 inclusive: 2978
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = null;
      try {
        iBANValidator_Validator0 = new IBANValidator.Validator("S1", 27, "S1");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid country Code; must be exactly 2 upper-case characters
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      IBANValidator.Validator iBANValidator_Validator0 = null;
      try {
        iBANValidator_Validator0 = new IBANValidator.Validator("pk", 27, "pk");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid country Code; must be exactly 2 upper-case characters
         //
         verifyException("org.apache.commons.validator.routines.IBANValidator$Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      IBANValidator.Validator iBANValidator_Validator0 = iBANValidator0.setValidator1("DO", 34, "DO");
      assertNotNull(iBANValidator_Validator0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.IBANValidator1();
      IBANValidator.Validator[] iBANValidator_ValidatorArray0 = iBANValidator0.DEFAULT_IBAN_VALIDATOR.getDefaultValidators();
      assertEquals(77, iBANValidator_ValidatorArray0.length);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      IBANValidator iBANValidator0 = IBANValidator.getInstance();
      boolean boolean0 = iBANValidator0.hasValidator("vkMR>/ua7t7x");
      assertFalse(boolean0);
  }
}
