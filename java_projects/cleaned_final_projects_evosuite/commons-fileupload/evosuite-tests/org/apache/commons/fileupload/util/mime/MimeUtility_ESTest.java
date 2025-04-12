

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



package org.apache.commons.fileupload.util.mime;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.UnsupportedEncodingException;
import org.apache.commons.fileupload.util.mime.MimeUtility;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MimeUtility_ESTest extends MimeUtility_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      // Undeclared exception!
      try { 
        MimeUtility.decodeText((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.util.mime.MimeUtility", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      try { 
        MimeUtility.decodeText("=?=?=?=?=?");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
         //
         // Invalid RFC 2047 encoding
         //
         verifyException("org.apache.commons.fileupload.util.mime.MimeUtility", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      try { 
        MimeUtility.decodeText("=?=?Q?6?=?=?=_?=?_=?");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
         //
         // Invalid RFC 2047 encoding
         //
         verifyException("org.apache.commons.fileupload.util.mime.MimeUtility", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      String string0 = MimeUtility.decodeText("=?=?");
      assertEquals("=?=?", string0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      String string0 = MimeUtility.decodeText(" =?");
      assertEquals(" =?", string0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      String string0 = MimeUtility.decodeText("=?=?=??=?==");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      String string0 = MimeUtility.decodeText("f=?=?j?.?=?=?");
      assertEquals("f=?=?j?.?=?=?", string0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      String string0 = MimeUtility.decodeText(" =??=??=?");
      assertEquals(" ", string0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      String string0 = MimeUtility.decodeText("G~Kx\"K-1)dL");
      assertEquals("G~Kx\"K-1)dL", string0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      String string0 = MimeUtility.decodeText("=?=?=?'? ");
      assertEquals("=?=?=?'?", string0);
  }
}
