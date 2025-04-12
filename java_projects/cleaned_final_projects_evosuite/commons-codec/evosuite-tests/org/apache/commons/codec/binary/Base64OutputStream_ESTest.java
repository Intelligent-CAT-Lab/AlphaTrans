
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
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base64OutputStream;
import org.apache.commons.codec.binary.BaseNCodecOutputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Base64OutputStream_ESTest extends Base64OutputStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)116;
      // Undeclared exception!
      try { 
        Base64OutputStream.Base64OutputStream2(byteArrayOutputStream0, false, 0, byteArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineSeparator must not contain base64 characters: [t]
         //
         verifyException("org.apache.commons.codec.binary.Base64", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("Parameter supplied to Base-N decode is not a byte[] or a String");
      BaseNCodecOutputStream baseNCodecOutputStream0 = Base64OutputStream.Base64OutputStream1(mockFileOutputStream0, false);
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      BaseNCodecOutputStream baseNCodecOutputStream0 = Base64OutputStream.Base64OutputStream0((OutputStream) null);
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)66;
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base64OutputStream base64OutputStream0 = null;
      try {
        base64OutputStream0 = new Base64OutputStream(baseNCodecOutputStream0, true, 1074, byteArray0, codecPolicy0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineSeparator must not contain base64 characters: [B]
         //
         verifyException("org.apache.commons.codec.binary.Base64", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      BaseNCodecOutputStream baseNCodecOutputStream0 = Base64OutputStream.Base64OutputStream2((OutputStream) null, true, (-907), (byte[]) null);
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base64OutputStream base64OutputStream0 = new Base64OutputStream((OutputStream) null, false, 0, byteArray0, codecPolicy0);
      assertFalse(base64OutputStream0.isStrictDecoding());
  }
}
