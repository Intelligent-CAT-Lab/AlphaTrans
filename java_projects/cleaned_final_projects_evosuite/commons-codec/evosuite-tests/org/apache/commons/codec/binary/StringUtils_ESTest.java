
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
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import org.apache.commons.codec.binary.StringUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class StringUtils_ESTest extends StringUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "");
      boolean boolean0 = StringUtils.equals((CharSequence) charBuffer0, (CharSequence) "\u00FD\u00FF");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      String string0 = StringUtils.newStringUtf8(byteArray0);
      assertEquals("\u0000\u0000\u0000\u0000\u0000\u0000", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringUtils.newStringUtf8(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      String string0 = StringUtils.newStringUtf16Le(byteArray0);
      assertEquals("\u0000\u0000\u0000\uFFFD", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf8("");
      String string0 = StringUtils.newStringUtf16Le(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      String string0 = StringUtils.newStringUtf16Be((byte[]) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = StringUtils.newStringUtf16Be(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      String string0 = StringUtils.newStringUtf16((byte[]) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf8("");
      String string0 = StringUtils.newStringUtf16(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String string0 = StringUtils.newStringUsAscii((byte[]) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      String string0 = StringUtils.newStringIso8859_1((byte[]) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf8((String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf8("");
      String string0 = StringUtils.newStringUsAscii(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Le((String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Le("");
      assertArrayEquals(new byte[] {}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Be((String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Be("");
      assertEquals(0, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16((String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16("");
      assertArrayEquals(new byte[] {}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUsAscii("org.apache.commons.codec.binary.StringUtils");
      assertEquals(43, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUsAscii("");
      String string0 = StringUtils.newStringIso8859_1(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesIso8859_1((String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesIso8859_1("");
      assertEquals(0, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        StringUtils.newString1(byteArray0, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.getBytesUnchecked(")6-mfS/n", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      String string0 = StringUtils.newString1((byte[]) null, "");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        StringUtils.newString1(byteArray0, " U?Cxe`>r");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         //  U?Cxe`>r: java.io.UnsupportedEncodingException:  U?Cxe`>r
         //
         verifyException("org.apache.commons.codec.binary.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUnchecked((String) null, (String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      ByteBuffer byteBuffer0 = StringUtils.getByteBufferUtf8((String) null);
      assertNull(byteBuffer0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "p1!:{z*U2sc");
      boolean boolean0 = StringUtils.equals((CharSequence) "p1!:{z*U2sc", (CharSequence) charBuffer0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      boolean boolean0 = StringUtils.equals((CharSequence) "gVVVAmed#(?:g6$k>%", (CharSequence) "L/RhaZ5");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      char[] charArray0 = new char[4];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      boolean boolean0 = StringUtils.equals((CharSequence) "\u0000\u0000\u0000\u0000\u0000\uFFFD", (CharSequence) charBuffer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      boolean boolean0 = StringUtils.equals((CharSequence) "t", (CharSequence) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "p1!:{z*U2sc");
      boolean boolean0 = StringUtils.equals((CharSequence) null, (CharSequence) charBuffer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      boolean boolean0 = StringUtils.equals((CharSequence) "\uFFFD", (CharSequence) "\uFFFD");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "n8");
      boolean boolean0 = StringUtils.equals((CharSequence) charBuffer0, (CharSequence) "\u6E00\u3800");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      String string0 = StringUtils.newStringUtf8((byte[]) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16("org.apache.commons.codec.binary.CharSequenceUtils");
      assertEquals(100, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      ByteBuffer byteBuffer0 = StringUtils.getByteBufferUtf8("lHYy }zC?J#&[EU#4");
      assertEquals(0, byteBuffer0.position());
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf8("\uFFFD");
      assertArrayEquals(new byte[] {(byte) (-17), (byte) (-65), (byte) (-67)}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesIso8859_1("scS");
      assertArrayEquals(new byte[] {(byte)115, (byte)99, (byte)83}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      StringUtils stringUtils0 = new StringUtils();
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      byte[] byteArray0 = new byte[11];
      String string0 = StringUtils.newStringUtf16(byteArray0);
      assertEquals("\u0000\u0000\u0000\u0000\u0000\uFFFD", string0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Le("n8");
      String string0 = StringUtils.newStringUtf16Be(byteArray0);
      assertEquals("\u6E00\u3800", string0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      String string0 = StringUtils.newStringUtf16Le((byte[]) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUsAscii((String) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Le("n8");
      String string0 = StringUtils.newStringIso8859_1(byteArray0);
      assertEquals("n\u00008\u0000", string0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Le("n8");
      String string0 = StringUtils.newStringUsAscii(byteArray0);
      assertEquals("n\u00008\u0000", string0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.getBytesUnchecked("", "o\u0000r\u0000g\u0000.\u0000a\u0000p\u0000a\u0000c\u0000h\u0000e\u0000.\u0000c\u0000o\u0000m\u0000m\u0000o\u0000n\u0000s\u0000.\u0000c\u0000o\u0000d\u0000e\u0000c\u0000.\u0000b\u0000i\u0000n\u0000a\u0000r\u0000y\u0000.\u0000S\u0000t\u0000r\u0000i\u0000n\u0000g\u0000U\u0000t\u0000i\u0000l\u0000s\u0000");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // o\u0000r\u0000g\u0000.\u0000a\u0000p\u0000a\u0000c\u0000h\u0000e\u0000.\u0000c\u0000o\u0000m\u0000m\u0000o\u0000n\u0000s\u0000.\u0000c\u0000o\u0000d\u0000e\u0000c\u0000.\u0000b\u0000i\u0000n\u0000a\u0000r\u0000y\u0000.\u0000S\u0000t\u0000r\u0000i\u0000n\u0000g\u0000U\u0000t\u0000i\u0000l\u0000s\u0000: java.io.UnsupportedEncodingException: o\u0000r\u0000g\u0000.\u0000a\u0000p\u0000a\u0000c\u0000h\u0000e\u0000.\u0000c\u0000o\u0000m\u0000m\u0000o\u0000n\u0000s\u0000.\u0000c\u0000o\u0000d\u0000e\u0000c\u0000.\u0000b\u0000i\u0000n\u0000a\u0000r\u0000y\u0000.\u0000S\u0000t\u0000r\u0000i\u0000n\u0000g\u0000U\u0000t\u0000i\u0000l\u0000s\u0000
         //
         verifyException("org.apache.commons.codec.binary.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      byte[] byteArray0 = StringUtils.getBytesUtf16Be("org.apache.commons.codec.binary.CharSequenceUtils");
      assertEquals(98, byteArray0.length);
  }
}
