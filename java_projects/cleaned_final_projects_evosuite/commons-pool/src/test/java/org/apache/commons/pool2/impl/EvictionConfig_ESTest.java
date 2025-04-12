


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
import java.time.temporal.ChronoUnit;
import org.apache.commons.pool2.impl.EvictionConfig;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class EvictionConfig_ESTest extends EvictionConfig_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      EvictionConfig evictionConfig0 = EvictionConfig.EvictionConfig0(0L, (-2632), 0);
      int int0 = evictionConfig0.getMinIdle();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      EvictionConfig evictionConfig0 = EvictionConfig.EvictionConfig0(5, 1371L, (-1));
      int int0 = evictionConfig0.getMinIdle();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 0);
      long long0 = evictionConfig0.getIdleSoftEvictTime();
      assertEquals(0L, long0);
      assertEquals(0, evictionConfig0.getMinIdle());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      EvictionConfig evictionConfig0 = EvictionConfig.EvictionConfig0((-3075L), 0, 0);
      long long0 = evictionConfig0.getIdleSoftEvictTime();
      assertEquals(9223372036854775807L, long0);
      assertEquals(0, evictionConfig0.getMinIdle());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      EvictionConfig evictionConfig0 = EvictionConfig.EvictionConfig0((-3075L), 0, 0);
      long long0 = evictionConfig0.getIdleEvictTime();
      assertEquals(0, evictionConfig0.getMinIdle());
      assertEquals(9223372036854775807L, long0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.ERAS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, (-14));
      // Undeclared exception!
      try { 
        evictionConfig0.getIdleEvictTime();
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // long overflow
         //
         verifyException("java.lang.Math", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 0);
      Duration duration1 = evictionConfig0.getIdleSoftEvictDuration();
      assertSame(duration1, duration0);
      assertEquals(0, evictionConfig0.getMinIdle());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 0);
      long long0 = evictionConfig0.getIdleEvictTime();
      assertEquals(0L, long0);
      assertEquals(0, evictionConfig0.getMinIdle());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 0);
      Duration duration1 = evictionConfig0.getIdleSoftEvictTimeDuration();
      assertEquals(0, evictionConfig0.getMinIdle());
      assertSame(duration1, duration0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      EvictionConfig evictionConfig0 = new EvictionConfig((Duration) null, (Duration) null, (-2632));
      Duration duration0 = evictionConfig0.getIdleEvictTimeDuration();
      assertNotNull(duration0);
      assertEquals((-2632), evictionConfig0.getMinIdle());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 0);
      Duration duration1 = evictionConfig0.getIdleEvictDuration();
      assertSame(duration1, duration0);
      assertEquals(0, evictionConfig0.getMinIdle());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 0);
      String string0 = evictionConfig0.toString();
      assertEquals("EvictionConfig [idleEvictDuration=PT0.000001S, idleSoftEvictDuration=PT0.000001S, minIdle=0]", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ChronoUnit chronoUnit0 = ChronoUnit.ERAS;
      Duration duration0 = chronoUnit0.getDuration();
      EvictionConfig evictionConfig0 = new EvictionConfig(duration0, duration0, 1);
      // Undeclared exception!
      try { 
        evictionConfig0.getIdleSoftEvictTime();
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // long overflow
         //
         verifyException("java.lang.Math", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      EvictionConfig evictionConfig0 = EvictionConfig.EvictionConfig0(14, 14, 14);
      int int0 = evictionConfig0.getMinIdle();
      assertEquals(14, int0);
  }
}
