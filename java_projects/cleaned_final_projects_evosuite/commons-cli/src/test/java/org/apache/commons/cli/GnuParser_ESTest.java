
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


package org.apache.commons.cli;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.GnuParser;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class GnuParser_ESTest extends GnuParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      GnuParser gnuParser0 = new GnuParser();
      Options options0 = new Options();
      String[] stringArray0 = new String[0];
      String[] stringArray1 = gnuParser0.flatten(options0, stringArray0, true);
      assertNotSame(stringArray1, stringArray0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Options options0 = new Options();
      GnuParser gnuParser0 = new GnuParser();
      Option option0 = Option.Option1("", ";A`_E&y2myH>x)#s,$");
      Options options1 = options0.addOption0(option0);
      String[] stringArray0 = new String[2];
      stringArray0[0] = ";A`_E&y2myH>x)#s,$";
      stringArray0[1] = "--,";
      CommandLine commandLine0 = gnuParser0.parse0(options1, stringArray0);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      GnuParser gnuParser0 = new GnuParser();
      Options options0 = new Options();
      options0.addOption3("", "", false, "");
      String[] stringArray0 = new String[7];
      stringArray0[0] = "";
      stringArray0[1] = "-=";
      // Undeclared exception!
      try { 
        gnuParser0.flatten(options0, stringArray0, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      GnuParser gnuParser0 = new GnuParser();
      Options options0 = new Options();
      String[] stringArray0 = new String[6];
      stringArray0[0] = "-=";
      String[] stringArray1 = gnuParser0.flatten(options0, stringArray0, true);
      assertEquals(6, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      GnuParser gnuParser0 = new GnuParser();
      Options options0 = new Options();
      options0.addOption3("prM", ",", true, " [ARG]");
      String[] stringArray0 = new String[7];
      stringArray0[0] = ",";
      stringArray0[1] = " [ARG]";
      stringArray0[2] = " [ARG]";
      stringArray0[3] = "--,";
      // Undeclared exception!
      try { 
        gnuParser0.parse0(options0, stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      GnuParser gnuParser0 = new GnuParser();
      Options options0 = new Options();
      String[] stringArray0 = new String[5];
      stringArray0[0] = "2*SgaMp@@\"c!Qzz\"=";
      stringArray0[1] = "Cv)w,&9";
      stringArray0[2] = "-";
      stringArray0[3] = "";
      stringArray0[4] = "--";
      String[] stringArray1 = gnuParser0.flatten(options0, stringArray0, true);
      assertEquals(5, stringArray1.length);
  }
}
