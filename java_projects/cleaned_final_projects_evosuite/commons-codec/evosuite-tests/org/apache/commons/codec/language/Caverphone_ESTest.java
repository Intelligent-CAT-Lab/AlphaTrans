
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
import org.apache.commons.codec.language.Caverphone;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Caverphone_ESTest extends Caverphone_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      boolean boolean0 = caverphone0.isCaverphoneEqual("Vj*RlZ<T/x<B", "%L_1Q)/{}g{@c)`q!");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      Object object0 = caverphone0.encode((Object) "sio");
      assertEquals("SA11111111", object0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      Object object0 = new Object();
      try { 
        caverphone0.encode0(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Caverphone encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Caverphone", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      String string0 = caverphone0.caverphone("dg");
      assertEquals("K111111111", string0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      String string0 = caverphone0.encode1("S}i-#eXys3+QIkD");
      assertEquals("SKSKKT1111", string0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      Object object0 = caverphone0.encode0("S}i-#eXys3+QIkD");
      assertEquals("SKSKKT1111", object0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      boolean boolean0 = caverphone0.isCaverphoneEqual(":h~k?EwnC.", ":h~k?EwnC.");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      Object object0 = new Object();
      try { 
        caverphone0.encode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Caverphone encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.Caverphone", e);
      }
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      Caverphone caverphone0 = new Caverphone();
      String string0 = caverphone0.encode("Q");
      assertEquals("K111111111", string0);
  }
}
