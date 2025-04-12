
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
import org.apache.commons.codec.language.ColognePhonetic;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ColognePhonetic_ESTest extends ColognePhonetic_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      boolean boolean0 = colognePhonetic0.isEncodeEqual("c[b,g9\"b}U1", "c[b,g9\"b}U1");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.encode1("A@xLt=oZG0D`m:'");
      assertEquals("048528426", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.encode1("+3,");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.encode("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      Object object0 = colognePhonetic0.encode((Object) "EYW");
      assertEquals("03", object0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("03");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      // Undeclared exception!
      try { 
        colognePhonetic0.isEncodeEqual((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      Object object0 = new Object();
      try { 
        colognePhonetic0.encode0(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // This method's parameter was expected to be of the type java.lang.String. But actually it was of the type java.lang.Object.
         //
         verifyException("org.apache.commons.codec.language.ColognePhonetic", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      // Undeclared exception!
      try { 
        colognePhonetic0.encode((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.language.ColognePhonetic", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      // Undeclared exception!
      try { 
        colognePhonetic0.encode0((Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.language.ColognePhonetic", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("c[b,g9\"b}U1");
      assertEquals("8141", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("org.apache.commons.codec.EncoderException");
      assertEquals("07414466828642748126", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("?%DZ ");
      assertEquals("8", string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("iJm_!R$9qcx");
      assertEquals("06748", string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      Object object0 = colognePhonetic0.encode0("<EWVtcAaI$g.J[$IC");
      assertEquals("038448", object0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("org.apache.commons.codec.language.ColognePhonetic$CologneOutputBuffer");
      assertEquals("074144668285644454636284546212137", string0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.encode1((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      try { 
        colognePhonetic0.encode((Object) colognePhonetic0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // This method's parameter was expected to be of the type java.lang.String. But actually it was of the type org.apache.commons.codec.language.ColognePhonetic.
         //
         verifyException("org.apache.commons.codec.language.ColognePhonetic", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.encode("org.apache.Eomm4ns.odec.EncoderExcep&ion");
      assertNotNull(string0);
      assertEquals("07414682864274816", string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      boolean boolean0 = colognePhonetic0.isEncodeEqual("[xL]-Kivs$O^bBhz", "c[b,g9\"b}U1");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      ColognePhonetic colognePhonetic0 = new ColognePhonetic();
      String string0 = colognePhonetic0.colognePhonetic("Cr}zYk/R{;i0az<Z?o");
      assertEquals("478478", string0);
  }
}
