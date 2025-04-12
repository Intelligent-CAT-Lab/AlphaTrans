



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
import java.io.ByteArrayInputStream;
import java.io.CharArrayWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.io.PipedReader;
import java.io.PipedWriter;
import java.io.SequenceInputStream;
import java.io.StringWriter;
import java.io.UncheckedIOException;
import java.nio.BufferOverflowException;
import java.nio.CharBuffer;
import java.nio.ReadOnlyBufferException;
import java.nio.charset.Charset;
import java.nio.file.LinkOption;
import java.util.List;
import java.util.PriorityQueue;
import java.util.function.UnaryOperator;
import java.util.stream.Stream;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVPrinter;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockFileWriter;
import org.evosuite.runtime.mock.java.io.MockPrintWriter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CSVPrinter_ESTest extends CSVPrinter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.ORACLE;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      InputStream[] inputStreamArray0 = new InputStream[2];
      Stream<InputStream> stream0 = Stream.of(inputStreamArray0);
      cSVPrinter0.printRecord2(stream0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      char[] charArray0 = new char[2];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      charBuffer0.put('N');
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVPrinter cSVPrinter0 = new CSVPrinter(charBuffer0, cSVFormat0);
      // Undeclared exception!
      try { 
        cSVPrinter0.println();
        fail("Expecting exception: BufferOverflowException");
      
      } catch(BufferOverflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.CharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      char[] charArray0 = new char[7];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      CharBuffer charBuffer1 = CharBuffer.wrap((CharSequence) charBuffer0, 0, 0);
      CSVPrinter cSVPrinter0 = new CSVPrinter(charBuffer1, cSVFormat0);
      Object[] objectArray0 = new Object[1];
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecords1(objectArray0);
        fail("Expecting exception: ReadOnlyBufferException");
      
      } catch(ReadOnlyBufferException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.CharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.EXCEL;
      Object[] objectArray0 = new Object[17];
      char[] charArray0 = new char[3];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(charBuffer0);
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecords1(objectArray0);
        fail("Expecting exception: BufferOverflowException");
      
      } catch(BufferOverflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.CharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecords1((Object[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      PipedWriter pipedWriter0 = new PipedWriter();
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(pipedWriter0);
      Object[] objectArray0 = new Object[8];
      try { 
        cSVPrinter0.printRecords1(objectArray0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedWriter", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecords0((Iterable<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.CSVPrinter", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecord2((Stream<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.CSVPrinter", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.ORACLE;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      InputStream[] inputStreamArray0 = new InputStream[2];
      byte[] byteArray0 = new byte[5];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0, (byte)44, 10);
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(byteArrayInputStream0, byteArrayInputStream0);
      inputStreamArray0[0] = (InputStream) sequenceInputStream0;
      Stream<InputStream> stream0 = Stream.of(inputStreamArray0);
      Stream<InputStream> stream1 = stream0.sorted();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecord2(stream1);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.io.SequenceInputStream cannot be cast to class java.lang.Comparable (java.io.SequenceInputStream and java.lang.Comparable are in module java.base of loader 'bootstrap')
         //
         verifyException("java.util.Comparators$NaturalOrderComparator", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.ORACLE;
      Object[] objectArray0 = new Object[4];
      CharBuffer charBuffer0 = CharBuffer.allocate(0);
      CSVPrinter cSVPrinter0 = new CSVPrinter(charBuffer0, cSVFormat0);
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecord1(objectArray0);
        fail("Expecting exception: BufferOverflowException");
      
      } catch(BufferOverflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.CharBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD_CSV;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecord1((Object[]) null);
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
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      OutputStreamWriter outputStreamWriter0 = new OutputStreamWriter(pipedOutputStream0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0);
      cSVPrinter0.close1(false);
      Object[] objectArray0 = new Object[7];
      try { 
        cSVPrinter0.printRecord1(objectArray0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecord0((Iterable<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.csv.CSVPrinter", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      PipedReader pipedReader0 = new PipedReader();
      CSVParser cSVParser0 = cSVFormat0.parse(pipedReader0);
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      // Undeclared exception!
      try { 
        cSVPrinter0.printRecord0(cSVParser0);
        fail("Expecting exception: UncheckedIOException");
      
      } catch(UncheckedIOException e) {
         //
         // IOException reading next record: java.io.IOException: Pipe not connected
         //
         verifyException("org.apache.commons.csv.CSVParser$CSVRecordIterator", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat.Builder cSVFormat_Builder1 = cSVFormat_Builder0.setCommentMarker0(']');
      CSVFormat cSVFormat0 = cSVFormat_Builder1.build();
      char[] charArray0 = new char[6];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(charBuffer0);
      // Undeclared exception!
      try { 
        cSVPrinter0.printComment("format");
        fail("Expecting exception: BufferOverflowException");
      
      } catch(BufferOverflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      Character character0 = Character.valueOf('b');
      cSVFormat_Builder0.setCommentMarker1(character0);
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      PipedWriter pipedWriter0 = new PipedWriter();
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(pipedWriter0);
      try { 
        cSVPrinter0.printComment(",Zt[8] x5W'eE3}");
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedWriter", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD_CSV;
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      OutputStreamWriter outputStreamWriter0 = new OutputStreamWriter(pipedOutputStream0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0);
      outputStreamWriter0.close();
      PipedInputStream pipedInputStream0 = new PipedInputStream(101);
      try { 
        cSVPrinter0.print(pipedInputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD_CSV;
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      OutputStreamWriter outputStreamWriter0 = new OutputStreamWriter(pipedOutputStream0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0);
      cSVPrinter0.close0();
      try { 
        cSVPrinter0.flush();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      MockFile mockFile0 = new MockFile("[szt,p!Q0Rxds", "[szt,p!Q0Rxds");
      Charset charset0 = Charset.defaultCharset();
      CSVPrinter cSVPrinter0 = cSVFormat0.print1(mockFile0, charset0);
      cSVPrinter0.close0();
      try { 
        cSVPrinter0.close1(true);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      OutputStreamWriter outputStreamWriter0 = new OutputStreamWriter(pipedOutputStream0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0);
      outputStreamWriter0.write(1);
      try { 
        cSVPrinter0.close0();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      MockFileWriter mockFileWriter0 = new MockFileWriter("format");
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(mockFileWriter0);
      cSVPrinter0.close1(true);
      try { 
        cSVPrinter0.close();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      Character character0 = Character.valueOf('a');
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat.Builder cSVFormat_Builder1 = cSVFormat_Builder0.setCommentMarker1(character0);
      Object[] objectArray0 = new Object[2];
      objectArray0[1] = (Object) cSVFormat0;
      CSVFormat.Builder cSVFormat_Builder2 = cSVFormat_Builder1.setHeaderComments0(objectArray0);
      CSVFormat cSVFormat1 = cSVFormat_Builder2.build();
      char[] charArray0 = new char[7];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      CSVPrinter cSVPrinter0 = null;
      try {
        cSVPrinter0 = new CSVPrinter(charBuffer0, cSVFormat1);
        fail("Expecting exception: BufferOverflowException");
      
      } catch(BufferOverflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      CSVPrinter cSVPrinter0 = null;
      try {
        cSVPrinter0 = new CSVPrinter((Appendable) null, cSVFormat0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // appendable
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.EXCEL;
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      Character character0 = Character.valueOf('u');
      CSVFormat.Builder cSVFormat_Builder1 = cSVFormat_Builder0.setCommentMarker1(character0);
      Object[] objectArray0 = new Object[17];
      objectArray0[13] = (Object) cSVFormat0;
      cSVFormat_Builder0.setHeaderComments0(objectArray0);
      CSVFormat cSVFormat1 = cSVFormat_Builder1.build();
      PipedWriter pipedWriter0 = new PipedWriter();
      CSVPrinter cSVPrinter0 = null;
      try {
        cSVPrinter0 = new CSVPrinter(pipedWriter0, cSVFormat1);
        fail("Expecting exception: IOException");
      
      } catch(Throwable e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedWriter", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      CharArrayWriter charArrayWriter0 = new CharArrayWriter();
      MockPrintWriter mockPrintWriter0 = new MockPrintWriter(charArrayWriter0, true);
      CSVFormat cSVFormat0 = CSVFormat.newFormat('+');
      CSVPrinter cSVPrinter0 = new CSVPrinter(mockPrintWriter0, cSVFormat0);
      LinkOption linkOption0 = LinkOption.NOFOLLOW_LINKS;
      LinkOption[] linkOptionArray0 = new LinkOption[3];
      linkOptionArray0[0] = linkOption0;
      linkOptionArray0[1] = linkOption0;
      linkOptionArray0[2] = linkOption0;
      List<LinkOption> list0 = List.of(linkOptionArray0);
      cSVPrinter0.printRecords0(list0);
      assertEquals(105, charArrayWriter0.size());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      StringWriter stringWriter0 = new StringWriter();
      CSVFormat cSVFormat0 = CSVFormat.EXCEL;
      CSVPrinter cSVPrinter0 = new CSVPrinter(stringWriter0, cSVFormat0);
      LinkOption[] linkOptionArray0 = new LinkOption[6];
      LinkOption linkOption0 = LinkOption.NOFOLLOW_LINKS;
      linkOptionArray0[0] = linkOption0;
      linkOptionArray0[1] = linkOptionArray0[0];
      linkOptionArray0[2] = linkOptionArray0[0];
      linkOptionArray0[3] = linkOptionArray0[0];
      linkOptionArray0[4] = linkOption0;
      linkOptionArray0[5] = linkOptionArray0[1];
      List<LinkOption> list0 = List.of(linkOptionArray0);
      cSVPrinter0.printRecord0(list0);
      assertEquals(6, list0.size());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.printComment((String) null);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.printComment("");
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.flush();
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      cSVFormat_Builder0.setAutoFlush(true);
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.close1(false);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.INFORMIX_UNLOAD;
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      OutputStreamWriter outputStreamWriter0 = new OutputStreamWriter(pipedOutputStream0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0);
      Object[] objectArray0 = new Object[7];
      cSVPrinter0.printRecord1(objectArray0);
      assertEquals(7, objectArray0.length);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      OutputStreamWriter outputStreamWriter0 = new OutputStreamWriter(pipedOutputStream0);
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(outputStreamWriter0);
      cSVPrinter0.println();
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringWriter stringWriter0 = new StringWriter(1820);
      StringBuffer stringBuffer0 = stringWriter0.getBuffer();
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(stringBuffer0);
      PriorityQueue<InputStream> priorityQueue0 = new PriorityQueue<InputStream>();
      Object[] objectArray0 = new Object[8];
      objectArray0[4] = (Object) priorityQueue0;
      cSVPrinter0.printRecords1(objectArray0);
      assertEquals("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n", stringBuffer0.toString());
      assertEquals("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n", stringWriter0.toString());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      cSVFormat_Builder0.setCommentMarker0('Z');
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.printComment("\r\n");
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      cSVFormat_Builder0.setCommentMarker0('d');
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.printComment("\r`");
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat.Builder cSVFormat_Builder1 = cSVFormat_Builder0.setCommentMarker0('a');
      CSVFormat cSVFormat0 = cSVFormat_Builder1.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.printComment("T\n");
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      Character character0 = Character.valueOf('%');
      cSVFormat_Builder0.setCommentMarker1(character0);
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      Object object0 = new Object();
      cSVPrinter0.print(object0);
      cSVPrinter0.printComment("RFC4180");
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      Character character0 = Character.valueOf(')');
      cSVFormat_Builder0.setCommentMarker1(character0);
      Object[] objectArray0 = new Object[5];
      objectArray0[0] = (Object) cSVFormat_Builder0;
      CSVFormat.Builder cSVFormat_Builder1 = cSVFormat_Builder0.setHeaderComments0(objectArray0);
      CSVFormat cSVFormat0 = cSVFormat_Builder1.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      assertNotNull(cSVPrinter0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      char[] charArray0 = new char[2];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      CSVFormat cSVFormat0 = CSVFormat.TDF;
      CSVPrinter cSVPrinter0 = new CSVPrinter(charBuffer0, cSVFormat0);
      cSVPrinter0.flush();
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      StringWriter stringWriter0 = new StringWriter(1820);
      StringBuffer stringBuffer0 = stringWriter0.getBuffer();
      CSVPrinter cSVPrinter0 = cSVFormat0.print0(stringBuffer0);
      cSVPrinter0.close1(false);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      cSVPrinter0.close();
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      Appendable appendable0 = cSVPrinter0.getOut();
      assertNotNull(appendable0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVPrinter cSVPrinter0 = cSVFormat0.printer();
      UnaryOperator<InputStream> unaryOperator0 = UnaryOperator.identity();
      Stream<InputStream> stream0 = Stream.iterate((InputStream) null, unaryOperator0);
      // Undeclared exception!
      cSVPrinter0.printRecord2(stream0);
  }
}
