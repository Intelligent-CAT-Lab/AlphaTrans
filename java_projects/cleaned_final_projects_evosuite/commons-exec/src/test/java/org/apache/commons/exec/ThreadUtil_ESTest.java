
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
import java.util.concurrent.ThreadFactory;
import org.apache.commons.exec.ThreadUtil;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.lang.MockThread;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ThreadUtil_ESTest extends ThreadUtil_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MockThread mockThread0 = new MockThread();
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      doReturn(mockThread0).when(threadFactory0).newThread(any(java.lang.Runnable.class));
      Thread thread0 = ThreadUtil.newThread(threadFactory0, mockThread0, ")_WKW0sj>]K|}_V2MN", false);
      assertFalse(thread0.isDaemon());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ThreadGroup threadGroup0 = mock(ThreadGroup.class, new ViolatedAssumptionAnswer());
      Thread thread0 = MockThread.currentThread();
      MockThread mockThread0 = new MockThread(threadGroup0, thread0, "('^Ey", 0L);
      // Undeclared exception!
      try { 
        ThreadUtil.newThread((ThreadFactory) null, mockThread0, "", false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.ThreadUtil", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Thread thread0 = MockThread.currentThread();
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      doReturn(thread0).when(threadFactory0).newThread(any(java.lang.Runnable.class));
      // Undeclared exception!
      try { 
        ThreadUtil.newThread(threadFactory0, (Runnable) null, "", false);
        fail("Expecting exception: IllegalThreadStateException");
      
      } catch(IllegalThreadStateException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.Thread", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      MockThread mockThread0 = new MockThread("RFtE_YF");
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(threadFactory0).toString();
      doReturn((Thread) null).when(threadFactory0).newThread(any(java.lang.Runnable.class));
      // Undeclared exception!
      try { 
        ThreadUtil.newThread(threadFactory0, mockThread0, "", true);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // The ThreadFactory null cound not construct a thread for ''
         //
         verifyException("org.apache.commons.exec.ThreadUtil", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      MockThread mockThread0 = new MockThread("RFtE_YF");
      ThreadFactory threadFactory0 = mock(ThreadFactory.class, new ViolatedAssumptionAnswer());
      doReturn(mockThread0).when(threadFactory0).newThread(any(java.lang.Runnable.class));
      Thread thread0 = ThreadUtil.newThread(threadFactory0, (Runnable) null, (String) null, true);
      assertTrue(thread0.isDaemon());
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ThreadUtil threadUtil0 = new ThreadUtil();
  }
}
