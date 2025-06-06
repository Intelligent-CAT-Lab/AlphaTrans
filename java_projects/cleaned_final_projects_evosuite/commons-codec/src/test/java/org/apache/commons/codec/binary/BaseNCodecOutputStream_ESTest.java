
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


package org.apache.commons.codec.binary;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PipedOutputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base16;
import org.apache.commons.codec.binary.Base32;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.BaseNCodec;
import org.apache.commons.codec.binary.BaseNCodecOutputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BaseNCodecOutputStream_ESTest extends BaseNCodecOutputStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("array");
      byte[] byteArray0 = new byte[8];
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base64 base64_0 = new Base64(51, byteArray0, false, codecPolicy0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockFileOutputStream0, base64_0, false);
      boolean boolean0 = baseNCodecOutputStream0.isStrictDecoding();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream((OutputStream) null, (BaseNCodec) null, false);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write1(73);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      MockPrintStream mockPrintStream0 = new MockPrintStream(pipedOutputStream0);
      Base16 base16_0 = Base16.Base162();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base16_0, false);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write1(4455);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid octet in encoded value: 103
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base16 base16_0 = Base16.Base162();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base16_0, true);
      try { 
        baseNCodecOutputStream0.write1(64);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base32 base32_0 = Base32.Base320();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base32_0, false);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write0((byte[]) null, 76, 64);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // array
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base32 base32_0 = Base32.Base322(true, (byte)0);
      byte[] byteArray0 = new byte[9];
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base32_0, true);
      try { 
        baseNCodecOutputStream0.write0(byteArray0, (byte)0, (byte)9);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, (BaseNCodec) null, true);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write((-1094));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base16 base16_0 = Base16.Base162();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base16_0, false);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write(64);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid octet in encoded value: 64
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Base32 base32_0 = Base32.Base322(true, (byte)62);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream((OutputStream) null, base32_0, true);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.flush0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      OutputStream outputStream0 = OutputStream.nullOutputStream();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(outputStream0, (BaseNCodec) null, true);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.eof();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, (BaseNCodec) null, true);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.close();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("org.apache.commons.codec.DecoderException", true);
      Base16 base16_0 = Base16.Base162();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockFileOutputStream0, base16_0, false);
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write0(byteArray0, (byte)1, 1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid octet in encoded value: 0
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      MockFile mockFile0 = new MockFile("I");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
      Base32 base32_0 = Base32.Base322(true, (byte)0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base32_0, true);
      byte[] byteArray0 = new byte[5];
      baseNCodecOutputStream0.write0(byteArray0, (byte)0, 1);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      MockFile mockFile0 = new MockFile("I", "I");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
      Base32 base32_0 = Base32.Base321(true);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base32_0, false);
      baseNCodecOutputStream0.eof();
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      MockFile mockFile0 = new MockFile("I");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
      Base32 base32_0 = Base32.Base322(true, (byte)0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base32_0, true);
      baseNCodecOutputStream0.write1((byte)0);
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      MockFile mockFile0 = new MockFile("I", "I");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
      Base32 base32_0 = Base32.Base321(true);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base32_0, false);
      baseNCodecOutputStream0.flush0();
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      byte[] byteArray0 = new byte[0];
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base64 base64_0 = new Base64(76, byteArray0, false, codecPolicy0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base64_0, false);
      baseNCodecOutputStream0.write(76);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.close();
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Strict decoding: Last encoded character (before the paddings if any) is a valid base 64 alphabet but not a possible encoding. Decoding requires at least two trailing 6-bit characters to create bytes.
         //
         verifyException("org.apache.commons.codec.binary.Base64", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base32 base32_0 = Base32.Base320();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base32_0, true);
      byte[] byteArray0 = new byte[2];
      baseNCodecOutputStream0.write0(byteArray0, (byte)0, (byte)0);
      assertEquals(2, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base32 base32_0 = Base32.Base322(true, (byte)0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base32_0, true);
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write0(byteArray0, (byte)0, 64);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      MockFile mockFile0 = new MockFile("I", "I");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
      Base32 base32_0 = Base32.Base321(true);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base32_0, false);
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write0(byteArray0, 76, 866);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base32 base32_0 = Base32.Base321(true);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base32_0, true);
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write0(byteArray0, 76, (-75));
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      byte[] byteArray0 = new byte[2];
      Base64 base64_0 = Base64.Base645();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base64_0, false);
      // Undeclared exception!
      try { 
        baseNCodecOutputStream0.write0(byteArray0, (-124), 76);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.BaseNCodecOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base32 base32_0 = Base32.Base321(true);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base32_0, true);
      baseNCodecOutputStream0.write(76);
      try { 
        baseNCodecOutputStream0.close();
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      byte[] byteArray0 = new byte[0];
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base64 base64_0 = new Base64(76, byteArray0, false, codecPolicy0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base64_0, false);
      baseNCodecOutputStream0.close();
      assertTrue(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("zpB<J*VSf#j>|7");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFileOutputStream0);
      Base16 base16_0 = Base16.Base161(true);
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(mockPrintStream0, base16_0, true);
      boolean boolean0 = baseNCodecOutputStream0.isStrictDecoding();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base16 base16_0 = Base16.Base162();
      BaseNCodecOutputStream baseNCodecOutputStream0 = new BaseNCodecOutputStream(pipedOutputStream0, base16_0, true);
      try { 
        baseNCodecOutputStream0.write(76);
        fail("Expecting exception: IOException");
      
      } catch(IOException e) {
         //
         // Pipe not connected
         //
         verifyException("java.io.PipedOutputStream", e);
      }
  }
}
