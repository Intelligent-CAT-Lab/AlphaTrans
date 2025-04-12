


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
import org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class GenericKeyedObjectPoolConfig_ESTest extends GenericKeyedObjectPoolConfig_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setMaxTotal(8);
      genericKeyedObjectPoolConfig0.toString();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotal());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
      
      genericKeyedObjectPoolConfig0.setMaxTotalPerKey(0);
      genericKeyedObjectPoolConfig0.toString();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMaxIdlePerKey((-196));
      StringBuilder stringBuilder0 = new StringBuilder();
      genericKeyedObjectPoolConfig0.toStringAppendFields(stringBuilder0);
      assertEquals("lifo=true, fairness=false, maxWaitDuration=PT-0.001S, minEvictableIdleTime=PT30M, softMinEvictableIdleTime=PT-0.001S, numTestsPerEvictionRun=3, evictionPolicyClassName=org.apache.commons.pool2.impl.DefaultEvictionPolicy, testOnCreate=false, testOnBorrow=false, testOnReturn=false, testWhileIdle=false, timeBetweenEvictionRuns=PT-0.001S, blockWhenExhausted=true, jmxEnabled=true, jmxNamePrefix=pool, jmxNameBase=null, minIdlePerKey=0, maxIdlePerKey=-196, maxTotalPerKey=8, maxTotal=-1", stringBuilder0.toString());
      assertEquals((-196), genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMinIdlePerKey((-1));
      genericKeyedObjectPoolConfig0.toString();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMinIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey());
      
      genericKeyedObjectPoolConfig0.setMinIdlePerKey(8);
      int int0 = genericKeyedObjectPoolConfig0.getMinIdlePerKey();
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey());
      
      genericKeyedObjectPoolConfig0.setMinIdlePerKey((-1));
      int int0 = genericKeyedObjectPoolConfig0.getMinIdlePerKey();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
      
      genericKeyedObjectPoolConfig0.setMaxTotalPerKey(0);
      int int0 = genericKeyedObjectPoolConfig0.getMaxTotalPerKey();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      GenericKeyedObjectPoolConfig<GenericKeyedObjectPoolConfig<Object>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<GenericKeyedObjectPoolConfig<Object>>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
      
      genericKeyedObjectPoolConfig0.setMaxTotalPerKey((-1));
      int int0 = genericKeyedObjectPoolConfig0.getMaxTotalPerKey();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxTotal());
      
      genericKeyedObjectPoolConfig0.setMaxTotal(0);
      int int0 = genericKeyedObjectPoolConfig0.getMaxTotal();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxTotal());
      
      genericKeyedObjectPoolConfig0.setMaxTotal(8);
      int int0 = genericKeyedObjectPoolConfig0.getMaxTotal();
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      GenericKeyedObjectPoolConfig<GenericKeyedObjectPoolConfig<Object>> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<GenericKeyedObjectPoolConfig<Object>>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
      
      genericKeyedObjectPoolConfig0.setMaxIdlePerKey(0);
      int int0 = genericKeyedObjectPoolConfig0.getMaxIdlePerKey();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMaxIdlePerKey((-3951));
      int int0 = genericKeyedObjectPoolConfig0.getMaxIdlePerKey();
      assertEquals((-3951), int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setTestWhileIdle(true);
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setTestOnReturn(true);
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setTestOnCreate(true);
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setTestOnBorrow(true);
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setNumTestsPerEvictionRun(0);
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setNumTestsPerEvictionRun((-1801));
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setMinIdlePerKey(8);
      genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMinIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
      
      genericKeyedObjectPoolConfig0.setMaxTotalPerKey(0);
      genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMaxTotalPerKey((-487));
      genericKeyedObjectPoolConfig0.clone();
      assertEquals((-487), genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      genericKeyedObjectPoolConfig0.setMaxTotal(8);
      genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotal());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
      
      genericKeyedObjectPoolConfig0.setMaxIdlePerKey(0);
      genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
      
      genericKeyedObjectPoolConfig0.setMaxIdlePerKey((-1));
      genericKeyedObjectPoolConfig0.clone();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setLifo(false);
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setJmxEnabled(false);
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setFairness(true);
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setBlockWhenExhausted(false);
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig1 = genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig1.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig1.getMaxTotal());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxTotalPerKey());
      assertEquals(8, genericKeyedObjectPoolConfig1.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      // Undeclared exception!
      try { 
        genericKeyedObjectPoolConfig0.toStringAppendFields((StringBuilder) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.BaseObjectPoolConfig", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      int int0 = genericKeyedObjectPoolConfig0.getMinIdlePerKey();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxTotal());
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      int int0 = genericKeyedObjectPoolConfig0.getMaxIdlePerKey();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxTotal());
      assertEquals(8, int0);
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Object> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Object>();
      genericKeyedObjectPoolConfig0.setMinIdlePerKey((-1));
      genericKeyedObjectPoolConfig0.clone();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMinIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      int int0 = genericKeyedObjectPoolConfig0.getMaxTotalPerKey();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey());
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxTotal());
      assertEquals(8, int0);
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      int int0 = genericKeyedObjectPoolConfig0.getMaxTotal();
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxIdlePerKey());
      assertEquals(8, genericKeyedObjectPoolConfig0.getMaxTotalPerKey());
      assertEquals((-1), int0);
      assertEquals(0, genericKeyedObjectPoolConfig0.getMinIdlePerKey());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      GenericKeyedObjectPoolConfig<Integer> genericKeyedObjectPoolConfig0 = new GenericKeyedObjectPoolConfig<Integer>();
      assertEquals((-1), genericKeyedObjectPoolConfig0.getMaxTotal());
      
      genericKeyedObjectPoolConfig0.setMaxTotal(0);
      genericKeyedObjectPoolConfig0.clone();
      assertEquals(0, genericKeyedObjectPoolConfig0.getMaxTotal());
  }
}
