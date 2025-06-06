

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
import java.util.regex.PatternSyntaxException;
import org.apache.commons.validator.routines.RegexValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class RegexValidator_ESTest extends RegexValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      RegexValidator regexValidator0 = RegexValidator.RegexValidator2(",", true);
      assertNotNull(regexValidator0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        RegexValidator.RegexValidator3("#ygk8#)0Ge.");
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unmatched closing ')' near index 5
         // #ygk8#)0Ge.
         //      ^
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        RegexValidator.RegexValidator2("", false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expression[0] is missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "C)";
      // Undeclared exception!
      try { 
        RegexValidator.RegexValidator1(stringArray0);
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unmatched closing ')' near index 0
         // C)
         // ^
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "(vcjCCBL";
      RegexValidator regexValidator0 = null;
      try {
        regexValidator0 = new RegexValidator(stringArray0, false);
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unclosed group near index 9
         // (vcjCCBL
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "] is missing";
      stringArray0[1] = "";
      RegexValidator regexValidator0 = null;
      try {
        regexValidator0 = new RegexValidator(stringArray0, false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expression[1] is missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      String[] stringArray0 = new String[1];
      RegexValidator regexValidator0 = null;
      try {
        regexValidator0 = new RegexValidator(stringArray0, false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expression[0] is missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      RegexValidator regexValidator0 = null;
      try {
        regexValidator0 = new RegexValidator((String[]) null, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expressions are missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      String[] stringArray0 = new String[0];
      RegexValidator regexValidator0 = null;
      try {
        regexValidator0 = new RegexValidator(stringArray0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expressions are missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "-Ei\"GMfjnI~b2X;,";
      stringArray0[1] = "-Ei\"GMfjnI~b2X;,";
      RegexValidator regexValidator0 = RegexValidator.RegexValidator1(stringArray0);
      String string0 = regexValidator0.toString();
      assertEquals("RegexValidator{-Ei\"GMfjnI~b2X;,,-Ei\"GMfjnI~b2X;,}", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      RegexValidator regexValidator0 = RegexValidator.RegexValidator3("F+6kta]M");
      String string0 = regexValidator0.validate("F+6kta]M");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      RegexValidator regexValidator0 = RegexValidator.RegexValidator3(",");
      String string0 = regexValidator0.validate((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "5<o;P~aV;";
      stringArray0[1] = "D9Ak13,T7ZX";
      stringArray0[2] = "RtvW";
      stringArray0[3] = "jQ/JY'Xg~_w]4< ";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, true);
      String string0 = regexValidator0.validate("D9Ak13,T7ZX");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "lr@6&yw^jRv";
      stringArray0[1] = "X#PPioi<bK<Gg_]_v";
      stringArray0[2] = "3";
      stringArray0[3] = "-Ei\"GMfjnI~b2X;,";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, true);
      String[] stringArray1 = regexValidator0.match("-Ei\"GMfjnI~b2X;,");
      assertNotNull(stringArray1);
      assertEquals(0, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      RegexValidator regexValidator0 = RegexValidator.RegexValidator3("-Ei\"GMfjnI~b2X;,");
      String[] stringArray0 = regexValidator0.match((String) null);
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "5<o;P~aV;";
      stringArray0[1] = "D9Ak13,T7ZX";
      stringArray0[2] = "RtvW";
      stringArray0[3] = "jQ/JY'Xg~_w]4< ";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, true);
      String[] stringArray1 = regexValidator0.match("iCc");
      assertNull(stringArray1);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      RegexValidator regexValidator0 = RegexValidator.RegexValidator3("-Ei\"GMfjnI~b2X;,");
      boolean boolean0 = regexValidator0.isValid("-Ei\"GMfjnI~b2X;,");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "5<o;P~aV;";
      stringArray0[1] = "D9Ak13,T7ZX";
      stringArray0[2] = "RtvW";
      stringArray0[3] = "jQ/JY'Xg~_w]4< ";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, true);
      boolean boolean0 = regexValidator0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[4];
      stringArray0[0] = "5<o;P~aV;";
      stringArray0[1] = "D9Ak13,T7ZX";
      stringArray0[2] = "RtvW";
      stringArray0[3] = "jQ/JY'Xg~_w]4< ";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, true);
      boolean boolean0 = regexValidator0.isValid("Regular expression[");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        RegexValidator.RegexValidator3("");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expression[0] is missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      // Undeclared exception!
      try { 
        RegexValidator.RegexValidator2("(vcjCCBL", false);
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unclosed group near index 9
         // (vcjCCBL
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      String[] stringArray0 = new String[0];
      // Undeclared exception!
      try { 
        RegexValidator.RegexValidator1(stringArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Regular expressions are missing
         //
         verifyException("org.apache.commons.validator.routines.RegexValidator", e);
      }
  }
}
