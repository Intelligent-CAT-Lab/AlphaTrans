


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
import org.apache.commons.pool2.KeyedObjectPool;
import org.apache.commons.pool2.proxy.JdkProxySource;
import org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool;
import org.apache.commons.pool2.proxy.ProxySource;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ProxiedKeyedObjectPool_ESTest extends ProxiedKeyedObjectPool_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 3);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, jdkProxySource0);
      Integer integer0 = new Integer(0);
      Integer integer1 = new Integer(0);
      try { 
        proxiedKeyedObjectPool0.returnObject(integer1, integer0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // not a proxy instance
         //
         verifyException("java.lang.reflect.Proxy", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      Integer integer0 = new Integer((-1));
      Integer integer1 = new Integer((-295));
      try { 
        proxiedKeyedObjectPool0.invalidateObject0(integer0, integer1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      proxiedKeyedObjectPool0.close();
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(keyedObjectPool0).getNumIdle1(anyInt());
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 9);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, jdkProxySource0);
      Integer integer0 = new Integer((-4495));
      int int0 = proxiedKeyedObjectPool0.getNumIdle1(integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((-1)).when(keyedObjectPool0).getNumIdle1(anyInt());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      Integer integer0 = new Integer(2163);
      int int0 = proxiedKeyedObjectPool0.getNumIdle1(integer0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(keyedObjectPool0).getNumIdle0();
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 1);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, jdkProxySource0);
      int int0 = proxiedKeyedObjectPool0.getNumIdle0();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(2295).when(keyedObjectPool0).getNumIdle0();
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumIdle0();
      assertEquals(2295, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(keyedObjectPool0).getNumActive1(anyInt());
      ClassLoader classLoader0 = ClassLoader.getPlatformClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 7);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, jdkProxySource0);
      Integer integer0 = new Integer((-1));
      int int0 = proxiedKeyedObjectPool0.getNumActive1(integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer(4151);
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(4151).when(keyedObjectPool0).getNumActive1(anyInt());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumActive1(integer0);
      assertEquals(4151, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(keyedObjectPool0).getNumActive0();
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumActive0();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(739).when(keyedObjectPool0).getNumActive0();
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumActive0();
      assertEquals(739, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      try { 
        proxiedKeyedObjectPool0.returnObject((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      // Undeclared exception!
      try { 
        proxiedKeyedObjectPool0.getNumIdle1((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      // Undeclared exception!
      try { 
        proxiedKeyedObjectPool0.getNumIdle0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      // Undeclared exception!
      try { 
        proxiedKeyedObjectPool0.getNumActive1((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      // Undeclared exception!
      try { 
        proxiedKeyedObjectPool0.getNumActive0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      try { 
        proxiedKeyedObjectPool0.clear1((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      try { 
        proxiedKeyedObjectPool0.clear0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(keyedObjectPool0).borrowObject(anyInt());
      ClassLoader classLoader0 = ClassLoader.getSystemClassLoader();
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 1);
      Class<Integer> class0 = Integer.class;
      classArray0[0] = class0;
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>(classLoader0, classArray0);
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, jdkProxySource0);
      try { 
        proxiedKeyedObjectPool0.borrowObject((Integer) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // java.lang.Integer is not an interface
         //
         verifyException("java.lang.reflect.Proxy$ProxyBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      try { 
        proxiedKeyedObjectPool0.addObject((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Integer integer0 = new Integer(0);
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(keyedObjectPool0).borrowObject(anyInt());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      try { 
        proxiedKeyedObjectPool0.borrowObject(integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      // Undeclared exception!
      try { 
        proxiedKeyedObjectPool0.close();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.ProxiedKeyedObjectPool", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Integer integer0 = new Integer(0);
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      proxiedKeyedObjectPool0.addObject(integer0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((-1760)).when(keyedObjectPool0).getNumActive0();
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumActive0();
      assertEquals((-1760), int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Integer integer0 = new Integer(0);
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      proxiedKeyedObjectPool0.clear1(integer0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, (ProxySource<Integer>) null);
      String string0 = proxiedKeyedObjectPool0.toString();
      assertEquals("ProxiedKeyedObjectPool [pool=null, proxySource=null]", string0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      proxiedKeyedObjectPool0.clear0();
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Integer integer0 = new Integer(0);
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((-1200)).when(keyedObjectPool0).getNumActive1(anyInt());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumActive1(integer0);
      assertEquals((-1200), int0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Integer integer0 = new Integer(0);
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn(1774).when(keyedObjectPool0).getNumIdle1(anyInt());
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumIdle1(integer0);
      assertEquals(1774, int0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      KeyedObjectPool<Integer, Integer> keyedObjectPool0 = (KeyedObjectPool<Integer, Integer>) mock(KeyedObjectPool.class, new ViolatedAssumptionAnswer());
      doReturn((-1)).when(keyedObjectPool0).getNumIdle0();
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>(keyedObjectPool0, (ProxySource<Integer>) null);
      int int0 = proxiedKeyedObjectPool0.getNumIdle0();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Class<Integer>[] classArray0 = (Class<Integer>[]) Array.newInstance(Class.class, 0);
      JdkProxySource<Integer> jdkProxySource0 = new JdkProxySource<Integer>((ClassLoader) null, classArray0);
      ProxiedKeyedObjectPool<Integer, Integer> proxiedKeyedObjectPool0 = new ProxiedKeyedObjectPool<Integer, Integer>((KeyedObjectPool<Integer, Integer>) null, jdkProxySource0);
      Integer integer0 = new Integer(2);
      try { 
        proxiedKeyedObjectPool0.invalidateObject0(integer0, integer0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // not a proxy instance
         //
         verifyException("java.lang.reflect.Proxy", e);
      }
  }
}
