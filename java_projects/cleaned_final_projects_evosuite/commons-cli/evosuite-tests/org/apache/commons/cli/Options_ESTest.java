
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
import java.util.List;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionGroup;
import org.apache.commons.cli.Options;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Options_ESTest extends Options_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addRequiredOption("4M", (String) null, true, "4M");
      assertSame(options0, options1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.addOption1("<;KF0E4@i;7}+,|l", false, "C6;r`@:sh`rI");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option '<;KF0E4@i;7}+,|l' contains an illegal character : '<'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Options options0 = new Options();
      List<Option> list0 = options0.helpOptions();
      assertTrue(list0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Options options0 = new Options();
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option(1, " :: ", "N,?#*fE", (String) null, true, option_Builder0);
      Options options1 = options0.addOption0(option0);
      List<Option> list0 = options1.helpOptions();
      assertFalse(list0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Option option0 = Option.Option2((String) null, true, "!?iczs^t1=D2BcoQp");
      Options options0 = new Options();
      OptionGroup optionGroup0 = options0.getOptionGroup(option0);
      assertNull(optionGroup0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Options options0 = new Options();
      OptionGroup optionGroup0 = new OptionGroup();
      Option option0 = Option.Option1("", "~%:SVI2n");
      OptionGroup optionGroup1 = optionGroup0.addOption(option0);
      optionGroup1.setRequired(true);
      options0.addOptionGroup(optionGroup1);
      OptionGroup optionGroup2 = options0.getOptionGroup(option0);
      assertNotNull(optionGroup2);
      assertFalse(option0.isRequired());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Options options0 = new Options();
      OptionGroup optionGroup0 = new OptionGroup();
      Option option0 = Option.Option1("", "~%:SVI2n");
      OptionGroup optionGroup1 = optionGroup0.addOption(option0);
      options0.addOptionGroup(optionGroup1);
      OptionGroup optionGroup2 = options0.getOptionGroup(option0);
      assertFalse(option0.isRequired());
      assertNotNull(optionGroup2);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Options options0 = new Options();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.required1(true);
      Option option0 = new Option(1, " :: ", "N,?#*fE", (String) null, true, option_Builder1);
      options0.addOption0(option0);
      Option option1 = options0.getOption((String) null);
      assertNull(option1.getLongOpt());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Options options0 = new Options();
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option(1, " :: ", "N,?#*fE", (String) null, true, option_Builder0);
      option0.setValueSeparator('|');
      Options options1 = options0.addOption0(option0);
      Option option1 = options1.getOption((String) null);
      assertEquals((-2), Option.UNLIMITED_VALUES);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Options options0 = new Options();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.hasArgs();
      Option option0 = new Option((-1092), "C*913)Z?>h^g\"Q=", "k", "C*913)Z?>h^g\"Q=", false, option_Builder0);
      options0.addOption0(option0);
      Option option1 = options0.getOption((String) null);
      assertNull(option1.getValue0());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption3("s", "nIW;QV\"gUH+C", true, "nIW;QV\"gUH+C");
      Option option0 = options1.getOption("nIW;QV\"gUH+C");
      assertEquals("nIW;QV\"gUH+C", option0.getDescription());
      assertEquals(1, option0.getArgs());
      assertNotNull(option0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption1("KZ", true, "KZ");
      assertSame(options1, options0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.addRequiredOption("U1Kpfcbzi<9kEY", "U1Kpfcbzi<9kEY", false, "U1Kpfcbzi<9kEY");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'U1Kpfcbzi<9kEY' contains an illegal character : '<'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.addOptionGroup((OptionGroup) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Options", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.addOption3("U1Kpfcbzi<9kEY", "U1Kpfcbzi<9kEY", false, "U1Kpfcbzi<9kEY");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'U1Kpfcbzi<9kEY' contains an illegal character : '<'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.addOption2(")I.%HqO($VQ", ")I.%HqO($VQ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option ')I.%HqO($VQ' contains an illegal character : ')'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.addOption0((Option) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Options", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Options options0 = new Options();
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.longOpt("");
      Option option0 = option_Builder1.build();
      Options options1 = options0.addOption0(option0);
      assertSame(options0, options1);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption3("", "", true, "");
      boolean boolean0 = options1.hasShortOption("");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Options options0 = new Options();
      boolean boolean0 = options0.hasShortOption("N,?#*fE");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Options options0 = new Options();
      options0.addOption3("", "nIW;QV\"gUH+C", true, "nIW;QV\"gUH+C");
      boolean boolean0 = options0.hasOption("nIW;QV\"gUH+C");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption2((String) null, (String) null);
      boolean boolean0 = options1.hasOption((String) null);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Options options0 = new Options();
      boolean boolean0 = options0.hasOption("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Options options0 = new Options();
      boolean boolean0 = options0.hasLongOption((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Options options0 = new Options();
      Option option0 = options0.getOption((String) null);
      assertNull(option0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Options options0 = new Options();
      options0.addRequiredOption("", "B", true, "B");
      List<String> list0 = options0.getMatchingOptions("");
      assertTrue(list0.contains("B"));
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption3("", "", true, "");
      List<String> list0 = options1.getMatchingOptions("sU`d");
      assertEquals(0, list0.size());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption3((String) null, "'6MWzZs~t'1", true, (String) null);
      // Undeclared exception!
      try { 
        options1.getMatchingOptions((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Options options0 = new Options();
      options0.addOption3("", "nIW;QV\"gUH+C", true, "nIW;QV\"gUH+C");
      List<String> list0 = options0.getMatchingOptions("nIW;QV\"gUH+C");
      assertTrue(list0.contains("nIW;QV\"gUH+C"));
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Options options0 = new Options();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.required1(true);
      Option option0 = new Option(1, " :: ", "N,?#*fE", (String) null, true, option_Builder1);
      Options options1 = options0.addOption0(option0);
      Options options2 = options0.addOption0(option0);
      assertSame(options2, options1);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "N,?#*fE");
      assertSame(options1, options0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Options options0 = new Options();
      Collection<OptionGroup> collection0 = options0.getOptionGroups();
      assertNotNull(collection0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        options0.getOptionGroup((Option) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Options", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Options options0 = new Options();
      String string0 = options0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Options options0 = new Options();
      List list0 = options0.getRequiredOptions();
      assertEquals(0, list0.size());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Options options0 = new Options();
      Collection<Option> collection0 = options0.getOptions();
      assertNotNull(collection0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addRequiredOption("ab", "ab", false, "ab");
      boolean boolean0 = options1.hasLongOption("ab");
      assertTrue(boolean0);
  }
}
