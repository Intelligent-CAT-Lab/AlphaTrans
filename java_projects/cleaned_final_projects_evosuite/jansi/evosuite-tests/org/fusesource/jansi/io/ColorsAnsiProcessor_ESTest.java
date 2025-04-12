
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


package org.fusesource.jansi.io;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.ByteArrayOutputStream;
import java.io.PipedOutputStream;
import java.util.ArrayList;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.fusesource.jansi.AnsiColors;
import org.fusesource.jansi.io.ColorsAnsiProcessor;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ColorsAnsiProcessor_ESTest extends ColorsAnsiProcessor_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      AnsiColors ansiColors0 = AnsiColors.Colors16;
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      Integer integer0 = new Integer(8902615);
      arrayList0.add((Object) integer0);
      boolean boolean0 = colorsAnsiProcessor0.processEscapeCommand(arrayList0, 109);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      AnsiColors ansiColors0 = AnsiColors.TrueColor;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(byteArrayOutputStream0, ansiColors0);
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      boolean boolean0 = colorsAnsiProcessor0.processEscapeCommand(arrayList0, 1257);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      Integer integer0 = new Integer((-280));
      arrayList0.add((Object) integer0);
      arrayList0.add((Object) integer0);
      Integer integer1 = new Integer(48);
      arrayList0.add((Object) integer1);
      AnsiColors ansiColors0 = AnsiColors.Colors16;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      // Undeclared exception!
      try { 
        colorsAnsiProcessor0.processEscapeCommand(arrayList0, 109);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      Integer integer0 = new Integer(48);
      arrayList0.add((Object) integer0);
      arrayList0.add((Object) integer0);
      AnsiColors ansiColors0 = AnsiColors.Colors256;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      // Undeclared exception!
      try { 
        colorsAnsiProcessor0.processEscapeCommand(arrayList0, 109);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.io.ColorsAnsiProcessor", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      Integer integer0 = new Integer(38);
      arrayList0.add((Object) integer0);
      AnsiColors ansiColors0 = AnsiColors.Colors256;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      // Undeclared exception!
      try { 
        colorsAnsiProcessor0.processEscapeCommand(arrayList0, 109);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      AnsiColors ansiColors0 = AnsiColors.Colors16;
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      Object object0 = new Object();
      arrayList0.add(object0);
      // Undeclared exception!
      try { 
        colorsAnsiProcessor0.processEscapeCommand(arrayList0, 109);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.io.ColorsAnsiProcessor", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      AnsiColors ansiColors0 = AnsiColors.Colors16;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      arrayList0.add((Object) null);
      // Undeclared exception!
      try { 
        colorsAnsiProcessor0.processEscapeCommand(arrayList0, 109);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.io.ColorsAnsiProcessor", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      AnsiColors ansiColors0 = AnsiColors.TrueColor;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      boolean boolean0 = colorsAnsiProcessor0.processEscapeCommand((ArrayList<Object>) null, 109);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      AnsiColors ansiColors0 = AnsiColors.Colors16;
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      boolean boolean0 = colorsAnsiProcessor0.processEscapeCommand(arrayList0, 27);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      AnsiColors ansiColors0 = AnsiColors.Colors16;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(pipedOutputStream0, ansiColors0);
      boolean boolean0 = colorsAnsiProcessor0.processOperatingSystemCommand(arrayList0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      MockPrintStream mockPrintStream0 = new MockPrintStream(pipedOutputStream0);
      AnsiColors ansiColors0 = AnsiColors.TrueColor;
      ColorsAnsiProcessor colorsAnsiProcessor0 = new ColorsAnsiProcessor(mockPrintStream0, ansiColors0);
      ArrayList<Object> arrayList0 = new ArrayList<Object>();
      boolean boolean0 = colorsAnsiProcessor0.processCharsetSelect0(arrayList0);
      assertFalse(boolean0);
  }
}
