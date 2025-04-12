


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
import java.time.Duration;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.concurrent.TimeUnit;
import org.apache.commons.pool2.PooledObjectFactory;
import org.apache.commons.pool2.impl.PoolImplUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.time.MockInstant;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PoolImplUtils_ESTest extends PoolImplUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.FOREVER;
      Duration duration0 = chronoUnit0.getDuration();
      Duration duration1 = Duration.ofSeconds((-1069L));
      Duration duration2 = PoolImplUtils.nonNull(duration1, duration0);
      assertSame(duration2, duration1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(1022L);
      Instant instant1 = MockInstant.minusSeconds(instant0, (-700L));
      Instant instant2 = PoolImplUtils.min(instant1, instant0);
      assertNotSame(instant2, instant1);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(1022L);
      Instant instant1 = MockInstant.minusSeconds(instant0, (-700L));
      Instant instant2 = PoolImplUtils.max(instant0, instant1);
      assertSame(instant2, instant1);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        PoolImplUtils.toDuration(1555L, (TimeUnit) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        PoolImplUtils.toChronoUnit((TimeUnit) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        PoolImplUtils.nonNull((Duration) null, (Duration) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // defaultValue
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        PoolImplUtils.min((Instant) null, (Instant) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.mock.java.time.MockInstant", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        PoolImplUtils.max((Instant) null, (Instant) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.mock.java.time.MockInstant", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Class<?> class0 = PoolImplUtils.getFactoryType((Class<? extends PooledObjectFactory>) null);
      assertNull(class0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.MINUTES;
      Duration duration0 = PoolImplUtils.toDuration((-700L), timeUnit0);
      Duration duration1 = PoolImplUtils.nonNull(duration0, duration0);
      assertSame(duration0, duration1);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Duration duration0 = Duration.ofDays(0L);
      Duration duration1 = PoolImplUtils.nonNull((Duration) null, duration0);
      assertSame(duration1, duration0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.DAYS;
      ChronoUnit chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0);
      assertEquals(ChronoUnit.DAYS, chronoUnit0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.HOURS;
      Duration duration0 = PoolImplUtils.toDuration((-1069L), timeUnit0);
      assertNotNull(duration0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.SECONDS;
      Duration duration0 = PoolImplUtils.toDuration((-982L), timeUnit0);
      assertNotNull(duration0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.MILLISECONDS;
      ChronoUnit chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0);
      assertEquals(ChronoUnit.MILLIS, chronoUnit0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.MICROSECONDS;
      ChronoUnit chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0);
      assertEquals(ChronoUnit.MICROS, chronoUnit0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.NANOSECONDS;
      ChronoUnit chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0);
      assertEquals(ChronoUnit.NANOS, chronoUnit0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(1022L);
      Instant instant1 = MockInstant.minusSeconds(instant0, 1022L);
      Instant instant2 = PoolImplUtils.min(instant1, instant0);
      assertSame(instant2, instant1);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(1022L);
      Instant instant1 = PoolImplUtils.min(instant0, instant0);
      assertSame(instant1, instant0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochMilli(1L);
      Instant instant1 = MockInstant.plusMillis(instant0, 1L);
      Instant instant2 = PoolImplUtils.max(instant1, instant0);
      assertNotSame(instant2, instant0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(1022L);
      Instant instant1 = PoolImplUtils.max(instant0, instant0);
      assertSame(instant0, instant1);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Duration duration0 = Duration.ofMillis(0L);
      boolean boolean0 = PoolImplUtils.isPositive(duration0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Duration duration0 = Duration.ofHours(1001L);
      boolean boolean0 = PoolImplUtils.isPositive(duration0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      boolean boolean0 = PoolImplUtils.isPositive((Duration) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Class<PooledObjectFactory> class0 = PooledObjectFactory.class;
      Class<?> class1 = PoolImplUtils.getFactoryType(class0);
      assertNull(class1);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      PoolImplUtils poolImplUtils0 = new PoolImplUtils();
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      TimeUnit timeUnit0 = TimeUnit.MINUTES;
      Duration duration0 = PoolImplUtils.toDuration((-700L), timeUnit0);
      boolean boolean0 = PoolImplUtils.isPositive(duration0);
      assertFalse(boolean0);
  }
}
