

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



package org.apache.commons.validator.util;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.validator.util.Flags;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Flags_ESTest extends Flags_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Flags flags0 = new Flags(1575, 1575);
      flags0.turnOn(1575);
      Flags flags1 = new Flags(1575, 4099L);
      boolean boolean0 = flags0.equals(flags1);
      assertEquals(0L, flags1.getFlags());
      assertEquals(1575L, flags0.getFlags());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Flags flags0 = new Flags(0, 0L);
      assertEquals(0L, flags0.getFlags());
      
      flags0.turnOnAll();
      flags0.turnOn((-1943L));
      assertEquals((-1L), flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Flags flags0 = new Flags(2211, 2211);
      assertEquals(0L, flags0.getFlags());
      
      flags0.turnOn(2211);
      boolean boolean0 = flags0.isOff(2211);
      assertEquals(2211L, flags0.getFlags());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Flags flags0 = new Flags((-237), (-237));
      boolean boolean0 = flags0.isOn((-1098L));
      assertFalse(boolean0);
      assertEquals(0L, flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Flags flags0 = new Flags(7, 7);
      assertEquals(0L, flags0.getFlags());
      
      flags0.turnOn(1L);
      long long0 = flags0.getFlags();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Flags flags0 = new Flags(2211, 2211);
      assertEquals(0L, flags0.getFlags());
      
      flags0.turnOnAll();
      long long0 = flags0.getFlags();
      assertEquals((-1L), long0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      String string0 = flags0.toString();
      assertEquals("0000000000000000000000000000000000000000000000000000000000000001", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      Flags flags1 = (Flags)flags0.clone();
      boolean boolean0 = flags0.equals(flags1);
      assertTrue(boolean0);
      assertEquals(1L, flags1.getFlags());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      Object object0 = new Object();
      boolean boolean0 = flags0.equals(object0);
      assertFalse(boolean0);
      assertEquals(1L, flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      boolean boolean0 = flags0.equals(flags0);
      assertTrue(boolean0);
      assertEquals(1L, flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      assertEquals(1L, flags0.getFlags());
      
      flags0.turnOffAll();
      boolean boolean0 = flags0.isOff(1L);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Flags flags0 = new Flags(702, 702);
      assertEquals(0L, flags0.getFlags());
      
      flags0.turnOnAll();
      boolean boolean0 = flags0.isOff((-1746L));
      assertEquals((-1L), flags0.getFlags());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Flags flags0 = new Flags(702, 702);
      assertEquals(0L, flags0.getFlags());
      
      flags0.turnOnAll();
      boolean boolean0 = flags0.isOn((-1746L));
      assertEquals((-1L), flags0.getFlags());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Flags flags0 = new Flags(702, 702);
      boolean boolean0 = flags0.isOn(702);
      assertEquals(0L, flags0.getFlags());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      flags0.hashCode();
      assertEquals(1L, flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Flags flags0 = new Flags(1767, 606L);
      Object object0 = flags0.clone();
      flags0.turnOnAll();
      boolean boolean0 = flags0.equals(object0);
      assertFalse(boolean0);
      assertEquals((-1L), flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Flags flags0 = new Flags(1767, 606L);
      long long0 = flags0.getFlags();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Flags flags0 = new Flags(1767, 606L);
      flags0.clear();
      assertEquals(0L, flags0.getFlags());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Flags flags0 = new Flags(1, 1);
      assertEquals(1L, flags0.getFlags());
      
      flags0.turnOff(1);
      assertEquals(0L, flags0.getFlags());
  }
}
