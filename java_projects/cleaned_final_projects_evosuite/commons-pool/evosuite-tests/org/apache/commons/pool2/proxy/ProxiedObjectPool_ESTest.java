


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
import org.apache.commons.pool2.ObjectPool;
import org.apache.commons.pool2.proxy.JdkProxySource;
import org.apache.commons.pool2.proxy.ProxiedObjectPool;
import org.apache.commons.pool2.proxy.ProxySource;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ProxiedObjectPool_ESTest extends ProxiedObjectPool_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 1);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      proxiedObjectPool0.close();
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ObjectPool<Integer> objectPool0 = (ObjectPool<Integer>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(objectPool0).getNumIdle();
      ProxiedObjectPool<Integer> proxiedObjectPool0 = new ProxiedObjectPool<Integer>(objectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedObjectPool0.getNumIdle();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ObjectPool<Integer> objectPool0 = (ObjectPool<Integer>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(2266).when(objectPool0).getNumIdle();
      ProxiedObjectPool<Integer> proxiedObjectPool0 = new ProxiedObjectPool<Integer>(objectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedObjectPool0.getNumIdle();
      assertEquals(2266, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 1);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((-1984)).when(objectPool0).getNumIdle();
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      int int0 = proxiedObjectPool0.getNumIdle();
      assertEquals((-1984), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(83).when(objectPool0).getNumActive();
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      int int0 = proxiedObjectPool0.getNumActive();
      assertEquals(83, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ObjectPool<Integer> objectPool0 = (ObjectPool<Integer>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((-3983)).when(objectPool0).getNumActive();
      ProxiedObjectPool<Integer> proxiedObjectPool0 = new ProxiedObjectPool<Integer>(objectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedObjectPool0.getNumActive();
      assertEquals((-3983), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, (ProxySource<Object>) null);
      try { 
        proxiedObjectPool0.returnObject((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, jdkProxySource0);
      Object object0 = new Object();
      try { 
        proxiedObjectPool0.returnObject(object0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // not a proxy instance
         //
         verifyException("java.lang.reflect.Proxy", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, (ProxySource<Object>) null);
      try { 
        proxiedObjectPool0.invalidateObject0((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, jdkProxySource0);
      try { 
        proxiedObjectPool0.invalidateObject0(jdkProxySource0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // not a proxy instance
         //
         verifyException("java.lang.reflect.Proxy", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, (ProxySource<Object>) null);
      // Undeclared exception!
      try { 
        proxiedObjectPool0.getNumActive();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, (ProxySource<Object>) null);
      try { 
        proxiedObjectPool0.clear();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ProxiedObjectPool<Integer> proxiedObjectPool0 = new ProxiedObjectPool<Integer>((ObjectPool<Integer>) null, (ProxySource<Integer>) null);
      try { 
        proxiedObjectPool0.borrowObject();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(objectPool0).borrowObject();
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 1);
      Class<Object> class0 = Object.class;
      classArray0[0] = class0;
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      try { 
        proxiedObjectPool0.borrowObject();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // java.lang.Object is not an interface
         //
         verifyException("java.lang.reflect.Proxy$ProxyBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, (ProxySource<Object>) null);
      try { 
        proxiedObjectPool0.addObject();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      proxiedObjectPool0.addObject();
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 1);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(objectPool0).getNumActive();
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      int int0 = proxiedObjectPool0.getNumActive();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(objectPool0).borrowObject();
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      Object object0 = proxiedObjectPool0.borrowObject();
      proxiedObjectPool0.returnObject(object0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      ProxiedObjectPool<Integer> proxiedObjectPool0 = new ProxiedObjectPool<Integer>((ObjectPool<Integer>) null, (ProxySource<Integer>) null);
      // Undeclared exception!
      try { 
        proxiedObjectPool0.close();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      ObjectPool<Integer> objectPool0 = (ObjectPool<Integer>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      ProxiedObjectPool<Integer> proxiedObjectPool0 = new ProxiedObjectPool<Integer>(objectPool0, jdkProxySource0);
      proxiedObjectPool0.clear();
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(objectPool0).borrowObject();
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      Object object0 = proxiedObjectPool0.borrowObject();
      proxiedObjectPool0.invalidateObject0(object0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>((ObjectPool<Object>) null, (ProxySource<Object>) null);
      // Undeclared exception!
      try { 
        proxiedObjectPool0.getNumIdle();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Object>[] classArray0 = (Class<Object>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Object> jdkProxySource0 = new JdkProxySource<Object>(classLoader0, classArray0);
      ObjectPool<Object> objectPool0 = (ObjectPool<Object>) mock(ObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(objectPool0).toString();
      ProxiedObjectPool<Object> proxiedObjectPool0 = new ProxiedObjectPool<Object>(objectPool0, jdkProxySource0);
      String string0 = proxiedObjectPool0.toString();
      assertNotNull(string0);
  }
}
