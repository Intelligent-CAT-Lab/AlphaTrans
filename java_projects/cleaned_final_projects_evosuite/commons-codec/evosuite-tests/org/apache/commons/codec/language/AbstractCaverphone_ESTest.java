
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
import org.apache.commons.codec.language.Caverphone1;
import org.apache.commons.codec.language.Caverphone2;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class AbstractCaverphone_ESTest extends AbstractCaverphone_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Caverphone2 caverphone2_0 = new Caverphone2();
      boolean boolean0 = caverphone2_0.isEncodeEqual("fH=wJ~F5?s/PRO=", "`+%='kr*{rr.a]b");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Caverphone2 caverphone2_0 = new Caverphone2();
      try { 
        caverphone2_0.encode((Object) caverphone2_0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Parameter supplied to Caverphone encode is not of type java.lang.String
         //
         verifyException("org.apache.commons.codec.language.AbstractCaverphone", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Caverphone2 caverphone2_0 = new Caverphone2();
      Object object0 = caverphone2_0.encode((Object) "");
      assertEquals("1111111111", object0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Caverphone1 caverphone1_0 = new Caverphone1();
      boolean boolean0 = caverphone1_0.isEncodeEqual("#k3$Fm", "#k3$Fm");
      assertTrue(boolean0);
  }
}
