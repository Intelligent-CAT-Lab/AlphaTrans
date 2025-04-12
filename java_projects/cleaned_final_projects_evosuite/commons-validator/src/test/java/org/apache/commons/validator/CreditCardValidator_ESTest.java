

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



package org.apache.commons.validator;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.validator.CreditCardValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CreditCardValidator_ESTest extends CreditCardValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = new CreditCardValidator((-1167));
      boolean boolean0 = creditCardValidator0.isValid("HASa~KzKe`FDv");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      // Undeclared exception!
      try { 
        creditCardValidator0.luhnCheck((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = new CreditCardValidator((-1283));
      assertEquals(0, CreditCardValidator.NONE);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      boolean boolean0 = creditCardValidator0.luhnCheck("91");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      boolean boolean0 = creditCardValidator0.luhnCheck("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      boolean boolean0 = creditCardValidator0.luhnCheck("6011");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      boolean boolean0 = creditCardValidator0.isValid("51,52,53,54,55,");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      boolean boolean0 = creditCardValidator0.isValid("50");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      boolean boolean0 = creditCardValidator0.isValid("Couldn't clone Flags object.");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(1107);
      boolean boolean0 = creditCardValidator0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(0);
      assertEquals(4, CreditCardValidator.MASTERCARD);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(9);
      boolean boolean0 = creditCardValidator0.isValid("Lo0;EKEUBmN&.\"3F./]");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator1();
      CreditCardValidator.CreditCardType creditCardValidator_CreditCardType0 = mock(CreditCardValidator.CreditCardType.class, new ViolatedAssumptionAnswer());
      creditCardValidator0.addAllowedCardType(creditCardValidator_CreditCardType0);
      assertEquals(4, CreditCardValidator.MASTERCARD);
  }
}
