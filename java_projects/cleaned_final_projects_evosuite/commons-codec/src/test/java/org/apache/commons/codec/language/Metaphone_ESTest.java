
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
import org.apache.commons.codec.language.Metaphone;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Metaphone_ESTest extends Metaphone_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      boolean boolean0 = metaphone0.isMetaphoneEqual("#jg_hah[Ya|GvHx&gd", "[i$d&Egr.(HJuNUgQ2");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      metaphone0.isMetaphoneEqual("/p", "/p");
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      assertEquals(4, metaphone0.getMaxCodeLen());
      
      metaphone0.setMaxCodeLen(0);
      int int0 = metaphone0.getMaxCodeLen();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      metaphone0.setMaxCodeLen((-2135));
      int int0 = metaphone0.getMaxCodeLen();
      assertEquals((-2135), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      metaphone0.encode("");
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      Object object0 = metaphone0.encode((Object) "R");
      assertEquals("R", object0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      try { 
        metaphone0.encode0(metaphone0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Metaphone encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Metaphone", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("EIY");
      assertEquals("E", string0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("/LcTwO}XcqbhQI>XCyB");
      //  // Unstable assertion: assertEquals("LKWK", string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("RTLK");
      //  // Unstable assertion: assertEquals("RXLK", string0);
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      metaphone0.setMaxCodeLen(83);
      metaphone0.metaphone("org.apache.commons.codec.language.Metaphone");
      assertEquals(83, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("hqp");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("KP", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("TG");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("TK", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("GE");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("J", string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("e;{0=K~GhIZqp\"%u ");
      assertEquals("EKKS", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("vS-#Dghx(jKP}3U");
      //  // Unstable assertion: assertEquals("FXTK", string0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("wDGy?ZTA");
      //  // Unstable assertion: assertEquals("JS0", string0);
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("u6bTADI");
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
      //  // Unstable assertion: assertEquals("UB0T", string0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("fC!4No[C");
      //  // Unstable assertion: assertEquals("FXNK", string0);
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("EtmB9EE O");
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
      //  // Unstable assertion: assertEquals("EXMB", string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("CYD+Oj");
      assertEquals("STJ", string0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("A{VN+x4");
      assertEquals("AFNK", string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("GN");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("N", string0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("X^ x,$Su5M)?");
      //  // Unstable assertion: assertEquals("XKSX", string0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("GH");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("PLPX");
      assertEquals("PLPK", string0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("KB");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("KB", string0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("^");
      assertEquals("^", string0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      metaphone0.metaphone("");
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      int int0 = metaphone0.getMaxCodeLen();
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.encode1("TPyIA");
      //  // Unstable assertion: assertEquals("XPY", string0);
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.encode("~6PhH");
      assertEquals("F", string0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("_4OxWCKa`Y!");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("KSK", string0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("2Wbi4GjH*VHiBK0");
      //  // Unstable assertion: assertEquals("BJFH", string0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.encode1("GH");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      Object object0 = metaphone0.encode0("vS-#Dghx(jKP}3U");
      //  // Unstable assertion: assertEquals("FXTK", object0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("CHE");
      assertEquals("K", string0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("CH");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("X", string0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("CHgE");
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
      //  // Unstable assertion: assertEquals("X", string0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("TsCH");
      //  // Unstable assertion: assertEquals("XSK", string0);
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.encode1("y_*C'EscEHJp'vLx,");
      //  // Unstable assertion: assertEquals("KXJP", string0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("SC");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("SK", string0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("Wse[)mb");
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
      //  // Unstable assertion: assertEquals("XM", string0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("wR");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("R", string0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("AEIOU");
      assertEquals(4, metaphone0.getMaxCodeLen());
      assertEquals("E", string0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.metaphone("WhkT<");
      //  // Unstable assertion: assertEquals("K0", string0);
      //  // Unstable assertion: assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.encode1("Ku4>w:+UX3~Qbv9e 9s");
      assertEquals("KKSK", string0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      String string0 = metaphone0.encode1("A!(,BJU");
      assertEquals("ABJ", string0);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      metaphone0.metaphone((String) null);
      assertEquals(4, metaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Metaphone metaphone0 = new Metaphone();
      Object object0 = new Object();
      try { 
        metaphone0.encode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Metaphone encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Metaphone", e);
      }
  }
}
