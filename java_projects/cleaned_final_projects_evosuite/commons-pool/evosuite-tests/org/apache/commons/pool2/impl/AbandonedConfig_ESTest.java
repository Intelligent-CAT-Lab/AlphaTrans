


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
import java.io.PrintWriter;
import java.time.Duration;
import org.apache.commons.pool2.impl.AbandonedConfig;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AbandonedConfig_ESTest extends AbandonedConfig_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(1762, (AbandonedConfig) null);
      abandonedConfig0.setUseUsageTracking(true);
      boolean boolean0 = abandonedConfig0.getUseUsageTracking();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(774, (AbandonedConfig) null);
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
      
      abandonedConfig0.setRequireFullStackTrace(false);
      boolean boolean0 = abandonedConfig0.getRequireFullStackTrace();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(137, (AbandonedConfig) null);
      Duration duration0 = Duration.ofMillis(137);
      abandonedConfig0.setRemoveAbandonedTimeout0(duration0);
      abandonedConfig0.getRemoveAbandonedTimeout();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig((-2312), (AbandonedConfig) null);
      Duration duration0 = Duration.ofNanos((-2312));
      abandonedConfig0.setRemoveAbandonedTimeout0(duration0);
      abandonedConfig0.getRemoveAbandonedTimeout();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(137, (AbandonedConfig) null);
      abandonedConfig0.setRemoveAbandonedOnMaintenance(true);
      boolean boolean0 = abandonedConfig0.getRemoveAbandonedOnMaintenance();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(1, (AbandonedConfig) null);
      abandonedConfig0.setRemoveAbandonedOnBorrow(true);
      boolean boolean0 = abandonedConfig0.getRemoveAbandonedOnBorrow();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(23, (AbandonedConfig) null);
      abandonedConfig0.setLogWriter((PrintWriter) null);
      abandonedConfig0.getLogWriter();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(631, (AbandonedConfig) null);
      abandonedConfig0.setLogAbandoned(true);
      boolean boolean0 = abandonedConfig0.getLogAbandoned();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(2567, (AbandonedConfig) null);
      abandonedConfig0.setUseUsageTracking(true);
      AbandonedConfig abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0);
      assertTrue(abandonedConfig0.getUseUsageTracking());
      assertFalse(abandonedConfig1.getRemoveAbandonedOnMaintenance());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(774, (AbandonedConfig) null);
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
      
      abandonedConfig0.setRequireFullStackTrace(false);
      AbandonedConfig abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0);
      assertFalse(abandonedConfig0.getRequireFullStackTrace());
      assertFalse(abandonedConfig1.getRemoveAbandonedOnMaintenance());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(137, (AbandonedConfig) null);
      abandonedConfig0.setRemoveAbandonedOnMaintenance(true);
      AbandonedConfig.copy(abandonedConfig0);
      assertTrue(abandonedConfig0.getRemoveAbandonedOnMaintenance());
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(631, (AbandonedConfig) null);
      abandonedConfig0.setRemoveAbandonedOnBorrow(true);
      AbandonedConfig abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0);
      assertTrue(abandonedConfig0.getRemoveAbandonedOnBorrow());
      assertFalse(abandonedConfig1.getRemoveAbandonedOnMaintenance());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(631, (AbandonedConfig) null);
      abandonedConfig0.setLogAbandoned(true);
      AbandonedConfig abandonedConfig1 = AbandonedConfig.copy(abandonedConfig0);
      assertTrue(abandonedConfig0.getLogAbandoned());
      assertTrue(abandonedConfig1.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = null;
      try {
        abandonedConfig0 = new AbandonedConfig(0, (AbandonedConfig) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.AbandonedConfig", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig((-1), (AbandonedConfig) null);
      PrintWriter printWriter0 = abandonedConfig0.getLogWriter();
      abandonedConfig0.setLogWriter(printWriter0);
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig((-2737), (AbandonedConfig) null);
      Duration duration0 = abandonedConfig0.getRemoveAbandonedTimeoutDuration();
      abandonedConfig0.setRemoveAbandonedTimeout0(duration0);
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(252, (AbandonedConfig) null);
      boolean boolean0 = abandonedConfig0.getRequireFullStackTrace();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(1762, (AbandonedConfig) null);
      abandonedConfig0.getUseUsageTracking();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(1, (AbandonedConfig) null);
      abandonedConfig0.getRemoveAbandonedOnBorrow();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(631, (AbandonedConfig) null);
      abandonedConfig0.getLogAbandoned();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig((-2737), (AbandonedConfig) null);
      abandonedConfig0.getRemoveAbandonedOnMaintenance();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = AbandonedConfig.copy((AbandonedConfig) null);
      assertNull(abandonedConfig0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(23, (AbandonedConfig) null);
      abandonedConfig0.toString();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig(23, (AbandonedConfig) null);
      abandonedConfig0.getRemoveAbandonedTimeout();
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      AbandonedConfig abandonedConfig0 = new AbandonedConfig((-1098), (AbandonedConfig) null);
      abandonedConfig0.setRemoveAbandonedTimeout1((-1098));
      assertTrue(abandonedConfig0.getRequireFullStackTrace());
  }
}
