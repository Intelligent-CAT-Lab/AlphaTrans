
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
import org.apache.commons.codec.language.RefinedSoundex;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class RefinedSoundex_ESTest extends RefinedSoundex_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      char char0 = refinedSoundex0.getMappingCode('K');
      assertEquals('3', char0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      String string0 = refinedSoundex0.encode1((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      char[] charArray0 = new char[0];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(2, "org.apache.commons.codec.EncoderException", charArray0);
      Object object0 = refinedSoundex0.encode0("org.apache.commons.codec.EncoderException");
      assertEquals("O094010303080830603083060905301608", object0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      char[] charArray0 = new char[4];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(2111, "9P\"jxFI\"0", charArray0);
      String string0 = refinedSoundex0.encode("9P\"jxFI\"0");
      assertEquals("P14520", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      String string0 = refinedSoundex0.encode("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      Object object0 = refinedSoundex0.encode((Object) "S_A{VA;rY7a9R[Y_T");
      assertEquals("S302090906", object0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      int int0 = refinedSoundex0.US_ENGLISH.difference("01360240043788015936020505", "");
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      int int0 = refinedSoundex0.difference("jxcuW`>v8iX\"L{MS+(", "S_A{VA;rY7a9R[Y_T");
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "h", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.getMappingCode('x');
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(0, "h", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.encode1("h");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      char[] charArray0 = new char[7];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "h", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.encode("h");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      char[] charArray0 = new char[6];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "h", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.encode((Object) "h");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = null;
      try {
        refinedSoundex0 = new RefinedSoundex(1, "q", (char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.language.RefinedSoundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "org.apache.commons.codec.language.RefinedSoundex", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.soundex("org.apache.commons.codec.language.RefinedSoundex");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      String string0 = refinedSoundex0.US_ENGLISH.soundex("S_A{VA;rY7a9R[Y_T");
      assertEquals("S302090906", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      String string0 = refinedSoundex0.soundex((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      String string0 = refinedSoundex0.soundex("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      try { 
        refinedSoundex0.encode0((Object) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to RefinedSoundex encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.RefinedSoundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      char[] charArray0 = new char[17];
      charArray0[4] = '.';
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "em2_", charArray0);
      String string0 = refinedSoundex0.encode1("em2_");
      assertEquals("E.", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "em2_", charArray0);
      String string0 = refinedSoundex0.encode1("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      String string0 = refinedSoundex0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "em2_", charArray0);
      char char0 = refinedSoundex0.getMappingCode('3');
      assertEquals('\u0000', char0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "PB[)'zS]s*a2JIM_", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.encode0("PB[)'zS]s*a2JIM_");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = new RefinedSoundex((-1), "", (char[]) null);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      char[] charArray0 = new char[9];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(0, "org.apache.commons.codec.EncoderException", charArray0);
      char char0 = refinedSoundex0.getMappingCode('U');
      assertEquals('o', char0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      char[] charArray0 = new char[17];
      RefinedSoundex refinedSoundex0 = new RefinedSoundex(1, "B7#wj/6Yh/", charArray0);
      // Undeclared exception!
      try { 
        refinedSoundex0.difference("B7#wj/6Yh/", "B7#wj/6Yh/");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      RefinedSoundex refinedSoundex0 = RefinedSoundex.US_ENGLISH;
      Object object0 = new Object();
      try { 
        refinedSoundex0.US_ENGLISH.encode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to RefinedSoundex encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.RefinedSoundex", e);
      }
  }
}
