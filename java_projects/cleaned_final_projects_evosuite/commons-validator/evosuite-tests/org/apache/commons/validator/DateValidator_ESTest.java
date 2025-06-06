

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
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Locale;
import org.apache.commons.validator.DateValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DateValidator_ESTest extends DateValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      boolean boolean0 = dateValidator0.isValid0("YcLj?v\"(b", "2", true);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      // Undeclared exception!
      try { 
        dateValidator0.isValid0("", "{Lm_<A!?'", false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'A'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator();
      boolean boolean0 = dateValidator0.isValid1("", (Locale) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator();
      Locale locale0 = Locale.CHINA;
      boolean boolean0 = dateValidator0.isValid1((String) null, locale0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      Locale locale0 = Locale.JAPAN;
      boolean boolean0 = dateValidator0.isValid1("2.$!W$QX1X$j", locale0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      boolean boolean0 = dateValidator0.isValid0("2.$!W$QX1X$j", "2", true);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator();
      boolean boolean0 = dateValidator0.isValid0("2", "2", false);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      boolean boolean0 = dateValidator0.isValid0("2)8~s.7G_nqk", "", true);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      boolean boolean0 = dateValidator0.isValid0("org.apache.commons.validator.DateValidator", (String) null, true);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DateValidator dateValidator0 = new DateValidator();
      boolean boolean0 = dateValidator0.isValid0((String) null, (String) null, true);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DateValidator dateValidator0 = DateValidator.getInstance();
      boolean boolean0 = dateValidator0.isValid0("2", "2", true);
      assertTrue(boolean0);
  }
}
