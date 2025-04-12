
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


package org.apache.commons.exec;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import org.apache.commons.exec.ShutdownHookProcessDestroyer;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ShutdownHookProcessDestroyer_ESTest extends ShutdownHookProcessDestroyer_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      shutdownHookProcessDestroyer0.add((Process) null);
      shutdownHookProcessDestroyer0.size();
      assertTrue(shutdownHookProcessDestroyer0.isAddedAsShutdownHook());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      Process process0 = mock(Process.class, new ViolatedAssumptionAnswer());
      shutdownHookProcessDestroyer0.add(process0);
      boolean boolean0 = shutdownHookProcessDestroyer0.isAddedAsShutdownHook();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      int int0 = shutdownHookProcessDestroyer0.size();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      shutdownHookProcessDestroyer0.add((Process) null);
      shutdownHookProcessDestroyer0.run();
      boolean boolean0 = shutdownHookProcessDestroyer0.remove((Process) null);
      assertTrue(shutdownHookProcessDestroyer0.isAddedAsShutdownHook());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      boolean boolean0 = shutdownHookProcessDestroyer0.remove((Process) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      shutdownHookProcessDestroyer0.add((Process) null);
      boolean boolean0 = shutdownHookProcessDestroyer0.isEmpty();
      assertTrue(shutdownHookProcessDestroyer0.isAddedAsShutdownHook());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      shutdownHookProcessDestroyer0.run();
      shutdownHookProcessDestroyer0.add((Process) null);
      boolean boolean0 = shutdownHookProcessDestroyer0.remove((Process) null);
      assertTrue(boolean0);
      assertFalse(shutdownHookProcessDestroyer0.isAddedAsShutdownHook());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      shutdownHookProcessDestroyer0.add((Process) null);
      shutdownHookProcessDestroyer0.add((Process) null);
      boolean boolean0 = shutdownHookProcessDestroyer0.remove((Process) null);
      assertTrue(shutdownHookProcessDestroyer0.isAddedAsShutdownHook());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      boolean boolean0 = shutdownHookProcessDestroyer0.isEmpty();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      boolean boolean0 = shutdownHookProcessDestroyer0.isAddedAsShutdownHook();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ShutdownHookProcessDestroyer shutdownHookProcessDestroyer0 = new ShutdownHookProcessDestroyer();
      shutdownHookProcessDestroyer0.add((Process) null);
      assertTrue(shutdownHookProcessDestroyer0.isAddedAsShutdownHook());
      
      boolean boolean0 = shutdownHookProcessDestroyer0.remove((Process) null);
      assertTrue(boolean0);
  }
}
