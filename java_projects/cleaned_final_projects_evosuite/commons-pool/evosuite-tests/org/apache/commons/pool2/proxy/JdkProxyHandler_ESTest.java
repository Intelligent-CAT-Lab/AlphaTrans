


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
import static org.evosuite.runtime.EvoAssertions.*;
import java.lang.reflect.Method;
import org.apache.commons.pool2.UsageTracking;
import org.apache.commons.pool2.proxy.JdkProxyHandler;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class JdkProxyHandler_ESTest extends JdkProxyHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Object[] objectArray0 = new Object[9];
      Integer integer0 = new Integer((-733));
      JdkProxyHandler<Integer> jdkProxyHandler0 = new JdkProxyHandler<Integer>(integer0, (UsageTracking<Integer>) null);
      try { 
        jdkProxyHandler0.invoke(integer0, (Method) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Object[] objectArray0 = new Object[9];
      JdkProxyHandler<Object> jdkProxyHandler0 = new JdkProxyHandler<Object>((Object) null, (UsageTracking<Object>) null);
      try { 
        jdkProxyHandler0.invoke((Object) null, (Method) null, objectArray0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // This object may no longer be used as it has been returned to the Object Pool.
         //
         verifyException("org.apache.commons.pool2.proxy.BaseProxyHandler", e);
      }
  }
}
