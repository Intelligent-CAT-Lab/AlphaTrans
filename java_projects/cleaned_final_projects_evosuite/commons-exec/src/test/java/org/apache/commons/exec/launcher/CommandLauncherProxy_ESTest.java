
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
import java.io.IOException;
import java.util.HashMap;
import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.launcher.Java13CommandLauncher;
import org.apache.commons.exec.launcher.OS2CommandLauncher;
import org.apache.commons.exec.launcher.WinNTCommandLauncher;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CommandLauncherProxy_ESTest extends CommandLauncherProxy_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher(java13CommandLauncher0);
      WinNTCommandLauncher winNTCommandLauncher0 = new WinNTCommandLauncher(oS2CommandLauncher0);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      CommandLine commandLine0 = CommandLine.parse1("*/0F", hashMap0);
      HashMap<String, String> hashMap1 = new HashMap<String, String>();
      String[] stringArray0 = new String[7];
      hashMap0.put(stringArray0[0], commandLine0);
      stringArray0[3] = "$ ";
      commandLine0.addArguments2(stringArray0);
      // Undeclared exception!
      try { 
        winNTCommandLauncher0.exec0(commandLine0, hashMap1);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      CommandLine commandLine0 = CommandLine.parse0("m|[p*q;%)");
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      WinNTCommandLauncher winNTCommandLauncher0 = new WinNTCommandLauncher(java13CommandLauncher0);
      try { 
        winNTCommandLauncher0.exec0(commandLine0, hashMap0);
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
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher(java13CommandLauncher0);
      // Undeclared exception!
      try { 
        oS2CommandLauncher0.exec0((CommandLine) null, hashMap0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.launcher.CommandLauncherImpl", e);
      }
  }
}
