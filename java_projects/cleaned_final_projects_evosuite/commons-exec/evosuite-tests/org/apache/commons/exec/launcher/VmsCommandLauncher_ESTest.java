
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


package org.apache.commons.exec.launcher;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.File;
import java.util.HashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.launcher.VmsCommandLauncher;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class VmsCommandLauncher_ESTest extends VmsCommandLauncher_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
      boolean boolean0 = vmsCommandLauncher0.isFailure((-1911));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
      boolean boolean0 = vmsCommandLauncher0.isFailure(34);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
      boolean boolean0 = vmsCommandLauncher0.isFailure(45);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
        try {
          VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
          HashMap<String, String> hashMap0 = new HashMap<String, String>();
          // Undeclared exception!
          try { 
            vmsCommandLauncher0.exec1((CommandLine) null, hashMap0, (File) null);
            fail("Expecting exception: SecurityException");
          
          } catch(SecurityException e) {
             //
             // Unable to create temporary file or directory
             //
             verifyException("java.nio.file.TempFileHelper", e);
          }
        } catch(Throwable t) {
            // Need to catch declared exceptions
        }
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
        try {
          VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
          HashMap<String, String> hashMap0 = new HashMap<String, String>();
          // Undeclared exception!
          try { 
            vmsCommandLauncher0.exec0((CommandLine) null, hashMap0);
            fail("Expecting exception: SecurityException");
          
          } catch(SecurityException e) {
             //
             // Unable to create temporary file or directory
             //
             verifyException("java.nio.file.TempFileHelper", e);
          }
        } catch(Throwable t) {
            // Need to catch declared exceptions
        }
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }
}
