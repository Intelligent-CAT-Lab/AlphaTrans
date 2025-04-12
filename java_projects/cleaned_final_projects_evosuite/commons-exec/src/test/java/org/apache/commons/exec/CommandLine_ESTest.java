
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
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.File;
import java.util.HashMap;
import org.apache.commons.exec.CommandLine;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CommandLine_ESTest extends CommandLine_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("bs");
      MockFile mockFile0 = new MockFile("bs");
      CommandLine commandLine1 = new CommandLine(1, commandLine0, mockFile0, "");
      boolean boolean0 = commandLine1.isFile();
      assertTrue(boolean0);
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("bs");
      MockFile mockFile0 = new MockFile("bs");
      CommandLine commandLine1 = new CommandLine(1, commandLine0, mockFile0, "");
      String[] stringArray0 = commandLine1.getArguments();
      CommandLine commandLine2 = commandLine1.addArguments3(stringArray0, true);
      assertTrue(commandLine2.isFile());
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("b4");
      MockFile mockFile0 = new MockFile("", "b4");
      CommandLine commandLine1 = new CommandLine(1, commandLine0, mockFile0, "");
      String[] stringArray0 = new String[1];
      CommandLine commandLine2 = commandLine1.addArguments2(stringArray0);
      assertFalse(commandLine0.isFile());
      assertTrue(commandLine2.isFile());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("b4");
      MockFile mockFile0 = new MockFile("", "b4");
      CommandLine commandLine1 = new CommandLine(1, commandLine0, mockFile0, "");
      CommandLine commandLine2 = commandLine1.addArguments1("", false);
      assertFalse(commandLine0.isFile());
      assertTrue(commandLine2.isFile());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("b4");
      MockFile mockFile0 = new MockFile("", "b4");
      CommandLine commandLine1 = new CommandLine(1, commandLine0, mockFile0, "");
      CommandLine commandLine2 = commandLine1.addArgument1("org.apache.commons.exec.CommandLine", true);
      assertTrue(commandLine2.isFile());
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("b4");
      MockFile mockFile0 = new MockFile("", "b4");
      CommandLine commandLine1 = new CommandLine(1, commandLine0, mockFile0, "");
      CommandLine commandLine2 = commandLine1.addArguments0("b4");
      CommandLine commandLine3 = commandLine2.addArgument0("");
      assertTrue(commandLine3.isFile());
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("Xr[>0O.2u<0q");
      CommandLine commandLine1 = commandLine0.addArgument0((String) null);
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      hashMap0.put("\"' ", "\"' ");
      CommandLine commandLine0 = CommandLine.parse1("$", hashMap0);
      // Undeclared exception!
      try { 
        commandLine0.toStrings();
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      CommandLine commandLine0 = CommandLine.parse1("org.apache.commons.exec.CommandLine", hashMap0);
      hashMap0.put("org.apache.commons.exec.CommandLine", commandLine0);
      commandLine0.getExecutable();
      commandLine0.toString();
      String[] stringArray0 = commandLine0.getArguments();
      CommandLine commandLine1 = CommandLine.parse1("org.apache.commons.exec.CommandLine", hashMap0);
      CommandLine commandLine2 = commandLine0.addArguments0("(s0<K");
      CommandLine commandLine3 = commandLine1.addArguments3(stringArray0, false);
      CommandLine commandLine4 = commandLine3.addArguments1("org.apache.commons.exec.CommandLine", true);
      CommandLine commandLine5 = commandLine3.addArguments0("org.apache.commons.exec.CommandLine");
      commandLine2.getSubstitutionMap();
      String[] stringArray1 = new String[1];
      stringArray1[0] = "[org.apache.commons.exec.CommandLine]";
      commandLine2.addArguments3(stringArray1, false);
      commandLine1.getExecutable();
      commandLine2.getExecutable();
      commandLine2.getExecutable();
      String[] stringArray2 = new String[7];
      stringArray2[0] = "org.apache.commons.exec.CommandLine";
      stringArray2[1] = "org.apache.commons.exec.CommandLine";
      stringArray2[2] = "c$zpV";
      stringArray2[3] = "org.apache.commons.exec.CommandLine";
      stringArray2[4] = "[org.apache.commons.exec.CommandLine]";
      stringArray2[5] = "org.apache.commons.exec.CommandLine";
      stringArray2[6] = "(s0<K";
      commandLine0.addArguments2(stringArray2);
      String[] stringArray3 = commandLine0.getArguments();
      commandLine5.addArguments3(stringArray3, false);
      // Undeclared exception!
      commandLine4.toString();
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      Object object0 = new Object();
      hashMap0.put("Delimiter not found for : ", object0);
      CommandLine commandLine0 = CommandLine.parse1("e@l7gh)A8$", hashMap0);
      // Undeclared exception!
      try { 
        commandLine0.toString();
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("foT0und");
      String[] stringArray0 = new String[4];
      stringArray0[2] = "?RL|^'Rw_W\">(Wv";
      // Undeclared exception!
      try { 
        commandLine0.addArguments3(stringArray0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0(", ");
      String[] stringArray0 = new String[9];
      stringArray0[3] = "$']0\"FoRn\"Fs8\"@7W";
      // Undeclared exception!
      try { 
        commandLine0.addArguments2(stringArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("line");
      // Undeclared exception!
      try { 
        commandLine0.addArgument1("[line, line, 'YX-{x!tVJ3?#+$Q\"Ds', line, line, line, line, line]", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0(";Q/");
      CommandLine commandLine1 = commandLine0.addArguments3((String[]) null, false);
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("$");
      // Undeclared exception!
      try { 
        commandLine0.addArguments1("Dq*<!/r-LQVtu>[\"", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unbalanced quotes in Dq*<!/r-LQVtu>[\"
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      CommandLine commandLine0 = CommandLine.parse1("zQKM-q", hashMap0);
      CommandLine commandLine1 = commandLine0.addArguments1((String) null, false);
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("org.apache.commons.exec.CommandLine$Argument");
      CommandLine commandLine1 = commandLine0.addArgument1("t", true);
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("{Y;[dt.CEM/^uk");
      CommandLine commandLine1 = commandLine0.addArgument1((String) null, true);
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      // Undeclared exception!
      try { 
        CommandLine.parse0("i-\"$~ur");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unbalanced quotes in i-\"$~ur
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      HashMap<String, CommandLine.Argument> hashMap0 = new HashMap<String, CommandLine.Argument>();
      CommandLine commandLine0 = CommandLine.parse1("~Ls6aOsm>%A(jqB!LY", hashMap0);
      CommandLine commandLine1 = commandLine0.addArguments0("");
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      CommandLine commandLine0 = CommandLine.parse1("Tsijy n", hashMap0);
      commandLine0.getSubstitutionMap();
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      // Undeclared exception!
      try { 
        CommandLine.parse1((String) null, hashMap0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Command line can not be null
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("line");
      commandLine0.getSubstitutionMap();
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("b4");
      boolean boolean0 = commandLine0.isFile();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("line");
      HashMap<String, CommandLine.Argument> hashMap0 = new HashMap<String, CommandLine.Argument>();
      commandLine0.setSubstitutionMap(hashMap0);
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      MockFile mockFile0 = new MockFile("");
      CommandLine commandLine0 = null;
      try {
        commandLine0 = new CommandLine((-1), (CommandLine) null, mockFile0, "");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Executable can not be empty
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("$");
      CommandLine commandLine1 = commandLine0.addArgument1("\"' ", false);
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("D");
      CommandLine commandLine1 = null;
      try {
        commandLine1 = new CommandLine(1, commandLine0, (File) null, "D");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("yf=Rxl?4");
      MockFile mockFile0 = new MockFile("yf=Rxl?4");
      CommandLine commandLine1 = new CommandLine(0, commandLine0, mockFile0, "yf=Rxl?4");
      assertFalse(commandLine1.isFile());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      CommandLine commandLine0 = CommandLine.parse1("zQKM-q", hashMap0);
      // Undeclared exception!
      try { 
        commandLine0.addArguments0("Can't handle single and double quotes in same argument");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unbalanced quotes in Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("e{\" K\"");
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0(" ?W");
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      // Undeclared exception!
      try { 
        CommandLine.parse1(" ", hashMap0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Command line can not be empty
         //
         verifyException("org.apache.commons.exec.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("line");
      String[] stringArray0 = new String[5];
      stringArray0[0] = "line";
      CommandLine commandLine1 = commandLine0.addArguments3(stringArray0, true);
      String[] stringArray1 = commandLine1.toStrings();
      assertFalse(commandLine1.isFile());
      assertEquals(2, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0(":T]^Xq6\"dI'g/*/\" ");
      String string0 = commandLine0.toString();
      assertEquals("[:T]^Xq6dI'g/*/]", string0);
      assertFalse(commandLine0.isFile());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CommandLine commandLine0 = CommandLine.parse0("'!'27:*zX<");
      // Undeclared exception!
      try { 
        commandLine0.addArgument0(",'\"Dj:");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      CommandLine commandLine0 = CommandLine.parse1("`/Q<!y$SW]&", hashMap0);
      MockFile mockFile0 = new MockFile("`/Q<!y$SW]&", "`/Q<!y$SW]&");
      CommandLine commandLine1 = new CommandLine(0, commandLine0, mockFile0, "");
      assertFalse(commandLine1.isFile());
  }
}
