
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
import java.util.concurrent.ThreadFactory;
import org.apache.commons.exec.TimeoutObserver;
import org.apache.commons.exec.Watchdog;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Watchdog_ESTest extends Watchdog_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Watchdog.Builder watchdog_Builder0 = Watchdog.builder();
      Thread thread0 = mock(Thread.class, new ViolatedAssumptionAnswer());
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      doReturn(thread0).when(threadFactory0).newThread(any(java.lang.Runnable.class));
      Watchdog.Builder watchdog_Builder1 = watchdog_Builder0.setThreadFactory(threadFactory0);
      Duration duration0 = Duration.ofNanos(412L);
      watchdog_Builder0.setTimeout(duration0);
      Watchdog watchdog0 = watchdog_Builder1.get();
      watchdog0.start();
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Watchdog.Builder watchdog_Builder0 = Watchdog.builder();
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(threadFactory0).toString();
      doReturn((Thread) null).when(threadFactory0).newThread(any(java.lang.Runnable.class));
      Watchdog.Builder watchdog_Builder1 = watchdog_Builder0.setThreadFactory(threadFactory0);
      Duration duration0 = Duration.ofMinutes(1635L);
      watchdog_Builder1.setTimeout(duration0);
      Watchdog watchdog0 = watchdog_Builder1.get();
      // Undeclared exception!
      try { 
        watchdog0.start();
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // The ThreadFactory null cound not construct a thread for 'CommonsExecWatchdog-'
         //
         verifyException("org.apache.commons.exec.ThreadUtil", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Watchdog.Builder watchdog_Builder0 = new Watchdog.Builder();
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Watchdog.Builder watchdog_Builder0 = Watchdog.builder();
      Duration duration0 = Duration.ofNanos(0L);
      Watchdog.Builder watchdog_Builder1 = watchdog_Builder0.setTimeout(duration0);
      // Undeclared exception!
      try { 
        watchdog_Builder1.get();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // timeout must not be less than 1.
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      // Undeclared exception!
      try { 
        Watchdog.Watchdog0((-1757L));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // timeout must not be less than 1.
         //
         verifyException("org.apache.commons.exec.Watchdog", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Watchdog watchdog0 = Watchdog.Watchdog0(2567L);
      // Undeclared exception!
      try { 
        watchdog0.start();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.ThreadUtil", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Watchdog watchdog0 = Watchdog.Watchdog0(2567L);
      watchdog0.stop();
      watchdog0.run();
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Watchdog watchdog0 = Watchdog.Watchdog0(2567L);
      TimeoutObserver timeoutObserver0 = mock(TimeoutObserver.class, new ViolatedAssumptionAnswer());
      watchdog0.addTimeoutObserver(timeoutObserver0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      Watchdog watchdog0 = Watchdog.Watchdog0(2L);
      TimeoutObserver timeoutObserver0 = mock(TimeoutObserver.class, new ViolatedAssumptionAnswer());
      watchdog0.removeTimeoutObserver(timeoutObserver0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      Watchdog watchdog0 = Watchdog.Watchdog0(2567L);
      watchdog0.fireTimeoutOccured();
  }
}
