


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
import java.lang.reflect.Method;
import org.apache.commons.pool2.UsageTracking;
import org.apache.commons.pool2.proxy.BaseProxyHandler;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BaseProxyHandler_ESTest extends BaseProxyHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Integer integer0 = new Integer(0);
      UsageTracking<Object> usageTracking0 = (UsageTracking<Object>) mock(UsageTracking.class, new ViolatedAssumptionAnswer());
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>(integer0, usageTracking0);
      baseProxyHandler0.validateProxiedObject();
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Integer integer0 = new Integer(0);
      BaseProxyHandler<Integer> baseProxyHandler0 = new BaseProxyHandler<Integer>(integer0, (UsageTracking<Integer>) null);
      UsageTracking<Object> usageTracking0 = (UsageTracking<Object>) mock(UsageTracking.class, new ViolatedAssumptionAnswer());
      BaseProxyHandler<Object> baseProxyHandler1 = new BaseProxyHandler<Object>(baseProxyHandler0, usageTracking0);
      Object object0 = baseProxyHandler1.getPooledObject();
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Object object0 = new Object();
      UsageTracking<Object> usageTracking0 = (UsageTracking<Object>) mock(UsageTracking.class, new ViolatedAssumptionAnswer());
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>(object0, usageTracking0);
      Object object1 = baseProxyHandler0.disableProxy();
      assertSame(object0, object1);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>((Object) null, (UsageTracking<Object>) null);
      // Undeclared exception!
      try { 
        baseProxyHandler0.validateProxiedObject();
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // This object may no longer be used as it has been returned to the Object Pool.
         //
         verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>((Object) null, (UsageTracking<Object>) null);
      try { 
        baseProxyHandler0.doInvoke((Method) null, (Object[]) null);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // This object may no longer be used as it has been returned to the Object Pool.
         //
         verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      UsageTracking<Object> usageTracking0 = (UsageTracking<Object>) mock(UsageTracking.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(usageTracking0).toString();
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>(usageTracking0, usageTracking0);
      try { 
        baseProxyHandler0.doInvoke((Method) null, (Object[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Object object0 = new Object();
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>(object0, (UsageTracking<Object>) null);
      try { 
        baseProxyHandler0.doInvoke((Method) null, (Object[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>((Object) null, (UsageTracking<Object>) null);
      Object object0 = baseProxyHandler0.disableProxy();
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>((Object) null, (UsageTracking<Object>) null);
      Object object0 = baseProxyHandler0.getPooledObject();
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      BaseProxyHandler<Object> baseProxyHandler0 = new BaseProxyHandler<Object>((Object) null, (UsageTracking<Object>) null);
      String string0 = baseProxyHandler0.toString();
      assertEquals("org.apache.commons.pool2.proxy.BaseProxyHandler [pooledObject=null, usageTracking=null]", string0);
  }
}
