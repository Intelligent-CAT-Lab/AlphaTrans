
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


package org.apache.commons.exec;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.time.Duration;
import org.apache.commons.exec.DefaultExecuteResultHandler;
import org.apache.commons.exec.ExecuteException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultExecuteResultHandler_ESTest extends DefaultExecuteResultHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      defaultExecuteResultHandler0.waitFor2((-1580L));
      assertFalse(defaultExecuteResultHandler0.hasResult());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      MockThrowable mockThrowable0 = new MockThrowable("");
      ExecuteException executeException0 = new ExecuteException((String) null, 3852, mockThrowable0);
      defaultExecuteResultHandler0.onProcessFailed(executeException0);
      boolean boolean0 = defaultExecuteResultHandler0.hasResult();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      assertFalse(defaultExecuteResultHandler0.hasResult());
      
      defaultExecuteResultHandler0.onProcessComplete(0);
      int int0 = defaultExecuteResultHandler0.getExitValue();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      assertFalse(defaultExecuteResultHandler0.hasResult());
      
      defaultExecuteResultHandler0.onProcessComplete(3256);
      int int0 = defaultExecuteResultHandler0.getExitValue();
      assertEquals(3256, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      MockThrowable mockThrowable0 = new MockThrowable("*sQi");
      ExecuteException executeException0 = new ExecuteException("*sQi", 0, mockThrowable0);
      defaultExecuteResultHandler0.onProcessFailed(executeException0);
      ExecuteException executeException1 = defaultExecuteResultHandler0.getException();
      assertSame(executeException1, executeException0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      // Undeclared exception!
      try { 
        defaultExecuteResultHandler0.waitFor1((Duration) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.time.Instant", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      boolean boolean0 = defaultExecuteResultHandler0.hasResult();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      defaultExecuteResultHandler0.onProcessComplete((-1));
      defaultExecuteResultHandler0.waitFor2((-1000000000L));
      assertTrue(defaultExecuteResultHandler0.hasResult());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      Duration duration0 = Duration.ofSeconds((-2095L));
      defaultExecuteResultHandler0.waitFor1(duration0);
      assertFalse(defaultExecuteResultHandler0.hasResult());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      defaultExecuteResultHandler0.onProcessComplete((-1));
      Duration duration0 = Duration.ofSeconds((long) (-1));
      defaultExecuteResultHandler0.waitFor1(duration0);
      assertTrue(defaultExecuteResultHandler0.hasResult());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      defaultExecuteResultHandler0.onProcessComplete((-1));
      defaultExecuteResultHandler0.waitFor0();
      assertTrue(defaultExecuteResultHandler0.hasResult());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      // Undeclared exception!
      try { 
        defaultExecuteResultHandler0.getExitValue();
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // The process has not exited yet therefore no result is available ...
         //
         verifyException("org.apache.commons.exec.DefaultExecuteResultHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      assertFalse(defaultExecuteResultHandler0.hasResult());
      
      defaultExecuteResultHandler0.onProcessComplete((-1));
      int int0 = defaultExecuteResultHandler0.getExitValue();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      // Undeclared exception!
      try { 
        defaultExecuteResultHandler0.getException();
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // The process has not exited yet therefore no result is available ...
         //
         verifyException("org.apache.commons.exec.DefaultExecuteResultHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      defaultExecuteResultHandler0.onProcessComplete((-1));
      ExecuteException executeException0 = defaultExecuteResultHandler0.getException();
      assertNull(executeException0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      MockThrowable mockThrowable0 = new MockThrowable("");
      ExecuteException executeException0 = new ExecuteException("", 1888, mockThrowable0);
      defaultExecuteResultHandler0.onProcessFailed(executeException0);
      ExecuteException executeException1 = defaultExecuteResultHandler0.getException();
      assertSame(executeException1, executeException0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DefaultExecuteResultHandler defaultExecuteResultHandler0 = new DefaultExecuteResultHandler();
      defaultExecuteResultHandler0.waitFor2(0L);
      assertFalse(defaultExecuteResultHandler0.hasResult());
  }
}
