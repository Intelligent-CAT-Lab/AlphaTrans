
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
import org.apache.commons.codec.language.Nysiis;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Nysiis_ESTest extends Nysiis_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(true);
      String string0 = nysiis0.encode1("HSCACT");
      assertTrue(nysiis0.isStrict());
      assertEquals("HSCACT", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.nysiis("RClpkggkVkz`Mr?-hN");
      assertEquals("RCLPCG", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.encode("m7l@s?b4kic>saDWeH");
      assertEquals("MLSBCA", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(false);
      boolean boolean0 = nysiis0.isStrict();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(true);
      nysiis0.encode1((String) null);
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(false);
      nysiis0.encode((String) null);
      assertFalse(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      nysiis0.encode("");
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(false);
      String string0 = nysiis0.nysiis(">X3+b]+v");
      assertEquals("XBV", string0);
      assertFalse(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.nysiis("(EE|IE)$");
      assertEquals("EY", string0);
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.nysiis(":4d2],8DdU<]");
      assertTrue(nysiis0.isStrict());
      assertEquals("D", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.nysiis("T2ay`f=A)4z+>/-");
      assertEquals("TAYF", string0);
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      nysiis0.nysiis("N");
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(false);
      nysiis0.nysiis("");
      assertFalse(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      try { 
        nysiis0.encode0(nysiis0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Nysiis encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Nysiis", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      boolean boolean0 = nysiis0.isStrict();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(false);
      Object object0 = nysiis0.encode0("org.apache.commons.codec.EncoderException");
      assertEquals("ORGAPACACANANSCADACANCADARAXCAPTAN", object0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      nysiis0.encode((Object) "D");
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      nysiis0.encode1("");
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Nysiis nysiis0 = new Nysiis(false);
      nysiis0.nysiis((String) null);
      assertFalse(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      try { 
        nysiis0.encode((Object) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Nysiis encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Nysiis", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.encode1("8caW");
      assertTrue(nysiis0.isStrict());
      assertEquals("C", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.nysiis(")-ZF*!\u0002'6Jjp}kNy");
      assertEquals("ZFJPNY", string0);
      assertTrue(nysiis0.isStrict());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      Object object0 = nysiis0.encode0("Ybqp-Hd(");
      assertTrue(nysiis0.isStrict());
      assertEquals("YBGFD", object0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.encode1("By@EbheBevSR p2+n");
      assertEquals("BYABAB", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      Object object0 = nysiis0.encode0("c}=[ljGyI?xU<h4{Ui");
      assertEquals("CLJGYA", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      String string0 = nysiis0.nysiis("org.apache.commons.codec.EncoderException");
      assertEquals("ORGAPA", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Nysiis nysiis0 = Nysiis.Nysiis1();
      Object object0 = nysiis0.encode((Object) "s nIO/DScH");
      assertEquals("SNAD", object0);
      assertTrue(nysiis0.isStrict());
  }
}
