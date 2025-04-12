
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
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base16;
import org.apache.commons.codec.binary.BaseNCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Base16_ESTest extends Base16_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(false);
      byte[] byteArray0 = new byte[7];
      byteArray0[4] = (byte) (-59);
      String string0 = base16_0.encodeAsString(byteArray0);
      assertEquals("00000000C50000", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base16 base16_0 = new Base16(false, codecPolicy0);
      byte[] byteArray0 = new byte[8];
      byteArray0[3] = (byte)96;
      byte[] byteArray1 = base16_0.encode(byteArray0);
      assertEquals(16, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      base16_0.encode2((byte[]) null, 2147483639, 9, baseNCodec_Context0);
      assertEquals(76, BaseNCodec.MIME_CHUNK_SIZE);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(false);
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      base16_0.encode2((byte[]) null, 10, 0, baseNCodec_Context0);
      assertEquals(76, BaseNCodec.MIME_CHUNK_SIZE);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[0] = (byte)71;
      Base16 base16_0 = Base16.Base161(false);
      // Undeclared exception!
      try { 
        base16_0.decode0(byteArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid octet in encoded value: 71
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[1];
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      baseNCodec_Context0.ibitWorkArea = 76;
      // Undeclared exception!
      try { 
        base16_0.decode1(byteArray0, (byte)49, (byte)49, baseNCodec_Context0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 49 out of bounds for length 1
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(false);
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      byte[] byteArray0 = new byte[3];
      // Undeclared exception!
      try { 
        base16_0.decode1(byteArray0, (-1459), 1, baseNCodec_Context0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1459 out of bounds for length 3
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(false);
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      baseNCodec_Context0.ibitWorkArea = (-2088);
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        base16_0.decode1(byteArray0, (byte)25, (byte)74, baseNCodec_Context0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 25 out of bounds for length 8
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(false);
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      baseNCodec_Context0.ibitWorkArea = (-2088);
      base16_0.decode1((byte[]) null, 380, (-3898), baseNCodec_Context0);
      assertEquals(64, BaseNCodec.PEM_CHUNK_SIZE);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)52;
      byte[] byteArray1 = base16_0.decode(byteArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[23];
      // Undeclared exception!
      try { 
        base16_0.encode2(byteArray0, (-1326), (-1326), (BaseNCodec.Context) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[0];
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      // Undeclared exception!
      try { 
        base16_0.encode2(byteArray0, 2, 2, baseNCodec_Context0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 0
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      // Undeclared exception!
      try { 
        base16_0.decode1((byte[]) null, (byte)50, (byte)50, (BaseNCodec.Context) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Base16 base16_0 = null;
      try {
        base16_0 = new Base16(false, (CodecPolicy) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // codecPolicy
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base16 base16_0 = new Base16(true, codecPolicy0);
      assertEquals(76, BaseNCodec.MIME_CHUNK_SIZE);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      Base16 base16_0 = new Base16(false, codecPolicy0);
      byte[] byteArray0 = new byte[0];
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      baseNCodec_Context0.ibitWorkArea = 64;
      // Undeclared exception!
      try { 
        base16_0.decode1(byteArray0, (-3695), (-3695), baseNCodec_Context0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Strict decoding: Last encoded character is a valid base 16 alphabetcharacter but not a possible encoding. Decoding requires at least two characters to create one byte.
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      boolean boolean0 = base16_0.isInAlphabet0((byte)65);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[1];
      boolean boolean0 = base16_0.containsAlphabetOrPad(byteArray0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      boolean boolean0 = base16_0.isInAlphabet0((byte) (-66));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[3];
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      // Undeclared exception!
      try { 
        base16_0.encode2(byteArray0, (byte)7, 2147483639, baseNCodec_Context0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Input length exceeds maximum size for encoded data: 2147483639
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[0];
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      base16_0.decode1(byteArray0, (-46), (-46), baseNCodec_Context0);
      base16_0.encode2(byteArray0, (-46), 102, baseNCodec_Context0);
      assertEquals(76, BaseNCodec.MIME_CHUNK_SIZE);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(false);
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte) (-59);
      // Undeclared exception!
      try { 
        base16_0.decode1(byteArray0, (byte)0, 7, baseNCodec_Context0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid octet in encoded value: -59
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      byte[] byteArray0 = new byte[1];
      byte[] byteArray1 = base16_0.encode(byteArray0);
      byte[] byteArray2 = base16_0.decode(byteArray1);
      assertArrayEquals(new byte[] {(byte)48, (byte)48}, byteArray1);
      assertArrayEquals(new byte[] {(byte)0}, byteArray2);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      byte[] byteArray0 = new byte[9];
      byteArray0[2] = (byte)50;
      byteArray0[3] = (byte)66;
      byteArray0[4] = (byte)50;
      base16_0.decode1(byteArray0, 3, 3, baseNCodec_Context0);
      // Undeclared exception!
      try { 
        base16_0.decode1(byteArray0, (-1), (byte)0, baseNCodec_Context0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 9
         //
         verifyException("org.apache.commons.codec.binary.Base16", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Base16 base16_0 = Base16.Base161(true);
      byte[] byteArray0 = new byte[6];
      byteArray0[1] = (byte)103;
      boolean boolean0 = base16_0.containsAlphabetOrPad(byteArray0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Base16 base16_0 = Base16.Base162();
      BaseNCodec.Context baseNCodec_Context0 = new BaseNCodec.Context();
      base16_0.encode2((byte[]) null, (-828), (-3015), baseNCodec_Context0);
      base16_0.decode1((byte[]) null, 10, 10, baseNCodec_Context0);
      assertEquals(64, BaseNCodec.PEM_CHUNK_SIZE);
  }
}
