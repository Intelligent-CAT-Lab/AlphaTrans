
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


package org.apache.commons.exec.environment;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.exec.environment.EnvironmentUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class EnvironmentUtils_ESTest extends EnvironmentUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      String[] stringArray0 = EnvironmentUtils.toStrings(hashMap0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Map<String, String> map0 = EnvironmentUtils.getProcEnvironment();
      // Undeclared exception!
      try { 
        EnvironmentUtils.addVariableToEnvironment(map0, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.environment.EnvironmentUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      String[] stringArray0 = EnvironmentUtils.toStrings((Map<String, String>) null);
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Map<String, String> map0 = EnvironmentUtils.getProcEnvironment();
      // Undeclared exception!
      try { 
        EnvironmentUtils.addVariableToEnvironment(map0, ")");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Environment variable for this platform must contain an equals sign ('=')
         //
         verifyException("org.apache.commons.exec.environment.EnvironmentUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      EnvironmentUtils.addVariableToEnvironment(hashMap0, "#=N'h3<\"");
      assertEquals(1, hashMap0.size());
  }
}
