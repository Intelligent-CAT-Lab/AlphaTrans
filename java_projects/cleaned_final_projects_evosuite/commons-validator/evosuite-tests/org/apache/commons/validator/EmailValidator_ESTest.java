

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
import org.apache.commons.validator.EmailValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class EmailValidator_ESTest extends EmailValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      String string0 = emailValidator0.stripComments("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      boolean boolean0 = emailValidator0.isValidUser("'_7K=");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.stripComments((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.isValidUser((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      emailValidator0.isValidSymbolicDomain("\"<Ja4p.bwv{&&v3$");
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      // Undeclared exception!
      try { 
        emailValidator0.isValidSymbolicDomain((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.isValidSymbolicDomain("cool");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.isValidIpAddress((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.isValidDomain((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      String string0 = emailValidator0.stripComments("u|R]lU |#8E&u`-V}[9");
      assertEquals("u|R]lU |#8E&u`-V}[9", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      // Undeclared exception!
      emailValidator0.isValidDomain("?zP-^cj.U$?rt");
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.isValidIpAddress("`l");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // No match found
         //
         verifyException("java.util.regex.Matcher", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      boolean boolean0 = emailValidator0.isValidDomain("b[]");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      // Undeclared exception!
      try { 
        emailValidator0.isValidDomain("g2");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      boolean boolean0 = emailValidator0.isValidUser("m!;\"[/YWY/!`2=?");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance();
      boolean boolean0 = emailValidator0.isValid("5#_3F.z 5");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator();
      // Undeclared exception!
      try { 
        emailValidator0.isValidDomain("[]");
       //  fail("Expecting exception: IllegalStateException");
       // Unstable assertion
      } catch(IllegalStateException e) {
         //
         // No match found
         //
         verifyException("java.util.regex.Matcher", e);
      }
  }
}
