

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
import org.apache.commons.validator.routines.CodeValidator;
import org.apache.commons.validator.routines.RegexValidator;
import org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit;
import org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit;
import org.apache.commons.validator.routines.checkdigit.CheckDigit;
import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit;
import org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit;
import org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit;
import org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit;
import org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CodeValidator_ESTest extends CodeValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      RegexValidator regexValidator0 = RegexValidator.RegexValidator2("Invalid Code Length = ", true);
      EAN13CheckDigit eAN13CheckDigit0 = (EAN13CheckDigit)ISBNCheckDigit.ISBN13_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator2(regexValidator0, eAN13CheckDigit0);
      boolean boolean0 = codeValidator0.isValid("Invalid Code Length = ");
      assertEquals((-1), codeValidator0.getMinLength());
      assertFalse(boolean0);
      assertEquals((-1), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("", (CheckDigit) null);
      codeValidator0.getRegexValidator();
      assertEquals((-1), codeValidator0.getMinLength());
      assertEquals((-1), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[8];
      ModulusTenCheckDigit modulusTenCheckDigit0 = new ModulusTenCheckDigit(intArray0, false, false);
      CodeValidator codeValidator0 = new CodeValidator(0, modulusTenCheckDigit0, 0, (RegexValidator) null, 0, "");
      int int0 = codeValidator0.getMinLength();
      assertEquals(0, codeValidator0.getMaxLength());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ISBN10CheckDigit iSBN10CheckDigit0 = (ISBN10CheckDigit)ISBN10CheckDigit.ISBN10_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("|nK^Q9LO0;,:i", iSBN10CheckDigit0);
      int int0 = codeValidator0.getMinLength();
      assertEquals((-1), int0);
      assertEquals((-1), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = (LuhnCheckDigit)LuhnCheckDigit.LUHN_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator1((RegexValidator) null, 2959, luhnCheckDigit0);
      int int0 = codeValidator0.getMaxLength();
      assertEquals(2959, int0);
      assertEquals(2959, codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = (LuhnCheckDigit)LuhnCheckDigit.LUHN_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator1((RegexValidator) null, 2959, luhnCheckDigit0);
      codeValidator0.getCheckDigit();
      assertEquals(2959, codeValidator0.getMaxLength());
      assertEquals(2959, codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      CodeValidator codeValidator0 = CodeValidator.CodeValidator4((String) null, (-1007), aBANumberCheckDigit0);
      assertEquals((-1007), codeValidator0.getMinLength());
      assertEquals((-1007), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      CodeValidator codeValidator0 = CodeValidator.CodeValidator1((RegexValidator) null, 0, iSBNCheckDigit0);
      int int0 = codeValidator0.getMaxLength();
      assertEquals(0, int0);
      assertEquals(0, codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      // Undeclared exception!
      try { 
        CodeValidator.CodeValidator5("Regular expression[", iSBNCheckDigit0);
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unclosed character class near index 18
         // Regular expression[
         //                   ^
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = (ISBNCheckDigit)ISBNCheckDigit.ISBN_CHECK_DIGIT;
      // Undeclared exception!
      try { 
        CodeValidator.CodeValidator4("~\"@8 m1+~XkJ)K", 4697, iSBNCheckDigit0);
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unmatched closing ')' near index 11
         // ~\"@8 m1+~XkJ)K
         //            ^
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("4<J", (CheckDigit) null);
      Object object0 = codeValidator0.validate("4<J");
      assertEquals((-1), codeValidator0.getMaxLength());
      assertNotNull(object0);
      assertEquals("", object0);
      assertEquals((-1), codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = (LuhnCheckDigit)LuhnCheckDigit.LUHN_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("", luhnCheckDigit0);
      codeValidator0.validate("");
      assertEquals((-1), codeValidator0.getMinLength());
      assertEquals((-1), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ABANumberCheckDigit aBANumberCheckDigit0 = new ABANumberCheckDigit();
      RegexValidator regexValidator0 = RegexValidator.RegexValidator2("ofA_jvDqiKl]", false);
      CodeValidator codeValidator0 = new CodeValidator(98, aBANumberCheckDigit0, 98, regexValidator0, 98, "");
      assertEquals(98, codeValidator0.getMaxLength());
      assertEquals(98, codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CodeValidator codeValidator0 = new CodeValidator(98, (CheckDigit) null, 98, (RegexValidator) null, (-153), (String) null);
      assertEquals(98, codeValidator0.getMaxLength());
      assertEquals((-153), codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      CodeValidator codeValidator0 = null;
      try {
        codeValidator0 = new CodeValidator((-4376), iSBNCheckDigit0, (-4376), (RegexValidator) null, (-4376), "9|/)@L");
        fail("Expecting exception: PatternSyntaxException");
      
      } catch(PatternSyntaxException e) {
         //
         // Unmatched closing ')' near index 2
         // 9|/)@L
         //   ^
         //
         verifyException("java.util.regex.Pattern", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      CodeValidator codeValidator0 = CodeValidator.CodeValidator4("", 0, cUSIPCheckDigit0);
      codeValidator0.validate("ofA_jvDqiKl]");
      assertEquals(0, codeValidator0.getMaxLength());
      assertEquals(0, codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      CodeValidator codeValidator0 = CodeValidator.CodeValidator4("s6i.=CxJ", 8, cUSIPCheckDigit0);
      codeValidator0.validate("s6i.=CxJ");
      assertEquals(8, codeValidator0.getMinLength());
      assertEquals(8, codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      String[] stringArray0 = new String[1];
      stringArray0[0] = "#_~uw";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, false);
      CodeValidator codeValidator0 = new CodeValidator(0, iSBNCheckDigit0, 1, regexValidator0, 0, "org.apache.commons.validator.routines.CodeValidator");
      codeValidator0.validate("org.apache.commons.validator.routines.CodeValidator");
      assertEquals(1, codeValidator0.getMaxLength());
      assertEquals(0, codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      VerhoeffCheckDigit verhoeffCheckDigit0 = new VerhoeffCheckDigit();
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("", verhoeffCheckDigit0);
      Object object0 = codeValidator0.validate("0");
      assertEquals((-1), codeValidator0.getMinLength());
      assertNotNull(object0);
      assertEquals((-1), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("%d", (CheckDigit) null);
      boolean boolean0 = codeValidator0.isValid("%d");
      assertEquals((-1), codeValidator0.getMinLength());
      assertEquals((-1), codeValidator0.getMaxLength());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      String[] stringArray0 = new String[1];
      stringArray0[0] = "#_~uw";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, false);
      CodeValidator codeValidator0 = new CodeValidator(0, iSBNCheckDigit0, 1, regexValidator0, 0, "org.apache.commons.validator.routines.CodeValidator");
      boolean boolean0 = codeValidator0.isValid("#_~uw");
      assertEquals(0, codeValidator0.getMinLength());
      assertFalse(boolean0);
      assertEquals(1, codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      LuhnCheckDigit luhnCheckDigit0 = (LuhnCheckDigit)LuhnCheckDigit.LUHN_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5((String) null, luhnCheckDigit0);
      codeValidator0.validate((String) null);
      assertEquals((-1), codeValidator0.getMaxLength());
      assertEquals((-1), codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      VerhoeffCheckDigit verhoeffCheckDigit0 = (VerhoeffCheckDigit)VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT;
      CodeValidator codeValidator0 = CodeValidator.CodeValidator4("", 3, verhoeffCheckDigit0);
      int int0 = codeValidator0.getMinLength();
      assertEquals(3, int0);
      assertEquals(3, codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      ISBNCheckDigit iSBNCheckDigit0 = new ISBNCheckDigit();
      String[] stringArray0 = new String[1];
      stringArray0[0] = "#_~uw";
      RegexValidator regexValidator0 = new RegexValidator(stringArray0, false);
      CodeValidator codeValidator0 = CodeValidator.CodeValidator1(regexValidator0, (-2353), iSBNCheckDigit0);
      assertEquals((-2353), codeValidator0.getMinLength());
      assertEquals((-2353), codeValidator0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("%d", (CheckDigit) null);
      RegexValidator regexValidator0 = codeValidator0.getRegexValidator();
      assertNotNull(regexValidator0);
      assertEquals((-1), codeValidator0.getMaxLength());
      assertEquals((-1), codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("%d", (CheckDigit) null);
      int int0 = codeValidator0.getMaxLength();
      assertEquals((-1), int0);
      assertEquals((-1), codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CodeValidator codeValidator0 = CodeValidator.CodeValidator5("", (CheckDigit) null);
      codeValidator0.getCheckDigit();
      assertEquals((-1), codeValidator0.getMaxLength());
      assertEquals((-1), codeValidator0.getMinLength());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CUSIPCheckDigit cUSIPCheckDigit0 = new CUSIPCheckDigit();
      CodeValidator codeValidator0 = CodeValidator.CodeValidator4("s=CxJ", 0, cUSIPCheckDigit0);
      Object object0 = codeValidator0.validate("s=CxJ");
      assertEquals(0, codeValidator0.getMaxLength());
      assertNull(object0);
      assertEquals(0, codeValidator0.getMinLength());
  }
}
