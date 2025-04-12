



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





package org.apache.commons.csv;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PipedReader;
import java.io.PipedWriter;
import java.io.Reader;
import java.io.StringReader;
import java.io.StringWriter;
import java.io.Writer;
import java.nio.CharBuffer;
import org.apache.commons.csv.IOUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.evosuite.runtime.mock.java.io.MockPrintWriter;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IOUtils_ESTest extends IOUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      Writer writer0 = Writer.nullWriter();
      char[] charArray0 = new char[9];
      long long0 = IOUtils.copyLarge1(reader0, writer0, charArray0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DataOutputStream dataOutputStream0 = new DataOutputStream((OutputStream) null);
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(dataOutputStream0, true);
      StringReader stringReader0 = new StringReader("&s[(A7A");
      long long0 = IOUtils.copyLarge0(stringReader0, mockPrintWriter0);
      assertEquals(7L, long0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      char[] charArray0 = new char[3];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0, 1, 1);
      long long0 = IOUtils.copy1(reader0, charBuffer0, charBuffer0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      StringReader stringReader0 = new StringReader("EHX4ktF3!? o\"y<I36#");
      File file0 = MockFile.createTempFile("EHX4ktF3!? o\"y<I36#", "EHX4ktF3!? o\"y<I36#");
      MockPrintStream mockPrintStream0 = new MockPrintStream(file0);
      long long0 = IOUtils.copy0(stringReader0, mockPrintStream0);
      assertEquals(19L, file0.length());
      assertEquals(19L, long0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      try { 
        IOUtils.rethrow((Throwable) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.IOUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(byteArrayOutputStream0, true);
      char[] charArray0 = new char[0];
      // Undeclared exception!
      IOUtils.copyLarge1(reader0, mockPrintWriter0, charArray0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      Writer writer0 = Writer.nullWriter();
      // Undeclared exception!
      try { 
        IOUtils.copyLarge1(reader0, writer0, (char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      PipedWriter pipedWriter0 = new PipedWriter();
      char[] charArray0 = new char[1];
      try { 
        IOUtils.copyLarge1(pipedReader0, pipedWriter0, charArray0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Writer writer0 = Writer.nullWriter();
      // Undeclared exception!
      try { 
        IOUtils.copyLarge0((Reader) null, writer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.IOUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      StringWriter stringWriter0 = new StringWriter();
      try { 
        IOUtils.copyLarge0(pipedReader0, stringWriter0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      // Undeclared exception!
      try { 
        IOUtils.copy1(reader0, (Appendable) null, (CharBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader(1);
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("org.apache.commons.csv.IOUtils", true);
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFileOutputStream0);
      CharBuffer charBuffer0 = CharBuffer.allocate(1);
      try { 
        IOUtils.copy1(pipedReader0, mockPrintStream0, charBuffer0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      StringReader stringReader0 = new StringReader("EHX4ktF3!? o\"y<I36#");
      // Undeclared exception!
      try { 
        IOUtils.copy0(stringReader0, (Appendable) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      try { 
        IOUtils.copy0(pipedReader0, (Appendable) null);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(byteArrayOutputStream0);
      char[] charArray0 = new char[4];
      StringReader stringReader0 = new StringReader("D*<> ZJ`^fqfzve");
      long long0 = IOUtils.copyLarge1(stringReader0, mockPrintWriter0, charArray0);
      assertEquals(15L, long0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      Writer writer0 = Writer.nullWriter();
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "");
      // Undeclared exception!
      IOUtils.copy1(reader0, writer0, charBuffer0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      Writer writer0 = Writer.nullWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(writer0);
      long long0 = IOUtils.copy0(reader0, mockPrintWriter0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      Writer writer0 = Writer.nullWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(writer0);
      long long0 = IOUtils.copyLarge0(reader0, mockPrintWriter0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable();
      try { 
        IOUtils.rethrow((Throwable) mockThrowable0);
        fail("Expecting exception: Throwable");
      
      } catch(Throwable e) {
      }
  }
}
