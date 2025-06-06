
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
import org.apache.commons.cli.MissingArgumentException;
import org.apache.commons.cli.Option;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MissingArgumentException_ESTest extends MissingArgumentException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.required0();
      option_Builder0.longOpt("org.apache.commons.cli.Option");
      Option option0 = option_Builder1.build();
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, "org.apache.commons.cli.Option", option0);
      Option option1 = missingArgumentException0.getOption();
      assertEquals((-2), Option.UNLIMITED_VALUES);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Option option0 = Option.Option1("m", "m");
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, "j=XDFq^zS*0=F1j[9f", option0);
      option0.setValueSeparator('\"');
      Option option1 = missingArgumentException0.getOption();
      assertFalse(option1.hasOptionalArg());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.optionalArg(true);
      Option option0 = new Option(1, "&JF\"<BZ%HI~TN,M", "&JF\"<BZ%HI~TN,M", "", true, option_Builder1);
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, "&JF\"<BZ%HI~TN,M", option0);
      Option option1 = missingArgumentException0.getOption();
      assertFalse(option1.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.hasArgs();
      option_Builder0.longOpt("org.apache.commons.cli.Option");
      Option option0 = option_Builder0.build();
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, "org.apache.commons.cli.Option", option0);
      Option option1 = missingArgumentException0.getOption();
      assertTrue(option1.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.argName("org.apache.commons.cli.Option");
      option_Builder0.longOpt("org.apache.commons.cli.Option");
      Option option0 = option_Builder0.build();
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, "org.apache.commons.cli.Option", option0);
      Option option1 = missingArgumentException0.getOption();
      assertTrue(option1.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Option option0 = Option.Option1("m", "m");
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, "j=XDFq^zS*0=F1j[9f", option0);
      option0.setArgs(0);
      Option option1 = missingArgumentException0.getOption();
      assertFalse(option1.hasArgName());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      // Undeclared exception!
      try { 
        MissingArgumentException.MissingArgumentException1(1, "~m=A%.&|J:F", (Option) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.MissingArgumentException", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Option option0 = Option.Option1("NO_ARGS_ALLOWED", "NO_ARGS_ALLOWED");
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1((-1), "NO_ARGS_ALLOWED", option0);
      assertNotNull(missingArgumentException0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("org.apache.commons.cli.Option");
      Option option0 = option_Builder0.build();
      MissingArgumentException missingArgumentException0 = new MissingArgumentException((-925), "org.apache.commons.cli.Option", option0);
      Option option1 = missingArgumentException0.getOption();
      assertNull(option1);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      MissingArgumentException missingArgumentException0 = MissingArgumentException.MissingArgumentException1(1, (String) null, option0);
      Option option1 = missingArgumentException0.getOption();
      assertEquals('\u0000', option1.getValueSeparator());
  }
}
