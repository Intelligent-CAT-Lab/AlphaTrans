

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
import org.apache.commons.validator.routines.InetAddressValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class InetAddressValidator_ESTest extends InetAddressValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      // Undeclared exception!
      try { 
        inetAddressValidator0.isValidInet6Address((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.InetAddressValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      // Undeclared exception!
      try { 
        inetAddressValidator0.isValid((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.InetAddressValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("E");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("-3c");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("::");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address(":");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("*?v-*/1");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet4Address("C|:UX#,.(t4K");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValid("0");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("+::t");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("::jA=$9OV$Stn.e");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("0:");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("org.pache.commons.vaidator.routines.RegexValidator:::");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("]d<I4I%~<e)D!v2{evQ");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address(":R$BE%%P.u&o>");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValid("Z]gXJR[/0");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = new InetAddressValidator();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("%)dID)\"/[?wfV}2B7");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValidInet6Address("2>Od\"/X;g/L8JO~9");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      InetAddressValidator inetAddressValidator0 = InetAddressValidator.getInstance();
      boolean boolean0 = inetAddressValidator0.isValid("::");
      assertTrue(boolean0);
  }
}
