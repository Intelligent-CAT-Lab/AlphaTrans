
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
import java.io.File;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.Comparator;
import java.util.Locale;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionGroup;
import org.apache.commons.cli.Options;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.evosuite.runtime.mock.java.io.MockPrintWriter;
import org.evosuite.runtime.testdata.EvoSuiteFile;
import org.evosuite.runtime.testdata.FileSystemHandling;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class HelpFormatter_ESTest extends HelpFormatter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      assertEquals("arg", helpFormatter0.getArgName());
      assertEquals(1, helpFormatter0.defaultLeftPad);
      assertEquals(" ", helpFormatter0.getLongOptSeparator());
      assertEquals(74, helpFormatter0.defaultWidth);
      assertEquals("usage: ", helpFormatter0.getSyntaxPrefix());
      assertEquals("-", helpFormatter0.getOptPrefix());
      assertEquals("--", helpFormatter0.getLongOptPrefix());
      assertEquals(3, helpFormatter0.defaultDescPad);
      
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("--");
      Locale locale0 = Locale.KOREAN;
      Options options0 = new Options();
      helpFormatter0.printUsage1(mockPrintWriter0, 2188, " | ", options0);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      HelpFormatter helpFormatter2 = new HelpFormatter();
      // Undeclared exception!
      helpFormatter2.printUsage1(mockPrintWriter0, 1, "arg", options0);
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Options options0 = new Options();
      Options options1 = options0.addOption2("TahItvRD", "arg");
      helpFormatter0.printUsage1(mockPrintWriter0, 74, "line.separator", options0);
      helpFormatter0.printHelp3(mockPrintWriter0, 74, "P.l2:\"Ue/;\"\"", "", options1, 0, 0, "-", true);
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      helpFormatter0.setLongOptPrefix("$Uz?US`7G");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      options0.addOption2("", "$9i{z]A");
      helpFormatter0.getNewLine();
      helpFormatter0.printHelp7("\n", ">", options0, "-", true);
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.optionComparator;
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.UK;
      Options options0 = new Options();
      helpFormatter0.printUsage1(mockPrintWriter0, 2188, (String) null, options0);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, (-3021), "90iuplHF#Ef;F", "", options0, (-3021), (-3021), "Iv", true);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      String string0 = "";
      FileSystemHandling.appendLineToFile((EvoSuiteFile) null, "");
      FileSystemHandling.appendStringToFile((EvoSuiteFile) null, "");
      FileSystemHandling.shouldThrowIOException((EvoSuiteFile) null);
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.optionComparator;
      FileSystemHandling fileSystemHandling0 = new FileSystemHandling();
      helpFormatter0.optionComparator = comparator0;
      helpFormatter0.optionComparator = comparator0;
      helpFormatter0.getNewLine();
      helpFormatter0.getOptionComparator();
      helpFormatter0.getLongOptSeparator();
      helpFormatter0.getNewLine();
      FileSystemHandling.createFolder((EvoSuiteFile) null);
      helpFormatter0.getSyntaxPrefix();
      helpFormatter0.getLongOptSeparator();
      helpFormatter0.getSyntaxPrefix();
      helpFormatter0.getOptPrefix();
      int int0 = (-3118);
      // Undeclared exception!
      try { 
        helpFormatter0.findWrapPos((String) null, (-2685), (-3118));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(3);
      Options options1 = new Options();
      boolean boolean0 = false;
      options1.addOption3("arg", "~-\"G8a,C{4L~C", false, "\n");
      Option option0 = Option.Option1("", "--");
      options0.addOption0(option0);
      StringBuffer stringBuffer0 = new StringBuffer((CharSequence) "--");
      int int0 = (-27);
      // Undeclared exception!
      try { 
        helpFormatter0.renderOptions(stringBuffer0, (-27), options1, 1406, 1);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.ITALY;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      mockPrintWriter0.format(locale0, "", objectArray0);
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "");
      helpFormatter0.printUsage1(mockPrintWriter0, 74, "90iuplHF#Ef;F", options1);
      helpFormatter0.printHelp3(mockPrintWriter0, 3, "ozVMke.x`", "P.l2:\"Ue/;\"\"", options1, 1, 74, "", true);
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      FileSystemHandling.appendLineToFile((EvoSuiteFile) null, "SRUVNsr-B\"");
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp5("usage: ", (Options) null, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      helpFormatter0.setLongOptPrefix("$Uz?US`7G");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      options0.addOption2("", "$9i{z]A");
      helpFormatter1.printHelp6("7l:hc%<nJ8*jEE:&/|", "7l:hc%<nJ8*jEE:&/|", options0, "%Gf!d()?}A8.");
      helpFormatter0.getNewLine();
      // Undeclared exception!
      try { 
        helpFormatter0.printUsage0(mockPrintWriter0, 1, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      file0.getAbsoluteFile();
      Locale locale0 = Locale.CHINA;
      file0.getAbsoluteFile();
      Object[] objectArray0 = new Object[0];
      mockPrintWriter0.format(locale0, "", objectArray0);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp7("'E,A(eG310V[", "'E,A(eG310V[", (Options) null, "", true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      helpFormatter0.setLongOptPrefix("$Uz?US`7G");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      options0.addOption2("", "$9i{z]A");
      helpFormatter1.printHelp6("7l:hc%<nJ8*jEE:&/|", "7l:hc%<nJ8*jEE:&/|", options0, "%Gf!d()?}A8.");
      helpFormatter0.getNewLine();
      helpFormatter0.printHelp7("\n", ">", options0, "-", true);
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      helpFormatter0.defaultDescPad = (-1111);
      Options options0 = new Options();
      options0.addOption3("arg", " ", true, (String) null);
      Option option0 = Option.Option1("v", " ");
      Options options1 = options0.addOption0(option0);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp7(" ", "", options1, "", true);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1111
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      options0.hasShortOption("");
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      helpFormatter0.setLeftPadding(2188);
      Locale locale0 = Locale.CHINA;
      StringWriter stringWriter0 = new StringWriter(3);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter0, true);
      FileSystemHandling.setPermissions((EvoSuiteFile) null, true, false, true);
      helpFormatter0.printHelp0(2188, " ", " ", options0, (String) null);
      Object[] objectArray0 = new Object[7];
      objectArray0[0] = (Object) helpFormatter0;
      objectArray0[1] = (Object) null;
      objectArray0[2] = (Object) "--";
      objectArray0[3] = (Object) "--";
      objectArray0[4] = (Object) mockPrintWriter0;
      objectArray0[5] = (Object) "";
      objectArray0[6] = (Object) mockPrintWriter0;
      mockPrintWriter0.format(locale0, "g+mdXNiuo85*!", objectArray0);
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3((PrintWriter) null, 1413, "", "NO_ARGS_ALLOWED", options0, 1585, 1585, "Cd:'&c>LjI+~<]fPk", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringWriter stringWriter0 = new StringWriter();
      StringWriter stringWriter1 = stringWriter0.append('=');
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter1, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('$');
      Options options0 = new Options();
      Object object0 = new Object();
      mockPrintWriter0.print(object0);
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(false);
      option_Builder0.option("");
      Option option0 = new Option(1467, "usage: ", "-", "arg", false, option_Builder0);
      Options options1 = options0.addOption0(option0);
      options0.getOption("--");
      helpFormatter0.printOptions(printWriter0, 3, options1, 0, 397);
      option_Builder0.hasArgs();
      int int0 = (-2);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, (-2), "", (String) null, options0, 61, 397, "*QE p8 >= E4:?dq", false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(74);
      Options options0 = new Options();
      options0.addOption3("arg", " ", true, (String) null);
      Option option0 = Option.Option2("arg", true, "v");
      Options options1 = options0.addOption0(option0);
      helpFormatter0.defaultArgName = "";
      helpFormatter0.printHelp7(" ", "", options1, "", true);
      helpFormatter0.getLeftPadding();
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREA;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      Options options0 = new Options();
      options0.getOptionGroups();
      Options options1 = options0.addOption2("", "");
      Options options2 = options1.addOption3("arg", "", true, (String) null);
      helpFormatter0.printHelp1(44, "' was specified but an option from this group has already been selected: '", "!F", options2, "cmdLineSyntax not provided", false);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      // Undeclared exception!
      helpFormatter1.printHelp3(mockPrintWriter0, 1, " *eqTk-k", "usage: ", options0, 74, 1, " *eqTk-k", false);
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      mockPrintWriter0.format(locale0, "", objectArray0);
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "");
      helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options1);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, 3, "ozVMke.x`", "P.l2:\"Ue/;\"\"", options1, (-471), 44, "", true);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -471
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      options0.addOption3("arg", " ", true, (String) null);
      Option option0 = Option.Option1("v", " ");
      Options options1 = options0.addOption0(option0);
      helpFormatter0.printHelp7(" ", "", options1, "", true);
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringWriter stringWriter0 = new StringWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter0, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('$');
      Options options0 = new Options();
      Object object0 = new Object();
      mockPrintWriter0.print(object0);
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(false);
      option_Builder0.option("");
      options0.getOption("--");
      helpFormatter0.printHelp2(printWriter0, (-1), "cmdLineSyntax not provided", "", options0, 4, 18, "cmdLineSyntax not provided");
      helpFormatter0.getOptPrefix();
      helpFormatter0.getLeftPadding();
      helpFormatter0.printUsage1(mockPrintWriter0, 1018, "-", options0);
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator((Comparator<Option>) null);
      String string0 = "-P=4e";
      helpFormatter0.setLongOptPrefix("-P=4e");
      String string1 = "s9B)]:UGqrO]S0:";
      Options options0 = new Options();
      Options options1 = options0.addOption2("arg", "");
      helpFormatter0.printHelp6("s9B)]:UGqrO]S0:", "ZAS,?@A\"()lQ", options1, "");
      String string2 = "cmdLineSyntax not provided";
      String string3 = "A";
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1(1, "", "-P=4e", options1, "A", false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp0(2155, "", "'w1=`5P00Y+", options0, "");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      options0.addOption3("arg", "-", true, (String) null);
      Option option0 = Option.Option1("v", " ");
      Options options1 = options0.addOption0(option0);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp2((PrintWriter) null, 70, (String) null, "", options1, (-1696), (-2), "' contains an illegal character : '");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setDescPadding((-3232));
      Comparator<Option> comparator0 = helpFormatter0.optionComparator;
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.getDescPadding();
      helpFormatter0.getSyntaxPrefix();
      MockFile mockFile0 = new MockFile("arg", "arg");
      // Undeclared exception!
      try { 
        MockFile.createTempFile((String) null, "-", (File) mockFile0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.vfs.VirtualFileSystem", e);
      }
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      int int0 = 44;
      Options options0 = new Options();
      options0.addOption2("", "");
      MockPrintWriter mockPrintWriter1 = new MockPrintWriter(mockPrintWriter0, true);
      int int1 = 61;
      // Undeclared exception!
      try { 
        helpFormatter0.printWrapped0(mockPrintWriter0, 61, (-24), "' was specified but an option from this group has already been selected: '");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -24
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      StringBuffer stringBuffer0 = new StringBuffer(3131);
      // Undeclared exception!
      try { 
        helpFormatter0.renderWrappedText((StringBuffer) null, 48, 44, "|s=8>L9;@:cZeHMiN");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      mockPrintWriter0.format(locale0, "", objectArray0);
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "");
      helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options1);
      int int0 = (-878);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp2(mockPrintWriter0, 9, "90iuplHF#Ef;F", "Cannot add value, list full.", options1, (-878), 2188, ", ");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -878
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      int int0 = 44;
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "");
      Options options2 = options1.addOption3("arg", "-", true, (String) null);
      helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options1);
      StringBuffer stringBuffer0 = new StringBuffer();
      helpFormatter0.renderOptions(stringBuffer0, 9, options1, 9, 44);
      int int1 = (-878);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp2(mockPrintWriter0, 9, "90iuplHF#Ef;F", "Cannot add value, list full.", options2, (-878), 2188, ", ");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -878
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Options options0 = new Options();
      String string0 = "";
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp0((-1968), "'w1=`5P00Y+", (String) null, options0, "");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp0((-1941), "'w1=`5P00Y+", (String) null, options0, "");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      String string0 = "org.apache.commons.cli.Options";
      int int0 = 2;
      StringBuffer stringBuffer0 = new StringBuffer("\n");
      stringBuffer0.appendCodePoint(3);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp0(2, "org.apache.commons.cli.Options", "org.apache.commons.cli.Options", (Options) null, "C*v/TNc");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix("-P=4e");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      Options options1 = options0.addOption2("arg", "");
      helpFormatter1.printHelp6("s9B)]:UGqrO]S0:", "arg", options1, "");
      helpFormatter1.getNewLine();
      StringBuffer stringBuffer0 = new StringBuffer(133);
      StringBuffer stringBuffer1 = helpFormatter1.renderWrappedText(stringBuffer0, 3, 74, "--");
      StringBuffer stringBuffer2 = helpFormatter0.renderWrappedText(stringBuffer1, 3, 0, "s9B)]:UGqrO]S0:");
      // Undeclared exception!
      helpFormatter1.renderOptions(stringBuffer2, 1, options1, 63, 133);
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "");
      Options options2 = options1.addOption3("arg", "-", true, (String) null);
      helpFormatter0.printHelp1(44, "' was specified but an option from this group has already been selected: '", "!F", options2, "cmdLineSyntax not provided", false);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(2188);
      helpFormatter1.setNewLine("\n");
      helpFormatter1.createPadding(805);
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      FileSystemHandling.shouldAllThrowIOExceptions();
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLongOptPrefix("");
      helpFormatter0.getArgName();
      helpFormatter0.getLongOptPrefix();
      helpFormatter0.getOptionComparator();
      StringBuffer stringBuffer0 = new StringBuffer("");
      StringBuffer stringBuffer1 = helpFormatter0.renderWrappedText(stringBuffer0, 63, (-55), "org.apache.commons.cli.HelpFormatter$1");
      // Undeclared exception!
      try { 
        helpFormatter0.renderOptions(stringBuffer1, 9, (Options) null, 415, 9);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      String string0 = "org.apache.commons.cli.Options";
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      mockPrintWriter0.format(locale0, "", objectArray0);
      // Undeclared exception!
      helpFormatter0.printWrapped1(mockPrintWriter0, 0, "-");
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("k=|<0KIztbIA+7Ab", "");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[3];
      objectArray0[0] = (Object) locale0;
      objectArray0[1] = (Object) file0;
      objectArray0[2] = (Object) mockPrintWriter0;
      mockPrintWriter0.format(locale0, "arg", objectArray0);
      // Undeclared exception!
      helpFormatter0.printWrapped1(mockPrintWriter0, 0, "X0Y}$oEsk}XD");
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setWidth(3231);
      helpFormatter0.setLongOptPrefix("-P=4e");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      String string0 = "s9B)]:UGqrO]S0:";
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "org.apache.commons.cli.HelpFormatter$OptionComparator");
      // Undeclared exception!
      try { 
        helpFormatter1.printHelp6("", "IX", options1, "s9B)]:UGqrO]S0:");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(3);
      options0.addOption3("arg", "~-\"G8a,C{4L~C", false, "\n");
      Option option0 = Option.Option1("", "--");
      options0.addOption0(option0);
      helpFormatter1.printHelp7(" ", "eQSc7v\"mC;1PC[C@j=c", options0, "-", true);
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringWriter stringWriter0 = new StringWriter();
      StringWriter stringWriter1 = stringWriter0.append('=');
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter1, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('$');
      Options options0 = new Options();
      String string0 = "usage: ";
      Object object0 = new Object();
      mockPrintWriter0.print(object0);
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(false);
      option_Builder0.option("");
      Option option0 = new Option(1467, "usage: ", "usage: ", "arg", false, option_Builder0);
      Options options1 = options0.addOption0(option0);
      FileSystemHandling.shouldThrowIOException((EvoSuiteFile) null);
      options0.getOption("--");
      helpFormatter0.printOptions(printWriter0, 3, options1, 0, 397);
      option0.setRequired(true);
      option_Builder0.hasArgs();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, (-1), "usage: ", "", options1, (-1), (-342), "usage: ", true);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringWriter stringWriter0 = new StringWriter();
      StringWriter stringWriter1 = stringWriter0.append('=');
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter1, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('$');
      Options options0 = new Options();
      Object object0 = new Object();
      mockPrintWriter0.print(object0);
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(false);
      option_Builder0.option("");
      Option option0 = new Option(1467, "usage: ", "usage: ", "arg", false, option_Builder0);
      Options options1 = options0.addOption0(option0);
      options0.getOption("--");
      helpFormatter0.printOptions(printWriter0, 3, options1, 0, 397);
      option_Builder0.hasArgs();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, (-1), "usage: ", "", options1, (-1), (-342), "usage: ", false);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setNewLine("");
      helpFormatter0.createPadding(0);
      helpFormatter0.getLongOptPrefix();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1(0, "--", "--", (Options) null, (String) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      mockPrintWriter0.format(locale0, "-", objectArray0);
      helpFormatter0.printWrapped1(mockPrintWriter0, 0, "");
      StringBuffer stringBuffer0 = new StringBuffer(3115);
      // Undeclared exception!
      try { 
        helpFormatter0.renderWrappedText(stringBuffer0, 2, (-30), "org.apache.commons.cli.Options");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -30
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("arg", options0, false);
      int int0 = 61;
      StringBuffer stringBuffer0 = new StringBuffer(61);
      Writer writer0 = Writer.nullWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(writer0, false);
      int int1 = (-2);
      // Undeclared exception!
      try { 
        helpFormatter0.printWrapped0(mockPrintWriter0, (-2), 61, "4Sc:'");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix("-P=4e");
      helpFormatter0.findWrapPos("-P=4e", 0, 3);
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Locale locale0 = Locale.FRENCH;
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Options options0 = new Options();
      HelpFormatter helpFormatter2 = new HelpFormatter();
      // Undeclared exception!
      try { 
        helpFormatter2.printHelp1(74, "", "arg", options0, "7>nn7mx6", false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      objectArray0[1] = (Object) helpFormatter0;
      objectArray0[2] = (Object) comparator0;
      Object object0 = new Object();
      objectArray0[3] = object0;
      String string0 = "cmdLineSyntax not provided";
      // Undeclared exception!
      try { 
        helpFormatter0.printWrapped1(mockPrintWriter0, (-858), "cmdLineSyntax not provided");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("(AfqMLkPKQFZ", options0, false);
      StringBuffer stringBuffer0 = new StringBuffer(3);
      helpFormatter0.renderWrappedText(stringBuffer0, 21, 61, "");
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "");
      Options options2 = options1.addOption3("arg", "-", true, (String) null);
      helpFormatter0.printHelp1(44, "' was specified but an option from this group has already been selected: '", "!F", options2, "cmdLineSyntax not provided", false);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setNewLine("\n");
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(3);
      options0.addOption3("arg", "~-\"G8a,C{4L~C", false, "\n");
      Option option0 = Option.Option1("", "--");
      options0.addOption0(option0);
      helpFormatter1.printHelp7(" ", "-", options0, "", false);
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printUsage1((PrintWriter) null, (-37), "_4^A*", options0);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      options0.getOptionGroups();
      Options options1 = options0.addOption2("", "");
      Options options2 = options1.addOption3("arg", "-", true, (String) null);
      helpFormatter0.printHelp1(44, "' was specified but an option from this group has already been selected: '", "!F", options2, "cmdLineSyntax not provided", false);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setNewLine("\n");
      helpFormatter1.getOptionComparator();
      helpFormatter0.printUsage1(mockPrintWriter0, 74, "org.apache.commons.cli.AlreadySelectedException", options1);
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options1 = new Options();
      options1.addOption3("arg", "~-\"G8a,C{4L~C", false, "\n");
      helpFormatter1.printHelp1(3, "arg", "[w( ?wH^RJJ~A^'", options1, "a4N.^Jlev[y$", false);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(" :: ");
      PrintWriter printWriter0 = mockPrintWriter0.append((CharSequence) "--");
      // Undeclared exception!
      try { 
        helpFormatter1.printHelp2(printWriter0, (-8), "--", "arg", options1, (-2035), 74, "");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, false);
      helpFormatter0.setSyntaxPrefix("&=r?(h!L");
      helpFormatter0.printHelp7("<", "6-l$y:vI'@VO", options0, (String) null, false);
      FileSystemHandling.shouldThrowIOException((EvoSuiteFile) null);
      helpFormatter0.setSyntaxPrefix("arg");
      MockFile mockFile0 = new MockFile("-", "\n");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(mockFile0);
      PrintWriter printWriter0 = mockPrintWriter0.format("&=r?(h!L", (Object[]) null);
      MockPrintWriter mockPrintWriter1 = new MockPrintWriter(printWriter0, true);
      helpFormatter0.printWrapped0(mockPrintWriter1, 0, 0, "");
      helpFormatter0.printUsage1(mockPrintWriter1, (-1), "<", options0);
      StringBuffer stringBuffer0 = new StringBuffer();
      helpFormatter0.renderOptions(stringBuffer0, (-1), options0, 0, 0);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp2(printWriter0, (-230), ", ", ", ", options0, (-230), (-230), "arg");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(2188);
      helpFormatter0.printHelp1((-1), "!F", "--", options0, "wq", false);
      HelpFormatter helpFormatter2 = new HelpFormatter();
      helpFormatter0.rtrim("");
      helpFormatter1.getDescPadding();
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, true);
      StringBuffer stringBuffer0 = new StringBuffer(61);
      Options options1 = new Options();
      helpFormatter0.printHelp1(61, "R{ba4P=jY`q]d U}O ", "cQ6<_Spk=),'ai", options0, "i", true);
      helpFormatter0.getArgName();
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLongOptSeparator("NS]&!");
      helpFormatter0.setWidth(375);
      StringWriter stringWriter0 = new StringWriter();
      stringWriter0.close();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter0, false);
      helpFormatter0.printUsage0(mockPrintWriter0, 375, "NS]&!");
      String string0 = "[ARG...]";
      String string1 = "lMge!Sr0Hj;hR";
      Options options0 = new Options();
      String string2 = "org.apache.commons.cli.ParseException";
      helpFormatter0.getArgName();
      try { 
        Option.Option2("--", false, "org.apache.commons.cli.ParseException");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option '--' contains an illegal character : '-'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringBuffer stringBuffer0 = new StringBuffer(3131);
      helpFormatter0.renderWrappedText(stringBuffer0, 2, 44, "org.apache.commons.cli.Options");
      assertEquals(86, stringBuffer0.length());
      assertEquals("or\n g\n .\n a\n p\n a\n c\n h\n e\n .\n c\n o\n m\n m\n o\n n\n s\n .\n c\n l\n i\n .\n O\n p\n t\n i\n o\n n\n s", stringBuffer0.toString());
      
      helpFormatter0.getLongOptSeparator();
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      options0.helpOptions();
      helpFormatter0.setLeftPadding((-803));
      helpFormatter0.getOptPrefix();
      helpFormatter0.getLongOptSeparator();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1((-803), "--", "!F", options0, "", false);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Locale locale0 = Locale.KOREAN;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      Options options1 = options0.addOption3("arg", " ", true, (String) null);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1(2188, (String) null, (String) null, options1, "<", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("org.apache.commons.cli.Options", options0, false);
      StringBuffer stringBuffer0 = new StringBuffer(74);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      // Undeclared exception!
      try { 
        helpFormatter1.printHelp1(74, " ", ",>qE(i8V$mkki", (Options) null, "Qssnyp{wg*", false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      mockPrintWriter0.format(locale0, "", objectArray0);
      helpFormatter0.printWrapped1(mockPrintWriter0, 0, "");
      StringBuffer stringBuffer0 = new StringBuffer(3131);
      helpFormatter0.renderWrappedText(stringBuffer0, 2, 44, "org.apache.commons.cli.Options");
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Options options0 = new Options();
      helpFormatter0.printUsage1(mockPrintWriter0, 2188, "90iuplHF#Ef;F", options0);
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, 3, "ozVMke.x`", "P.l2:\"Ue/;\"\"", options0, (-471), 74, "", true);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -471
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      mockPrintWriter0.format(locale0, "", objectArray0);
      Options options0 = new Options();
      helpFormatter0.printHelp7("org.apache.commons.cli.Options", "", options0, "?]$qj_&w", false);
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLeftPadding(3);
      StringWriter stringWriter0 = new StringWriter();
      StringWriter stringWriter1 = stringWriter0.append('=');
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter1, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('$');
      Options options0 = new Options();
      String string0 = "usage: ";
      Object object0 = new Object();
      mockPrintWriter0.print(object0);
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(false);
      option_Builder0.option("");
      Option option0 = new Option(1467, "usage: ", "usage: ", "arg", false, option_Builder0);
      Options options1 = options0.addOption0(option0);
      options0.getOption("--");
      helpFormatter0.printOptions(printWriter0, 3, options1, 0, 397);
      option_Builder0.hasArgs();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp3(mockPrintWriter0, (-1), "usage: ", "", options1, (-1), (-342), "usage: ", true);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      helpFormatter0.setLongOptPrefix("m39M&P@*<_R:RNd");
      helpFormatter0.findWrapPos("", (-3653), 23);
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix("\n");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      Options options1 = options0.addOption2("arg", "");
      helpFormatter1.printHelp6("usage: ", "--", options1, "");
      helpFormatter1.getNewLine();
      helpFormatter0.printHelp7("\n", " ", options1, "usage: ", true);
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, true);
      StringBuffer stringBuffer0 = new StringBuffer(61);
      options0.addOption2("arg", "--");
      helpFormatter0.printHelp1(61, "R{ba4P=jY`q]d U}O ", "cQ6<_Spk=),'ai", options0, "i", true);
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLongOptPrefix("-P=4e");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter1.printHelp6("--", "6/", options0, "usage: ");
      helpFormatter1.getNewLine();
      // Undeclared exception!
      try { 
        helpFormatter1.printHelp7("", "usage: ", options0, "\n", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp4((String) null, options0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      MockPrintStream mockPrintStream0 = new MockPrintStream("'");
      mockPrintStream0.print((Object) helpFormatter0);
      Options options0 = new Options();
      helpFormatter0.defaultLongOptPrefix = null;
      helpFormatter0.setDescPadding(48);
      helpFormatter0.setOptPrefix((String) null);
      options0.getOption("[ Options: [ short ");
      StringBuffer stringBuffer0 = null;
      try {
        stringBuffer0 = new StringBuffer((-1));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Locale locale0 = Locale.CHINA;
      Options options0 = new Options();
      OptionGroup optionGroup0 = new OptionGroup();
      options0.addOptionGroup(optionGroup0);
      helpFormatter0.printHelp6("org.apache.commons.cli.Options", "org.apache.commons.cli.Options", options0, "org.apache.commons.cli.Options");
      StringBuffer stringBuffer0 = new StringBuffer(1);
      helpFormatter0.renderWrappedText(stringBuffer0, 44, 44, "org.apache.commons.cli.Options");
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      MockPrintStream mockPrintStream0 = new MockPrintStream("'");
      mockPrintStream0.print((Object) helpFormatter0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(mockPrintStream0, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('-');
      int int0 = 360;
      Options options0 = new Options();
      helpFormatter0.printOptions(printWriter0, 360, options0, 360, 360);
      String string0 = null;
      helpFormatter0.defaultLongOptPrefix = null;
      helpFormatter0.setDescPadding(48);
      helpFormatter0.setOptPrefix((String) null);
      options0.getOption("[ Options: [ short ");
      helpFormatter0.setSyntaxPrefix((String) null);
      int int1 = 0;
      helpFormatter0.defaultLeftPad = 0;
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp7("", (String) null, options0, "", true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringBuffer stringBuffer0 = new StringBuffer();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.renderWrappedText(stringBuffer0, 74, 4, "");
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      StringBuffer stringBuffer0 = new StringBuffer(74);
      // Undeclared exception!
      helpFormatter0.renderWrappedText(stringBuffer0, 0, 0, "9rg.apache.commons.cli.Optio#s");
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("cQ6<_Spk=),'ai", options0, false);
      StringBuffer stringBuffer0 = new StringBuffer(61);
      helpFormatter0.renderWrappedText(stringBuffer0, 61, 0, "cQ6<_Spk=),'ai");
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getSyntaxPrefix();
      int int0 = 0;
      helpFormatter0.setSyntaxPrefix("usage: ");
      helpFormatter0.setDescPadding(0);
      helpFormatter0.setLongOptPrefix("usage: ");
      helpFormatter0.getDescPadding();
      String string0 = "JWJ#5C;m~S9k%-|]";
      Options options0 = new Options();
      String string1 = "5Kc)]; g]RX";
      // Undeclared exception!
      try { 
        options0.addOption2("5Kc)]; g]RX", "");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option '5Kc)]; g]RX' contains an illegal character : ')'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      PrintWriter printWriter0 = mockPrintWriter0.format(locale0, "\n", objectArray0);
      // Undeclared exception!
      try { 
        helpFormatter0.printUsage0(printWriter0, (-109), "ie1i|");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      options0.addOption3("arg", " ", true, (String) null);
      Option option0 = Option.Option1("v", " ");
      Options options1 = options0.addOption0(option0);
      helpFormatter0.setLeftPadding(18);
      helpFormatter0.printHelp7(" ", "", options1, "", false);
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Locale locale0 = Locale.KOREAN;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      Options options1 = options0.addOption3("arg", " ", true, (String) null);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.printHelp1(2188, "--", (String) null, options1, "", true);
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      helpFormatter0.setLeftPadding(2188);
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte) (-79);
      byteArray0[2] = (byte) (-103);
      Option option0 = Option.Option2((String) null, true, "arg");
      Options options1 = options0.addOption0(option0);
      helpFormatter0.printHelp6("&8=Y4Uh*,3}iTl", "--", options1, "--");
      FileSystemHandling.appendDataToFile((EvoSuiteFile) null, byteArray0);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.defaultArgName = "LWbH@wD~$>E'%^B9";
      StringBuffer stringBuffer0 = new StringBuffer((CharSequence) "!F");
      // Undeclared exception!
      try { 
        helpFormatter0.renderWrappedText(stringBuffer0, (byte) (-79), 3, "org.apache.commons.cli.AlreadySelectedException");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix("-P=4e");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      Options options1 = options0.addOption2("arg", "");
      helpFormatter1.printHelp6("s9B)]:UGqrO]S0:", "ZAS,?@A\"()lQ", options1, "");
      helpFormatter1.getNewLine();
      helpFormatter0.printHelp7("-:", " ", options1, ",ew\"kYN0~!xTraJV<(6", true);
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Options options0 = new Options();
      helpFormatter0.printUsage1(mockPrintWriter0, 3, "usage: ", options0);
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.FRENCH;
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Options options0 = new Options();
      HelpFormatter helpFormatter2 = new HelpFormatter();
      // Undeclared exception!
      helpFormatter2.printHelp1(1, "usage: ", "VqU>bqb{}J/@+_nT5 ", options0, "org.apache.commons.cli.Options", false);
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix("(9z");
      HelpFormatter helpFormatter1 = new HelpFormatter();
      Options options0 = new Options();
      Options options1 = options0.addOption2((String) null, "-");
      helpFormatter1.printHelp6("arg", "(9z", options1, "(9z");
      helpFormatter1.getNewLine();
      helpFormatter1.printHelp7("tHF|5lJ@!^d7S3bn2", (String) null, options0, "W7>QbNh>[_W^k", true);
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("\n");
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      objectArray0[1] = (Object) helpFormatter0;
      objectArray0[2] = (Object) comparator0;
      Object object0 = new Object();
      objectArray0[3] = object0;
      objectArray0[4] = (Object) comparator0;
      objectArray0[5] = (Object) locale0;
      mockPrintWriter0.format(locale0, "--", objectArray0);
      helpFormatter0.printUsage0(mockPrintWriter0, 12, "Up]p^HwcDq^yH`lq");
      helpFormatter0.getNewLine();
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      PrintWriter printWriter0 = mockPrintWriter0.format(locale0, "", objectArray0);
      // Undeclared exception!
      helpFormatter0.printUsage0(printWriter0, 0, "Up]p^HwcDq^yH`lq");
  }

  @Test(timeout = 4000)
  public void test086()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLeftPadding(3);
      StringWriter stringWriter0 = new StringWriter();
      StringWriter stringWriter1 = stringWriter0.append('=');
      boolean boolean0 = false;
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter1, false);
      PrintWriter printWriter0 = mockPrintWriter0.append('$');
      Options options0 = new Options();
      String string0 = "usage: ";
      Object object0 = new Object();
      mockPrintWriter0.print(object0);
      Option.Builder option_Builder0 = Option.builder0();
      option_Builder0.optionalArg(false);
      Option option0 = new Option(1467, "usage: ", "usage: ", "arg", false, option_Builder0);
      Options options1 = options0.addOption0(option0);
      int int0 = 397;
      options0.getOption("--");
      helpFormatter0.printOptions(printWriter0, 3, options1, 0, 397);
      option_Builder0.hasArgs();
      helpFormatter0.getOptionComparator();
      // Undeclared exception!
      try { 
        helpFormatter0.printUsage0(mockPrintWriter0, (-2), "usage: ");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      File file0 = MockFile.createTempFile("org.apache.commons.cli.Options", "-");
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(file0);
      Locale locale0 = Locale.CHINA;
      Object[] objectArray0 = new Object[0];
      mockPrintWriter0.format(locale0, "", objectArray0);
      helpFormatter0.setNewLine("org.apache.commons.cli.Options");
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLongOptSeparator("B^<D?N");
      helpFormatter0.defaultDescPad = 2641;
      helpFormatter0.setNewLine("7");
      String string0 = "#v1t=R";
      String string1 = "!vUp3Jm?Ec#s3#y";
      Options options0 = new Options();
      boolean boolean0 = true;
      try { 
        Option.Option2("usage: ", true, "Z^K],5e(j");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'usage: ' contains an illegal character : ':'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLongOptSeparator("NS]&!");
      helpFormatter0.setWidth(375);
      StringWriter stringWriter0 = new StringWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(stringWriter0, false);
      helpFormatter0.printUsage0(mockPrintWriter0, 375, "NS]&!");
      String string0 = "[ARG...]";
      String string1 = "lMge!Sr0Hj;hR";
      Options options0 = new Options();
      String string2 = "org.apache.commons.cli.ParseException";
      try { 
        Option.Option2("--", false, "org.apache.commons.cli.ParseException");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option '--' contains an illegal character : '-'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      String string0 = ", ";
      Options options0 = null;
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp4(", ", (Options) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.rtrim("usage: ");
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptPrefix();
      int int0 = 1;
      helpFormatter0.setDescPadding(1);
      helpFormatter0.setArgName("3Y#;%");
      helpFormatter0.getOptionComparator();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter("3Y#;%");
      String string0 = "`z0#>5^pF<Wn<";
      Options options0 = new Options();
      Options options1 = options0.addOption2("", "3Y#;%");
      OptionGroup optionGroup0 = new OptionGroup();
      options1.addOptionGroup(optionGroup0);
      // Undeclared exception!
      try { 
        options1.addOption1("kJb>X{", false, (String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'kJb>X{' contains an illegal character : '>'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getSyntaxPrefix();
      helpFormatter0.setArgName("usage: ");
      int int0 = (-2);
      helpFormatter0.setDescPadding((-2));
      StringBuffer stringBuffer0 = new StringBuffer();
      int int1 = 1532;
      // Undeclared exception!
      try { 
        helpFormatter0.renderWrappedText(stringBuffer0, (-2), 1532, "usage: ");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      helpFormatter0.setLeftPadding((-803));
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1((-803), "&8=Y4Uh*,3}iTl", "", options0, "", false);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      helpFormatter0.setLeftPadding(1);
      helpFormatter0.printHelp1(74, "--", "!F", options0, "usage: ", false);
      helpFormatter0.setNewLine("0bx4.8E/g<>n\"5z0|");
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getLongOptPrefix();
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp4("&8=Y4Uh*,3}iTl", options0);
      helpFormatter0.getLongOptPrefix();
      helpFormatter0.setLeftPadding((-803));
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1((-803), "--", "!F", options0, "", false);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLongOptSeparator("");
  }

  @Test(timeout = 4000)
  public void test099()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix("-P=4e");
      helpFormatter0.findWrapPos("-P=4e", 0, 0);
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setDescPadding((-2948));
      helpFormatter0.getWidth();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp1(74, "7fs_C)Ji1Nl", "7fs_C)Ji1Nl", (Options) null, "dAN$])9N>PPzV", false);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2948
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(3);
      Options options1 = new Options();
      options1.addOption3("arg", "~-\"G8a,C{4L~C", false, "\n");
      Option option0 = Option.Option1("", "--");
      options0.addOption0(option0);
      helpFormatter1.printHelp7(" ", "-", options1, "", false);
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter1.setLeftPadding(3);
      Options options1 = new Options();
      options1.addOption3("arg", "~-\"G8a,C{4L~C", false, "\n");
      Option.Option1("", "--");
      helpFormatter1.printHelp1(8, "arg", "[w( ?wH^RJJ~A^'", options1, "a4N.^Jlev[y$", false);
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringBuffer stringBuffer0 = new StringBuffer(1);
      HelpFormatter helpFormatter1 = new HelpFormatter();
      // Undeclared exception!
      try { 
        helpFormatter1.renderWrappedText(stringBuffer0, (-1466), 3, "\n");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setDescPadding((-3180));
      Locale locale0 = Locale.CHINA;
      FileSystemHandling fileSystemHandling0 = new FileSystemHandling();
      StringBuffer stringBuffer0 = new StringBuffer(3131);
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printUsage1((PrintWriter) null, 74, "_4^A*", options0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.rtrim("org.apache.commons.cli.Option");
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      // Undeclared exception!
      try { 
        helpFormatter0.findWrapPos("@|bn", 13, (-3245));
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getWidth();
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Locale locale0 = Locale.FRENCH;
      HelpFormatter helpFormatter1 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Options options0 = new Options();
      helpFormatter1.printHelp1(3, "--", "usage: ", options0, "usage: ", true);
      helpFormatter0.getLongOptSeparator();
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      helpFormatter0.printHelp5("org.apache.commons.cli.Options", options0, false);
      StringBuffer stringBuffer0 = new StringBuffer(74);
      // Undeclared exception!
      helpFormatter0.renderWrappedText(stringBuffer0, 0, 0, "org.apache.commons.cli.Options");
  }

  @Test(timeout = 4000)
  public void test111()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      String string0 = "";
      helpFormatter0.setSyntaxPrefix("");
      String string1 = "zIK9Sre o?ZD~GZ";
      helpFormatter0.defaultNewLine = "zIK9Sre o?ZD~GZ";
      helpFormatter0.getDescPadding();
      boolean boolean0 = true;
      helpFormatter0.defaultArgName = "zIK9Sre o?ZD~GZ";
      MockPrintWriter mockPrintWriter0 = null;
      try {
        mockPrintWriter0 = new MockPrintWriter((OutputStream) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.io.Writer", e);
      }
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      // Undeclared exception!
      try { 
        helpFormatter0.printHelp5("", options0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // cmdLineSyntax not provided
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringBuffer stringBuffer0 = new StringBuffer(3131);
      helpFormatter0.renderWrappedText(stringBuffer0, 2, 44, "org.apache.commons.cli.Options");
      // Undeclared exception!
      try { 
        helpFormatter0.createPadding((-2));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      // Undeclared exception!
      try { 
        helpFormatter0.createPadding((-1375));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1375
         //
         verifyException("org.apache.commons.cli.HelpFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      int int0 = (-1699);
      helpFormatter0.setLeftPadding((-1699));
      MockPrintWriter mockPrintWriter0 = null;
      try {
        mockPrintWriter0 = new MockPrintWriter("usage: ", "-");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(Throwable e) {
         //
         // -
         //
         verifyException("org.evosuite.runtime.mock.java.io.MockPrintWriter", e);
      }
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.setLeftPadding((-3772));
      try { 
        Option.Option1("usage: ", "arg");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'usage: ' contains an illegal character : ':'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      int int0 = (-192);
      helpFormatter0.setWidth((-192));
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.optionComparator = comparator0;
      String string0 = "Ky:Yl(H_I2A@!%\\";
      String string1 = "o:M >Welh`/qD`qV^W[";
      Options options0 = new Options();
      Option option0 = Option.Option1("", "");
      Options options1 = options0.addOption0(option0);
      boolean boolean0 = true;
      // Undeclared exception!
      try { 
        options1.addOption3("usage: ", "-", true, "o:M >Welh`/qD`qV^W[");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'usage: ' contains an illegal character : ':'
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.setLongOptPrefix(":lU/1)h$D");
      helpFormatter0.getOptPrefix();
      assertEquals(":lU/1)h$D", helpFormatter0.getLongOptPrefix());
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Options options0 = new Options();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.optionComparator = comparator0;
      String string0 = helpFormatter0.rtrim("org.apache.commons.cli.Option");
      assertEquals("usage: ", helpFormatter0.getSyntaxPrefix());
      assertEquals("org.apache.commons.cli.Option", string0);
      assertEquals(3, helpFormatter0.defaultDescPad);
      assertEquals("--", helpFormatter0.getLongOptPrefix());
      assertEquals(1, helpFormatter0.defaultLeftPad);
      assertEquals("arg", helpFormatter0.getArgName());
      assertEquals("-", helpFormatter0.getOptPrefix());
      assertEquals(" ", helpFormatter0.getLongOptSeparator());
      assertEquals(74, helpFormatter0.defaultWidth);
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      Comparator<Option> comparator0 = helpFormatter0.getOptionComparator();
      helpFormatter0.setOptionComparator(comparator0);
      helpFormatter0.getNewLine();
      String string0 = "--";
      Options options0 = new Options();
      String string1 = "";
      Options options1 = options0.addRequiredOption("", "-", true, "");
      String string2 = "spaW_a8 TFA\\uA";
      String string3 = "'0-";
      helpFormatter0.defaultWidth = 13;
      // Undeclared exception!
      try { 
        options1.addOption3(string2, "'0-", false, "YywJrD%|J");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'spaW_a8 TFA\\uA' contains an illegal character : ' '
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      helpFormatter0.getOptionComparator();
      Locale locale0 = Locale.KOREAN;
      Object[] objectArray0 = new Object[6];
      objectArray0[0] = (Object) helpFormatter0;
      helpFormatter0.setLeftPadding(2188);
      Options options0 = new Options();
      options0.addOption3("arg", " ", true, (String) null);
      helpFormatter0.setSyntaxPrefix((String) null);
      helpFormatter0.findWrapPos("", 2188, 2188);
      helpFormatter0.getArgName();
      assertEquals(2188, helpFormatter0.defaultLeftPad);
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      String string0 = "";
      helpFormatter0.setSyntaxPrefix("");
      String string1 = "k{xs;{[P";
      MockPrintWriter mockPrintWriter0 = null;
      try {
        mockPrintWriter0 = new MockPrintWriter("usage: ", "k{xs;{[P");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(Throwable e) {
         //
         // k{xs;{[P
         //
         verifyException("org.evosuite.runtime.mock.java.io.MockPrintWriter", e);
      }
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      HelpFormatter helpFormatter0 = new HelpFormatter();
      StringBuffer stringBuffer0 = new StringBuffer(3);
      String string0 = "[";
      helpFormatter0.defaultSyntaxPrefix = "[";
      int int0 = 881;
      Options options0 = new Options();
      String string1 = "qV'{Ui";
      boolean boolean0 = false;
      // Undeclared exception!
      try { 
        options0.addRequiredOption("qV'{Ui", "", false, "\n");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The option 'qV'{Ui' contains an illegal character : '''
         //
         verifyException("org.apache.commons.cli.OptionValidator", e);
      }
  }
}
