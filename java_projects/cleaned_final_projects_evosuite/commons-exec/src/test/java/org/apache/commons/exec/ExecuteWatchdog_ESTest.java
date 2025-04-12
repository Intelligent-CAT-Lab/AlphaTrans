
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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.time.Duration;
import java.time.temporal.ChronoField;
import java.time.temporal.TemporalUnit;
import java.util.concurrent.ThreadFactory;
import org.apache.commons.exec.ExecuteWatchdog;
import org.apache.commons.exec.Watchdog;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.lang.MockException;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ExecuteWatchdog_ESTest extends ExecuteWatchdog_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      assertNotNull(executeWatchdog_Builder0);
      
      executeWatchdog_Builder0.setTimeout((Duration) null);
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      executeWatchdog_Builder0.setThreadFactory(threadFactory0);
      ExecuteWatchdog executeWatchdog0 = ExecuteWatchdog.ExecuteWatchdog0(1L);
      MockException mockException0 = new MockException("sOk1g-c1");
      executeWatchdog0.setProcessNotStarted();
      executeWatchdog0.failedToStart(mockException0);
      executeWatchdog0.isWatching();
      boolean boolean0 = executeWatchdog0.isWatching();
      assertFalse(boolean0);
      
      Watchdog watchdog0 = mock(Watchdog.class, new ViolatedAssumptionAnswer());
      ExecuteWatchdog.builder();
      MockException mockException1 = new MockException("");
      MockException mockException2 = new MockException();
      mockException2.printStackTrace();
      executeWatchdog0.failedToStart(mockException0);
      executeWatchdog0.destroyProcess();
      assertFalse(executeWatchdog0.killedProcess());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ExecuteWatchdog.builder();
      ExecuteWatchdog executeWatchdog0 = ExecuteWatchdog.ExecuteWatchdog0(1120L);
      executeWatchdog0.cleanUp();
      assertFalse(executeWatchdog0.killedProcess());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ExecuteWatchdog executeWatchdog0 = ExecuteWatchdog.ExecuteWatchdog0(905L);
      executeWatchdog0.failedToStart((Exception) null);
      executeWatchdog0.killedProcess();
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = new ExecuteWatchdog.Builder();
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      ExecuteWatchdog.Builder executeWatchdog_Builder1 = executeWatchdog_Builder0.setThreadFactory(threadFactory0);
      // Undeclared exception!
      try { 
        executeWatchdog_Builder1.get();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      executeWatchdog_Builder0.setThreadFactory(threadFactory0);
      ExecuteWatchdog executeWatchdog0 = ExecuteWatchdog.ExecuteWatchdog0(1L);
      MockException mockException0 = new MockException("sOk1g-c1");
      MockException mockException1 = new MockException("sOk1g-c1", mockException0);
      executeWatchdog0.setProcessNotStarted();
      executeWatchdog0.failedToStart(mockException1);
      executeWatchdog0.isWatching();
      executeWatchdog0.isWatching();
      // Undeclared exception!
      try { 
        executeWatchdog0.start((Process) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // processToMonitor
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      ExecuteWatchdog.Builder executeWatchdog_Builder1 = executeWatchdog_Builder0.setTimeout((Duration) null);
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      executeWatchdog_Builder0.setThreadFactory(threadFactory0);
      ExecuteWatchdog executeWatchdog0 = ExecuteWatchdog.ExecuteWatchdog0(1L);
      MockException mockException0 = new MockException("sOk1g-c1");
      MockException mockException1 = new MockException("sOk1g-c1", mockException0);
      executeWatchdog0.setProcessNotStarted();
      executeWatchdog0.failedToStart(mockException1);
      boolean boolean0 = executeWatchdog0.killedProcess();
      boolean boolean1 = executeWatchdog0.isWatching();
      assertTrue(boolean1 == boolean0);
      
      ExecuteWatchdog.Builder executeWatchdog_Builder2 = new ExecuteWatchdog.Builder();
      ThreadFactory threadFactory1 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      executeWatchdog_Builder1.setThreadFactory(threadFactory1);
      executeWatchdog_Builder1.setTimeout(executeWatchdog0.INFINITE_TIMEOUT_DURATION);
      assertFalse(executeWatchdog0.killedProcess());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      Duration duration0 = null;
      executeWatchdog_Builder0.setTimeout((Duration) null);
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      executeWatchdog_Builder0.setThreadFactory(threadFactory0);
      ExecuteWatchdog executeWatchdog0 = ExecuteWatchdog.ExecuteWatchdog0(1L);
      MockException mockException0 = new MockException("sOk1g-c1");
      MockException mockException1 = new MockException("sOk1g-c1", mockException0);
      executeWatchdog0.setProcessNotStarted();
      executeWatchdog0.failedToStart(mockException1);
      executeWatchdog0.isWatching();
      executeWatchdog0.isWatching();
      // Undeclared exception!
      try { 
        executeWatchdog0.start((Process) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // processToMonitor
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = new ExecuteWatchdog.Builder();
      // Undeclared exception!
      try { 
        executeWatchdog_Builder0.get();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        ExecuteWatchdog.ExecuteWatchdog0(0L);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // timeout must not be less than 1.
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      // Undeclared exception!
      try { 
        executeWatchdog_Builder0.get();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = new ExecuteWatchdog.Builder();
      long long0 = (-561L);
      // Undeclared exception!
      try { 
        ExecuteWatchdog.ExecuteWatchdog0((-561L));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // timeout must not be less than 1.
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = new ExecuteWatchdog.Builder();
      Duration duration0 = Duration.ZERO;
      ChronoField chronoField0 = ChronoField.NANO_OF_SECOND;
      TemporalUnit temporalUnit0 = chronoField0.getRangeUnit();
      duration0.plus(614L, temporalUnit0);
      ExecuteWatchdog.Builder executeWatchdog_Builder1 = executeWatchdog_Builder0.setTimeout(duration0);
      assertSame(executeWatchdog_Builder0, executeWatchdog_Builder1);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      ExecuteWatchdog.Builder executeWatchdog_Builder1 = executeWatchdog_Builder0.setThreadFactory((ThreadFactory) null);
      // Undeclared exception!
      try { 
        executeWatchdog_Builder1.get();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ExecuteWatchdog.Builder executeWatchdog_Builder0 = ExecuteWatchdog.builder();
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      ExecuteWatchdog.Builder executeWatchdog_Builder1 = executeWatchdog_Builder0.setThreadFactory(threadFactory0);
      ExecuteWatchdog.Builder executeWatchdog_Builder2 = executeWatchdog_Builder1.setTimeout((Duration) null);
      ExecuteWatchdog.Builder executeWatchdog_Builder3 = executeWatchdog_Builder2.setTimeout((Duration) null);
      assertSame(executeWatchdog_Builder3, executeWatchdog_Builder1);
  }
}
