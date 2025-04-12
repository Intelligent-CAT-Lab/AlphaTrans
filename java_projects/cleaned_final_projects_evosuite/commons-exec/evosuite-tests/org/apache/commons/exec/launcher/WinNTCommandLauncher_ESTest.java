
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
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.launcher.Java13CommandLauncher;
import org.apache.commons.exec.launcher.VmsCommandLauncher;
import org.apache.commons.exec.launcher.WinNTCommandLauncher;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class WinNTCommandLauncher_ESTest extends WinNTCommandLauncher_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
      WinNTCommandLauncher winNTCommandLauncher0 = new WinNTCommandLauncher(vmsCommandLauncher0);
      CommandLine commandLine0 = CommandLine.parse1("org.apache.commons.exec.launcher.WinNTCommandLauncher", (Map<String, ?>) null);
      MockFile mockFile0 = new MockFile("org.apache.commons.exec.launcher.WinNTCommandLauncher");
      CommandLine commandLine1 = new CommandLine((-3420), commandLine0, mockFile0, "Tr [wn\"M'*)M,3:~D");
      // Undeclared exception!
      try { 
        winNTCommandLauncher0.exec1(commandLine1, (Map<String, String>) null, mockFile0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      WinNTCommandLauncher winNTCommandLauncher0 = new WinNTCommandLauncher(java13CommandLauncher0);
      CommandLine commandLine0 = CommandLine.parse0("W8");
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      MockFile mockFile0 = new MockFile("W8");
      try { 
        winNTCommandLauncher0.exec1(commandLine0, hashMap0, mockFile0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Cannot start processes in a unit test
         //
         verifyException("org.evosuite.runtime.mock.java.lang.MockRuntime", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      WinNTCommandLauncher winNTCommandLauncher0 = new WinNTCommandLauncher(java13CommandLauncher0);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      // Undeclared exception!
      try { 
        winNTCommandLauncher0.exec1((CommandLine) null, hashMap0, (File) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.launcher.CommandLauncherImpl", e);
      }
  }
}
