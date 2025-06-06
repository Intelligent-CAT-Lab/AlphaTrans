
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
import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.launcher.CommandLauncher;
import org.apache.commons.exec.launcher.Java13CommandLauncher;
import org.apache.commons.exec.launcher.OS2CommandLauncher;
import org.apache.commons.exec.launcher.VmsCommandLauncher;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OS2CommandLauncher_ESTest extends OS2CommandLauncher_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher(java13CommandLauncher0);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      CommandLine commandLine0 = CommandLine.parse1("$ ", hashMap0);
      HashMap<String, String> hashMap1 = new HashMap<String, String>();
      Object object0 = new Object();
      hashMap0.put("$ ", object0);
      MockFile mockFile0 = new MockFile("$ ");
      // Undeclared exception!
      try { 
        oS2CommandLauncher0.exec1(commandLine0, hashMap1, mockFile0);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      VmsCommandLauncher vmsCommandLauncher0 = new VmsCommandLauncher();
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher(vmsCommandLauncher0);
      CommandLine commandLine0 = CommandLine.parse0("aM%X5#M}d6<\"<&}\"X");
      File file0 = MockFile.createTempFile("xOYjGs\"(3J>'}", "xOYjGs\"(3J>'}");
      CommandLine commandLine1 = new CommandLine(2, commandLine0, file0, "xOYjGs\"(3J>'}");
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      // Undeclared exception!
      try { 
        oS2CommandLauncher0.exec1(commandLine1, hashMap0, file0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Java13CommandLauncher java13CommandLauncher0 = new Java13CommandLauncher();
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher(java13CommandLauncher0);
      CommandLine commandLine0 = CommandLine.parse0("1jtm>");
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      MockFile mockFile0 = new MockFile("1jtm>");
      try { 
        oS2CommandLauncher0.exec1(commandLine0, hashMap0, mockFile0);
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
      OS2CommandLauncher oS2CommandLauncher0 = new OS2CommandLauncher((CommandLauncher) null);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      // Undeclared exception!
      try { 
        oS2CommandLauncher0.exec1((CommandLine) null, hashMap0, (File) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.launcher.CommandLauncherProxy", e);
      }
  }
}
