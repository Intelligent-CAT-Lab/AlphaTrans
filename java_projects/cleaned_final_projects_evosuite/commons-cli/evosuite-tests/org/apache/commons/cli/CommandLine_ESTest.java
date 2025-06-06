
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
import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.Option;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CommandLine_ESTest extends CommandLine_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.option("");
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      Option option1 = option_Builder0.build();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String[] stringArray0 = commandLine0.getOptionValues1(option1);
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.valueSeparator0();
      option_Builder1.longOpt("P z=Y");
      option_Builder0.hasArgs();
      Option option0 = option_Builder0.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      option0.addValueForProcessing("P z=Y");
      Properties properties0 = commandLine0.getOptionProperties1("P z=Y");
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.valueSeparator0();
      option_Builder1.hasArgs();
      option_Builder1.longOpt("P z=Y");
      Option option0 = option_Builder0.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      option0.addValueForProcessing("org.apache.commons.cli.CommandLine");
      CommandLine commandLine0 = commandLine_Builder1.build();
      Properties properties0 = commandLine0.getOptionProperties0(option0);
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("", "");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      Option option1 = Option.Option2("", true, (String) null);
      Properties properties0 = commandLine0.getOptionProperties0(option1);
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.addArg("l+J,/7dJzJM?GcA\"T");
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Class<Option> class0 = Option.class;
      option_Builder1.type(class0);
      option_Builder0.longOpt("Y");
      Option option0 = option_Builder0.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder1.build();
      Object object0 = commandLine0.getOptionObject1("Y");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("Y", "Y");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      boolean boolean0 = commandLine0.hasOption2("Y");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("Y", "Y");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      boolean boolean0 = commandLine0.hasOption0('Y');
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt(" $ip");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing(" $ip");
      CommandLine commandLine0 = commandLine_Builder0.build();
      Object object0 = commandLine0.getParsedOptionValue2(" $ip");
      assertEquals(" $ip", object0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.longOpt("");
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      Option[] optionArray0 = commandLine0.getOptions();
      assertEquals(1, optionArray0.length);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      String[] stringArray0 = commandLine0.getOptionValues2("Y");
      assertEquals(1, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      String[] stringArray0 = commandLine0.getOptionValues0('Y');
      assertEquals(1, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.getOptionValue5((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.getOptionValue5("Jpx]bJzR{{!bhe$]Si", "");
      assertEquals("", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      option_Builder0.longOpt("Y");
      Option option0 = option_Builder1.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder1.build();
      String string0 = commandLine0.getOptionValue4("Y");
      assertEquals("Y", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("");
      CommandLine commandLine0 = commandLine_Builder1.build();
      String string0 = commandLine0.getOptionValue4("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1((String) null, (String) null);
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue3(option0, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("");
      Option option0 = option_Builder0.build();
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.getOptionValue3(option0, "");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.hasArg0();
      option_Builder0.longOpt("Y");
      Option option0 = option_Builder0.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder1.build();
      String string0 = commandLine0.getOptionValue2(option0);
      assertEquals("Y", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.getOptionValue1('9', (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue1('5', "");
      assertNotNull(string0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue0('Y');
      assertEquals("Y", string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.hasArg0();
      option_Builder0.longOpt("Y");
      Option option0 = option_Builder0.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder1.build();
      Object object0 = commandLine0.getOptionObject1("Y");
      assertEquals("Y", object0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addArg("7");
      CommandLine commandLine0 = commandLine_Builder1.build();
      String[] stringArray0 = commandLine0.getArgs();
      assertEquals(1, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addArg("");
      CommandLine commandLine0 = commandLine_Builder1.build();
      List<String> list0 = commandLine0.getArgList();
      assertEquals(1, list0.size());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.hasOption2("oBl{\"?:$tOSy");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.hasOption0('+');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Class<Option> class0 = Option.class;
      option_Builder0.type(class0);
      Option option0 = option_Builder1.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("w[p;");
      CommandLine commandLine0 = commandLine_Builder1.build();
      try { 
        commandLine0.getParsedOptionValue2("Y");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to handle the class: class org.apache.commons.cli.Option
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("Y", "Y");
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getParsedOptionValue2((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Class<Option> class0 = Option.class;
      option_Builder1.type(class0);
      option_Builder1.longOpt("P z=Y");
      Option option0 = option_Builder0.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      CommandLine commandLine0 = commandLine_Builder1.build();
      try { 
        commandLine0.getParsedOptionValue1(option0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to handle the class: class org.apache.commons.cli.Option
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      commandLine_Builder0.addOption((Option) null);
      Option option0 = Option.Option1("Y", "Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      // Undeclared exception!
      try { 
        commandLine0.getParsedOptionValue1(option0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getParsedOptionValue0('');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder0.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValues2("u_^lb~8=xM>%5");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValues0('7');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("Y", "[ option: null   [ARG] :: null :: class java.lang.Object ]");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValue5((String) null, ".");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1((String) null, (String) null);
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValue4((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      commandLine_Builder0.addOption((Option) null);
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.longOpt("Y");
      Option option0 = option_Builder1.build();
      CommandLine commandLine0 = commandLine_Builder0.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValue2(option0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValue1('c', "IhF\" _O%X");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValue0('f');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionProperties1("Exception found converting ");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder1.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionProperties0((Option) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("Y", "Y");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionObject1((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      commandLine0.addOption((Option) null);
      // Undeclared exception!
      try { 
        commandLine0.getOptionObject0('\u001F');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      Option option0 = Option.Option1("", (String) null);
      boolean boolean0 = commandLine0.hasOption1(option0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      Object object0 = commandLine0.getParsedOptionValue1((Option) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      String[] stringArray0 = commandLine0.getOptionValues1(option0);
      assertEquals(1, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1((String) null, (String) null);
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder1.build();
      String[] stringArray0 = commandLine0.getOptionValues1((Option) null);
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      commandLine_Builder0.addOption((Option) null);
      CommandLine commandLine0 = commandLine_Builder0.build();
      // Undeclared exception!
      try { 
        commandLine0.getOptionValues1((Option) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.CommandLine", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      option_Builder0.option("Y");
      Option option0 = option_Builder1.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("w[p;");
      CommandLine commandLine0 = commandLine_Builder1.build();
      String string0 = commandLine0.getOptionValue3(option0, "AO5awyh8i6aR{9hp");
      assertEquals("w[p;", string0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("");
      CommandLine commandLine0 = commandLine_Builder1.build();
      String string0 = commandLine0.getOptionValue2(option0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = option_Builder0.build();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue2(option0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue2((Option) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      String string0 = commandLine0.getOptionValue4("i}m6]H");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      boolean boolean0 = commandLine0.hasOption2("oBl{\"?:$tOSy");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      Object object0 = commandLine0.getParsedOptionValue2(" $ip");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("P z=Y");
      Option option0 = option_Builder0.build();
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      String[] stringArray0 = commandLine0.getOptionValues2("P z=Y");
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.longOpt("Y");
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      boolean boolean0 = commandLine0.hasOption1(option0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("Y");
      Option option0 = option_Builder0.build();
      CommandLine.Builder commandLine_Builder1 = commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder1.build();
      String[] stringArray0 = commandLine0.getOptionValues0('L');
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue5("Y", "Y");
      assertEquals("Y", string0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      option_Builder1.longOpt("P z=Y");
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      Object object0 = commandLine0.getParsedOptionValue1(option0);
      assertEquals("P z=Y", object0);
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("P z=Y");
      Option option0 = option_Builder0.build();
      CommandLine commandLine0 = commandLine_Builder0.build();
      Object object0 = commandLine0.getParsedOptionValue1(option0);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties1("Y");
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.valueSeparator0();
      option_Builder1.longOpt("P z=Y");
      option_Builder0.hasArgs();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties1("P z=Y");
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("", "");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties1("{4");
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder1("Y");
      Option option0 = option_Builder0.build();
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties1("Y");
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      option_Builder1.longOpt("P z=Y");
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties0(option0);
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.valueSeparator0();
      option_Builder1.longOpt("P z=Y");
      option_Builder1.hasArgs();
      Option option0 = option_Builder1.build();
      commandLine_Builder0.addOption(option0);
      option0.addValueForProcessing("P z=Y");
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties0(option0);
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      Option option0 = Option.Option1("Y", "Y");
      commandLine_Builder0.addOption(option0);
      CommandLine commandLine0 = commandLine_Builder0.build();
      Properties properties0 = commandLine0.getOptionProperties0((Option) null);
      assertNotNull(properties0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      Object object0 = commandLine0.getOptionObject0('\u001F');
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String[] stringArray0 = commandLine0.getArgs();
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      Option[] optionArray0 = commandLine0.getOptions();
      assertEquals(0, optionArray0.length);
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue0('7');
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      Object object0 = commandLine0.getParsedOptionValue0('F');
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      String string0 = commandLine0.getOptionValue1('/', "<d\rCWue");
      assertEquals("<d\rCWue", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      CommandLine commandLine0 = new CommandLine();
      List<String> list0 = commandLine0.getArgList();
      assertTrue(list0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      Iterator<Option> iterator0 = commandLine0.iterator();
      assertNotNull(iterator0);
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      CommandLine.Builder commandLine_Builder0 = new CommandLine.Builder();
      CommandLine commandLine0 = commandLine_Builder0.build();
      boolean boolean0 = commandLine0.hasOption0('L');
      assertFalse(boolean0);
  }
}
