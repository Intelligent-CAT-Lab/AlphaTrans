
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
import org.apache.commons.exec.launcher.CommandLauncher;
import org.apache.commons.exec.launcher.Java13CommandLauncher;
import org.apache.commons.exec.launcher.OS2CommandLauncher;
import org.apache.commons.exec.launcher.WinNTCommandLauncher;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CommandLauncherImpl_ESTest extends CommandLauncherImpl_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      boolean boolean0 = java13CommandLauncher0.isFailure(1451);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      WinNTCommandLauncher winNTCommandLauncher0 = new WinNTCommandLauncher((CommandLauncher) null);
      CommandLine commandLine0 = CommandLine.parse0("org.apache.commons.exec.launcher.CommandLauncherImpl");
      File file0 = MockFile.createTempFile("^Ip6~$6.-[p]$_F", "");
      // Undeclared exception!
      try { 
        winNTCommandLauncher0.exec1(commandLine0, (Map<String, String>) null, file0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.launcher.CommandLauncherProxy", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      CommandLine commandLine0 = CommandLine.parse0("al{");
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      try { 
        java13CommandLauncher0.exec1(commandLine0, hashMap0, (File) null);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Cannot start processes in a unit test
         //
         verifyException("org.evosuite.runtime.mock.java.lang.MockRuntime", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      hashMap0.put("$", "$");
      CommandLine commandLine0 = CommandLine.parse1("$", hashMap0);
      HashMap<String, String> hashMap1 = new HashMap<String, String>();
      // Undeclared exception!
      try { 
        java13CommandLauncher0.exec0(commandLine0, hashMap1);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      CommandLine commandLine0 = CommandLine.parse0("Command line can not be empty");
      try { 
        java13CommandLauncher0.exec0(commandLine0, (Map<String, String>) null);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Cannot start processes in a unit test
         //
         verifyException("org.evosuite.runtime.mock.java.lang.MockRuntime", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher(java13CommandLauncher0);
      boolean boolean0 = oS2CommandLauncher0.isFailure((-256));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      boolean boolean0 = java13CommandLauncher0.isFailure(0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      // Undeclared exception!
      try { 
        java13CommandLauncher0.exec0((CommandLine) null, (Map<String, String>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.launcher.CommandLauncherImpl", e);
      }
  }
}
