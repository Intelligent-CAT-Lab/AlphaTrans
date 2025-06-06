
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
import java.util.Collection;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionGroup;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptionGroup_ESTest extends OptionGroup_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      optionGroup0.setRequired(true);
      boolean boolean0 = optionGroup0.isRequired();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.longOpt("--");
      Option option0 = new Option(2147483645, ",#mo|9z3u<6T*", "--", "The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. ", true, option_Builder1);
      optionGroup0.setSelected(option0);
      String string0 = optionGroup0.getSelected();
      assertEquals("--", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = option_Builder0.build();
      optionGroup0.setSelected(option0);
      String string0 = optionGroup0.getSelected();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option(703, "org.apache.commons.cli.Option$Builder", "]", "]", true, option_Builder0);
      optionGroup0.setRequired(true);
      optionGroup0.addOption(option0);
      assertTrue(optionGroup0.isRequired());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      // Undeclared exception!
      try { 
        optionGroup0.addOption((Option) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.OptionGroup", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Collection<Option> collection0 = optionGroup0.getOptions();
      assertNotNull(collection0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option(1, ",#mo|9z3u<6T*", "", "", false, option_Builder0);
      optionGroup0.addOption(option0);
      Option.Builder option_Builder1 = option_Builder0.longOpt("--");
      Option option1 = new Option(2147483645, ",#mo|9z3u<6T*", "--", "The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. ", true, option_Builder1);
      OptionGroup optionGroup1 = optionGroup0.addOption(option1);
      String string0 = optionGroup1.toString();
      assertEquals("[--null, ----]", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option option0 = Option.Option1("JN", "=x@IC-)5T]Z9qG'[}l");
      optionGroup0.addOption(option0);
      String string0 = optionGroup0.toString();
      assertEquals("[-JN =x@IC-)5T]Z9qG'[}l]", string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = option_Builder0.build();
      optionGroup0.setSelected(option0);
      optionGroup0.setSelected(option0);
      assertEquals((-1), Option.UNINITIALIZED);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option(1, ",#mo|9z3u<6T*", "", "", false, option_Builder0);
      Option.Builder option_Builder1 = option_Builder0.longOpt("--");
      Option option1 = new Option(2147483645, ",#mo|9z3u<6T*", "--", "The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. ", true, option_Builder1);
      optionGroup0.setSelected(option1);
      try { 
        optionGroup0.setSelected(option0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // The option 'null' was specified but an option from this group has already been selected: '--'
         //
         verifyException("org.apache.commons.cli.AlreadySelectedException", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      optionGroup0.setSelected((Option) null);
      assertNull(optionGroup0.getSelected());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      String string0 = optionGroup0.getSelected();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      Collection<String> collection0 = optionGroup0.getNames();
      assertNotNull(collection0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      OptionGroup optionGroup0 = new OptionGroup();
      boolean boolean0 = optionGroup0.isRequired();
      assertFalse(boolean0);
  }
}
