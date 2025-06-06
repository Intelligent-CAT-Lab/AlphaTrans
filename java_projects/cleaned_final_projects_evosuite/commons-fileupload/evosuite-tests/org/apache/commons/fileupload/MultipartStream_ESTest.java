

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



package org.apache.commons.fileupload;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.BufferedInputStream;
import java.io.ByteArrayInputStream;
import java.io.DataInputStream;
import java.io.FileDescriptor;
import java.io.IOException;
import java.io.InputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import org.apache.commons.fileupload.MultipartStream;
import org.apache.commons.fileupload.ProgressListener;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockFileInputStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MultipartStream_ESTest extends MultipartStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte) (-1));
      byte[] byteArray1 = new byte[9];
      byteArray1[0] = (byte)9;
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = new MultipartStream(byteArrayInputStream0, byteArray0, (byte)9, multipartStream_ProgressNotifier0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      int int0 = multipartStream_ItemInputStream0.read();
      assertEquals(0, byteArrayInputStream0.available());
      assertEquals(9, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip((byte)13);
      multipartStream0.newInputStream();
      assertEquals(0, byteArrayInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      multipartStream0.readByte();
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      assertEquals(0, byteArrayInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      byteArray0[0] = (byte)20;
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(byteArrayInputStream0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(bufferedInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      try { 
        multipartStream_ItemInputStream0.read1(byteArray0, 1, 2006);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      byte[] byteArray1 = new byte[8];
      byteArray1[0] = (byte)13;
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      try { 
        multipartStream_ItemInputStream0.close0();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip((byte)13);
      int int0 = multipartStream0.findByte((byte) (-1), 0);
      assertEquals(0, byteArrayInputStream0.available());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FileDescriptor fileDescriptor0 = new FileDescriptor();
      MockFileInputStream mockFileInputStream0 = new MockFileInputStream(fileDescriptor0);
      byte[] byteArray0 = new byte[0];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(mockFileInputStream0, byteArray0);
      int int0 = multipartStream0.findByte((byte)36, 8);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      byte[] byteArray0 = new byte[19];
      boolean boolean0 = MultipartStream.arrayequals(byteArray0, byteArray0, (byte)13);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      byteArray0[0] = (byte)20;
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(byteArrayInputStream0);
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte)20);
      MultipartStream multipartStream0 = new MultipartStream(bufferedInputStream0, byteArray0, (byte)20, multipartStream_ProgressNotifier0);
      try { 
        multipartStream0.readHeaders();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      PipedInputStream pipedInputStream0 = new PipedInputStream(pipedOutputStream0);
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream1(pipedInputStream0, byteArray0, 490);
      byte[] byteArray1 = new byte[6];
      try { 
        multipartStream0.setBoundary(byteArray1);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // The length of a boundary token cannot be changed
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte) (-1));
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(byteArrayInputStream0);
      MultipartStream multipartStream0 = new MultipartStream(bufferedInputStream0, byteArray0, (byte)9, multipartStream_ProgressNotifier0);
      assertEquals(10240, MultipartStream.HEADER_PART_SIZE_MAX);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier((ProgressListener) null, 0);
      multipartStream_ProgressNotifier0.noteBytesRead(0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      int int0 = multipartStream_ItemInputStream0.available();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      byteArray0[0] = (byte)20;
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(byteArrayInputStream0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(bufferedInputStream0, byteArray0);
      byte byte0 = multipartStream0.readByte();
      assertEquals(0, byteArrayInputStream0.available());
      assertEquals((byte)20, byte0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      byte[] byteArray1 = new byte[0];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray1);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip(0L);
      assertEquals(0, byteArrayInputStream0.available());
      
      MultipartStream.ItemInputStream multipartStream_ItemInputStream1 = multipartStream0.newInputStream();
      assertEquals(19, multipartStream_ItemInputStream1.available());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3((InputStream) null, byteArray0);
      int int0 = multipartStream0.findSeparator();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3((InputStream) null, byteArray0);
      // Undeclared exception!
      try { 
        multipartStream0.readHeaders();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, 0L);
      MultipartStream multipartStream1 = MultipartStream.MultipartStream2(multipartStream_ItemInputStream0, byteArray0, multipartStream_ProgressNotifier0);
      try { 
        multipartStream1.readByte();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream1((InputStream) null, byteArray0, 468);
      // Undeclared exception!
      try { 
        multipartStream0.readByte();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip((-284L));
      // Undeclared exception!
      try { 
        multipartStream0.readBoundary();
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -276 out of bounds for length 4096
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      byte[] byteArray1 = new byte[0];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray1);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip((-8L));
      // Undeclared exception!
      try { 
        multipartStream0.newInputStream();
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -8 out of bounds for length 4096
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      byte[] byteArray0 = new byte[19];
      // Undeclared exception!
      try { 
        MultipartStream.arrayequals((byte[]) null, byteArray0, 1748);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      // Undeclared exception!
      try { 
        MultipartStream.MultipartStream3(pipedInputStream0, (byte[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // boundary may not be null
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (-1815L));
      // Undeclared exception!
      try { 
        MultipartStream.MultipartStream2(pipedInputStream0, (byte[]) null, multipartStream_ProgressNotifier0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // boundary may not be null
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      byte[] byteArray1 = new byte[4];
      byteArray1[0] = (byte)45;
      boolean boolean0 = MultipartStream.arrayequals(byteArray1, byteArray0, (byte)13);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte)9);
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      MultipartStream multipartStream0 = new MultipartStream(byteArrayInputStream0, byteArray0, 59, multipartStream_ProgressNotifier0);
      multipartStream0.readByte();
      assertEquals(0, byteArrayInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      try { 
        multipartStream0.readByte();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // No more data is available
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      multipartStream0.readByte();
      byte byte0 = multipartStream0.readByte();
      assertEquals(0, byteArrayInputStream0.available());
      assertEquals((byte)0, byte0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      byte[] byteArray0 = new byte[2];
      MultipartStream multipartStream0 = null;
      try {
        multipartStream0 = new MultipartStream(pipedInputStream0, byteArray0, 5, (MultipartStream.ProgressNotifier) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The buffer size specified for the MultipartStream is too small
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier((ProgressListener) null, 0);
      MultipartStream multipartStream0 = null;
      try {
        multipartStream0 = new MultipartStream(inputStream0, (byte[]) null, 1024, multipartStream_ProgressNotifier0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // boundary may not be null
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      MultipartStream.MalformedStreamException multipartStream_MalformedStreamException0 = new MultipartStream.MalformedStreamException("[pyuK61Ga;b5b)id+");
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      MultipartStream.IllegalBoundaryException multipartStream_IllegalBoundaryException0 = new MultipartStream.IllegalBoundaryException("]j`?$`2Z)i(q");
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte) (-1));
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      MultipartStream multipartStream0 = new MultipartStream(byteArrayInputStream0, byteArray0, (byte)25, multipartStream_ProgressNotifier0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.close1(true);
      try { 
        multipartStream_ItemInputStream0.skip(0L);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      byte[] byteArray1 = new byte[0];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray1);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip(0L);
      try { 
        multipartStream_ItemInputStream0.close0();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.close1(true);
      multipartStream_ItemInputStream0.close0();
      assertTrue(multipartStream_ItemInputStream0.isClosed());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      // Undeclared exception!
      try { 
        multipartStream_ItemInputStream0.read1(byteArray1, (byte)13, 1024);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.skip((-1321L));
      // Undeclared exception!
      try { 
        multipartStream_ItemInputStream0.read1(byteArray1, 10240, (-2532));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      FileDescriptor fileDescriptor0 = new FileDescriptor();
      MockFileInputStream mockFileInputStream0 = new MockFileInputStream(fileDescriptor0);
      byte[] byteArray0 = new byte[3];
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier((ProgressListener) null, (byte)0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream2(mockFileInputStream0, byteArray0, multipartStream_ProgressNotifier0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.read1(byteArray0, (byte)13, (byte)0);
      assertEquals(0, multipartStream_ItemInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte) (-1));
      byte[] byteArray1 = new byte[9];
      byteArray1[2] = (byte) (-1);
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = new MultipartStream(byteArrayInputStream0, byteArray0, (byte)25, multipartStream_ProgressNotifier0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      byteArrayInputStream0.read(byteArray0);
      int int0 = multipartStream_ItemInputStream0.read();
      assertEquals(1L, multipartStream_ItemInputStream0.getBytesRead());
      assertEquals(255, int0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      try { 
        multipartStream_ItemInputStream0.readAllBytes();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      multipartStream_ItemInputStream0.close1(true);
      try { 
        multipartStream_ItemInputStream0.read();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.MultipartStream$ItemInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte) (-1));
      byte[] byteArray1 = new byte[9];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray1);
      MultipartStream multipartStream0 = new MultipartStream(byteArrayInputStream0, byteArray0, (byte)25, multipartStream_ProgressNotifier0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.new ItemInputStream();
      int int0 = multipartStream_ItemInputStream0.read0();
      assertEquals(0, byteArrayInputStream0.available());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      byte[] byteArray0 = new byte[23];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(byteArrayInputStream0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(bufferedInputStream0, byteArray0);
      multipartStream0.readByte();
      int int0 = multipartStream0.findByte((byte)36, 8);
      assertEquals(0, byteArrayInputStream0.available());
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      FileDescriptor fileDescriptor0 = new FileDescriptor();
      MockFileInputStream mockFileInputStream0 = new MockFileInputStream(fileDescriptor0);
      byte[] byteArray0 = new byte[0];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(mockFileInputStream0, byteArray0);
      // Undeclared exception!
      try { 
        multipartStream0.findByte((byte)36, (-2044));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2044 out of bounds for length 4096
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        MultipartStream.arrayequals(byteArray0, byteArray0, 70);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      boolean boolean0 = MultipartStream.arrayequals(byteArray0, byteArray0, (-2071));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)13;
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(byteArrayInputStream0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(bufferedInputStream0, byteArray0);
      try { 
        multipartStream0.readHeaders();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      byte[] byteArray1 = new byte[5];
      byteArray1[0] = (byte)13;
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(byteArrayInputStream0, byteArray1);
      assertEquals((byte)13, MultipartStream.CR);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      multipartStream0.setBoundary(byteArray0);
      assertNull(multipartStream0.getHeaderEncoding());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      try { 
        multipartStream0.readBoundary();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Stream ended unexpectedly
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      // Undeclared exception!
      try { 
        MultipartStream.MultipartStream1(multipartStream_ItemInputStream0, byteArray0, (-10));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The buffer size specified for the MultipartStream is too small
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3((InputStream) null, byteArray0);
      byte[] byteArray1 = new byte[4];
      try { 
        multipartStream0.setBoundary(byteArray1);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // The length of a boundary token cannot be changed
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      multipartStream0.setHeaderEncoding("");
      assertEquals(10240, MultipartStream.HEADER_PART_SIZE_MAX);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      PipedInputStream pipedInputStream0 = new PipedInputStream(pipedOutputStream0);
      DataInputStream dataInputStream0 = new DataInputStream(pipedInputStream0);
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(dataInputStream0, byteArray0);
      String string0 = multipartStream0.getHeaderEncoding();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      // Undeclared exception!
      try { 
        MultipartStream.MultipartStream0();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // boundary may not be null
         //
         verifyException("org.apache.commons.fileupload.MultipartStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      byte[] byteArray0 = new byte[19];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(pipedInputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      multipartStream_ItemInputStream0.getBytesRead();
      assertEquals(0, multipartStream_ItemInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[1];
      MultipartStream multipartStream0 = MultipartStream.MultipartStream3(inputStream0, byteArray0);
      MultipartStream.ItemInputStream multipartStream_ItemInputStream0 = multipartStream0.newInputStream();
      multipartStream_ItemInputStream0.isClosed();
      assertEquals(0, multipartStream_ItemInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      ProgressListener progressListener0 = mock(ProgressListener.class, new ViolatedAssumptionAnswer());
      MultipartStream.ProgressNotifier multipartStream_ProgressNotifier0 = new MultipartStream.ProgressNotifier(progressListener0, (byte)9);
      multipartStream_ProgressNotifier0.noteItem();
  }
}
