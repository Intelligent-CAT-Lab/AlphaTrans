


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
import java.util.concurrent.locks.AbstractQueuedLongSynchronizer;
import java.util.concurrent.locks.Condition;
import org.apache.commons.pool2.impl.InterruptibleReentrantLock;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class InterruptibleReentrantLock_ESTest extends InterruptibleReentrantLock_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      InterruptibleReentrantLock interruptibleReentrantLock0 = new InterruptibleReentrantLock(true);
      interruptibleReentrantLock0.tryLock();
      Condition condition0 = interruptibleReentrantLock0.newCondition();
      interruptibleReentrantLock0.interruptWaiters(condition0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      InterruptibleReentrantLock interruptibleReentrantLock0 = new InterruptibleReentrantLock(true);
      // Undeclared exception!
      try { 
        interruptibleReentrantLock0.interruptWaiters((Condition) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.concurrent.locks.ReentrantLock", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      InterruptibleReentrantLock interruptibleReentrantLock0 = new InterruptibleReentrantLock(true);
      AbstractQueuedLongSynchronizer abstractQueuedLongSynchronizer0 = mock(AbstractQueuedLongSynchronizer.class, new ViolatedAssumptionAnswer());
      AbstractQueuedLongSynchronizer.ConditionObject abstractQueuedLongSynchronizer_ConditionObject0 = abstractQueuedLongSynchronizer0.new ConditionObject();
      // Undeclared exception!
      try { 
        interruptibleReentrantLock0.interruptWaiters(abstractQueuedLongSynchronizer_ConditionObject0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // not owner
         //
         verifyException("java.util.concurrent.locks.ReentrantLock", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      InterruptibleReentrantLock interruptibleReentrantLock0 = new InterruptibleReentrantLock(true);
      Condition condition0 = interruptibleReentrantLock0.newCondition();
      // Undeclared exception!
      try { 
        interruptibleReentrantLock0.interruptWaiters(condition0);
        fail("Expecting exception: IllegalMonitorStateException");
      
      } catch(IllegalMonitorStateException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject", e);
      }
  }
}
