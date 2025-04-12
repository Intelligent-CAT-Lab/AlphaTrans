

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
import org.apache.commons.validator.routines.ISBNValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ISBNValidator_ESTest extends ISBNValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ISBNValidator iSBNValidator0 = new ISBNValidator(true);
      // Undeclared exception!
      try { 
        iSBNValidator0.convertToISBN13("/1b;{)/7N0 ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Check digit error for '/1b;{)/7N0' - Invalid Character[4] = '/'
         //
         verifyException("org.apache.commons.validator.routines.ISBNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.ISBNValidator1();
      // Undeclared exception!
      try { 
        iSBNValidator0.convertToISBN13("Check digit error for '");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid length 23 for 'Check digit error for ''
         //
         verifyException("org.apache.commons.validator.routines.ISBNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.getInstance0();
      String string0 = iSBNValidator0.validateISBN13(",aq2");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ISBNValidator iSBNValidator0 = new ISBNValidator(true);
      boolean boolean0 = iSBNValidator0.isValidISBN13("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ISBNValidator iSBNValidator0 = new ISBNValidator(false);
      boolean boolean0 = iSBNValidator0.isValidISBN10("`j");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.getInstance1(true);
      // Undeclared exception!
      try { 
        iSBNValidator0.convertToISBN13("' - ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid length 3 for '' -'
         //
         verifyException("org.apache.commons.validator.routines.ISBNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.getInstance1(true);
      String string0 = iSBNValidator0.validate("u;Z$EP");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.getInstance1(false);
      assertNotNull(iSBNValidator0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.getInstance1(true);
      boolean boolean0 = iSBNValidator0.isValid("L&&r7G7F J*w|M_*7");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.ISBNValidator1();
      String string0 = iSBNValidator0.validateISBN10("]$KE|h");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ISBNValidator iSBNValidator0 = ISBNValidator.getInstance0();
      String string0 = iSBNValidator0.convertToISBN13((String) null);
      assertNull(string0);
  }
}
