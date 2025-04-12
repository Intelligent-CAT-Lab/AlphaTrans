


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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.time.Duration;
import java.util.concurrent.ScheduledFuture;
import org.apache.commons.pool2.impl.BaseGenericObjectPool;
import org.apache.commons.pool2.impl.EvictionTimer;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.lang.MockThread;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class EvictionTimer_ESTest extends EvictionTimer_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      BaseGenericObjectPool<MockThread> baseGenericObjectPool0 = (BaseGenericObjectPool<MockThread>) mock(BaseGenericObjectPool.class, new ViolatedAssumptionAnswer());
      BaseGenericObjectPool.Evictor baseGenericObjectPool_Evictor0 = baseGenericObjectPool0.new Evictor();
      Duration duration0 = Duration.ofMillis(100);
      ScheduledFuture<Object> scheduledFuture0 = (ScheduledFuture<Object>) mock(ScheduledFuture.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(scheduledFuture0).cancel(anyBoolean());
      baseGenericObjectPool_Evictor0.setScheduledFuture(scheduledFuture0);
      EvictionTimer.cancel(baseGenericObjectPool_Evictor0, duration0, true);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      BaseGenericObjectPool<MockThread> baseGenericObjectPool0 = (BaseGenericObjectPool<MockThread>) mock(BaseGenericObjectPool.class, new ViolatedAssumptionAnswer());
      BaseGenericObjectPool.Evictor baseGenericObjectPool_Evictor0 = baseGenericObjectPool0.new Evictor();
      Duration duration0 = Duration.ofMillis((-1L));
      // Undeclared exception!
      try { 
        EvictionTimer.cancel(baseGenericObjectPool_Evictor0, duration0, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.BaseGenericObjectPool$Evictor", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Duration duration0 = Duration.ZERO;
      EvictionTimer.cancel((BaseGenericObjectPool.Evictor) null, duration0, false);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      int int0 = EvictionTimer.getNumTasks();
      assertEquals(0, int0);
  }
}
