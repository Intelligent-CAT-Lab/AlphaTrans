
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


package org.apache.commons.codec.language;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.codec.StringEncoder;
import org.apache.commons.codec.language.Caverphone1;
import org.apache.commons.codec.language.DoubleMetaphone;
import org.apache.commons.codec.language.Nysiis;
import org.apache.commons.codec.language.Soundex;
import org.apache.commons.codec.language.SoundexUtils;
import org.apache.commons.codec.net.QuotedPrintableCodec;
import org.apache.commons.codec.net.URLCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SoundexUtils_ESTest extends SoundexUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int int0 = SoundexUtils.differenceEncoded("+;QPb(ml$JI1G.@rw", "");
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Caverphone1 caverphone1_0 = new Caverphone1();
      int int0 = SoundexUtils.difference(caverphone1_0, "3kh3", "oFyd^R@gA\"+v");
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      String string0 = SoundexUtils.clean("^D+mkc^3m+C$Tf*w!EV");
      assertEquals("DMKCMCTFWEV", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      URLCodec uRLCodec0 = new URLCodec("$");
      try { 
        SoundexUtils.difference(uRLCodec0, "$", "$");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // $
         //
         verifyException("org.apache.commons.codec.net.URLCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        SoundexUtils.difference((StringEncoder) null, "01230120022455012623010202", "01230120022455012623010202");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.language.SoundexUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-1767));
      // Undeclared exception!
      try { 
        SoundexUtils.difference(doubleMetaphone0, "D%|5", "G'm//{nD4[7Z4zH3Z/");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1767
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      char[] charArray0 = new char[2];
      Soundex soundex0 = new Soundex(0, true, "", charArray0);
      // Undeclared exception!
      try { 
        SoundexUtils.difference(soundex0, "re>K3]qov//$BCi*N", "01230120022455012623010202");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: R (index=17)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      // Undeclared exception!
      try { 
        SoundexUtils.difference(quotedPrintableCodec0, "", "");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3 out of bounds for length 0
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int int0 = SoundexUtils.differenceEncoded("w3", "w3");
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_GENEALOGY;
      int int0 = SoundexUtils.difference(soundex0, "6B3<. lZ#Hvq2}r", (String) null);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(true);
      int int0 = SoundexUtils.difference(nysiis0, "TT", "a]]T0");
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      String string0 = SoundexUtils.clean("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      String string0 = SoundexUtils.clean((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(true);
      int int0 = SoundexUtils.difference(nysiis0, (String) null, "+43U");
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      SoundexUtils soundexUtils0 = new SoundexUtils();
  }
}
