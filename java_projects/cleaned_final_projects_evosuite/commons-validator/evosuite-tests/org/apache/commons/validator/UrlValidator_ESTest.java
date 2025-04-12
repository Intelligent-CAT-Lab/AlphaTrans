

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
import org.apache.commons.validator.UrlValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class UrlValidator_ESTest extends UrlValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator1(4);
      boolean boolean0 = urlValidator0.isValidFragment("C.)PG+(ux2DgJjGym(");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      UrlValidator urlValidator0 = new UrlValidator((String[]) null, 697);
      int int0 = urlValidator0.countToken("cG$", "q\u00078#Yzdzx");
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      // Undeclared exception!
      urlValidator0.countToken("", "");
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      // Undeclared exception!
      try { 
        urlValidator0.countToken((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator2((String[]) null);
      assertEquals(2, UrlValidator.ALLOW_2_SLASHES);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      UrlValidator urlValidator0 = new UrlValidator((String[]) null, 0);
      int int0 = urlValidator0.countToken("N`:C", "N`:C");
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      UrlValidator urlValidator0 = new UrlValidator((String[]) null, 0);
      boolean boolean0 = urlValidator0.isValidFragment((String) null);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValidQuery((String) null);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UrlValidator urlValidator0 = new UrlValidator((String[]) null, 0);
      boolean boolean0 = urlValidator0.isValidQuery("LpnAp+Bwe");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String[] stringArray0 = new String[1];
      UrlValidator urlValidator0 = new UrlValidator(stringArray0, (-2372));
      boolean boolean0 = urlValidator0.isValidPath("xn--e1a4c");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValidPath((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValidPath("");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValidAuthority((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      // Undeclared exception!
      try { 
        urlValidator0.isValidAuthority("");
       //  fail("Expecting exception: IllegalStateException");
       // Unstable assertion
      } catch(IllegalStateException e) {
         //
         // No match found
         //
         verifyException("java.util.regex.Matcher", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "xn--e1a4c";
      UrlValidator urlValidator0 = new UrlValidator(stringArray0, (-2372));
      boolean boolean0 = urlValidator0.isValidScheme("xn--e1a4c");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator1(1);
      boolean boolean0 = urlValidator0.isValidScheme("xn--e1a4c");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      String[] stringArray0 = new String[1];
      UrlValidator urlValidator0 = new UrlValidator(stringArray0, (-2372));
      boolean boolean0 = urlValidator0.isValidScheme("`:");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValidScheme((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValid("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      boolean boolean0 = urlValidator0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      String[] stringArray0 = new String[1];
      UrlValidator urlValidator0 = new UrlValidator(stringArray0, (-2372));
      boolean boolean0 = urlValidator0.isValidScheme("xn--e1a4c");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator3();
      // Undeclared exception!
      try { 
        urlValidator0.isValid("bh");
       //  fail("Expecting exception: IllegalStateException");
       // Unstable assertion
      } catch(IllegalStateException e) {
         //
         // No match found
         //
         verifyException("java.util.regex.Matcher", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      UrlValidator urlValidator0 = UrlValidator.UrlValidator1((-9));
      boolean boolean0 = urlValidator0.isValidPath("");
      assertTrue(boolean0);
  }
}
