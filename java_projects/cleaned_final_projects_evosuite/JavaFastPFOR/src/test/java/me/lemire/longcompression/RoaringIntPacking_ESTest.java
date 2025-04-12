
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


package me.lemire.longcompression;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Comparator;
import me.lemire.longcompression.RoaringIntPacking;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class RoaringIntPacking_ESTest extends RoaringIntPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      String string0 = RoaringIntPacking.toUnsignedString(0L);
      assertEquals("0", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      long long0 = RoaringIntPacking.pack(0, 0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      long long0 = RoaringIntPacking.pack((-3583), 1);
      assertEquals((-15388867821567L), long0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int int0 = RoaringIntPacking.low(0L);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int int0 = RoaringIntPacking.low(1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int int0 = RoaringIntPacking.high(9831180138545L);
      assertEquals(2288, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int int0 = RoaringIntPacking.high((-809L));
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int int0 = RoaringIntPacking.compareUnsigned((-416), (-416));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int int0 = RoaringIntPacking.compareUnsigned(247, 2523);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String string0 = RoaringIntPacking.toUnsignedString((-524L));
      assertEquals("18446744073709551092", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      String string0 = RoaringIntPacking.toUnsignedString(1L);
      assertEquals("1", string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int int0 = RoaringIntPacking.highestHigh(true);
      assertEquals(Integer.MAX_VALUE, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int int0 = RoaringIntPacking.highestHigh(false);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int int0 = RoaringIntPacking.high(2725L);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      long long0 = RoaringIntPacking.pack(1811, 1811);
      assertEquals(7778185774867L, long0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int int0 = RoaringIntPacking.low((-1));
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Comparator<Integer> comparator0 = RoaringIntPacking.unsignedComparator();
      assertNotNull(comparator0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int int0 = RoaringIntPacking.compareUnsigned(2288, 1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      RoaringIntPacking roaringIntPacking0 = new RoaringIntPacking();
  }
}
