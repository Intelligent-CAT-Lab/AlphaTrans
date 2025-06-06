


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
import org.apache.commons.pool2.proxy.CglibProxySource;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CglibProxySource_ESTest extends CglibProxySource_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Class<Object> class0 = Object.class;
      CglibProxySource<Object> cglibProxySource0 = new CglibProxySource<Object>(class0);
      String string0 = cglibProxySource0.toString();
      assertEquals("CglibProxySource [superclass=class java.lang.Object]", string0);
  }
}
