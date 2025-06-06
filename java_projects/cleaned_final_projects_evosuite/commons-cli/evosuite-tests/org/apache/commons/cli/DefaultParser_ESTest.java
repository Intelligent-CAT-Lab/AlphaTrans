
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
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionGroup;
import org.apache.commons.cli.Options;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultParser_ESTest extends DefaultParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Boolean boolean0 = Boolean.valueOf(false);
      DefaultParser defaultParser0 = new DefaultParser(0, true, boolean0);
      defaultParser0.handleConcatenatedOptions("");
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Options options0 = new Options();
      String[] stringArray0 = new String[4];
      stringArray0[0] = "----bHyQ}NI|`fyQSze=|";
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      defaultParser_Builder0.setAllowPartialMatching(false);
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      try { 
        defaultParser0.parse0(options0, stringArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: ----bHyQ}NI|`fyQSze=|
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      Options options0 = new Options();
      String[] stringArray0 = new String[5];
      stringArray0[0] = "A[:Tyr#Yqv";
      defaultParser0.parse1(options0, stringArray0, true);
      defaultParser0.checkRequiredOptions();
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Options options0 = new Options();
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[5];
      stringArray0[0] = "-e=Q}!8Te5`g(/W8`I/";
      CommandLine commandLine0 = defaultParser0.parse1(options0, stringArray0, true);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Boolean boolean0 = Boolean.valueOf(false);
      DefaultParser defaultParser0 = new DefaultParser(0, true, boolean0);
      Options options0 = new Options();
      Properties properties0 = new Properties();
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-;RfOwY";
      CommandLine commandLine0 = defaultParser0.parse3(options0, stringArray0, properties0, true);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Options options0 = new Options();
      String[] stringArray0 = new String[6];
      stringArray0[0] = "----bHyQ}NI|`fyQSze=|";
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      CommandLine commandLine0 = defaultParser0.parse1(options0, stringArray0, true);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Options options0 = new Options();
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      String[] stringArray0 = new String[1];
      stringArray0[0] = "-,";
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      Properties properties0 = new Properties();
      try { 
        defaultParser0.parse3(options0, stringArray0, properties0, false);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: -,
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      DefaultParser defaultParser0 = new DefaultParser(1757, true, boolean0);
      Options options0 = new Options();
      Properties properties0 = new Properties();
      String[] stringArray0 = new String[2];
      properties0.put(defaultParser0, "EG'LT");
      stringArray0[0] = "EG'LT";
      // Undeclared exception!
      try { 
        defaultParser0.parse3(options0, stringArray0, properties0, true);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class org.apache.commons.cli.DefaultParser cannot be cast to class java.lang.String (org.apache.commons.cli.DefaultParser is in unnamed module of loader org.evosuite.instrumentation.InstrumentingClassLoader @163a30b3; java.lang.String is in module java.base of loader 'bootstrap')
         //
         verifyException("java.util.Properties", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Options options0 = new Options();
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[0];
      Properties properties0 = new Properties();
      properties0.put(defaultParser_Builder0, defaultParser_Builder0);
      // Undeclared exception!
      try { 
        defaultParser0.parse2(options0, stringArray0, properties0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class org.apache.commons.cli.DefaultParser$Builder cannot be cast to class java.lang.String (org.apache.commons.cli.DefaultParser$Builder is in unnamed module of loader org.evosuite.instrumentation.InstrumentingClassLoader @163a30b3; java.lang.String is in module java.base of loader 'bootstrap')
         //
         verifyException("java.util.Properties", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Options options0 = new Options();
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      defaultParser0.parse1(options0, (String[]) null, false);
      try { 
        defaultParser0.handleConcatenatedOptions("-^V'Itm$AU9=5");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: -^V'Itm$AU9=5
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      DefaultParser defaultParser0 = new DefaultParser(1507, false, boolean0);
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Object object0 = new Object();
      linkedList0.offer(object0);
      defaultParser0.expectedOpts = (List) linkedList0;
      try { 
        defaultParser0.checkRequiredOptions();
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Missing required option: java.lang.Object@2f81c924
         //
         verifyException("org.apache.commons.cli.MissingOptionException", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Boolean boolean0 = Boolean.FALSE;
      DefaultParser defaultParser0 = new DefaultParser(0, false, boolean0);
      // Undeclared exception!
      try { 
        defaultParser0.checkRequiredOptions();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DefaultParser defaultParser0 = new DefaultParser((-1855), false, (Boolean) null);
      Options options0 = new Options();
      Properties properties0 = new Properties();
      CommandLine commandLine0 = defaultParser0.parse3(options0, (String[]) null, properties0, true);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Boolean boolean0 = Boolean.valueOf(false);
      DefaultParser defaultParser0 = new DefaultParser(0, false, boolean0);
      Options options0 = new Options();
      OptionGroup optionGroup0 = new OptionGroup();
      Option option0 = Option.Option1("", "<Y");
      OptionGroup optionGroup1 = optionGroup0.addOption(option0);
      options0.addOptionGroup(optionGroup1);
      String[] stringArray0 = new String[9];
      // Undeclared exception!
      try { 
        defaultParser0.parse3(options0, stringArray0, (Properties) null, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      DefaultParser defaultParser0 = new DefaultParser(1, false, boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Options options0 = new Options();
      options0.addRequiredOption("a7", "a7", true, "a7");
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      Boolean boolean0 = Boolean.TRUE;
      defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0);
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[5];
      stringArray0[0] = "--a7";
      Properties properties0 = new Properties();
      // Undeclared exception!
      try { 
        defaultParser0.parse2(options0, stringArray0, properties0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addRequiredOption("a7", "a7", true, "a7");
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[8];
      stringArray0[0] = "--a7";
      stringArray0[1] = "---e=Q}!8Te5`g(/W8`I/";
      // Undeclared exception!
      try { 
        defaultParser0.parse0(options1, stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      DefaultParser defaultParser0 = new DefaultParser(2786, false, boolean0);
      Options options0 = new Options();
      Properties properties0 = new Properties();
      String[] stringArray0 = new String[9];
      stringArray0[0] = "wF_;l@-0|Ks\"";
      stringArray0[1] = "-";
      // Undeclared exception!
      try { 
        defaultParser0.parse3(options0, stringArray0, properties0, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      DefaultParser defaultParser0 = new DefaultParser(2786, false, boolean0);
      Options options0 = new Options();
      String[] stringArray0 = new String[2];
      stringArray0[0] = "--";
      Properties properties0 = new Properties();
      CommandLine commandLine0 = defaultParser0.parse2(options0, stringArray0, properties0);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Boolean boolean0 = Boolean.valueOf(false);
      DefaultParser defaultParser0 = new DefaultParser(0, true, boolean0);
      Options options0 = new Options();
      String[] stringArray0 = new String[3];
      stringArray0[0] = "a72@9'`8,";
      stringArray0[1] = "-^V'Itm$9U9=5";
      try { 
        defaultParser0.parse0(options0, stringArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: -^V'Itm$9U9=5
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      Options options0 = new Options();
      options0.addRequiredOption("17Q", "a7", true, "17Q");
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[5];
      stringArray0[0] = "--a7";
      stringArray0[1] = "a7";
      stringArray0[2] = "-e=Q}!8Te5`g(/W8`I/";
      try { 
        defaultParser0.parse0(options0, stringArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: -e=Q}!8Te5`g(/W8`I/
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      Options options0 = new Options();
      DefaultParser defaultParser0 = new DefaultParser(0, true, boolean0);
      String[] stringArray0 = new String[5];
      stringArray0[0] = "HNb#}Cz Zh";
      stringArray0[1] = "-Y";
      try { 
        defaultParser0.parse1(options0, stringArray0, false);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: -Y
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Options options0 = new Options();
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      Properties properties0 = new Properties();
      properties0.put("a7", defaultParser_Builder0);
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      try { 
        defaultParser0.parse2(options0, (String[]) null, properties0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Default option wasn't defined
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Options options0 = new Options();
      OptionGroup optionGroup0 = new OptionGroup();
      Option option0 = Option.Option2("a7", false, "a7");
      OptionGroup optionGroup1 = optionGroup0.addOption(option0);
      Options options1 = options0.addOptionGroup(optionGroup1);
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[7];
      stringArray0[0] = "a7";
      stringArray0[1] = "-a7";
      // Undeclared exception!
      try { 
        defaultParser0.parse0(options1, stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Options options0 = new Options();
      Options options1 = options0.addRequiredOption("a7", "a7", true, "a7");
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      Boolean boolean0 = Boolean.valueOf("---e=Q}!8Te5`g(/W8`I/");
      defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0);
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[8];
      stringArray0[0] = "--a7";
      stringArray0[2] = "---e=Q}!8Te5`g(/W8`I/";
      try { 
        defaultParser0.parse0(options1, stringArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unrecognized option: ---e=Q}!8Te5`g(/W8`I/
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      Options options0 = new Options();
      Properties properties0 = new Properties();
      DefaultParser defaultParser0 = new DefaultParser((-77807378), true, boolean0);
      String[] stringArray0 = new String[1];
      stringArray0[0] = "--<Y";
      defaultParser0.parse3(options0, stringArray0, properties0, true);
      defaultParser0.handleConcatenatedOptions("--)");
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Boolean boolean0 = Boolean.FALSE;
      DefaultParser defaultParser0 = new DefaultParser(1757, true, boolean0);
      // Undeclared exception!
      try { 
        defaultParser0.handleConcatenatedOptions("-\"%Y6)Hb@!U0");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.DefaultParser", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      defaultParser0.handleConcatenatedOptions("]");
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Options options0 = new Options();
      options0.addRequiredOption("a7", "a7", true, "a7");
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      defaultParser_Builder0.setAllowPartialMatching(false);
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[2];
      stringArray0[0] = "--a7";
      // Undeclared exception!
      try { 
        defaultParser0.parse1(options0, stringArray0, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Boolean boolean0 = Boolean.FALSE;
      DefaultParser defaultParser0 = new DefaultParser(1757, true, boolean0);
      Options options0 = new Options();
      options0.addRequiredOption("a7", "a7", true, "a7");
      String[] stringArray0 = new String[5];
      stringArray0[0] = "--a7";
      stringArray0[1] = "-\"%Y6)Hb@!U0";
      stringArray0[2] = "--a7";
      stringArray0[3] = "a7";
      stringArray0[4] = "e=Q}!8Te5`g(/W8`I/";
      CommandLine commandLine0 = defaultParser0.parse0(options0, stringArray0);
      assertNotNull(commandLine0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Boolean boolean0 = Boolean.FALSE;
      Options options0 = new Options();
      options0.addRequiredOption("a7", "a7", true, "a7");
      DefaultParser.Builder defaultParser_Builder0 = DefaultParser.builder();
      defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0);
      Option.Builder option_Builder0 = Option.builder1("a7");
      Option.Builder option_Builder1 = option_Builder0.hasArgs();
      Option option0 = option_Builder1.build();
      options0.addOption0(option0);
      DefaultParser defaultParser0 = defaultParser_Builder0.build();
      String[] stringArray0 = new String[5];
      stringArray0[0] = "--a7";
      Properties properties0 = new Properties();
      try { 
        defaultParser0.parse2(options0, stringArray0, properties0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Missing required option: a7
         //
         verifyException("org.apache.commons.cli.MissingOptionException", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Boolean boolean0 = Boolean.TRUE;
      DefaultParser defaultParser0 = new DefaultParser((-2), false, boolean0);
      Options options0 = new Options();
      options0.addRequiredOption("17Q", "a7", true, "17Q");
      Properties properties0 = new Properties();
      String[] stringArray0 = new String[2];
      stringArray0[0] = "--a7";
      stringArray0[1] = "--a7";
      try { 
        defaultParser0.parse2(options0, stringArray0, properties0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Missing argument for option: 17Q
         //
         verifyException("org.apache.commons.cli.MissingArgumentException", e);
      }
  }
}
