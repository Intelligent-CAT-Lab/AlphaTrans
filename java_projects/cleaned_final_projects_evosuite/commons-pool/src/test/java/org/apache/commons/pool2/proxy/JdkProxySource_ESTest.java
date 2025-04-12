


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




package org.apache.commons.pool2.proxy;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.lang.reflect.Array;
import org.apache.commons.pool2.UsageTracking;
import org.apache.commons.pool2.proxy.JdkProxyHandler;
import org.apache.commons.pool2.proxy.JdkProxySource;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class JdkProxySource_ESTest extends JdkProxySource_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      // Undeclared exception!
      try { 
        jdkProxySource0.resolveProxy((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.reflect.Proxy", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 4);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      // Undeclared exception!
      try { 
        jdkProxySource0.resolveProxy(classLoader0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // not a proxy instance
         //
         verifyException("java.lang.reflect.Proxy", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 1);
      Class<Integer> class0 = Integer.class;
      classArray0[0] = class0;
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      UsageTracking<Object> usageTracking0 = (UsageTracking<Object>) mock(UsageTracking.class, new ViolatedAssumptionAnswer());
      // Undeclared exception!
      try { 
        jdkProxySource0.createProxy(jdkProxySource0, usageTracking0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // java.lang.Integer is not an interface
         //
         verifyException("java.lang.reflect.Proxy$ProxyBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      JdkProxySource<JdkProxyHandler<Object>> jdkProxySource0 = null;
      try {
        jdkProxySource0 = new JdkProxySource<JdkProxyHandler<Object>>(classLoader0, (Class<?>[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.JdkProxySource", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 4);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      String string0 = jdkProxySource0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 1);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      Class<Object>[] classArray1 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource1 = new JdkProxySource<Object>(classLoader0, classArray1);
      UsageTracking<Object> usageTracking0 = (UsageTracking<Object>) mock(UsageTracking.class, new ViolatedAssumptionAnswer());
      Object object0 = jdkProxySource1.createProxy(jdkProxySource0, usageTracking0);
      Object object1 = jdkProxySource1.resolveProxy(object0);
      assertNotNull(object1);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 1);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      // Undeclared exception!
      try { 
        jdkProxySource0.createProxy(classLoader0, (UsageTracking<Object>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }
}
