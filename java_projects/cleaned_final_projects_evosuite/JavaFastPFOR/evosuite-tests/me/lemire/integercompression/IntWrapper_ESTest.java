
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


package me.lemire.integercompression;

import org.junit.Test;
import static org.junit.Assert.*;
import me.lemire.integercompression.IntWrapper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntWrapper_ESTest extends IntWrapper_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper((-734));
      intWrapper0.add(1533);
      long long0 = intWrapper0.longValue();
      assertEquals(799L, long0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.set((-4021));
      long long0 = intWrapper0.longValue();
      assertEquals((-4021), intWrapper0.get());
      assertEquals((-4021L), long0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      intWrapper0.increment();
      int int0 = intWrapper0.intValue();
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.set((-4021));
      int int0 = intWrapper0.intValue();
      assertEquals((-4021), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(1);
      int int0 = intWrapper0.get();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.set((-4021));
      int int0 = intWrapper0.get();
      assertEquals("-4021", intWrapper0.toString());
      assertEquals((-4021), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper((-734));
      intWrapper0.add(1533);
      float float0 = intWrapper0.floatValue();
      assertEquals(799.0F, float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.set((-4021));
      float float0 = intWrapper0.floatValue();
      assertEquals((-4021), intWrapper0.get());
      assertEquals((-4021.0F), float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper((-734));
      intWrapper0.add(1533);
      double double0 = intWrapper0.doubleValue();
      assertEquals(799.0, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.set((-4021));
      double double0 = intWrapper0.doubleValue();
      assertEquals((-4021.0F), intWrapper0.floatValue(), 0.01F);
      assertEquals((-4021.0), double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      int int0 = intWrapper0.intValue();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      float float0 = intWrapper0.floatValue();
      assertEquals(0.0F, float0, 0.01F);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      String string0 = intWrapper0.toString();
      assertEquals("0", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      int int0 = intWrapper0.get();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(0);
      double double0 = intWrapper0.doubleValue();
      assertEquals(0.0, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      long long0 = intWrapper0.longValue();
      assertEquals(0L, long0);
  }
}
