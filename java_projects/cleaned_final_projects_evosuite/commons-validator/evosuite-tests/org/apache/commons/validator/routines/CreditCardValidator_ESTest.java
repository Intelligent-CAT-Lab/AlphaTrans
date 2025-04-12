

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
import org.apache.commons.validator.routines.CodeValidator;
import org.apache.commons.validator.routines.CreditCardValidator;
import org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit;
import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CreditCardValidator_ESTest extends CreditCardValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[1];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(0, "", "", 0, 19, intArray0);
      boolean boolean0 = CreditCardValidator.validLength(3, creditCardValidator_CreditCardRange0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[3];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(973, "Q)]4V'!+", "#c,wp2_8D#1g", 0, (-2444), intArray0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[1];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange((-9), ",G@vYXW9.EgVRF|", ",G@vYXW9.EgVRF|", (-9), (-9), intArray0);
      boolean boolean0 = CreditCardValidator.validLength((-9), creditCardValidator_CreditCardRange0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[0];
      ABANumberCheckDigit aBANumberCheckDigit0 = (ABANumberCheckDigit)ABANumberCheckDigit.ABAN_CHECK_DIGIT;
      CodeValidator codeValidator0 = CreditCardValidator.createRangeValidator(creditCardValidator_CreditCardRangeArray0, aBANumberCheckDigit0);
      assertEquals((-1), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        CreditCardValidator.validLength(3378, (CreditCardValidator.CreditCardRange) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[1];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[0];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(3, 3, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      // Undeclared exception!
      try { 
        creditCardValidator0.isValid("00");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      EAN13CheckDigit eAN13CheckDigit0 = (EAN13CheckDigit)ISBNCheckDigit.ISBN13_CHECK_DIGIT;
      // Undeclared exception!
      try { 
        CreditCardValidator.createRangeValidator((CreditCardValidator.CreditCardRange[]) null, eAN13CheckDigit0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator$1", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[6];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[5];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(1, (-1475), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      assertEquals(0L, CreditCardValidator.NONE);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[3];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[6];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(0, (-2309L), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      assertEquals(8L, CreditCardValidator.DISCOVER);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator0(0, (-2444));
      assertEquals(16L, CreditCardValidator.DINERS);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[2];
      int[] intArray0 = new int[9];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(1, "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit", "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit", 3, (-67), intArray0);
      creditCardValidator_CreditCardRangeArray0[0] = creditCardValidator_CreditCardRange0;
      creditCardValidator_CreditCardRangeArray0[1] = creditCardValidator_CreditCardRange0;
      CodeValidator[] codeValidatorArray0 = new CodeValidator[7];
      codeValidatorArray0[0] = creditCardValidator0.VPAY_VALIDATOR;
      codeValidatorArray0[1] = creditCardValidator0.MASTERCARD_VALIDATOR;
      codeValidatorArray0[2] = creditCardValidator0.MASTERCARD_VALIDATOR;
      codeValidatorArray0[3] = creditCardValidator0.VISA_VALIDATOR;
      codeValidatorArray0[4] = creditCardValidator0.DISCOVER_VALIDATOR;
      codeValidatorArray0[5] = creditCardValidator0.VPAY_VALIDATOR;
      codeValidatorArray0[6] = creditCardValidator0.MASTERCARD_VALIDATOR;
      CreditCardValidator creditCardValidator1 = new CreditCardValidator(3, 882L, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      Object object0 = creditCardValidator1.validate("00");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[2];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[7];
      codeValidatorArray0[0] = creditCardValidator0.VPAY_VALIDATOR;
      codeValidatorArray0[1] = creditCardValidator0.MASTERCARD_VALIDATOR;
      codeValidatorArray0[2] = creditCardValidator0.MASTERCARD_VALIDATOR;
      codeValidatorArray0[3] = creditCardValidator0.VISA_VALIDATOR;
      codeValidatorArray0[4] = creditCardValidator0.DISCOVER_VALIDATOR;
      codeValidatorArray0[5] = creditCardValidator0.VPAY_VALIDATOR;
      codeValidatorArray0[6] = creditCardValidator0.DISCOVER_VALIDATOR;
      CreditCardValidator creditCardValidator1 = new CreditCardValidator(3, 882L, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      Object object0 = creditCardValidator1.validate("org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[1];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(0, "", "l'EI", 0, 0, intArray0);
      boolean boolean0 = CreditCardValidator.validLength(0, creditCardValidator_CreditCardRange0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[1];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(0, "p-!rKBj@6Z`lHn0P", "ylYy:@R:Vx5pMc", 625, 625, intArray0);
      boolean boolean0 = CreditCardValidator.validLength(0, creditCardValidator_CreditCardRange0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[1];
      intArray0[0] = 94;
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(94, "X", "X", 94, 94, intArray0);
      boolean boolean0 = CreditCardValidator.validLength(94, creditCardValidator_CreditCardRange0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[2];
      int[] intArray0 = new int[9];
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(1, "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit", "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit", 3, (-67), intArray0);
      creditCardValidator_CreditCardRangeArray0[0] = creditCardValidator_CreditCardRange0;
      CodeValidator[] codeValidatorArray0 = new CodeValidator[7];
      codeValidatorArray0[0] = creditCardValidator0.VPAY_VALIDATOR;
      codeValidatorArray0[1] = creditCardValidator0.MASTERCARD_VALIDATOR;
      codeValidatorArray0[2] = creditCardValidator0.MASTERCARD_VALIDATOR;
      codeValidatorArray0[3] = creditCardValidator0.VISA_VALIDATOR;
      codeValidatorArray0[4] = creditCardValidator0.DISCOVER_VALIDATOR;
      codeValidatorArray0[5] = creditCardValidator0.VPAY_VALIDATOR;
      codeValidatorArray0[6] = creditCardValidator0.VPAY_VALIDATOR;
      CreditCardValidator creditCardValidator1 = new CreditCardValidator(3, 882L, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      // Undeclared exception!
      try { 
        creditCardValidator1.validate("00");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CreditCardValidator.CreditCardRange creditCardValidator_CreditCardRange0 = new CreditCardValidator.CreditCardRange(0, "", "", 0, (-12), (int[]) null);
      boolean boolean0 = CreditCardValidator.validLength(0, creditCardValidator_CreditCardRange0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      Object object0 = creditCardValidator0.validate((String) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      boolean boolean0 = creditCardValidator0.isValid("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      boolean boolean0 = creditCardValidator0.isValid("TMKe/T5OKYI");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CodeValidator[] codeValidatorArray0 = new CodeValidator[8];
      CreditCardValidator creditCardValidator0 = null;
      try {
        creditCardValidator0 = new CreditCardValidator(3, 525L, (CreditCardValidator.CreditCardRange[]) null, codeValidatorArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Card ranges are missing
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[6];
      CreditCardValidator creditCardValidator0 = null;
      try {
        creditCardValidator0 = new CreditCardValidator(3, (-2215L), creditCardValidator_CreditCardRangeArray0, (CodeValidator[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Card validators are missing
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[0];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[1];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator((-3703), (-3703), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      assertEquals(16L, CreditCardValidator.DINERS);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = null;
      try {
        creditCardValidator0 = new CreditCardValidator(2, 2, (CreditCardValidator.CreditCardRange[]) null, (CodeValidator[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Card ranges are missing
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[3];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[5];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(2, 0L, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      assertEquals(8L, CreditCardValidator.DISCOVER);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = null;
      try {
        creditCardValidator0 = new CreditCardValidator(1, 16L, (CreditCardValidator.CreditCardRange[]) null, (CodeValidator[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Card validators are missing
         //
         verifyException("org.apache.commons.validator.routines.CreditCardValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[1];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[0];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(0, (-2L), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      assertEquals(64L, CreditCardValidator.MASTERCARD_PRE_OCT2016);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CreditCardValidator.CreditCardRange[] creditCardValidator_CreditCardRangeArray0 = new CreditCardValidator.CreditCardRange[0];
      CodeValidator[] codeValidatorArray0 = new CodeValidator[19];
      CreditCardValidator creditCardValidator0 = new CreditCardValidator(0, 0, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0);
      assertEquals(64L, CreditCardValidator.MASTERCARD_PRE_OCT2016);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator1(172);
      assertEquals(4L, CreditCardValidator.MASTERCARD);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.CreditCardValidator0();
      Object object0 = creditCardValidator0.validate("");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CreditCardValidator creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2();
      boolean boolean0 = creditCardValidator0.isValid((String) null);
      assertFalse(boolean0);
  }
}
