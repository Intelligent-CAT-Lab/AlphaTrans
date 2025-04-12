
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
import org.apache.commons.codec.net.QCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class QCodec_ESTest extends QCodec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      byte[] byteArray0 = new byte[6];
      byteArray0[0] = (byte)120;
      byteArray0[1] = (byte)95;
      byte[] byteArray1 = qCodec0.doDecoding(byteArray0);
      assertFalse(qCodec0.isEncodeBlanks());
      assertArrayEquals(new byte[] {(byte)120, (byte)32, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      assertFalse(qCodec0.isEncodeBlanks());
      
      qCodec0.setEncodeBlanks(true);
      boolean boolean0 = qCodec0.isEncodeBlanks();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.getEncoding();
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      QCodec qCodec0 = new QCodec(256, "K^G'n\"74t", (Charset) null);
      qCodec0.getCharset();
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      byte[] byteArray0 = new byte[4];
      byte[] byteArray1 = qCodec0.doEncoding(byteArray0);
      assertNotNull(byteArray1);
      assertEquals(12, byteArray1.length);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = qCodec0.doEncoding(byteArray0);
      assertNotSame(byteArray1, byteArray0);
      assertNotNull(byteArray1);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      byte[] byteArray0 = new byte[0];
      qCodec0.doDecoding(byteArray0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.decode0("=?UTF-8?Q??=");
      assertFalse(qCodec0.isEncodeBlanks());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.decode((String) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.decode("=?UTF-8?Q?l=5FTU?=");
      assertNotNull(string0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Object object0 = qCodec0.decode((Object) "=?UTF-8?Q? cannot be encoded using Q codec?=");
      assertNotNull(object0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      QCodec qCodec0 = new QCodec(23, "3O%", (Charset) null);
      // Undeclared exception!
      try { 
        qCodec0.getDefaultCharset();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.net.QCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      QCodec qCodec0 = new QCodec((-224), ")?R<cq2o", (Charset) null);
      // Undeclared exception!
      try { 
        qCodec0.encode3("v");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      // Undeclared exception!
      try { 
        qCodec0.encode1("4djD", "4djD");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // 4djD
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      // Undeclared exception!
      try { 
        qCodec0.encode1("Objects of type ", "Objects of type ");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // Objects of type 
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      // Undeclared exception!
      try { 
        qCodec0.encode1("4djD", (String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      // Undeclared exception!
      try { 
        qCodec0.encode0("pJE)/|2", (Charset) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      QCodec qCodec0 = new QCodec(33, "+%6|UeAMo64v*", (Charset) null);
      // Undeclared exception!
      try { 
        qCodec0.encode("+%6|UeAMo64v*");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      QCodec qCodec0 = new QCodec((-820), "", (Charset) null);
      // Undeclared exception!
      try { 
        qCodec0.encode((Object) "");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)61;
      try { 
        qCodec0.doDecoding(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid quoted-printable encoding
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      try { 
        qCodec0.decode0("wMj");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: malformed encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      try { 
        qCodec0.decode("This codec cannot decode ");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: malformed encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Object object0 = new Object();
      try { 
        qCodec0.decode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be decoded using Q codec
         //
         verifyException("org.apache.commons.codec.net.QCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      // Undeclared exception!
      try { 
        QCodec.QCodec0("org.apache.commons.codec.EncoderException");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // org.apache.commons.codec.EncoderException
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      // Undeclared exception!
      try { 
        QCodec.QCodec0("");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // 
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        QCodec.QCodec0((String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.decode1((Object) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Object object0 = new Object();
      try { 
        qCodec0.encode3(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be encoded using Q codec
         //
         verifyException("org.apache.commons.codec.net.QCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.encode3((Object) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Object object0 = qCodec0.encode3("");
      assertEquals("=?UTF-8?Q??=", object0);
      assertNotNull(object0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec((-476), (String) null, charset0);
      qCodec0.encode2((String) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      QCodec qCodec0 = new QCodec(60, "org.apache.commons.codec.net.QuotedPrintableCodec", (Charset) null);
      // Undeclared exception!
      try { 
        qCodec0.encode2("org.apache.commons.codec.net.Utils");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec(1288, "s%Xm_*i,urfC9'<4iP'", charset0);
      String string0 = qCodec0.encode0("", charset0);
      assertFalse(qCodec0.isEncodeBlanks());
      assertEquals("=?UTF-8?Q??=", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec(1, "", charset0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec((byte)41, (String) null, charset0);
      qCodec0.getCharset();
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      try { 
        qCodec0.decode1(qCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.QCodec cannot be decoded using Q codec
         //
         verifyException("org.apache.commons.codec.net.QCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Object object0 = qCodec0.decode1("=?UTF-8?Q??=");
      assertNotNull(object0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      try { 
        qCodec0.encode((Object) qCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.QCodec cannot be encoded using Q codec
         //
         verifyException("org.apache.commons.codec.net.QCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.encode((Object) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.decode0((String) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.encode((String) null);
      assertFalse(qCodec0.isEncodeBlanks());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.encode1((String) null, "");
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.encode1("UTF-8", "UTF-8");
      assertEquals("=?UTF-8?Q?UTF-8?=", string0);
      assertNotNull(string0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec(1288, "s%Xm_*i,urfC9'<4iP'", charset0);
      qCodec0.encode0((String) null, charset0);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.decode0("=?UTF-8?Q?org.apache.commons.codec.net.QCodec?=");
      assertFalse(qCodec0.isEncodeBlanks());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.doDecoding((byte[]) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.doEncoding((byte[]) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec((-586), " cannot be quoted-printable encoded", charset0);
      String string0 = qCodec0.encode2(" cannot be quoted-printable encoded");
      assertEquals("=?UTF-8?Q? cannot be quoted-printable encoded?=", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Object object0 = qCodec0.encode((Object) "");
      assertFalse(qCodec0.isEncodeBlanks());
      assertEquals("=?UTF-8?Q??=", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      assertFalse(qCodec0.isEncodeBlanks());
      
      qCodec0.setEncodeBlanks(true);
      qCodec0.encode(" cannGt be encoded using Q c]dec");
      assertTrue(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec0("UTF-8");
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      boolean boolean0 = qCodec0.isEncodeBlanks();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.getDefaultCharset();
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      qCodec0.decode((Object) null);
      assertFalse(qCodec0.isEncodeBlanks());
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.decode("=?UTF-8?Q??=");
      assertNotNull(string0);
      assertFalse(qCodec0.isEncodeBlanks());
  }
}
