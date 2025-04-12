


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
import java.time.chrono.ChronoLocalDate;
import java.time.temporal.ChronoUnit;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.impl.DefaultEvictionPolicy;
import org.apache.commons.pool2.impl.EvictionConfig;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.System;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultEvictionPolicy_ESTest extends DefaultEvictionPolicy_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DefaultEvictionPolicy<Integer> defaultEvictionPolicy0 = new DefaultEvictionPolicy<Integer>();
      ChronoUnit chronoUnit0 = ChronoUnit.NANOS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 7);
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(duration0, duration0).when(pooledObject0).getIdleDuration();
      defaultEvictionPolicy0.evict(evictionConfig0, pooledObject0, 1);
      DefaultEvictionPolicy<Object> defaultEvictionPolicy1 = new DefaultEvictionPolicy<Object>();
      DefaultEvictionPolicy<Integer> defaultEvictionPolicy2 = new DefaultEvictionPolicy<Integer>();
      ChronoUnit chronoUnit1 = ChronoUnit.MILLIS;
      Duration duration1 = chronoUnit1.getDuration();
      PooledObject<Integer> pooledObject1 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(duration1, duration0).when(pooledObject1).getIdleDuration();
      DefaultEvictionPolicy<ChronoLocalDate> defaultEvictionPolicy3 = new DefaultEvictionPolicy<ChronoLocalDate>();
      PooledObject<ChronoLocalDate> pooledObject2 = (PooledObject<ChronoLocalDate>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(duration1, duration1).when(pooledObject2).getIdleDuration();
      defaultEvictionPolicy3.evict(evictionConfig0, pooledObject2, 7);
      DefaultEvictionPolicy<Integer> defaultEvictionPolicy4 = new DefaultEvictionPolicy<Integer>();
      defaultEvictionPolicy2.evict(evictionConfig0, pooledObject1, 1);
      System.setCurrentTimeMillis(7);
      PooledObject<Integer> pooledObject3 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn((Duration) null).when(pooledObject3).getIdleDuration();
      // Undeclared exception!
      try { 
        defaultEvictionPolicy0.evict(evictionConfig0, pooledObject3, 7);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.time.Duration", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultEvictionPolicy<Integer> defaultEvictionPolicy0 = new DefaultEvictionPolicy<Integer>();
      ChronoUnit chronoUnit0 = ChronoUnit.NANOS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, (-19));
      ChronoUnit chronoUnit1 = ChronoUnit.MILLIS;
      Duration duration1 = chronoUnit1.getDuration();
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(duration1).when(pooledObject0).getIdleDuration();
      boolean boolean0 = defaultEvictionPolicy0.evict(evictionConfig0, pooledObject0, 1);
      assertTrue(boolean0);
  }
}
