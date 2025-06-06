
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
import java.nio.charset.Charset;
import java.nio.charset.IllegalCharsetNameException;
import java.nio.charset.UnsupportedCharsetException;
import org.apache.commons.codec.binary.Hex;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Hex_ESTest extends Hex_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Hex hex0 = new Hex(1, "[o", (Charset) null);
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        hex0.decode(byteArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Hex hex0 = new Hex(1, "", (Charset) null);
      String string0 = hex0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      char[] charArray0 = new char[0];
      Hex.encodeHex4(byteArray0, 9, (-1213), false, charArray0, (byte)52);
      assertArrayEquals(new char[] {}, charArray0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex((-5568), "%y&) p 5}yd6|p~b}r", charset0);
      try { 
        hex0.decode2(charset0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // class sun.nio.cs.UTF_8 cannot be cast to class [C (sun.nio.cs.UTF_8 and [C are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int int0 = Hex.toDigit('0', 2419);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int int0 = Hex.toDigit('a', (-1285));
      assertEquals(10, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(785);
      String string0 = Hex.encodeHexString3(byteBuffer0, true);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocateDirect(0);
      String string0 = Hex.encodeHexString3(byteBuffer0, false);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(2536);
      String string0 = Hex.encodeHexString2(byteBuffer0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(200);
      Hex.encodeHex6(byteBuffer0);
      String string0 = Hex.encodeHexString2(byteBuffer0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      String string0 = Hex.encodeHexString1(byteArray0, false);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      String string0 = Hex.encodeHexString0(byteArray0);
      assertEquals("000000", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      char[] charArray0 = new char[0];
      byte[] byteArray0 = Hex.decodeHex0(charArray0);
      String string0 = Hex.encodeHexString0(byteArray0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(65);
      char[] charArray0 = new char[1];
      char[] charArray1 = Hex.encodeHex8(byteBuffer0, charArray0);
      assertEquals(130, charArray1.length);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocateDirect(0);
      char[] charArray0 = new char[8];
      char[] charArray1 = Hex.encodeHex8(byteBuffer0, charArray0);
      assertEquals(0, charArray1.length);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      char[] charArray0 = Hex.encodeHex3(byteArray0, 1, 0, false);
      assertEquals(0, charArray0.length);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      char[] charArray0 = Hex.encodeHex0(byteArray0);
      char[] charArray1 = Hex.encodeHex2(byteArray0, charArray0);
      assertEquals(14, charArray1.length);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      char[] charArray0 = new char[0];
      byte[] byteArray0 = Hex.decodeHex0(charArray0);
      char[] charArray1 = Hex.encodeHex2(byteArray0, charArray0);
      assertNotSame(charArray1, charArray0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      char[] charArray0 = Hex.encodeHex1(byteArray0, false);
      assertEquals(0, charArray0.length);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      byte[] byteArray0 = Hex.decodeHex2("eC");
      char[] charArray0 = Hex.encodeHex0(byteArray0);
      //  // Unstable assertion: assertArrayEquals(new char[] {'0', '0'}, charArray0);
      //  // Unstable assertion: assertArrayEquals(new byte[] {(byte) (-20)}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      char[] charArray0 = Hex.encodeHex0(byteArray0);
      assertEquals(0, charArray0.length);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ByteBuffer byteBuffer0 = ByteBuffer.wrap(byteArray0);
      char[] charArray0 = Hex.encodeHex6(byteBuffer0);
      assertArrayEquals(new char[] {'0', '0', '0', '0'}, charArray0);
      
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex((byte)101, "", charset0);
      byte[] byteArray1 = hex0.encode1(byteBuffer0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      byte[] byteArray0 = new byte[2];
      Hex hex0 = new Hex(6, "(", charset0);
      byte[] byteArray1 = hex0.encode0(byteArray0);
      assertArrayEquals(new byte[] {(byte)48, (byte)48, (byte)48, (byte)48}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex((-520), "UTF-8", charset0);
      byte[] byteArray1 = hex0.encode0(byteArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex(0, "k6?1S;zkxMx``d", charset0);
      byte[] byteArray0 = new byte[5];
      byte[] byteArray1 = hex0.encode(byteArray0);
      assertArrayEquals(new byte[] {(byte)48, (byte)48, (byte)48, (byte)48, (byte)48, (byte)48, (byte)48, (byte)48, (byte)48, (byte)48}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      ByteBuffer byteBuffer0 = ByteBuffer.wrap(byteArray0);
      char[] charArray0 = Hex.encodeHex6(byteBuffer0);
      byte[] byteArray1 = new byte[2];
      int int0 = Hex.decodeHex1(charArray0, byteArray1, (-737));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocateDirect(246);
      char[] charArray0 = Hex.encodeHex7(byteBuffer0, true);
      byte[] byteArray0 = Hex.decodeHex0(charArray0);
      assertEquals(246, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      Charset charset0 = Charset.forName("UTF-8");
      Hex hex0 = new Hex(12, "UTF-8", charset0);
      byte[] byteArray1 = hex0.decode0(byteArray0);
      assertFalse(byteArray1.equals((Object)byteArray0));
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      try { 
        Hex.toDigit('$', 1061);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Illegal hexadecimal character $ at index 1061
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHexString1((byte[]) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      char[] charArray0 = new char[1];
      // Undeclared exception!
      try { 
        Hex.encodeHex8((ByteBuffer) null, charArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(91);
      char[] charArray0 = new char[0];
      // Undeclared exception!
      try { 
        Hex.encodeHex8(byteBuffer0, charArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHex7((ByteBuffer) null, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHex6((ByteBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHex3((byte[]) null, 16, 16, true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      byte[] byteArray0 = Hex.decodeHex2("");
      // Undeclared exception!
      try { 
        Hex.encodeHex3(byteArray0, (-2003), (-2003), true);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -4006
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(1262);
      char[] charArray0 = Hex.encodeHex6(byteBuffer0);
      // Undeclared exception!
      try { 
        Hex.encodeHex2((byte[]) null, charArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      char[] charArray0 = new char[0];
      // Undeclared exception!
      try { 
        Hex.encodeHex2(byteArray0, charArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex(1687, "hUP\"5}", charset0);
      try { 
        hex0.encode2(charset0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // class sun.nio.cs.UTF_8 cannot be cast to class [B (sun.nio.cs.UTF_8 and [B are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.encode1((ByteBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.encode((ByteBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.encode((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      try { 
        Hex.decodeHex2(")qv!ia");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Illegal hexadecimal character ) at index 0
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.decodeHex2((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        Hex.decodeHex1((char[]) null, byteArray0, (-1662));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      ByteBuffer byteBuffer0 = ByteBuffer.wrap(byteArray0);
      char[] charArray0 = Hex.encodeHex6(byteBuffer0);
      // Undeclared exception!
      try { 
        Hex.decodeHex1(charArray0, byteArray0, (-1728));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1728 out of bounds for length 3
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      char[] charArray0 = new char[8];
      try { 
        Hex.decodeHex0(charArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Illegal hexadecimal character \u0000 at index 0
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(53);
      try { 
        hex0.decode1(byteBuffer0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Odd number of characters.
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.decode1((ByteBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      byte[] byteArray0 = Hex.decodeHex2("eC");
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex((-696), "eC", charset0);
      try { 
        hex0.decode0(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Odd number of characters.
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.decode((ByteBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.decode((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.Hex0("org.apache.commons.codec.DecoderException");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // org.apache.commons.codec.DecoderException
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.Hex0("");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // 
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.Hex0((String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      Hex hex0 = new Hex(5, "", (Charset) null);
      // Undeclared exception!
      try { 
        hex0.encode2((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex(7, "(", charset0);
      Object object0 = hex0.encode2("(");
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      try { 
        hex0.decode2("UTF8");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Illegal hexadecimal character U at index 0
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      char[] charArray0 = new char[0];
      CharBuffer charBuffer0 = CharBuffer.wrap(charArray0);
      ByteBuffer byteBuffer0 = charset0.encode(charBuffer0);
      char[] charArray1 = Hex.encodeHex7(byteBuffer0, false);
      assertEquals(0, charArray1.length);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      char[] charArray0 = Hex.encodeHex1(byteArray0, true);
      assertArrayEquals(new char[] {'0', '0', '0', '0', '0', '0'}, charArray0);
      assertEquals(6, charArray0.length);
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHex1((byte[]) null, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      ByteBuffer byteBuffer0 = ByteBuffer.wrap(byteArray0);
      char[] charArray0 = Hex.encodeHex6(byteBuffer0);
      int int0 = Hex.decodeHex1(charArray0, byteArray0, 0);
      assertEquals(2, int0);
      assertArrayEquals(new byte[] {(byte)0, (byte)0}, byteArray0);
      assertArrayEquals(new char[] {'0', '0', '0', '0'}, charArray0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      char[] charArray0 = new char[5];
      try { 
        Hex.decodeHex1(charArray0, byteArray0, 6);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Odd number of characters.
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF-8");
      Charset charset0 = hex0.getCharset();
      assertTrue(charset0.canEncode());
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.decodeHex0((char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHexString0((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHex0((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(200);
      Hex.encodeHex6(byteBuffer0);
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex(3, (String) null, charset0);
      byte[] byteArray0 = hex0.decode(byteBuffer0);
      assertEquals(0, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHexString2((ByteBuffer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(3326);
      hex0.encode2(byteBuffer0);
      assertEquals(3326, byteBuffer0.position());
      assertEquals(0, byteBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      try { 
        hex0.decode((Object) "UTF8");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Illegal hexadecimal character U at index 0
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      char[] charArray0 = new char[0];
      // Undeclared exception!
      try { 
        Hex.encodeHex4(byteArray0, (byte) (-78), 891, true, charArray0, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      byte[] byteArray0 = Hex.decodeHex2("");
      // Undeclared exception!
      try { 
        Hex.encodeHex3(byteArray0, 1000, 1000, false);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      char[] charArray0 = new char[0];
      byte[] byteArray0 = new byte[0];
      try { 
        Hex.decodeHex1(charArray0, byteArray0, 1298);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Output array is not large enough to accommodate decoded data.
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      // Undeclared exception!
      try { 
        hex0.encode((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      Object object0 = hex0.encode((Object) "UTF8");
      try { 
        hex0.encode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // class [C cannot be cast to class [B ([C and [B are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      // Undeclared exception!
      try { 
        Hex.encodeHexString3((ByteBuffer) null, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test77()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      String string0 = Hex.encodeHexString1(byteArray0, false);
      assertEquals("00000000000000", string0);
  }

  @Test(timeout = 4000)
  public void test78()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex(61, "Output array is not large enough to accommodate decoded data.", charset0);
      // Undeclared exception!
      try { 
        hex0.encode0((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test79()  throws Throwable  {
      byte[] byteArray0 = Hex.decodeHex2("eC");
      Charset charset0 = Charset.defaultCharset();
      Hex hex0 = new Hex(710, "eC", charset0);
      try { 
        hex0.decode(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Odd number of characters.
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }

  @Test(timeout = 4000)
  public void test80()  throws Throwable  {
      Hex hex0 = Hex.Hex0("UTF8");
      ByteBuffer byteBuffer0 = ByteBuffer.allocate(740);
      try { 
        hex0.decode(byteBuffer0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Illegal hexadecimal character \u0000 at index 0
         //
         verifyException("org.apache.commons.codec.binary.Hex", e);
      }
  }
}
