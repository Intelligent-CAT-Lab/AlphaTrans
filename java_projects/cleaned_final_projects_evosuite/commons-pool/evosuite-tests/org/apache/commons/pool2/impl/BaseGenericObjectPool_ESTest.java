


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
import java.time.Duration;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.concurrent.ScheduledFuture;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.impl.BaseGenericObjectPool;
import org.apache.commons.pool2.impl.DefaultEvictionPolicy;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BaseGenericObjectPool_ESTest extends BaseGenericObjectPool_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      BaseGenericObjectPool<Object> baseGenericObjectPool0 = (BaseGenericObjectPool<Object>) mock(BaseGenericObjectPool.class, CALLS_REAL_METHODS);
      BaseGenericObjectPool.Evictor baseGenericObjectPool_Evictor0 = baseGenericObjectPool0.new Evictor();
      ScheduledFuture<Object> scheduledFuture0 = (ScheduledFuture<Object>) mock(ScheduledFuture.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(scheduledFuture0).cancel(anyBoolean());
      baseGenericObjectPool_Evictor0.setScheduledFuture(scheduledFuture0);
      baseGenericObjectPool_Evictor0.cancel();
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      BaseGenericObjectPool<Duration> baseGenericObjectPool0 = (BaseGenericObjectPool<Duration>) mock(BaseGenericObjectPool.class, CALLS_REAL_METHODS);
      ArrayDeque<PooledObject<Duration>> arrayDeque0 = new ArrayDeque<PooledObject<Duration>>();
      PooledObject<Duration> pooledObject0 = (PooledObject<Duration>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(pooledObject0).toString();
      arrayDeque0.add(pooledObject0);
      BaseGenericObjectPool.EvictionIterator baseGenericObjectPool_EvictionIterator0 = baseGenericObjectPool0.new EvictionIterator(arrayDeque0);
      baseGenericObjectPool_EvictionIterator0.next();
      baseGenericObjectPool_EvictionIterator0.remove();
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Long long0 = new Long(0L);
      BaseGenericObjectPool.IdentityWrapper<Long> baseGenericObjectPool_IdentityWrapper0 = new BaseGenericObjectPool.IdentityWrapper<Long>(long0);
      BaseGenericObjectPool.IdentityWrapper<Object> baseGenericObjectPool_IdentityWrapper1 = new BaseGenericObjectPool.IdentityWrapper<Object>(baseGenericObjectPool_IdentityWrapper0);
      Object object0 = baseGenericObjectPool_IdentityWrapper1.getObject();
      boolean boolean0 = baseGenericObjectPool_IdentityWrapper0.equals(object0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DefaultEvictionPolicy<Duration> defaultEvictionPolicy0 = new DefaultEvictionPolicy<Duration>();
      BaseGenericObjectPool.IdentityWrapper<DefaultEvictionPolicy<Duration>> baseGenericObjectPool_IdentityWrapper0 = new BaseGenericObjectPool.IdentityWrapper<DefaultEvictionPolicy<Duration>>(defaultEvictionPolicy0);
      BaseGenericObjectPool.IdentityWrapper<Object> baseGenericObjectPool_IdentityWrapper1 = new BaseGenericObjectPool.IdentityWrapper<Object>(baseGenericObjectPool_IdentityWrapper0);
      boolean boolean0 = baseGenericObjectPool_IdentityWrapper1.equals(baseGenericObjectPool_IdentityWrapper0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      BaseGenericObjectPool.IdentityWrapper<Object> baseGenericObjectPool_IdentityWrapper0 = new BaseGenericObjectPool.IdentityWrapper<Object>("");
      boolean boolean0 = baseGenericObjectPool_IdentityWrapper0.equals("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      BaseGenericObjectPool<Object> baseGenericObjectPool0 = (BaseGenericObjectPool<Object>) mock(BaseGenericObjectPool.class, CALLS_REAL_METHODS);
      ArrayDeque<PooledObject<Object>> arrayDeque0 = new ArrayDeque<PooledObject<Object>>();
      BaseGenericObjectPool.EvictionIterator baseGenericObjectPool_EvictionIterator0 = baseGenericObjectPool0.new EvictionIterator(arrayDeque0);
      boolean boolean0 = baseGenericObjectPool_EvictionIterator0.hasNext();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      BaseGenericObjectPool<Object> baseGenericObjectPool0 = (BaseGenericObjectPool<Object>) mock(BaseGenericObjectPool.class, CALLS_REAL_METHODS);
      ArrayDeque<PooledObject<Object>> arrayDeque0 = new ArrayDeque<PooledObject<Object>>();
      BaseGenericObjectPool.EvictionIterator baseGenericObjectPool_EvictionIterator0 = baseGenericObjectPool0.new EvictionIterator(arrayDeque0);
      Deque<PooledObject<Object>> deque0 = baseGenericObjectPool_EvictionIterator0.getIdleObjects();
      assertEquals(0, deque0.size());
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      BaseGenericObjectPool.IdentityWrapper<Object> baseGenericObjectPool_IdentityWrapper0 = new BaseGenericObjectPool.IdentityWrapper<Object>("");
      String string0 = baseGenericObjectPool_IdentityWrapper0.toString();
      assertEquals("IdentityWrapper [instance=]", string0);
  }
}
