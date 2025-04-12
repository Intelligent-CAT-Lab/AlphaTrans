



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
import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;
import org.apache.commons.csv.ExtendedBufferedReader;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ExtendedBufferedReader_ESTest extends ExtendedBufferedReader_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      char[] charArray0 = extendedBufferedReader0.lookAhead2(1406);
      // Undeclared exception!
      try { 
        extendedBufferedReader0.read1(charArray0, 478, (-1));
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.io.BufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      StringReader stringReader0 = new StringReader("1SQFO+3-8;p^-wG-Cnt");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      char[] charArray0 = new char[1];
      char[] charArray1 = extendedBufferedReader0.lookAhead1(charArray0);
      assertEquals(1, charArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      char[] charArray0 = extendedBufferedReader0.lookAhead2(0);
      char[] charArray1 = extendedBufferedReader0.lookAhead1(charArray0);
      assertEquals(0, charArray1.length);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      StringReader stringReader0 = new StringReader("zu-4~(,lL9p (");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      int int0 = extendedBufferedReader0.lookAhead0();
      assertEquals(122, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      StringReader stringReader0 = new StringReader("F,2=");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      char[] charArray0 = extendedBufferedReader0.lookAhead2(4612);
      int int0 = extendedBufferedReader0.read1(charArray0, 1, 32);
      assertEquals(4, int0);
      assertEquals(4612, charArray0.length);
      
      int int1 = extendedBufferedReader0.lookAhead0();
      assertEquals((-1), int1);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.close();
      boolean boolean0 = extendedBufferedReader0.isClosed();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      int int0 = extendedBufferedReader0.read0();
      assertEquals((-1), int0);
      
      long long0 = extendedBufferedReader0.getPosition();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      char[] charArray0 = new char[2];
      extendedBufferedReader0.read1(charArray0, 1, 1);
      long long0 = extendedBufferedReader0.getPosition();
      assertEquals((-1L), long0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      StringReader stringReader0 = new StringReader("1SQFO+3-8;p^-wG-Cnt");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      int int0 = extendedBufferedReader0.read0();
      int int1 = extendedBufferedReader0.getLastChar();
      assertEquals(49, int1);
      assertTrue(int1 == int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.close();
      try { 
        extendedBufferedReader0.readLine();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream closed
         //
         verifyException("java.io.BufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      // Undeclared exception!
      try { 
        extendedBufferedReader0.read1((char[]) null, 30, 30);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      char[] charArray0 = new char[6];
      extendedBufferedReader0.close();
      try { 
        extendedBufferedReader0.read1(charArray0, 1, 1);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream closed
         //
         verifyException("java.io.BufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.close();
      try { 
        extendedBufferedReader0.read0();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream closed
         //
         verifyException("java.io.BufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      // Undeclared exception!
      try { 
        extendedBufferedReader0.lookAhead2((-4253));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -4253
         //
         verifyException("org.apache.commons.csv.ExtendedBufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.close();
      try { 
        extendedBufferedReader0.lookAhead2(212);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream closed
         //
         verifyException("java.io.BufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      // Undeclared exception!
      try { 
        extendedBufferedReader0.lookAhead1((char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.ExtendedBufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.close();
      char[] charArray0 = new char[1];
      try { 
        extendedBufferedReader0.lookAhead1(charArray0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream closed
         //
         verifyException("java.io.BufferedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ExtendedBufferedReader extendedBufferedReader0 = null;
      try {
        extendedBufferedReader0 = new ExtendedBufferedReader((Reader) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.io.Reader", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      String string0 = extendedBufferedReader0.readLine();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      int int0 = extendedBufferedReader0.read1((char[]) null, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.read0();
      int int0 = extendedBufferedReader0.read0();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      StringReader stringReader0 = new StringReader("q>:2TkH(M");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      char[] charArray0 = new char[6];
      int int0 = extendedBufferedReader0.read1(charArray0, 1, 1);
      assertEquals(1, int0);
      assertArrayEquals(new char[] {'\u0000', 'q', '\u0000', '\u0000', '\u0000', '\u0000'}, charArray0);
      
      long long0 = extendedBufferedReader0.getCurrentLineNumber();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      int int0 = extendedBufferedReader0.read0();
      assertEquals((-1), int0);
      
      long long0 = extendedBufferedReader0.getCurrentLineNumber();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      long long0 = extendedBufferedReader0.getCurrentLineNumber();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      StringReader stringReader0 = new StringReader("1SQFO+3-8;p^-wG-Cnt");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      String string0 = extendedBufferedReader0.readLine();
      assertEquals("1SQFO+3-8;p^-wG-Cnt", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      long long0 = extendedBufferedReader0.getPosition();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      StringReader stringReader0 = new StringReader("1SQFO+3-8;p^-wG-Cnt");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      int int0 = extendedBufferedReader0.getLastChar();
      assertEquals((-2), int0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      boolean boolean0 = extendedBufferedReader0.isClosed();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      extendedBufferedReader0.close();
      try { 
        extendedBufferedReader0.lookAhead0();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream closed
         //
         verifyException("java.io.BufferedReader", e);
      }
  }
}
