
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
import java.io.OutputStream;
import java.io.PipedOutputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base32OutputStream;
import org.apache.commons.codec.binary.BaseNCodecOutputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Base32OutputStream_ESTest extends Base32OutputStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      // Undeclared exception!
      try { 
        Base32OutputStream.Base32OutputStream2((OutputStream) null, true, 4, (byte[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineLength 4 > 0, but lineSeparator is null
         //
         verifyException("org.apache.commons.codec.binary.Base32", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      MockPrintStream mockPrintStream0 = new MockPrintStream("RZ15");
      BaseNCodecOutputStream baseNCodecOutputStream0 = Base32OutputStream.Base32OutputStream1(mockPrintStream0, false);
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      MockPrintStream mockPrintStream0 = new MockPrintStream("RZ15");
      byte[] byteArray0 = new byte[1];
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base32OutputStream base32OutputStream0 = new Base32OutputStream(mockPrintStream0, false, 0, byteArray0, codecPolicy0);
      BaseNCodecOutputStream baseNCodecOutputStream0 = Base32OutputStream.Base32OutputStream2(base32OutputStream0, false, (-4040), byteArray0);
      assertFalse(baseNCodecOutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      BaseNCodecOutputStream baseNCodecOutputStream0 = Base32OutputStream.Base32OutputStream0(pipedOutputStream0);
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base32OutputStream base32OutputStream0 = null;
      try {
        base32OutputStream0 = new Base32OutputStream(baseNCodecOutputStream0, true, 5618, (byte[]) null, codecPolicy0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // lineLength 5618 > 0, but lineSeparator is null
         //
         verifyException("org.apache.commons.codec.binary.Base32", e);
      }
  }
}
