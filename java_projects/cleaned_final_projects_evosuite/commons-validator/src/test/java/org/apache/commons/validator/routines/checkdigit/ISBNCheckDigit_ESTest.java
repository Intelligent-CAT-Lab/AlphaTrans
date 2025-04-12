

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
import org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ISBNCheckDigit_ESTest extends ISBNCheckDigit_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      boolean boolean0 = iSBNCheckDigit0.isValid("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      try { 
        iSBNCheckDigit0.calculate("YOmVf)F!");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid ISBN Length = 8
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      boolean boolean0 = iSBNCheckDigit0.isValid("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      boolean boolean0 = iSBNCheckDigit0.isValid("zIO8;%A5\t;");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      boolean boolean0 = iSBNCheckDigit0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      boolean boolean0 = iSBNCheckDigit0.isValid("1v#[/[\"o>v4ro");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      try { 
        iSBNCheckDigit0.calculate("org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid ISBN Length = 63
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      try { 
        iSBNCheckDigit0.calculate("oX~n>Vl[UJD");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[1] = 'o'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      try { 
        iSBNCheckDigit0.calculate("");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // ISBN Code is missing
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      try { 
        iSBNCheckDigit0.calculate("{Il^|idEG");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid Character[1] = '{'
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      try { 
        iSBNCheckDigit0.calculate((String) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // ISBN Code is missing
         //
         verifyException("org.apache.commons.validator.routines.checkdigit.CheckDigitException", e);
      }
  }
}
