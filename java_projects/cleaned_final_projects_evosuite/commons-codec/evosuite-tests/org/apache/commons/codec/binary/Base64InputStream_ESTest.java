
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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.DataInputStream;
import java.io.InputStream;
import java.io.PipedInputStream;
import java.io.SequenceInputStream;
import java.util.Enumeration;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base64InputStream;
import org.apache.commons.codec.binary.BaseNCodecInputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Base64InputStream_ESTest extends Base64InputStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      byteArray0[0] = (byte)65;
      // Undeclared exception!
      try { 
        Base64InputStream.Base64InputStream2((InputStream) null, true, 0, byteArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineSeparator must not contain base64 characters: [A\u0000]
         //
         verifyException("org.apache.commons.codec.binary.Base64", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)56;
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base64InputStream base64InputStream0 = null;
      try {
        base64InputStream0 = new Base64InputStream((InputStream) null, true, 0, byteArray0, codecPolicy0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineSeparator must not contain base64 characters: [8]
         //
         verifyException("org.apache.commons.codec.binary.Base64", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      byte[] byteArray0 = new byte[4];
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base64InputStream base64InputStream0 = new Base64InputStream(pipedInputStream0, false, 0, byteArray0, codecPolicy0);
      DataInputStream dataInputStream0 = new DataInputStream(base64InputStream0);
      BaseNCodecInputStream baseNCodecInputStream0 = Base64InputStream.Base64InputStream1(dataInputStream0, false);
      assertEquals(1, baseNCodecInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Enumeration<SequenceInputStream> enumeration0 = (Enumeration<SequenceInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      byte[] byteArray0 = new byte[5];
      BaseNCodecInputStream baseNCodecInputStream0 = Base64InputStream.Base64InputStream2(sequenceInputStream0, true, 752, byteArray0);
      assertFalse(baseNCodecInputStream0.markSupported());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      BaseNCodecInputStream baseNCodecInputStream0 = Base64InputStream.Base64InputStream0((InputStream) null);
      assertEquals(1, baseNCodecInputStream0.available());
  }
}
