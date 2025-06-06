
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
import org.apache.commons.cli.Option;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Option_ESTest extends Option_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option((-266), "!#)~^=7Qj1M:N`x", "O5\"EO5B9F:4<A", "8", true, option_Builder0);
      option0.setArgs((-266));
      boolean boolean0 = option0.requiresArg();
      assertEquals((-266), option0.getArgs());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.setValueSeparator('y');
      option0.setArgs('y');
      option0.addValueForProcessing(";mn#dgl4w341i3y1q?F");
      assertEquals(121, option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      option_Builder0.numberOfArgs(0);
      Option option0 = new Option((-166), "mnWdglww341i3yRq?F", (String) null, "", true, option_Builder0);
      // Undeclared exception!
      try { 
        option0.addValueForProcessing("");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Cannot add value, list full.
         //
         verifyException("org.apache.commons.cli.Option", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.valueSeparator1(',');
      assertSame(option_Builder0, option_Builder1);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.required1(false);
      assertSame(option_Builder1, option_Builder0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      Object object0 = option0.getType();
      option0.setType1(object0);
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.required0();
      Option option0 = new Option(48, "", "", "g/SNMWkTVe|,Z$", false, option_Builder1);
      boolean boolean0 = option0.isRequired();
      assertTrue(boolean0);
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing("");
      option0.getValuesList();
      assertFalse(option0.hasValueSeparator());
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Option option0 = Option.Option2("", true, (String) null);
      option0.setValueSeparator('3');
      char char0 = option0.getValueSeparator();
      assertEquals('3', char0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.setValueSeparator('y');
      char char0 = option0.getValueSeparator();
      assertEquals('y', char0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.getValue2((String) null);
      assertFalse(option0.hasLongOpt());
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing("[ option:   [ARG] ::  :: class java.lang.String ]");
      String string0 = option0.getValue1(0);
      assertFalse(option0.hasLongOpt());
      assertFalse(option0.hasValueSeparator());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing(";mn#dgl4w341i3y1q?F");
      String string0 = option0.getValue0();
      assertFalse(option0.hasValueSeparator());
      assertNotNull(string0);
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option((-1), "", "", "", false, option_Builder0);
      option0.getType();
      assertEquals('0', option0.getValueSeparator());
      assertFalse(option0.isRequired());
      assertFalse(option0.hasOptionalArg());
      assertEquals(1, option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = new Option((-1), "", ">~DUr<`Nbfb/{,", "@;#u#<0I", false, option_Builder0);
      option0.getOpt();
      assertEquals('0', option0.getValueSeparator());
      assertFalse(option0.hasOptionalArg());
      assertFalse(option0.isRequired());
      assertEquals(1, option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Option option0 = Option.Option2("o7", false, "Kd");
      String string0 = option0.getOpt();
      assertNotNull(string0);
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
      assertEquals("Kd", option0.getDescription());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      String string0 = option0.getLongOpt();
      assertEquals((-1), option0.getArgs());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("~wM:b");
      Option option0 = option_Builder0.build();
      option0.getLongOpt();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option((-664), "org.apache.commons.cli.Option$1", "org.apache.commons.cli.Option$1", "<u0;", true, option_Builder0);
      option0.getKey();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Option option0 = Option.Option1("j", "");
      String string0 = option0.getKey();
      assertEquals((-1), option0.getArgs());
      assertEquals("", option0.getDescription());
      assertFalse(option0.hasLongOpt());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Option option0 = Option.Option2("", false, "LDE$IPc0Ine3waBb9x");
      String string0 = option0.getKey();
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
      assertNotNull(string0);
      assertEquals("LDE$IPc0Ine3waBb9x", option0.getDescription());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1((String) null);
      Option.Builder option_Builder1 = option_Builder0.longOpt("Ul6P5;IM>9m,Q(Rv4");
      Option option0 = option_Builder1.build();
      int int0 = option0.getId();
      assertEquals(85, int0);
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.desc("A CloneNotSupportedException was thrown: ");
      Option option0 = new Option((-215), "A CloneNotSupportedException was thrown: ", "A CloneNotSupportedException was thrown: ", "A CloneNotSupportedException was thrown: ", false, option_Builder0);
      option0.getDescription();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      String string0 = option0.getDescription();
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.numberOfArgs(48);
      Option option0 = new Option(48, "", "", "", false, option_Builder0);
      int int0 = option0.getArgs();
      assertEquals(48, int0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Option option0 = Option.Option2("", false, "LDE$IPc0Ine3waBb9x");
      option0.setArgName("Illegal option name '");
      option0.getArgName();
      assertEquals("LDE$IPc0Ine3waBb9x", option0.getDescription());
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Option option0 = Option.Option1("", ">}H/I`");
      option0.setArgName("");
      option0.getArgName();
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
      assertEquals(">}H/I`", option0.getDescription());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing("");
      try { 
        option0.getValue1(2757);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      // Undeclared exception!
      try { 
        Option.builder1("*^5MS$s9`|cUF+VY");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option '*^5MS$s9`|cUF+VY' contains an illegal character : '*'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Option option0 = Option.Option2((String) null, true, (String) null);
      option0.setValueSeparator('I');
      // Undeclared exception!
      try { 
        option0.addValueForProcessing((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Option", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      try { 
        Option.Option2("m\",{Wl:.*:", false, "m\",{Wl:.*:");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'm\",{Wl:.*:' contains an illegal character : '\"'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      try { 
        Option.Option1("P6UGMg;=r~{Ai9~r", "P6UGMg;=r~{Ai9~r");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'P6UGMg;=r~{Ai9~r' contains an illegal character : ';'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Option option0 = null;
      try {
        option0 = new Option((-3), "org.apache.commons.cli.OptionValidator", "org.apache.commons.cli.OptionValidator", "org.apache.commons.cli.OptionValidator", true, (Option.Builder) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.Option$Builder", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Option option0 = null;
      try {
        option0 = new Option(0, ">4", ">4", ">4", false, (Option.Builder) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option '>4' contains an illegal character : '>'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      option0.setValueSeparator('3');
      boolean boolean0 = option0.hasValueSeparator();
      assertEquals('3', option0.getValueSeparator());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      boolean boolean0 = option0.hasValueSeparator();
      assertEquals((-1), option0.getArgs());
      assertFalse(boolean0);
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Option option0 = Option.Option1("w", "w");
      boolean boolean0 = option0.hasArgs();
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.numberOfArgs(48);
      Option option0 = new Option(48, "", "", "", false, option_Builder0);
      boolean boolean0 = option0.hasArgs();
      assertTrue(boolean0);
      assertEquals(48, option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("~wM:b");
      Option.Builder option_Builder1 = option_Builder0.hasArgs();
      Option option0 = option_Builder1.build();
      boolean boolean0 = option0.hasArgs();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArgs();
      Option option0 = new Option(1777, "", "", "", true, option_Builder1);
      boolean boolean0 = option0.hasArg();
      assertTrue(boolean0);
      assertEquals((-2), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option((-1), "", "", "", true, option_Builder0);
      boolean boolean0 = option0.hasArg();
      assertEquals('0', option0.getValueSeparator());
      assertTrue(boolean0);
      assertFalse(option0.hasOptionalArg());
      assertFalse(option0.isRequired());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Option option0 = Option.Option1("5l", "5l");
      boolean boolean0 = option0.hasArg();
      assertFalse(boolean0);
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing("");
      String string0 = option0.getValue0();
      assertFalse(option0.hasLongOpt());
      assertNotNull(string0);
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = new Option(48, "", "", "g/SNMWkTVe|,Z$", false, option_Builder0);
      option0.getValue0();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      Option option0 = new Option(0, "4Yl0", "4Yl0", "4Yl0", false, (Option.Builder) null);
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      char char0 = option0.getValueSeparator();
      assertFalse(option0.hasLongOpt());
      assertEquals('\u0000', char0);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.longOpt("");
      Option option0 = option_Builder0.build();
      option0.hasOptionalArg();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.option("");
      assertSame(option_Builder1, option_Builder0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option option0 = new Option((-1), "", "", "", false, option_Builder0);
      String string0 = option0.toString();
      assertFalse(option0.isRequired());
      assertEquals("[ option: null  [ARG] ::  ]", string0);
      assertEquals('0', option0.getValueSeparator());
      assertFalse(option0.hasOptionalArg());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      assertFalse(option0.hasLongOpt());
      
      option0.setLongOpt("");
      String string0 = option0.toString();
      assertEquals("[ option:    ::  :: class java.lang.String ]", string0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.hasArgs();
      Option option0 = option_Builder1.build();
      option0.addValueForProcessing("");
      boolean boolean0 = option0.requiresArg();
      assertFalse(boolean0);
      assertTrue(option0.hasArg());
      assertEquals((-2), option0.getArgs());
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option.Builder option_Builder1 = option_Builder0.hasArgs();
      Option option0 = option_Builder1.build();
      boolean boolean0 = option0.requiresArg();
      assertTrue(boolean0);
      assertEquals((-2), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      Option option0 = Option.Option1("6", "6");
      option0.setOptionalArg(true);
      boolean boolean0 = option0.requiresArg();
      assertTrue(option0.hasOptionalArg());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.setValueSeparator(':');
      option0.addValueForProcessing("[ option:   [ARG] ::  :: class java.lang.String ]");
      assertEquals(':', option0.getValueSeparator());
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      assertFalse(option0.hasLongOpt());
      
      option0.setLongOpt("~|}]x'8((y.$0R~Vpz");
      boolean boolean0 = option0.hasLongOpt();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      boolean boolean0 = option0.hasLongOpt();
      assertFalse(boolean0);
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.hasArgs();
      Option option0 = new Option(7330, "7CLs[:", (String) null, "f;3$8j#0IWpx:%", true, option_Builder0);
      String string0 = option0.toString();
      assertEquals("[ option: null [ARG...] :: null :: class java.lang.String ]", string0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      option0.setArgName("");
      boolean boolean0 = option0.hasArgName();
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      Option option0 = Option.Option1("6", "6");
      boolean boolean0 = option0.hasArgName();
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      String[] stringArray0 = option0.getValues();
      assertNull(stringArray0);
      assertFalse(option0.hasLongOpt());
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing("");
      String[] stringArray0 = option0.getValues();
      assertNotNull(stringArray0);
      assertFalse(option0.hasLongOpt());
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      Option option0 = new Option(0, "", "", " [ARG]", true, (Option.Builder) null);
      option0.getValue1(63);
      assertEquals(" [ARG]", option0.getDescription());
      assertEquals("", option0.getLongOpt());
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      String string0 = option0.getValue2("");
      assertEquals('\u0000', option0.getValueSeparator());
      assertFalse(option0.hasLongOpt());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing(" [ARG]");
      String string0 = option0.getValue2("");
      assertFalse(option0.hasLongOpt());
      assertEquals(" [ARG]", string0);
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      // Undeclared exception!
      try { 
        option0.getId();
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      Option option1 = Option.Option1((String) null, "");
      boolean boolean0 = option0.equals(option1);
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option1.getArgs());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      Option option0 = Option.Option1("f6", "f6");
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.longOpt("f6");
      Option option1 = option_Builder1.build();
      boolean boolean0 = option0.equals(option1);
      assertTrue(option1.hasLongOpt());
      assertFalse(boolean0);
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
      assertEquals((-1), option1.getArgs());
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      boolean boolean0 = option0.equals("");
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      Option option0 = Option.Option2("", false, "{LDE$3Pc0Ine3wBb9");
      boolean boolean0 = option0.equals(option0);
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertEquals("{LDE$3Pc0Ine3wBb9", option0.getDescription());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      // Undeclared exception!
      try { 
        option0.addValueForProcessing("");
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // NO_ARGS_ALLOWED
         //
         verifyException("org.apache.commons.cli.Option", e);
      }
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.addValueForProcessing(" [ARG]");
      boolean boolean0 = option0.acceptsArg();
      assertFalse(option0.hasLongOpt());
      assertFalse(boolean0);
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      assertTrue(option0.hasArg());
      
      option0.addValueForProcessing("");
      String string0 = option0.getValue1(0);
      assertNotNull(string0);
      assertFalse(option0.hasValueSeparator());
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg1(false);
      assertSame(option_Builder1, option_Builder0);
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      // Undeclared exception!
      try { 
        option_Builder0.build();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Either opt or longOpt must be specified
         //
         verifyException("org.apache.commons.cli.Option$Builder", e);
      }
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      Option option0 = Option.Option1("6", "6");
      Class<Option> class0 = Option.class;
      option0.setType0(class0);
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      String string0 = option0.getOpt();
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      Option option0 = Option.Option1("X", "X");
      // Undeclared exception!
      try { 
        option0.addValue("X");
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. 
         //
         verifyException("org.apache.commons.cli.Option", e);
      }
  }

  @Test(timeout = 4000)
  public void test77()  throws Throwable  {
      Option option0 = new Option(0, "", "", " [ARG]", true, (Option.Builder) null);
      String string0 = option0.getLongOpt();
      assertEquals("", string0);
      assertEquals(" [ARG]", option0.getDescription());
      assertEquals(1, option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test78()  throws Throwable  {
      Option option0 = Option.Option2("", true, "");
      option0.hashCode();
      assertFalse(option0.hasLongOpt());
      assertEquals(1, option0.getArgs());
      assertFalse(option0.hasValueSeparator());
  }

  @Test(timeout = 4000)
  public void test79()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = new Option(48, "", "", "g/SNMWkTVe|,Z$", false, option_Builder0);
      option0.isRequired();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test80()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder1("");
      Option option0 = new Option(48, "", "", "g/SNMWkTVe|,Z$", false, option_Builder0);
      option0.getDescription();
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test81()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      int int0 = option0.getArgs();
      assertEquals((-1), int0);
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test82()  throws Throwable  {
      Option option0 = Option.Option1("X", "X");
      option0.clearValues();
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test83()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      boolean boolean0 = option0.requiresArg();
      assertFalse(boolean0);
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test84()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      option0.setDescription("");
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
  }

  @Test(timeout = 4000)
  public void test85()  throws Throwable  {
      Option option0 = Option.Option1("6", "6");
      option0.setArgName("6");
      boolean boolean0 = option0.hasArgName();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test86()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      Option option1 = (Option)option0.clone();
      boolean boolean0 = option0.equals(option1);
      assertNotSame(option1, option0);
      assertEquals((-1), option1.getArgs());
      assertTrue(boolean0);
      assertFalse(option1.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test87()  throws Throwable  {
      Option option0 = Option.Option1((String) null, (String) null);
      // Undeclared exception!
      try { 
        option0.getId();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test88()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      option0.getValuesList();
      assertEquals((-1), option0.getArgs());
      assertFalse(option0.hasLongOpt());
  }

  @Test(timeout = 4000)
  public void test89()  throws Throwable  {
      Option option0 = Option.Option1("", "");
      // Undeclared exception!
      try { 
        option0.setType1("");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.String cannot be cast to class java.lang.Class (java.lang.String and java.lang.Class are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.cli.Option", e);
      }
  }

  @Test(timeout = 4000)
  public void test90()  throws Throwable  {
      Option option0 = Option.Option1("X", "X");
      option0.setRequired(true);
      assertTrue(option0.isRequired());
  }

  @Test(timeout = 4000)
  public void test91()  throws Throwable  {
      Option option0 = Option.Option1("6", "6");
      option0.setOptionalArg(true);
      boolean boolean0 = option0.acceptsArg();
      assertTrue(option0.hasOptionalArg());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test92()  throws Throwable  {
      Option option0 = Option.Option2("", false, "LDE$IPc0Ine3waBb9x");
      option0.getArgName();
      assertEquals("LDE$IPc0Ine3waBb9x", option0.getDescription());
      assertFalse(option0.hasLongOpt());
      assertEquals((-1), option0.getArgs());
      assertEquals("", option0.getOpt());
  }

  @Test(timeout = 4000)
  public void test93()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Class<Object> class0 = Object.class;
      Option.Builder option_Builder1 = option_Builder0.type(class0);
      assertSame(option_Builder1, option_Builder0);
  }

  @Test(timeout = 4000)
  public void test94()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.hasArgs();
      Option option0 = new Option(7330, "7CLs[:", (String) null, "f;3$8j#0IWpx:%", true, option_Builder0);
      option0.setValueSeparator(':');
      option0.addValueForProcessing("7CLs[:");
      assertEquals(':', option0.getValueSeparator());
  }

  @Test(timeout = 4000)
  public void test95()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(true);
      option_Builder0.longOpt("");
      Option option0 = option_Builder0.build();
      boolean boolean0 = option0.hasOptionalArg();
      assertEquals((-1), option0.getArgs());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test96()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.hasArg0();
      assertSame(option_Builder0, option_Builder1);
  }

  @Test(timeout = 4000)
  public void test97()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.valueSeparator0();
      assertSame(option_Builder0, option_Builder1);
  }

  @Test(timeout = 4000)
  public void test98()  throws Throwable  {
      Option.Builder option_Builder0 = Option.builder0();
      Option.Builder option_Builder1 = option_Builder0.argName("R@@Zf5H#f1)Bzz");
      assertSame(option_Builder0, option_Builder1);
  }
}
