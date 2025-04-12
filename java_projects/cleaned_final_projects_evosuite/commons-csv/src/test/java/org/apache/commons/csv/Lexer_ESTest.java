



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
import java.io.PipedReader;
import java.io.Reader;
import java.io.StringReader;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.ExtendedBufferedReader;
import org.apache.commons.csv.Lexer;
import org.apache.commons.csv.Token;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Lexer_ESTest extends Lexer_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.readEndOfLine(13);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader("KQ$O+cyb{;");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isStartOfLine((-2588));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.newFormat('\u008A');
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isEscapeDelimiter();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      cSVFormat_Builder0.setCommentMarker0('s');
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isCommentStart(65534);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      cSVFormat_Builder0.setDelimiter1("?N0<'");
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader("");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.readEndOfLine(0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isStartOfLine(549);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      Lexer lexer0 = new Lexer(cSVFormat0, (ExtendedBufferedReader) null);
      boolean boolean0 = lexer0.isQuoteChar((-3398));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader("");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isEscape(0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isEndOfFile((-1));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      Lexer lexer0 = new Lexer(cSVFormat0, (ExtendedBufferedReader) null);
      boolean boolean0 = lexer0.isEndOfFile(0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.newFormat('y');
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isDelimiter((-992));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader("");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isCommentStart(0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader("");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      lexer0.close();
      boolean boolean0 = lexer0.isClosed();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      Token token0 = new Token();
      lexer0.nextToken(token0);
      String string0 = lexer0.getFirstEol();
      assertEquals("\r\n", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      lexer0.readEscape();
      long long0 = lexer0.getCurrentLineNumber();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      lexer0.readEscape();
      long long0 = lexer0.getCharacterPosition();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader("");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      // Undeclared exception!
      try { 
        lexer0.trimTrailingSpaces((StringBuilder) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.Lexer", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      Lexer lexer0 = new Lexer(cSVFormat0, (ExtendedBufferedReader) null);
      // Undeclared exception!
      try { 
        lexer0.readEscape();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.Lexer", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      Lexer lexer0 = new Lexer(cSVFormat0, (ExtendedBufferedReader) null);
      // Undeclared exception!
      try { 
        lexer0.nextToken((Token) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.Lexer", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_CSV;
      PipedReader pipedReader0 = new PipedReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(pipedReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      Token token0 = new Token();
      try { 
        lexer0.nextToken(token0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      Lexer lexer0 = new Lexer(cSVFormat0, (ExtendedBufferedReader) null);
      // Undeclared exception!
      try { 
        lexer0.isEscapeDelimiter();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.Lexer", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(pipedReader0);
      CSVFormat cSVFormat0 = CSVFormat.ORACLE;
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      try { 
        lexer0.isEscapeDelimiter();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = null;
      try {
        lexer0 = new Lexer((CSVFormat) null, extendedBufferedReader0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.Lexer", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      StringBuilder stringBuilder0 = new StringBuilder();
      lexer0.trimTrailingSpaces(stringBuilder0);
      assertEquals("", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      StringReader stringReader0 = new StringReader("t# EauyH9!1");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      int int0 = lexer0.readEscape();
      assertEquals(9, int0);
      
      int int1 = lexer0.readEscape();
      assertEquals((-1), int1);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader("org.apache.commons.csv.Lexer");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      int int0 = lexer0.readEscape();
      assertEquals((-1), int0);
      
      int int1 = lexer0.readEscape();
      assertEquals(13, int1);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader("bZFFw_G;");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      int int0 = lexer0.readEscape();
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      int int0 = lexer0.readEscape();
      assertEquals((-1), int0);
      
      lexer0.readEscape();
      int int1 = lexer0.readEscape();
      assertEquals(10, int1);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.readEndOfLine(13);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Token token0 = new Token();
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      Token token1 = lexer0.nextToken(token0);
      assertSame(token1, token0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      Token token0 = new Token();
      Token token1 = lexer0.nextToken(token0);
      Token token2 = lexer0.nextToken(token1);
      assertSame(token2, token0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      StringReader stringReader0 = new StringReader("khe delimiter canno. be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      Token token0 = new Token();
      Token token1 = lexer0.nextToken(token0);
      Token token2 = lexer0.nextToken(token1);
      assertSame(token1, token2);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      Token token0 = new Token();
      lexer0.readEscape();
      lexer0.readEscape();
      Token token1 = lexer0.nextToken(token0);
      assertSame(token0, token1);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isStartOfLine(10);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      StringReader stringReader0 = new StringReader("2\"jd5*jbNaI)QKi");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      int int0 = lexer0.readEscape();
      assertEquals((-1), int0);
      
      int int1 = lexer0.readEscape();
      assertEquals(34, int1);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      lexer0.readEscape();
      Token token0 = new Token();
      Token token1 = lexer0.nextToken(token0);
      assertSame(token1, token0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isEscapeDelimiter();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isDelimiter(9);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      Reader reader0 = Reader.nullReader();
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(reader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isCommentStart(65534);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Token token0 = new Token();
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      lexer0.nextToken(token0);
      try { 
        lexer0.readEscape();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // EOF whilst processing escape sequence
         //
         verifyException("org.apache.commons.csv.Lexer", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader("");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      boolean boolean0 = lexer0.isClosed();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader("The delimiter cannot be a line break");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      long long0 = lexer0.getCurrentLineNumber();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      String string0 = lexer0.getFirstEol();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      StringReader stringReader0 = new StringReader(")\r\n");
      ExtendedBufferedReader extendedBufferedReader0 = new ExtendedBufferedReader(stringReader0);
      Lexer lexer0 = new Lexer(cSVFormat0, extendedBufferedReader0);
      long long0 = lexer0.getCharacterPosition();
      assertEquals(0L, long0);
  }
}
