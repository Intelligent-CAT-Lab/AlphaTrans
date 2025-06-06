
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
import org.apache.commons.codec.net.QCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class RFC1522Codec_ESTest extends RFC1522Codec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      Charset charset0 = Charset.defaultCharset();
      String string0 = qCodec0.encodeText0("nN-", charset0);
      assertEquals("=?UTF-8?Q?nN-?=", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decodeText("=?UTF-8?B?PT9VVEYtOD9RPz0zRD0zRlVURi04PTNGUT0zRm4tPTNGPTNEPz0=?=?=?=?=");
      assertEquals("=?UTF-8?Q?=3D=3FUTF-8=3FQ=3Fn-=3F=3D?=", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decodeText("=?UTF-8?B??=");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encodeText1("k", "k");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // k
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encodeText1("=>[ySVTkOjI*,Q5<", "=>[ySVTkOjI*,Q5<");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // =>[ySVTkOjI*,Q5<
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.encodeText1("/Pd>}/R", (String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      // Undeclared exception!
      try { 
        qCodec0.encodeText0("", (Charset) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      // Undeclared exception!
      try { 
        bCodec0.decodeText("=?=");
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      BCodec bCodec0 = new BCodec(charset0, codecPolicy0);
      try { 
        bCodec0.decode1("=?UTF-8?Q?nN-?=");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // This codec cannot decode Q encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decodeText("=?fB?=?=");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: encoding token not found
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decodeText("=??=?=");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: charset not specified
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decodeText("=?fB?=");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: charset token not found
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      try { 
        bCodec0.decodeText("=?");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: malformed encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec((-189081844), " cannot be quoted-printable encoded", charset0);
      try { 
        qCodec0.decode0("?=");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // RFC 1522 violation: malformed encoded content
         //
         verifyException("org.apache.commons.codec.net.RFC1522Codec", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      String string0 = bCodec0.decodeText((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      QCodec qCodec0 = QCodec.QCodec2();
      String string0 = qCodec0.encodeText1((String) null, "~");
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QCodec qCodec0 = new QCodec((-189081844), " cannot be quoted-printable encoded", charset0);
      String string0 = qCodec0.encodeText1(" cannot be quoted-printable encoded", "UTF-8");
      assertNotNull(string0);
      assertEquals("=?UTF-8?Q? cannot be quoted-printable encoded?=", string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      BCodec bCodec0 = BCodec.BCodec0();
      Charset charset0 = Charset.defaultCharset();
      String string0 = bCodec0.encodeText0((String) null, charset0);
      assertNull(string0);
  }
}
