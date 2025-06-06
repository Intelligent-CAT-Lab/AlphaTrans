


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
import java.time.chrono.ChronoLocalDate;
import java.time.temporal.ChronoUnit;
import org.apache.commons.pool2.impl.DefaultEvictionPolicy;
import org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig;
import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BaseObjectPoolConfig_ESTest extends BaseObjectPoolConfig_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      
      genericObjectPoolConfig0.setTestOnBorrow(true);
      genericObjectPoolConfig0.toString();
      assertTrue(genericObjectPoolConfig0.getTestOnBorrow());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setTestOnCreate(true);
      genericObjectPoolConfig0.toString();
      assertTrue(genericObjectPoolConfig0.getTestOnCreate());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      
      genericObjectPoolConfig0.setEvictionPolicyClassName(", testOnCreate=");
      genericObjectPoolConfig0.toString();
      assertEquals(", testOnCreate=", genericObjectPoolConfig0.getEvictionPolicyClassName());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      
      genericObjectPoolConfig0.setNumTestsPerEvictionRun(0);
      genericObjectPoolConfig0.toString();
      assertEquals(0, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setSoftMinEvictableIdleTime(genericKeyedObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
      String string0 = genericObjectPoolConfig0.toString();
      assertEquals("GenericObjectPoolConfig [lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT30M, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0]", string0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMinEvictableIdleTimeMillis(995L);
      StringBuilder stringBuilder0 = new StringBuilder();
      genericKeyedObjectPoolConfig0.toStringAppendFields(stringBuilder0);
      assertEquals("lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT0.995S, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, minIdlePerKey=0, maxIdlePerKey=8, maxTotalPerKey=8, maxTotal=-1", stringBuilder0.toString());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setMaxWait(genericObjectPoolConfig0.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT);
      String string0 = genericObjectPoolConfig0.toString();
      assertEquals("GenericObjectPoolConfig [lifo=true, fairness=false, maxWaitDuration=PT10S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0]", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Integer>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Integer>>();
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      
      genericKeyedObjectPoolConfig0.setFairness(true);
      genericKeyedObjectPoolConfig0.toString();
      assertTrue(genericKeyedObjectPoolConfig0.getFairness());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      genericObjectPoolConfig0.setLifo(false);
      genericObjectPoolConfig0.toString();
      assertFalse(genericObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setTestOnReturn(false);
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setTestOnCreate(false);
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setLifo(true);
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.setEvictorShutdownTimeoutMillis0((Duration) null);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setTimeBetweenEvictionRunsMillis((-1L));
      genericKeyedObjectPoolConfig0.getTimeBetweenEvictionRuns();
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      genericObjectPoolConfig0.setSoftMinEvictableIdleTimeMillis(9223372036854775807L);
      genericObjectPoolConfig0.getSoftMinEvictableIdleTime();
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setSoftMinEvictableIdleTimeMillis(0L);
      genericKeyedObjectPoolConfig0.getSoftMinEvictableIdleDuration();
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMinEvictableIdleTime(genericKeyedObjectPoolConfig0.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT);
      genericKeyedObjectPoolConfig0.getMinEvictableIdleTime();
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      GenericObjectPoolConfig<DefaultEvictionPolicy<Object>> genericObjectPoolConfig0 = new GenericObjectPoolConfig<DefaultEvictionPolicy<Object>>();
      GenericObjectPoolConfig<Object> genericObjectPoolConfig1 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig1.setMinEvictableIdleTime(genericObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
      genericObjectPoolConfig1.getMinEvictableIdleDuration();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig1.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig1.getBlockWhenExhausted());
      assertTrue(genericObjectPoolConfig1.getJmxEnabled());
      assertFalse(genericObjectPoolConfig1.getFairness());
      assertEquals(3, genericObjectPoolConfig1.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig1.getLifo());
      assertFalse(genericObjectPoolConfig1.getTestOnCreate());
      assertFalse(genericObjectPoolConfig1.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig1.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig1.getTestOnReturn());
      assertFalse(genericObjectPoolConfig1.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setEvictorShutdownTimeoutMillis1((-1L));
      genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutDuration();
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      genericObjectPoolConfig0.setEvictorShutdownTimeoutMillis1(2488L);
      genericObjectPoolConfig0.getEvictorShutdownTimeout();
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      StringBuilder stringBuilder0 = new StringBuilder();
      genericObjectPoolConfig0.toStringAppendFields(stringBuilder0);
      assertEquals("lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, maxTotal=8, maxIdle=8, minIdle=0", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setTimeBetweenEvictionRunsMillis(0);
      long long0 = genericObjectPoolConfig0.getTimeBetweenEvictionRunsMillis();
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(0L, long0);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setTimeBetweenEvictionRunsMillis(187L);
      long long0 = genericObjectPoolConfig0.getTimeBetweenEvictionRunsMillis();
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(187L, long0);
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      
      genericObjectPoolConfig0.setTestWhileIdle(true);
      boolean boolean0 = genericObjectPoolConfig0.getTestWhileIdle();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      
      genericKeyedObjectPoolConfig0.setTestOnReturn(true);
      boolean boolean0 = genericKeyedObjectPoolConfig0.getTestOnReturn();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      
      genericObjectPoolConfig0.setTestOnBorrow(true);
      boolean boolean0 = genericObjectPoolConfig0.getTestOnBorrow();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      ChronoUnit chronoUnit0 = ChronoUnit.MICROS;
      Duration duration0 = Duration.of((-1), chronoUnit0);
      genericObjectPoolConfig0.setSoftMinEvictableIdleTime(duration0);
      long long0 = genericObjectPoolConfig0.getSoftMinEvictableIdleTimeMillis();
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals(0L, long0);
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setSoftMinEvictableIdleTime(genericKeyedObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
      long long0 = genericObjectPoolConfig0.getSoftMinEvictableIdleTimeMillis();
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals(1800000L, long0);
      assertTrue(genericObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setMaxWait(genericObjectPoolConfig0.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT);
      long long0 = genericObjectPoolConfig0.getMaxWaitMillis();
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals(10000L, long0);
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      
      genericKeyedObjectPoolConfig0.setLifo(false);
      boolean boolean0 = genericKeyedObjectPoolConfig0.getLifo();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      
      genericObjectPoolConfig0.setJmxNamePrefix((String) null);
      String string0 = genericObjectPoolConfig0.getJmxNamePrefix();
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      
      genericKeyedObjectPoolConfig0.setJmxNamePrefix("");
      String string0 = genericKeyedObjectPoolConfig0.getJmxNamePrefix();
      assertEquals("", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setJmxNameBase("%&]X");
      String string0 = genericKeyedObjectPoolConfig0.getJmxNameBase();
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals("%&]X", genericKeyedObjectPoolConfig0.getJmxNameBase());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      
      genericObjectPoolConfig0.setJmxEnabled(false);
      boolean boolean0 = genericObjectPoolConfig0.getJmxEnabled();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertFalse(genericObjectPoolConfig0.getFairness());
      
      genericObjectPoolConfig0.setFairness(true);
      boolean boolean0 = genericObjectPoolConfig0.getFairness();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setEvictorShutdownTimeout(genericObjectPoolConfig0.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME);
      long long0 = genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutMillis();
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals((-1L), long0);
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      
      genericObjectPoolConfig0.setEvictionPolicyClassName("");
      String string0 = genericObjectPoolConfig0.getEvictionPolicyClassName();
      assertNotNull(string0);
      assertEquals("", genericObjectPoolConfig0.getEvictionPolicyClassName());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      DefaultEvictionPolicy<Object> defaultEvictionPolicy0 = new DefaultEvictionPolicy<Object>();
      genericKeyedObjectPoolConfig0.setEvictionPolicy(defaultEvictionPolicy0);
      genericKeyedObjectPoolConfig0.getEvictionPolicy();
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      
      genericObjectPoolConfig0.setBlockWhenExhausted(false);
      boolean boolean0 = genericObjectPoolConfig0.getBlockWhenExhausted();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      // Undeclared exception!
      try { 
        genericObjectPoolConfig0.toStringAppendFields((StringBuilder) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.BaseObjectPoolConfig", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.setTimeBetweenEvictionRuns(genericKeyedObjectPoolConfig0.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME);
      genericObjectPoolConfig0.getDurationBetweenEvictionRuns();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      long long0 = genericObjectPoolConfig0.getTimeBetweenEvictionRunsMillis();
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals((-1L), long0);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.setJmxNameBase("");
      String string0 = genericObjectPoolConfig0.getJmxNameBase();
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertEquals("", genericObjectPoolConfig0.getJmxNameBase());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertNotNull(string0);
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      
      genericKeyedObjectPoolConfig0.setNumTestsPerEvictionRun(0);
      int int0 = genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      genericObjectPoolConfig0.setMinEvictableIdleTime(genericObjectPoolConfig0.DEFAULT_MAX_WAIT);
      long long0 = genericObjectPoolConfig0.getMinEvictableIdleTimeMillis();
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals((-1L), long0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Integer>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Integer>>();
      String string0 = genericKeyedObjectPoolConfig0.getJmxNamePrefix();
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertNotNull(string0);
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", string0);
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.getMinEvictableIdleDuration();
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.getMaxWaitDuration();
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      
      genericObjectPoolConfig0.setEvictionPolicyClassName((String) null);
      String string0 = genericObjectPoolConfig0.getEvictionPolicyClassName();
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertNull(string0);
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      String string0 = genericObjectPoolConfig0.getJmxNameBase();
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertNull(string0);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      boolean boolean0 = genericObjectPoolConfig0.getTestWhileIdle();
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(boolean0);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.getEvictionPolicy();
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setJmxEnabled(true);
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setEvictorShutdownTimeoutMillis1(0);
      long long0 = genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutMillis();
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(0L, long0);
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      boolean boolean0 = genericKeyedObjectPoolConfig0.getTestOnReturn();
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(boolean0);
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Integer>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Integer>>();
      genericKeyedObjectPoolConfig0.setFairness(false);
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      long long0 = genericKeyedObjectPoolConfig0.getSoftMinEvictableIdleTimeMillis();
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals((-1L), long0);
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      boolean boolean0 = genericObjectPoolConfig0.getTestOnCreate();
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(boolean0);
      assertTrue(genericObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      genericObjectPoolConfig0.setBlockWhenExhausted(true);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.setMaxWaitMillis(0L);
      long long0 = genericObjectPoolConfig0.getMaxWaitMillis();
      assertEquals(0L, long0);
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      boolean boolean0 = genericObjectPoolConfig0.getFairness();
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(boolean0);
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Object>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Object>>();
      genericKeyedObjectPoolConfig0.setTestWhileIdle(false);
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      boolean boolean0 = genericObjectPoolConfig0.getTestOnBorrow();
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(boolean0);
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      boolean boolean0 = genericObjectPoolConfig0.getJmxEnabled();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(boolean0);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.setTestOnBorrow(false);
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      genericObjectPoolConfig0.setMaxWait(genericObjectPoolConfig0.DEFAULT_MIN_EVICTABLE_IDLE_DURATION);
      genericObjectPoolConfig0.getMaxWaitDuration();
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      long long0 = genericKeyedObjectPoolConfig0.getEvictorShutdownTimeoutMillis();
      assertEquals(10000L, long0);
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      GenericObjectPoolConfig<Integer> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Integer>();
      String string0 = genericObjectPoolConfig0.getEvictionPolicyClassName();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", string0);
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertNotNull(string0);
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericObjectPoolConfig0.getFairness());
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.getMinEvictableIdleTime();
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      boolean boolean0 = genericKeyedObjectPoolConfig0.getLifo();
      assertEquals(3, genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertTrue(boolean0);
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      long long0 = genericObjectPoolConfig0.getMinEvictableIdleTimeMillis();
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertEquals(1800000L, long0);
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      long long0 = genericObjectPoolConfig0.getMaxWaitMillis();
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertEquals((-1L), long0);
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      GenericObjectPoolConfig<ChronoLocalDate> genericObjectPoolConfig0 = new GenericObjectPoolConfig<ChronoLocalDate>();
      genericObjectPoolConfig0.getDurationBetweenEvictionRuns();
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
      assertTrue(genericObjectPoolConfig0.getBlockWhenExhausted());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertTrue(genericObjectPoolConfig0.getLifo());
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Object>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Object>>();
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      
      genericKeyedObjectPoolConfig0.setTestOnCreate(true);
      boolean boolean0 = genericKeyedObjectPoolConfig0.getTestOnCreate();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Object>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<DefaultEvictionPolicy<Object>>();
      int int0 = genericKeyedObjectPoolConfig0.getNumTestsPerEvictionRun();
      assertFalse(genericKeyedObjectPoolConfig0.getTestWhileIdle());
      assertFalse(genericKeyedObjectPoolConfig0.getFairness());
      assertTrue(genericKeyedObjectPoolConfig0.getBlockWhenExhausted());
      assertTrue(genericKeyedObjectPoolConfig0.getJmxEnabled());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericKeyedObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnCreate());
      assertEquals("pool", genericKeyedObjectPoolConfig0.getJmxNamePrefix());
      assertTrue(genericKeyedObjectPoolConfig0.getLifo());
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnBorrow());
      assertEquals(3, int0);
      assertFalse(genericKeyedObjectPoolConfig0.getTestOnReturn());
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      GenericObjectPoolConfig<Object> genericObjectPoolConfig0 = new GenericObjectPoolConfig<Object>();
      boolean boolean0 = genericObjectPoolConfig0.getBlockWhenExhausted();
      assertFalse(genericObjectPoolConfig0.getTestOnBorrow());
      assertEquals("pool", genericObjectPoolConfig0.getJmxNamePrefix());
      assertFalse(genericObjectPoolConfig0.getTestOnCreate());
      assertEquals("org.apache.commons.pool2.impl.DefaultEvictionPolicy", genericObjectPoolConfig0.getEvictionPolicyClassName());
      assertFalse(genericObjectPoolConfig0.getFairness());
      assertTrue(genericObjectPoolConfig0.getJmxEnabled());
      assertTrue(boolean0);
      assertTrue(genericObjectPoolConfig0.getLifo());
      assertEquals(3, genericObjectPoolConfig0.getNumTestsPerEvictionRun());
      assertFalse(genericObjectPoolConfig0.getTestOnReturn());
      assertFalse(genericObjectPoolConfig0.getTestWhileIdle());
  }
}
