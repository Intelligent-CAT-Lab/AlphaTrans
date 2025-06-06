
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
import org.apache.commons.codec.language.Soundex;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Soundex_ESTest extends Soundex_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      char[] charArray0 = new char[1];
      Soundex soundex0 = new Soundex(1, false, "Parameter supplied to Soundex encode is not of type java.lang.String", charArray0);
      String string0 = soundex0.soundex("Uv|Ukt\"Yq!_wY,O(");
      assertEquals("U os", string0);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      char[] charArray0 = new char[6];
      Soundex soundex0 = new Soundex(1, true, "tMZ~y", charArray0);
      // Undeclared exception!
      try { 
        soundex0.difference("8F=We8&{CTF0]dYY-mz", " K=");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: F (index=5)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Soundex soundex0 = new Soundex('-', false, "01230120022455012623010202", (char[]) null);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_SIMPLIFIED;
      soundex0.setMaxLength(0);
      int int0 = soundex0.getMaxLength();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      soundex0.setMaxLength((-1299));
      int int0 = soundex0.getMaxLength();
      assertEquals((-1299), int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_GENEALOGY;
      String string0 = soundex0.US_ENGLISH.encode1((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.US_ENGLISH.encode1("?Pw7GN2$jH_}}AWKO");
      assertEquals("P252", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.encode1("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.US_ENGLISH_GENEALOGY.encode("01230120022455012623010202");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_SIMPLIFIED;
      Object object0 = soundex0.encode((Object) "01230120022455012623010202");
      assertEquals("", object0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      char[] charArray0 = new char[6];
      Soundex soundex0 = new Soundex(1, true, "SG}9^jv)Z*t]", charArray0);
      // Undeclared exception!
      try { 
        soundex0.soundex("SG}9^jv)Z*t]");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: S (index=18)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      char[] charArray0 = new char[17];
      Soundex soundex0 = new Soundex(1, false, "l&nU<S=b[mc O/|", charArray0);
      // Undeclared exception!
      try { 
        soundex0.encode0("l&nU<S=b[mc O/|");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: U (index=20)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Soundex soundex0 = new Soundex(1, false, "Rvd]jKog8&kE#Bw!oI", (char[]) null);
      // Undeclared exception!
      try { 
        soundex0.encode("Rvd]jKog8&kE#Bw!oI");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: V (index=21)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Soundex soundex0 = null;
      try {
        soundex0 = new Soundex(2, false, "01230120022455012623010202", (char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_GENEALOGY;
      String string0 = soundex0.soundex(" (index=");
      assertEquals("I532", string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.soundex("?Pw7GN2$jH_}}AWKO");
      assertEquals("P252", string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.US_ENGLISH_SIMPLIFIED.soundex("&R]`C$ZjTTG/mkXWX&1");
      assertEquals("R232", string0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      String string0 = soundex0.soundex((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_GENEALOGY;
      try { 
        soundex0.encode0(soundex0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Soundex encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      Object object0 = soundex0.US_ENGLISH_SIMPLIFIED.encode0("GEx%a(J=Kn");
      assertEquals("G225", object0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_SIMPLIFIED;
      String string0 = soundex0.encode("&R]`C$ZjTTG/mkXWX&1");
      assertEquals("R232", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      int int0 = soundex0.difference(",&hw.", ",&hw.");
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      char[] charArray0 = new char[6];
      Soundex soundex0 = new Soundex(1, true, "tMZ~y", charArray0);
      int int0 = soundex0.US_ENGLISH.difference("tMZ~y", "ls}L,=e5s");
      assertEquals(0, int0);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH_GENEALOGY;
      String string0 = soundex0.soundex("");
      assertNotNull(string0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      Object object0 = new Object();
      try { 
        soundex0.US_ENGLISH_GENEALOGY.encode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Soundex encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      char[] charArray0 = new char[5];
      charArray0[0] = '-';
      Soundex soundex0 = new Soundex(2, false, "01230120022455012623010202", charArray0);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      char[] charArray0 = new char[5];
      Soundex soundex0 = new Soundex((-3189), false, "#wn`ah#", charArray0);
      String string0 = soundex0.soundex("#wn`ah#");
      assertEquals("W500", string0);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Soundex soundex0 = new Soundex(1, true, "[ESVm-:1-J%d xs", (char[]) null);
      // Undeclared exception!
      try { 
        soundex0.encode1("[ESVm-:1-J%d xs");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: S (index=18)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      char[] charArray0 = new char[1];
      Soundex soundex0 = new Soundex(2, false, "R232", charArray0);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Soundex soundex0 = new Soundex(0, true, "01230120022455012623010202", (char[]) null);
      assertEquals(4, soundex0.getMaxLength());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      char[] charArray0 = new char[1];
      Soundex soundex0 = new Soundex(1, false, "SG}9^jv)ZK*t]", charArray0);
      // Undeclared exception!
      try { 
        soundex0.encode((Object) "SG}9^jv)ZK*t]");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // The character is not mapped: S (index=18)
         //
         verifyException("org.apache.commons.codec.language.Soundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Soundex soundex0 = Soundex.US_ENGLISH;
      int int0 = soundex0.getMaxLength();
      assertEquals(4, int0);
  }
}
