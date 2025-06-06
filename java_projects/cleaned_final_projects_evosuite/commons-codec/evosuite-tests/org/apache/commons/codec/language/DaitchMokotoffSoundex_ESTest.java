
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
import org.apache.commons.codec.language.DaitchMokotoffSoundex;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DaitchMokotoffSoundex_ESTest extends DaitchMokotoffSoundex_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = new DaitchMokotoffSoundex(true);
      Object object0 = daitchMokotoffSoundex0.encode((Object) "org.apache.commons.codec.EncoderException");
      assertEquals("095744", object0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = new DaitchMokotoffSoundex(false);
      String string0 = daitchMokotoffSoundex0.encode1((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = new DaitchMokotoffSoundex(false);
      try { 
        daitchMokotoffSoundex0.encode0((Object) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to DaitchMokotoffSoundex encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.DaitchMokotoffSoundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      String string0 = daitchMokotoffSoundex0.soundex0("=A8S(N$6mMVaL'?");
      assertEquals("046678", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      // Undeclared exception!
      try { 
        daitchMokotoffSoundex0.soundex0((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.language.DaitchMokotoffSoundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      String string0 = daitchMokotoffSoundex0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      Object object0 = daitchMokotoffSoundex0.encode0("/*\u00EE=i");
      assertEquals("000000", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = new DaitchMokotoffSoundex(false);
      String string0 = daitchMokotoffSoundex0.encode1("`%");
      assertEquals("000000", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      String string0 = daitchMokotoffSoundex0.encode("Malformed folding statement - patterns are not single characters: ");
      assertEquals("687963", string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      String string0 = daitchMokotoffSoundex0.soundex0("org.apache.comm4ns.codec.language.DaitchMokotoffSoundex");
      assertEquals("095744|095745|095754|095755", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      try { 
        daitchMokotoffSoundex0.encode((Object) daitchMokotoffSoundex0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to DaitchMokotoffSoundex encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.DaitchMokotoffSoundex", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DaitchMokotoffSoundex daitchMokotoffSoundex0 = DaitchMokotoffSoundex.DaitchMokotoffSoundex1();
      String string0 = daitchMokotoffSoundex0.encode("-9`W-?Z8IdNqxm;==");
      assertEquals("743655", string0);
  }
}
