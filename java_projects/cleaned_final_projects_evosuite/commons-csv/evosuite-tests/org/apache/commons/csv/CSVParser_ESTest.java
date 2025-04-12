



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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.io.PipedReader;
import java.io.Reader;
import java.io.UncheckedIOException;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.util.NoSuchElementException;
import java.util.function.Consumer;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.csv.DuplicateHeaderMode;
import org.apache.commons.csv.QuoteMode;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.net.MockURL;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CSVParser_ESTest extends CSVParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      MockFile mockFile0 = new MockFile("");
      Charset charset0 = Charset.defaultCharset();
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVParser cSVParser0 = CSVParser.parse0(mockFile0, charset0, cSVFormat0);
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("L}F", cSVFormat0);
      CSVParser.CSVRecordIterator cSVParser_CSVRecordIterator0 = cSVParser0.new CSVRecordIterator();
      cSVParser_CSVRecordIterator0.hasNext();
      cSVParser0.nextRecord();
      assertEquals(1L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("N", cSVFormat0);
      cSVParser0.nextRecord();
      assertEquals(1L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      PipedReader pipedReader0 = new PipedReader();
      CSVParser cSVParser0 = CSVParser.CSVParser1(pipedReader0, cSVFormat0);
      cSVParser0.iterator();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("N", cSVFormat0);
      cSVParser0.close();
      boolean boolean0 = cSVParser0.isClosed();
      assertTrue(boolean0);
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      Consumer<Object> consumer0 = (Consumer<Object>) mock(Consumer.class, new ViolatedAssumptionAnswer());
      cSVParser0.forEach(consumer0);
      long long0 = cSVParser0.getRecordNumber();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      Consumer<Object> consumer0 = (Consumer<Object>) mock(Consumer.class, new ViolatedAssumptionAnswer());
      cSVParser0.forEach(consumer0);
      long long0 = cSVParser0.getCurrentLineNumber();
      assertEquals(1L, cSVParser0.getRecordNumber());
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      URL uRL0 = MockURL.getHttpExample();
      Charset charset0 = Charset.defaultCharset();
      try { 
        CSVParser.parse5(uRL0, charset0, cSVFormat0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Could not find: www.someFakeButWellFormedURL.org
         //
         verifyException("org.evosuite.runtime.mock.java.net.EvoHttpURLConnection", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      // Undeclared exception!
      try { 
        CSVParser.parse4((String) null, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // string
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      // Undeclared exception!
      try { 
        CSVParser.parse3(pipedReader0, (CSVFormat) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // format
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      MockFile mockFile0 = new MockFile("&{?cjN08V<.");
      Path path0 = mockFile0.toPath();
      Charset charset0 = Charset.defaultCharset();
      try { 
        CSVParser.parse2(path0, charset0, cSVFormat0);
        fail("Expecting exception: NoSuchFileException");
      
      } catch(NoSuchFileException e) {
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_CSV;
      // Undeclared exception!
      try { 
        CSVParser.parse2((Path) null, charset0, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // path
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Charset charset0 = Charset.defaultCharset();
      // Undeclared exception!
      try { 
        CSVParser.parse1((InputStream) null, charset0, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // inputStream
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      MockFile mockFile0 = new MockFile("\fe_");
      Charset charset0 = Charset.defaultCharset();
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      try { 
        CSVParser.parse0(mockFile0, charset0, cSVFormat0);
        fail("Expecting exception: NoSuchFileException");
      
      } catch(NoSuchFileException e) {
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      PipedReader pipedReader0 = new PipedReader();
      CSVParser cSVParser0 = CSVParser.CSVParser1(pipedReader0, cSVFormat0);
      try { 
        cSVParser0.nextRecord();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedReader", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = cSVFormat0.parse(pipedReader0);
      // Undeclared exception!
      try { 
        cSVParser0.getRecords();
        fail("Expecting exception: UncheckedIOException");
      
      } catch(UncheckedIOException e) {
         //
         // IOException reading next record: java.io.IOException: Pipe not connected
         //
         verifyException("org.apache.commons.csv.CSVParser$CSVRecordIterator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      // Undeclared exception!
      try { 
        CSVParser.CSVParser1((Reader) null, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // reader
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.ORACLE;
      CSVParser cSVParser0 = null;
      try {
        cSVParser0 = new CSVParser((Reader) null, cSVFormat0, 0L, (-554L));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // reader
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Reader reader0 = Reader.nullReader();
      CSVParser cSVParser0 = CSVParser.parse3(reader0, cSVFormat0);
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      PipedInputStream pipedInputStream0 = new PipedInputStream(pipedOutputStream0);
      Charset charset0 = Charset.defaultCharset();
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse1(pipedInputStream0, charset0, cSVFormat0);
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("N", cSVFormat0);
      cSVParser0.isClosed();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = new CSVParser(reader0, cSVFormat0, 4086L, 4086L);
      Consumer<Object> consumer0 = (Consumer<Object>) mock(Consumer.class, new ViolatedAssumptionAnswer());
      cSVParser0.forEach(consumer0);
      assertEquals(4085L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVParser cSVParser0 = CSVParser.parse4("E<OF", cSVFormat0);
      cSVParser0.stream();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Reader reader0 = Reader.nullReader();
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD_CSV;
      CSVParser cSVParser0 = new CSVParser(reader0, cSVFormat0, 0L, 0L);
      long long0 = cSVParser0.getRecordNumber();
      assertEquals((-1L), long0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("L}F", cSVFormat0);
      boolean boolean0 = cSVParser0.hasTrailerComment();
      assertFalse(boolean0);
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4(")\"MF;N=", cSVFormat0);
      boolean boolean0 = cSVParser0.hasHeaderComment();
      assertEquals(0L, cSVParser0.getRecordNumber());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Character character0 = Character.valueOf('(');
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat.Builder cSVFormat_Builder1 = cSVFormat_Builder0.setNullString("]N");
      QuoteMode quoteMode0 = QuoteMode.NONE;
      DuplicateHeaderMode duplicateHeaderMode0 = DuplicateHeaderMode.ALLOW_EMPTY;
      String[] stringArray0 = new String[6];
      CSVFormat cSVFormat0 = new CSVFormat((-711), true, true, "]N", "A header name is missing in ", character0, true, true, cSVFormat_Builder1, character0, true, character0, quoteMode0, true, duplicateHeaderMode0, stringArray0, true, true, stringArray0, "A header name is missing in ");
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      cSVParser0.getRecords();
      assertEquals(1L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("L}F", cSVFormat0);
      cSVParser0.getHeaderMap();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVParser cSVParser0 = CSVParser.parse4(" ", cSVFormat0);
      cSVParser0.getRecords();
      assertEquals(1L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("#C2rpb%", cSVFormat0);
      cSVParser0.getRecords();
      CSVParser.CSVRecordIterator cSVParser_CSVRecordIterator0 = cSVParser0.new CSVRecordIterator();
      // Undeclared exception!
      try { 
        cSVParser_CSVRecordIterator0.next();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // No more CSV records available
         //
         verifyException("org.apache.commons.csv.CSVParser$CSVRecordIterator", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("#C2rpb%", cSVFormat0);
      CSVParser.CSVRecordIterator cSVParser_CSVRecordIterator0 = cSVParser0.new CSVRecordIterator();
      CSVRecord cSVRecord0 = cSVParser_CSVRecordIterator0.next();
      assertEquals(1L, cSVParser0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4(")\"MF;N=", cSVFormat0);
      cSVParser0.close();
      CSVParser.CSVRecordIterator cSVParser_CSVRecordIterator0 = cSVParser0.new CSVRecordIterator();
      // Undeclared exception!
      try { 
        cSVParser_CSVRecordIterator0.next();
        fail("Expecting exception: NoSuchElementException");
      
      } catch(NoSuchElementException e) {
         //
         // CSVParser has been closed
         //
         verifyException("org.apache.commons.csv.CSVParser$CSVRecordIterator", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("L}F", cSVFormat0);
      CSVParser.CSVRecordIterator cSVParser_CSVRecordIterator0 = cSVParser0.new CSVRecordIterator();
      cSVParser_CSVRecordIterator0.hasNext();
      boolean boolean0 = cSVParser_CSVRecordIterator0.hasNext();
      assertEquals(1L, cSVParser0.getRecordNumber());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      cSVParser0.close();
      cSVParser0.getRecords();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      long long0 = cSVParser0.getRecordNumber();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      PipedReader pipedReader0 = new PipedReader();
      CSVParser cSVParser0 = CSVParser.CSVParser1(pipedReader0, cSVFormat0);
      cSVParser0.getTrailerComment();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.EXCEL;
      Charset charset0 = Charset.defaultCharset();
      // Undeclared exception!
      try { 
        CSVParser.parse5((URL) null, charset0, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // url
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("aJ", cSVFormat0);
      cSVParser0.getHeaderComment();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Charset charset0 = Charset.defaultCharset();
      // Undeclared exception!
      try { 
        CSVParser.parse0((File) null, charset0, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // file
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      MockFile mockFile0 = new MockFile("");
      Path path0 = mockFile0.toPath();
      Charset charset0 = Charset.defaultCharset();
      CSVParser cSVParser0 = CSVParser.parse2(path0, charset0, cSVFormat0);
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.newFormat('F');
      CSVParser cSVParser0 = CSVParser.parse4("", cSVFormat0);
      cSVParser0.getHeaderNames();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      cSVParser0.getCurrentLineNumber();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVParser cSVParser0 = CSVParser.parse4("]N", cSVFormat0);
      cSVParser0.getFirstEndOfLine();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.EXCEL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      cSVParser0.getHeaderMapRaw();
      assertEquals(0L, cSVParser0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVParser cSVParser0 = CSVParser.parse4("E<OF", cSVFormat0);
      CSVParser.CSVRecordIterator cSVParser_CSVRecordIterator0 = cSVParser0.new CSVRecordIterator();
      // Undeclared exception!
      try { 
        cSVParser_CSVRecordIterator0.remove();
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.CSVParser$CSVRecordIterator", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("vwt<sh@~`,g:5", cSVFormat0);
      cSVParser0.getRecords();
      assertEquals(1L, cSVParser0.getRecordNumber());
  }
}
