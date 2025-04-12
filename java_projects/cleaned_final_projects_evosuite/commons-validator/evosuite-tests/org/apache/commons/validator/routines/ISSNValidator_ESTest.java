

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
import org.apache.commons.validator.routines.ISSNValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ISSNValidator_ESTest extends ISSNValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ISSNValidator iSSNValidator0 = new ISSNValidator();
      // Undeclared exception!
      try { 
        iSSNValidator0.extractFromEAN13(" for '");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid length 5 for 'for ''
         //
         verifyException("org.apache.commons.validator.routines.ISSNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ISSNValidator iSSNValidator0 = ISSNValidator.getInstance();
      // Undeclared exception!
      try { 
        iSSNValidator0.convertToEAN13("R>?Vp:25SO][{uFz96", (String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Suffix must be two digits: 'null'
         //
         verifyException("org.apache.commons.validator.routines.ISSNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ISSNValidator iSSNValidator0 = ISSNValidator.getInstance();
      String string0 = iSSNValidator0.convertToEAN13("X#NFD!n", "00");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ISSNValidator iSSNValidator0 = ISSNValidator.getInstance();
      // Undeclared exception!
      try { 
        iSSNValidator0.extractFromEAN13((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.ISSNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ISSNValidator iSSNValidator0 = new ISSNValidator();
      // Undeclared exception!
      try { 
        iSSNValidator0.extractFromEAN13("E@3/HhLeRFq'%O1N[/");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid length 18 for 'E@3/HhLeRFq'%O1N[/'
         //
         verifyException("org.apache.commons.validator.routines.ISSNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ISSNValidator iSSNValidator0 = new ISSNValidator();
      // Undeclared exception!
      try { 
        iSSNValidator0.extractFromEAN13(";WlmbW'T0_cf ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Prefix must be 977 to contain an ISSN: ';WlmbW'T0_cf '
         //
         verifyException("org.apache.commons.validator.routines.ISSNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      ISSNValidator iSSNValidator0 = ISSNValidator.getInstance();
      // Undeclared exception!
      try { 
        iSSNValidator0.convertToEAN13("2UFxk<.Udl", "2UFxk<.Udl");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Suffix must be two digits: '2UFxk<.Udl'
         //
         verifyException("org.apache.commons.validator.routines.ISSNValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      ISSNValidator iSSNValidator0 = new ISSNValidator();
      Object object0 = iSSNValidator0.validateEan("T~wOJr|t9GHP");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      ISSNValidator iSSNValidator0 = new ISSNValidator();
      boolean boolean0 = iSSNValidator0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      ISSNValidator iSSNValidator0 = new ISSNValidator();
      Object object0 = iSSNValidator0.validate("DFa8n[o!mzU+B-");
      assertNull(object0);
  }
}
