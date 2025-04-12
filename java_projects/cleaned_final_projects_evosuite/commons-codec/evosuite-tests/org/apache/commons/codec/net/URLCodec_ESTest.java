
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
import java.io.UnsupportedEncodingException;
import java.util.BitSet;
import org.apache.commons.codec.net.URLCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class URLCodec_ESTest extends URLCodec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode("2e78\\*%8E!tY");
      assertNotNull(string0);
      assertEquals("2e78\\*\uFFFD!tY", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      String string0 = uRLCodec0.getEncoding();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("");
      String string0 = uRLCodec0.getEncoding();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      String string0 = uRLCodec0.getDefaultCharset();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("");
      String string0 = uRLCodec0.getDefaultCharset();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode2("UTF-8");
      assertNotNull(string0);
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode2("");
      assertNotNull(string0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("UTF-8");
      String string0 = uRLCodec0.encode1("?_w7cN!&1n6~", "UTF-8");
      assertEquals("%3F_w7cN%21%261n6%7E", string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode1("", "UTF-8");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = uRLCodec0.encode0((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = uRLCodec0.encode0(byteArray0);
      assertFalse(byteArray1.equals((Object)byteArray0));
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = uRLCodec0.encode(byteArray0);
      assertArrayEquals(new byte[] {}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("UTF-8");
      String string0 = uRLCodec0.encode("", "UTF-8");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode("");
      assertEquals("", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      Object object0 = uRLCodec0.encode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = URLCodec.decodeUrl(byteArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      Object object0 = uRLCodec0.decode3("");
      assertNotNull(object0);
      assertEquals("", object0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode2(" cannot be URL encoded");
      assertEquals(" cannot be URL encoded", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode2("");
      assertNotNull(string0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode1("UTF-8", "UTF-8");
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("");
      String string0 = uRLCodec0.decode1("", "UTF-8");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = uRLCodec0.decode0((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = uRLCodec0.decode0(byteArray0);
      assertFalse(byteArray1.equals((Object)byteArray0));
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("");
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = uRLCodec0.decode(byteArray0);
      assertNotSame(byteArray0, byteArray1);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode("UTF-8", "UTF-8");
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode("");
      assertEquals("", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      // Undeclared exception!
      try { 
        uRLCodec0.encode3("t-|W");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      // Undeclared exception!
      try { 
        uRLCodec0.encode2("hzlHZ");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      // Undeclared exception!
      try { 
        uRLCodec0.encode1("", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      // Undeclared exception!
      try { 
        uRLCodec0.encode("Jfcw2_]6_up!M", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.encode("n$QREO", "n$QREO");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("org.apache.commons.codec.EncoderException");
      try { 
        uRLCodec0.encode("org.apache.commons.codec.EncoderException");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // org.apache.commons.codec.EncoderException
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.encode((Object) uRLCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.URLCodec cannot be URL encoded
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      // Undeclared exception!
      try { 
        uRLCodec0.encode((Object) "");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)37;
      try { 
        URLCodec.decodeUrl(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: 
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      // Undeclared exception!
      try { 
        uRLCodec0.decode2("v/bxk7u;csysg#G");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.decode1("eGy%4Mx'v]B=>>", "eGy%4Mx'v]B=>>");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 77
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      // Undeclared exception!
      try { 
        uRLCodec0.decode1("", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[5];
      byteArray0[4] = (byte)37;
      try { 
        uRLCodec0.decode0(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: 
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[7];
      byteArray0[2] = (byte)37;
      try { 
        uRLCodec0.decode(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 0
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.decode("D'v%fT+BHb R3hi", "D'v%fT+BHb R3hi");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 84
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      // Undeclared exception!
      try { 
        uRLCodec0.decode("", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.decode("(<Y!83%eLd@?!!'");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 76
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      uRLCodec0.charset = null;
      // Undeclared exception!
      try { 
        uRLCodec0.decode("2~");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      // Undeclared exception!
      try { 
        uRLCodec0.decode((Object) "S19DVVOo.EMKWtsI");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      // Undeclared exception!
      try { 
        uRLCodec0.decode3("7}23EFK6iGGK! ");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      Object object0 = uRLCodec0.decode3((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.decode3(uRLCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.URLCodec cannot be URL decoded
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.encode3(uRLCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.URLCodec cannot be URL encoded
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      Object object0 = uRLCodec0.encode3("org.apache.commons.codec.EncoderException");
      assertEquals("org.apache.commons.codec.EncoderException", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode2((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("");
      try { 
        uRLCodec0.decode2("");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // 
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode1((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec(";u ");
      try { 
        uRLCodec0.encode2("T7<V;1");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // ;u 
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.encode1("", "");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
      }
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[1] = (byte)43;
      byte[] byteArray1 = URLCodec.decodeUrl(byteArray0);
      assertArrayEquals(new byte[] {(byte)0, (byte)32, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      byte[] byteArray0 = URLCodec.decodeUrl((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      byteArray0[0] = (byte)1;
      BitSet bitSet0 = BitSet.valueOf(byteArray0);
      byte[] byteArray1 = URLCodec.encodeUrl(bitSet0, byteArray0);
      assertArrayEquals(new byte[] {(byte)37, (byte)48, (byte)49, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
      assertEquals(7, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[3] = (byte)32;
      byte[] byteArray1 = URLCodec.encodeUrl((BitSet) null, byteArray0);
      assertEquals(19, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      byte[] byteArray0 = URLCodec.encodeUrl((BitSet) null, (byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[6];
      byte[] byteArray1 = uRLCodec0.decode0(byteArray0);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.getDefaultCharset();
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("UTF-8");
      byte[] byteArray0 = new byte[1];
      byte[] byteArray1 = uRLCodec0.encode0(byteArray0);
      assertArrayEquals(new byte[] {(byte)37, (byte)48, (byte)48}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.decode((Object) uRLCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.URLCodec cannot be URL decoded
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      Object object0 = uRLCodec0.decode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      Object object0 = uRLCodec0.encode3((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.decode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec((String) null);
      String string0 = uRLCodec0.decode((String) null, "_(?q5&LC;Ur*r");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode2((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode1((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      try { 
        uRLCodec0.decode1("f'f&Pxk/l+UpuzNX73", "f'f&Pxk/l+UpuzNX73");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
      }
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = uRLCodec0.decode((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[3] = (byte) (-38);
      BitSet bitSet0 = new BitSet();
      byte[] byteArray1 = URLCodec.encodeUrl(bitSet0, byteArray0);
      assertEquals(18, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = URLCodec.encodeUrl((BitSet) null, byteArray0);
      assertFalse(byteArray1.equals((Object)byteArray0));
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = uRLCodec0.encode((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test77()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[1];
      byte[] byteArray1 = uRLCodec0.encode(byteArray0);
      byte[] byteArray2 = URLCodec.decodeUrl(byteArray1);
      assertArrayEquals(new byte[] {(byte)0}, byteArray2);
      assertArrayEquals(new byte[] {(byte)37, (byte)48, (byte)48}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test78()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("org.apache.commons.codec.binary.StringUtils");
      String string0 = uRLCodec0.encode("U6LBB~lW6", "UTF-8");
      assertEquals("U6LBB%7ElW6", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test79()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      byte[] byteArray0 = new byte[7];
      byte[] byteArray1 = uRLCodec0.decode(byteArray0);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test80()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      Object object0 = uRLCodec0.encode((Object) "org.apache.commons.codec.binary.StringUtils");
      assertEquals("org.apache.commons.codec.binary.StringUtils", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test81()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("UTF-8");
      try { 
        uRLCodec0.decode("UTF-8", "D0uaKD;");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
      }
  }

  @Test(timeout = 4000)
  public void test82()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.getEncoding();
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test83()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      String string0 = uRLCodec0.encode(" cannot be URL encoded");
      assertNotNull(string0);
      assertEquals("+cannot+be+URL+encoded", string0);
  }

  @Test(timeout = 4000)
  public void test84()  throws Throwable  {
      URLCodec uRLCodec0 = URLCodec.URLCodec1();
      assertEquals("UTF-8", uRLCodec0.getDefaultCharset());
      
      Object object0 = uRLCodec0.decode((Object) "org.apache.commons.codec.binary.StringUtils");
      assertEquals("org.apache.commons.codec.binary.StringUtils", object0);
      assertNotNull(object0);
  }
}
