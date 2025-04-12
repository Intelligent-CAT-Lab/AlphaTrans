


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




package org.apache.commons.pool2.impl;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.PrintWriter;
import org.apache.commons.pool2.impl.ThrowableCallStack;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockPrintWriter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ThrowableCallStack_ESTest extends ThrowableCallStack_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ThrowableCallStack throwableCallStack0 = null;
      try {
        throwableCallStack0 = new ThrowableCallStack((String) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ThrowableCallStack throwableCallStack0 = null;
      try {
        throwableCallStack0 = new ThrowableCallStack("?;6EJ3", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Illegal pattern character 'J'
         //
         verifyException("java.text.SimpleDateFormat", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ThrowableCallStack throwableCallStack0 = new ThrowableCallStack("", false);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("nv<y'|Y5`|d!F ");
      throwableCallStack0.fillInStackTrace();
      boolean boolean0 = throwableCallStack0.printStackTrace(mockPrintWriter0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ThrowableCallStack throwableCallStack0 = new ThrowableCallStack("", false);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("nv<y'|Y5`|d!F ");
      boolean boolean0 = throwableCallStack0.printStackTrace(mockPrintWriter0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ThrowableCallStack throwableCallStack0 = new ThrowableCallStack("", true);
      throwableCallStack0.fillInStackTrace();
      // Undeclared exception!
      try { 
        throwableCallStack0.printStackTrace((PrintWriter) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.ThrowableCallStack", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ThrowableCallStack throwableCallStack0 = new ThrowableCallStack("Uz*mZ5Zn$8f#H\"e +e", false);
      throwableCallStack0.clear();
  }
}
