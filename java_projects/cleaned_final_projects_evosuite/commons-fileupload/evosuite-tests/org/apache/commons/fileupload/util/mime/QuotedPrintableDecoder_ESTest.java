

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



package org.apache.commons.fileupload.util.mime;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class QuotedPrintableDecoder_ESTest extends QuotedPrintableDecoder_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[9];
      byteArray0[3] = (byte)61;
      byteArray0[4] = (byte)13;
      byteArray0[5] = (byte)13;
      try { 
        QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Invalid quoted printable encoding; CR must be followed by LF
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte)61;
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)61);
      try { 
        QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Invalid quoted printable encoding; truncated escape sequence
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[0] = (byte)97;
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(0);
      int int0 = QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
      assertEquals(6, byteArrayOutputStream0.size());
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[1] = (byte)95;
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(0);
      int int0 = QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
      assertEquals(6, byteArrayOutputStream0.size());
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        QuotedPrintableDecoder.decode(byteArray0, (OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)61);
      byte[] byteArray0 = new byte[6];
      byteArray0[1] = (byte)61;
      byteArray0[2] = (byte)51;
      try { 
        QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Invalid quoted printable encoding: not a valid hex digit: 0
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[3];
      byteArray0[0] = (byte)61;
      byteArray0[1] = (byte)13;
      try { 
        QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Invalid quoted printable encoding; CR must be followed by LF
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)61);
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)61;
      try { 
        QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Invalid quoted printable encoding; truncated escape sequence
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream((byte)61);
      byte[] byteArray0 = new byte[3];
      byteArray0[0] = (byte)61;
      try { 
        QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Invalid quoted printable encoding: not a valid hex digit: 0
         //
         verifyException("org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)95;
      int int0 = QuotedPrintableDecoder.decode(byteArray0, byteArrayOutputStream0);
      assertEquals(1, byteArrayOutputStream0.size());
      assertEquals(0, int0);
  }
}
