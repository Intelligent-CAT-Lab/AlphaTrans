/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:56:12 GMT 2024
 */

package org.apache.commons.validator.routines;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedList;
import org.apache.commons.validator.routines.DomainValidator;
import org.apache.commons.validator.routines.EmailValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class EmailValidator_ESTest extends EmailValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(true, true);
      boolean boolean0 = emailValidator0.isValidUser("(((\\.)|[^sp{Cntrl}()<>@,;:'\\\".[]]|')+|(\"(\\\"|[^\"])*\"))");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = new DomainValidator(523, linkedList0, true);
      EmailValidator emailValidator0 = new EmailValidator((-725), false, true, domainValidator0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(false, true);
      boolean boolean0 = emailValidator0.isValidUser("J");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance0();
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
  public void test04()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(true, false);
      assertNotNull(emailValidator0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator(1158, true, true, (DomainValidator) null);
      boolean boolean0 = emailValidator0.isValidUser("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(false, false);
      boolean boolean0 = emailValidator0.isValidUser("^(((\\.)|[^sp{Cntrl}()<>@,;:'\\\".[]]|')+|(\"(\\\"|[^\"])*\"))(.(((\\.)|[^sp{Cntrl}()<>@,;:'\\\".[]]|')+|(\"(\\\"|[^\"])*\")))*$");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance0();
      boolean boolean0 = emailValidator0.isValidUser((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(false, true);
      boolean boolean0 = emailValidator0.isValidDomain("barcelona");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      EmailValidator emailValidator0 = new EmailValidator(1158, true, true, (DomainValidator) null);
      boolean boolean0 = emailValidator0.isValidDomain(".-+z|Gh.=ZJ$qY5");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance0();
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

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(false, false);
      boolean boolean0 = emailValidator0.isValidDomain("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance0();
      // Undeclared exception!
      try { 
        emailValidator0.isValid("(\\.)|[^sp{Cntrl}()<>@,;:'\\\".[]]");
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
  public void test13()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance0();
      boolean boolean0 = emailValidator0.isValid("wang.");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(false, false);
      boolean boolean0 = emailValidator0.isValid("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = new DomainValidator(0, linkedList0, true);
      EmailValidator emailValidator0 = null;
      try {
        emailValidator0 = new EmailValidator(0, false, true, domainValidator0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // DomainValidator must agree with allowLocal setting
         //
         verifyException("org.apache.commons.validator.routines.EmailValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = new DomainValidator(0, linkedList0, true);
      EmailValidator emailValidator0 = new EmailValidator(0, true, true, domainValidator0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      EmailValidator emailValidator0 = null;
      try {
        emailValidator0 = new EmailValidator(0, true, false, (DomainValidator) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // DomainValidator cannot be null
         //
         verifyException("org.apache.commons.validator.routines.EmailValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(false, true);
      boolean boolean0 = emailValidator0.isValidDomain("-+z|Gh.=ZJ$qY5");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance2(true);
      assertNotNull(emailValidator0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance1(true, true);
      boolean boolean0 = emailValidator0.isValidDomain("0");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.EmailValidator0(false);
      assertNotNull(emailValidator0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      EmailValidator emailValidator0 = EmailValidator.getInstance0();
      boolean boolean0 = emailValidator0.isValid((String) null);
      assertFalse(boolean0);
  }
}