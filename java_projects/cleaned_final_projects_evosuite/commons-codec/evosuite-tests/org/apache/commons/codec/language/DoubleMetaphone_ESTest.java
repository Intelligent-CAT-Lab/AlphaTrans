
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
import org.apache.commons.codec.language.DoubleMetaphone;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DoubleMetaphone_ESTest extends DoubleMetaphone_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(0);
      doubleMetaphone_DoubleMetaphoneResult0.appendPrimary0('&');
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary());
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      char char0 = doubleMetaphone0.charAt("+~5PB", 1538);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals('\u0000', char0);
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("ALL", false);
      assertEquals("AL", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      boolean boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0("_Zb^s46tSWs-", "WRWZZ7F");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      boolean boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0("Z|z", "c*MU`#R%u Y_gI");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("'7 [zRSl7#-c#W|");
      assertEquals("SRSL", string0);
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("Yj*4u%=");
      assertEquals("AJ", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("WRIGHNIX%*(#");
      assertEquals("RNKS", string0);
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("4IGhnX%*(");
      assertEquals("NKS", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("GH7t4e");
      assertEquals("KT", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      
      doubleMetaphone0.setMaxCodeLen(0);
      int int0 = doubleMetaphone0.getMaxCodeLen();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-1501));
      int int0 = doubleMetaphone0.getMaxCodeLen();
      assertEquals((-1501), int0);
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("4");
      assertNotNull(string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      Object object0 = doubleMetaphone0.encode0("");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.encode((String) null);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("W");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      Object object0 = doubleMetaphone0.encode((Object) "");
      assertNull(object0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.doubleMetaphone0((String) null);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("/");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      String[] stringArray0 = new String[3];
      stringArray0[0] = "";
      boolean boolean0 = DoubleMetaphone.contains("", 0, 0, stringArray0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      String[] stringArray0 = new String[0];
      boolean boolean0 = DoubleMetaphone.contains("9o +gSm>o/(vTN[$c@", (-1), (-1), stringArray0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      char char0 = doubleMetaphone0.charAt("]gC;9Vy8h", 4);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals('9', char0);
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      char char0 = doubleMetaphone0.charAt("8&Rhj1s},ogZD]1~", 4);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals('j', char0);
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-1742));
      // Undeclared exception!
      try { 
        doubleMetaphone0.isDoubleMetaphoneEqual1("2'G?gT \"", ": ", false);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1742
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-53786696));
      // Undeclared exception!
      try { 
        doubleMetaphone0.isDoubleMetaphoneEqual0("KNJT8=]%J]@NZWHWTQCI", "KNJT8=]%J]@NZWHWTQCI");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -53786696
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-1));
      // Undeclared exception!
      try { 
        doubleMetaphone0.encode1("w ~mpSH");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-3036));
      // Undeclared exception!
      try { 
        doubleMetaphone0.encode0("org.apache.commons.codec.binary.StringUtils");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -3036
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-1490));
      // Undeclared exception!
      try { 
        doubleMetaphone0.encode("ALLE");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1490
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      try { 
        doubleMetaphone0.encode((Object) doubleMetaphone0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // DoubleMetaphone encode parameter is not of type String
         //
         verifyException("org.apache.commons.codec.language.DoubleMetaphone", e);
      }
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-4008));
      // Undeclared exception!
      try { 
        doubleMetaphone0.encode((Object) "HOLM");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -4008
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-545));
      // Undeclared exception!
      try { 
        doubleMetaphone0.doubleMetaphone1("M`U", false);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -545
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen((-153869933));
      // Undeclared exception!
      try { 
        doubleMetaphone0.doubleMetaphone0("Hens(DH.P:!(dW1<");
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -153869933
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      String[] stringArray0 = new String[0];
      // Undeclared exception!
      try { 
        DoubleMetaphone.contains("{,M", 2, (-3127), stringArray0);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      // Undeclared exception!
      try { 
        DoubleMetaphone.contains((String) null, 3001, (-1), (String[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      // Undeclared exception!
      try { 
        doubleMetaphone0.charAt((String) null, 86);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult((-4040));
      boolean boolean0 = doubleMetaphone_DoubleMetaphoneResult0.isComplete();
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(4);
      boolean boolean0 = doubleMetaphone_DoubleMetaphoneResult0.isComplete();
      assertFalse(boolean0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(1904);
      doubleMetaphone_DoubleMetaphoneResult0.appendAlternate1("");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(1);
      doubleMetaphone_DoubleMetaphoneResult0.appendAlternate1("i~49,5M\">bBIj`6{C$R");
      assertEquals("i", doubleMetaphone_DoubleMetaphoneResult0.getAlternate());
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(0);
      doubleMetaphone_DoubleMetaphoneResult0.appendPrimary1("y'%5A6i");
      assertEquals("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary());
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(83);
      doubleMetaphone_DoubleMetaphoneResult0.appendPrimary1("");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(83);
      doubleMetaphone_DoubleMetaphoneResult0.appendAlternate0('A');
      assertEquals("A", doubleMetaphone_DoubleMetaphoneResult0.getAlternate());
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(5);
      doubleMetaphone_DoubleMetaphoneResult0.append3("2^hR}&vk%=i", "OPp\"cBJ3Yl00uC%D");
      doubleMetaphone_DoubleMetaphoneResult0.appendAlternate0('1');
      assertEquals("2^hR}", doubleMetaphone_DoubleMetaphoneResult0.getPrimary());
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(5);
      doubleMetaphone_DoubleMetaphoneResult0.appendPrimary0('1');
      assertEquals("1", doubleMetaphone_DoubleMetaphoneResult0.getPrimary());
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("(4'He)4FAf7VvcC~", true);
      assertEquals("FFFK", string0);
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("AKKS", false);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("AKS", string0);
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("d'ffr?%du)\"", true);
      assertEquals("TFRT", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("sEGbbG4+$,z o", false);
      assertEquals("SKPK", string0);
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("`?,I'Kh*CRChT^o!q", false);
      assertEquals("KKRK", string0);
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.doubleMetaphone1((String) null, false);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult((-450));
      doubleMetaphone_DoubleMetaphoneResult0.append1('J', '$');
      assertEquals("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary());
      assertEquals("", doubleMetaphone_DoubleMetaphoneResult0.getAlternate());
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult((-450));
      doubleMetaphone_DoubleMetaphoneResult0.append0('P');
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("", doubleMetaphone_DoubleMetaphoneResult0.getAlternate());
      assertEquals("", doubleMetaphone_DoubleMetaphoneResult0.getPrimary());
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      int int0 = doubleMetaphone0.getMaxCodeLen();
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(1);
      doubleMetaphone_DoubleMetaphoneResult0.getPrimary();
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(1);
      doubleMetaphone_DoubleMetaphoneResult0.append2("WZ7f");
      assertEquals("W", doubleMetaphone_DoubleMetaphoneResult0.getAlternate());
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(1);
      doubleMetaphone_DoubleMetaphoneResult0.getAlternate();
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      DoubleMetaphone.DoubleMetaphoneResult doubleMetaphone_DoubleMetaphoneResult0 = doubleMetaphone0.new DoubleMetaphoneResult(4);
      doubleMetaphone_DoubleMetaphoneResult0.append3("GQXQp}+}2_X#", "K");
      boolean boolean0 = doubleMetaphone_DoubleMetaphoneResult0.isComplete();
      assertEquals("K", doubleMetaphone_DoubleMetaphoneResult0.getAlternate());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("W", false);
      assertEquals("", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1(">>UMB3]RX1tm~0&\"");
      assertEquals("MPRK", string0);
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("UMB", true);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("AM", string0);
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("A~mLLE");
      assertEquals("AML", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("ACH");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("AK", string0);
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("ORCHES");
      assertEquals("ARKS", string0);
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("BACHER");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("PKR", string0);
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.isDoubleMetaphoneEqual1("KNACH", "", false);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("I0zzyi");
      assertEquals("AS", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("aA$Zh&LxS1wZp1}s2aJ");
      assertEquals("AJLK", string0);
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("o6zppx");
      assertEquals("ASPK", string0);
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("X");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
      assertEquals("S", string0);
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("WRWITZ");
      assertEquals("RTS", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      boolean boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual1("!`t^+vtmI", "OWSKI", false);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode(">*4GneK'U[W");
      assertEquals("KNK", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.isDoubleMetaphoneEqual0("t->mow ", "t->mow ");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("WH");
      assertNotNull(string0);
      assertEquals("A", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("cT'I\"tT7P$4.++.y");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("KTTP", string0);
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("TTH");
      assertEquals("0", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("Cs,thnic%IJ}");
      assertEquals("KS0N", string0);
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("TCH");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("X", string0);
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("SCy");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
      assertEquals("S", string0);
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("SCH");
      assertEquals("X", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("SC$H");
      assertEquals("SK", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.isDoubleMetaphoneEqual0("PSCH", "PSCH");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("SN");
      assertEquals("SN", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("SIA");
      assertEquals("S", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("KNSIO");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("NS", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("s;zM]sH)b|4");
      assertEquals("SSMX", string0);
  }

  @Test(timeout = 4000)
  public void test086()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("SUGAR");
      assertNotNull(string0);
      assertEquals("XKR", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("YSL");
      assertEquals("AL", string0);
      assertNotNull(string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("*B#ewR{O>J'rr4aDL");
      assertEquals("PRJR", string0);
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("IER");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("A", string0);
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      boolean boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0("WR", "KNPP");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("?FgphvCi");
      assertEquals("FKFF", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("ALLwE");
      assertNotNull(string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("AL", string0);
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("WRILLA", true);
      assertEquals("R", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("Z@,WOlJHhS");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("SLS", string0);
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen(2556);
      doubleMetaphone0.doubleMetaphone1(" a *r,bvP]3g#2coJj<", false);
      assertEquals(2556, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("'BdAujA");
      assertEquals("PTJ", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("iB}>I&f:}YJ@mB^3-6!W");
      assertEquals("APFJ", string0);
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("PSAJOSs");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
      assertEquals("SJS", string0);
  }

  @Test(timeout = 4000)
  public void test099()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("PSJOSE");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("SJS", string0);
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("JOSE");
      assertEquals("HS", string0);
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("WIhLTZ");
      assertNotNull(string0);
      assertEquals("ALTS", string0);
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      boolean boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual0((String) null, "HO J~&G*:u,>.NW0A#");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("IGhniX%*(#");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("ANKS", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("<GhY$C");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("KK", string0);
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("GHjt4");
      assertEquals("KT", string0);
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("OGGI");
      assertEquals("AJ", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("KN?GY");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("NK", string0);
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("OGY", true);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("AK", string0);
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("MANGER");
      assertEquals("MNJR", string0);
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("GeBkap]=pBcMW'd");
      assertEquals("KPKP", string0);
  }

  @Test(timeout = 4000)
  public void test111()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      boolean boolean0 = doubleMetaphone0.isDoubleMetaphoneEqual1("8gnQDJ\u0002", "8gnQDJ\u0002", false);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("oGN:");
      assertEquals("AKN", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("$DD5*dUAY;");
      assertEquals("TT", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("KNDGY");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("NJ", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("DG");
      assertEquals("TK", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("MCHR");
      assertEquals("MKR", string0);
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("CHORE");
      assertEquals("XR", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("CHOR");
      assertEquals("KR", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      Object object0 = doubleMetaphone0.encode0("CCE");
      assertEquals("X", object0);
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("WRUCCES");
      assertEquals("RKSS", string0);
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("CIE");
      assertEquals("S", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("Y4P1CI}YkHun9r%:|h");
      assertEquals("APSK", string0);
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("wb,M5CkfYOfe7Z5/Sf/");
      assertEquals("PMKF", string0);
  }

  @Test(timeout = 4000)
  public void test124()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("UCCES");
      assertEquals("AKSS", string0);
  }

  @Test(timeout = 4000)
  public void test125()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("ni8&a=%/Cz4Z");
      assertEquals("NSS", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test126()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("CAESAR");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("SSR", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test127()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone0("CHIA");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertNotNull(string0);
      assertEquals("K", string0);
  }

  @Test(timeout = 4000)
  public void test128()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      try { 
        doubleMetaphone0.encode0(doubleMetaphone0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // DoubleMetaphone encode parameter is not of type String
         //
         verifyException("org.apache.commons.codec.language.DoubleMetaphone", e);
      }
  }

  @Test(timeout = 4000)
  public void test129()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("~_w)WYAvH!EQQ#5p6", false);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("FKP", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test130()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("KNNLNP", true);
      assertNotNull(string0);
      assertEquals("NLNP", string0);
  }

  @Test(timeout = 4000)
  public void test131()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("gv%FFsz\"0cgmXN|ADT");
      assertEquals("KFFS", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test132()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode1("Joq@4Bb{.+;|");
      assertEquals("JKP", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test133()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1(")y{!T,!", false);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("T", string0);
  }

  @Test(timeout = 4000)
  public void test134()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("}vJ\"8auQ`ZY<djr|", false);
      assertNotNull(string0);
      assertEquals("FJKS", string0);
  }

  @Test(timeout = 4000)
  public void test135()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("R#(l{=(s~:5HGg2<[e");
      assertEquals("RLSK", string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test136()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("ChNbhPGqKdLAet");
      assertEquals("KNPP", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test137()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.encode1((String) null);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test138()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      Object object0 = doubleMetaphone0.encode((Object) "RX92");
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
      assertEquals("RKS", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test139()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.encode("mvWogHXG");
      assertEquals("MFKK", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test140()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("WICZ", true);
      assertEquals("FKTS", string0);
      assertNotNull(string0);
      assertEquals(4, doubleMetaphone0.getMaxCodeLen());
  }

  @Test(timeout = 4000)
  public void test141()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      doubleMetaphone0.setMaxCodeLen(489);
      assertEquals(489, doubleMetaphone0.getMaxCodeLen());
      
      String string0 = doubleMetaphone0.doubleMetaphone1("org.apache.commons.codec.EncoderException", false);
      assertEquals("ARKPXKMNSKTKNKTRKSPXN", string0);
  }

  @Test(timeout = 4000)
  public void test142()  throws Throwable  {
      DoubleMetaphone doubleMetaphone0 = new DoubleMetaphone();
      String string0 = doubleMetaphone0.doubleMetaphone1("KNMVWOGHXG", true);
      assertEquals("NMFK", string0);
  }
}
