
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
import java.io.FileDescriptor;
import java.io.InputStream;
import java.io.PipedInputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base32InputStream;
import org.apache.commons.codec.binary.BaseNCodecInputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFileInputStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Base32InputStream_ESTest extends Base32InputStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      InputStream inputStream0 = InputStream.nullInputStream();
      byte[] byteArray0 = new byte[0];
      BaseNCodecInputStream baseNCodecInputStream0 = Base32InputStream.Base32InputStream2(inputStream0, true, 1327, byteArray0);
      assertFalse(baseNCodecInputStream0.markSupported());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      FileDescriptor fileDescriptor0 = new FileDescriptor();
      MockFileInputStream mockFileInputStream0 = new MockFileInputStream(fileDescriptor0);
      BaseNCodecInputStream baseNCodecInputStream0 = Base32InputStream.Base32InputStream1(mockFileInputStream0, true);
      assertFalse(baseNCodecInputStream0.markSupported());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      byte[] byteArray0 = new byte[0];
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base32InputStream base32InputStream0 = new Base32InputStream(pipedInputStream0, true, 2781, byteArray0, codecPolicy0);
      assertEquals(1, base32InputStream0.available());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base32InputStream base32InputStream0 = null;
      try {
        base32InputStream0 = new Base32InputStream(pipedInputStream0, true, 1703, (byte[]) null, codecPolicy0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineLength 1703 > 0, but lineSeparator is null
         //
         verifyException("org.apache.commons.codec.binary.Base32", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      BaseNCodecInputStream baseNCodecInputStream0 = Base32InputStream.Base32InputStream0(pipedInputStream0);
      // Undeclared exception!
      try { 
        Base32InputStream.Base32InputStream2(baseNCodecInputStream0, false, 23, (byte[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineLength 23 > 0, but lineSeparator is null
         //
         verifyException("org.apache.commons.codec.binary.Base32", e);
      }
  }
}
