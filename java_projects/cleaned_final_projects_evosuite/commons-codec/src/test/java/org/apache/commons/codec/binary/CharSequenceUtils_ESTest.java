
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
import java.nio.CharBuffer;
import org.apache.commons.codec.binary.CharSequenceUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CharSequenceUtils_ESTest extends CharSequenceUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(3941);
      CharBuffer charBuffer1 = charBuffer0.put((int) '-', '-');
      charBuffer0.get();
      boolean boolean0 = CharSequenceUtils.regionMatches(charBuffer0, true, '-', charBuffer1, 28, 3941);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(30);
      char[] charArray0 = new char[7];
      CharBuffer charBuffer1 = CharBuffer.wrap(charArray0);
      // Undeclared exception!
      try { 
        CharSequenceUtils.regionMatches(charBuffer1, false, 4, charBuffer0, 4, 30);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(3951);
      boolean boolean0 = CharSequenceUtils.regionMatches(charBuffer0, true, 0, charBuffer0, 1186, 95);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      boolean boolean0 = CharSequenceUtils.regionMatches("Mc`h*+", true, 101, "", 3880, 1100);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.wrap((CharSequence) "&");
      // Undeclared exception!
      try { 
        CharSequenceUtils.regionMatches("&", true, 45, charBuffer0, 27, 27);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      // Undeclared exception!
      try { 
        CharSequenceUtils.regionMatches((CharSequence) null, false, 43, (CharSequence) null, 43, 43);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.binary.CharSequenceUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(3946);
      CharBuffer charBuffer1 = charBuffer0.put((int) '-', '-');
      boolean boolean0 = CharSequenceUtils.regionMatches(charBuffer0, false, '-', charBuffer1, 37, 3946);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(3978);
      CharBuffer charBuffer1 = charBuffer0.put((int) '2', '2');
      boolean boolean0 = CharSequenceUtils.regionMatches(charBuffer0, true, '2', charBuffer1, 33, 3978);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      CharBuffer charBuffer0 = CharBuffer.allocate(3941);
      boolean boolean0 = CharSequenceUtils.regionMatches("", true, 3941, charBuffer0, 3941, (-9));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      CharSequenceUtils charSequenceUtils0 = new CharSequenceUtils();
  }
}
