
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


package org.apache.commons.codec.net;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.nio.charset.Charset;
import java.nio.charset.IllegalCharsetNameException;
import java.nio.charset.UnsupportedCharsetException;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.net.BCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BCodec_ESTest extends BCodec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.getEncoding();
      assertEquals("B", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      BCodec bCodec0 = new BCodec((Charset) null, codecPolicy0);
      Charset charset0 = bCodec0.getCharset();
      assertNull(charset0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.encode3("");
      assertEquals("=?UTF-8?B??=", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.encode2("_+}]N\"Bm7*-");
      assertEquals("=?UTF-8?B?Xyt9XU4iQm03Ki0=?=", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.encode1("UTF-8", "UTF-8");
      assertNotNull(string0);
      assertEquals("=?UTF-8?B?VVRGLTg=?=", string0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Charset charset0 = Charset.defaultCharset();
      String string0 = bCodec0.encode((String) null, charset0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Charset charset0 = Charset.defaultCharset();
      String string0 = bCodec0.encode("", charset0);
      assertEquals("=?UTF-8?B??=", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.encode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      byte[] byteArray0 = new byte[2];
      byte[] byteArray1 = bCodec0.doEncoding(byteArray0);
      assertNotSame(byteArray1, byteArray0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = bCodec0.doEncoding(byteArray0);
      assertArrayEquals(new byte[] {}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      BCodec bCodec0 = new BCodec(charset0, codecPolicy0);
      byte[] byteArray0 = new byte[8];
      byteArray0[1] = (byte)73;
      byteArray0[6] = (byte)118;
      byte[] byteArray1 = bCodec0.doDecoding(byteArray0);
      assertEquals(1, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      byte[] byteArray0 = new byte[5];
      byte[] byteArray1 = bCodec0.doDecoding(byteArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decode0("=?UTF-8?B?Xyt9XU4iQm03Ki0=?=");
      assertEquals("_+}]N\"Bm7*-", string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decode0("=?UTF-8?B??=");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.decode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.decode((Object) "=?UTF-8?B??=");
      assertEquals("", object0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec1((Charset) null);
      // Undeclared exception!
      try { 
        bCodec0.getDefaultCharset();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.net.BCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encode1("A", "A");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // A
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encode1("", (String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encode0("", (Charset) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec1((Charset) null);
      // Undeclared exception!
      try { 
        bCodec0.encode("");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec1((Charset) null);
      // Undeclared exception!
      try { 
        bCodec0.encode((Object) "`!9MNQn,#=");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      BCodec bCodec0 = new BCodec(charset0, codecPolicy0);
      byte[] byteArray0 = new byte[11];
      byteArray0[1] = (byte)86;
      // Undeclared exception!
      try { 
        bCodec0.doDecoding(byteArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Strict decoding: Last encoded character (before the paddings if any) is a valid base 64 alphabet but not a possible encoding. Decoding requires at least two trailing 6-bit characters to create bytes.
         //
         verifyException("org.apache.commons.codec.binary.Base64", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decode("");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: malformed encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      // Undeclared exception!
      try { 
        BCodec.BCodec2("mXPI");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // mXPI
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      // Undeclared exception!
      try { 
        BCodec.BCodec2("|8");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // |8
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      // Undeclared exception!
      try { 
        BCodec.BCodec2((String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decode1(bCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.BCodec cannot be decoded using BCodec
         //
         verifyException("org.apache.commons.codec.net.BCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec1((Charset) null);
      // Undeclared exception!
      try { 
        bCodec0.encode3("QYieMAk<yvxSkf");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = new Object();
      try { 
        bCodec0.encode3(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be encoded using BCodec
         //
         verifyException("org.apache.commons.codec.net.BCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decode0("");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: malformed encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec1((Charset) null);
      // Undeclared exception!
      try { 
        bCodec0.encode2("|/VzA^TOX{m:Fc^$h2");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Charset charset0 = Charset.defaultCharset();
      String string0 = bCodec0.encode0("", charset0);
      assertNotNull(string0);
      assertEquals("=?UTF-8?B??=", string0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      BCodec bCodec0 = BCodec.BCodec1(charset0);
      String string0 = bCodec0.decode("=?UTF-8?B?WnghWyF8aFddKD1ZRTNvSzs=?=");
      assertEquals("Zx![!|hW](=YE3oK;", string0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Charset charset0 = bCodec0.getCharset();
      assertEquals("UTF-8", charset0.toString());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.decode1("=?UTF-8?B??=");
      assertEquals("", object0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.decode1((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.encode((Object) bCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.BCodec cannot be encoded using BCodec
         //
         verifyException("org.apache.commons.codec.net.BCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.encode3((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decode0((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.encode2((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.encode1((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encode1("org.apache.commons.codecCodcPolicy", "");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // 
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Charset charset0 = Charset.defaultCharset();
      String string0 = bCodec0.encode0((String) null, charset0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      byte[] byteArray0 = bCodec0.doDecoding((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      byte[] byteArray0 = bCodec0.doEncoding((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      CodecPolicy codecPolicy0 = CodecPolicy.STRICT;
      BCodec bCodec0 = new BCodec(charset0, codecPolicy0);
      boolean boolean0 = bCodec0.isStrictDecoding();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      boolean boolean0 = bCodec0.isStrictDecoding();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decode("=?UTF-8?B??=");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encode("", (Charset) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec2("UTF-8");
      assertEquals("UTF-8", bCodec0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.encode("");
      assertEquals("=?UTF-8?B??=", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Object object0 = bCodec0.encode((Object) "");
      assertNotNull(object0);
      assertEquals("=?UTF-8?B??=", object0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.getDefaultCharset();
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decode((Object) bCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.BCodec cannot be decoded using BCodec
         //
         verifyException("org.apache.commons.codec.net.BCodec", e);
      }
  }
}
