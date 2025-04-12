
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
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.Util;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Util_ESTest extends Util_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[0] = (-1);
      int int0 = Util.unpackw(intArray0, 0, intArray0, 2, 2);
      assertArrayEquals(new int[] {3, 3, 0}, intArray0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.unpackw(intArray0, 1, intArray0, (-32), (-32));
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.unpackw(intArray0, 1, intArray0, 1, (-101));
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        Util.unpackw(intArray0, 1647, intArray0, 0, 212);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1647 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = 1;
      intArray0[5] = 1;
      // Undeclared exception!
      try { 
        Util.packw(intArray0, 4, intArray0, 21, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.packw(intArray0, 1, intArray0, 1, (-165));
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        Util.packw(intArray0, 18, intArray0, 0, (-496));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int int0 = Util.packsizew(0, (-244));
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.unpack(intArray0, 1, intArray0, 0, 1, (-196));
      assertEquals((-12), int0);
      assertArrayEquals(new int[] {0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        Util.unpack(intArray0, 1, intArray0, 1, 577, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.unpack(intArray0, Integer.MIN_VALUE, intArray0, (-1459), Integer.MIN_VALUE, 16);
      assertEquals(Integer.MIN_VALUE, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = Util.pack(intArray0, 1, intArray0, 1, 1, (-1));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[4] = 3;
      intArray0[5] = (-17);
      // Undeclared exception!
      try { 
        Util.pack(intArray0, 1, intArray0, 1, 37, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[20];
      int[] intArray1 = new int[9];
      intArray1[4] = 3;
      int int0 = Util.pack(intArray0, 3, intArray1, 3, 3, 3);
      assertEquals(4, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 3, 0, 0, 0, 0}, intArray1);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.pack(intArray0, 26, intArray0, 1, (-678), 16);
      assertEquals(26, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[2] = 1920;
      // Undeclared exception!
      try { 
        Util.maxdiffbits(500, intArray0, 0, 500);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[1] = (-93);
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = (-2001);
      intArray0[8] = (-2001);
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1;
      intArray0[7] = 1;
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1;
      intArray0[6] = 1;
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1;
      intArray0[5] = 1;
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1;
      intArray0[4] = 1;
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1;
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1;
      intArray0[2] = 1;
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = (-2001);
      intArray0[1] = (-2001);
      // Undeclared exception!
      try { 
        Util.maxbits32(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = (-812);
      intArray0[2] = 665;
      // Undeclared exception!
      try { 
        Util.maxbits(intArray0, 1, 460);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int int0 = Util.maxbits((int[]) null, (-13), (-13));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      boolean boolean0 = Util.smallerorequalthan(2147483640, 2147483640);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = Util.unpack(intArray0, 1, intArray0, 1, 1, 260);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[2];
      int int0 = Util.pack(intArray0, 1, intArray0, 1, 1, 1826);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.unpack(intArray0, 1, intArray0, 1, 1, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int int0 = Util.packsizew((-1), (-1));
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int int0 = Util.packsize(0, 606);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      int int0 = Util.packsize((-1851), 8);
      assertEquals((-462), int0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      int[] intArray0 = new int[1];
      int int0 = Util.pack((int[]) null, (-1437), intArray0, (-1437), 0, 564);
      assertEquals((-1437), int0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = Util.maxdiffbits(0, intArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      int[] intArray0 = new int[41];
      intArray0[15] = 22;
      int int0 = Util.maxbits32(intArray0, 0);
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 1;
      int int0 = Util.maxbits(intArray0, 1, 1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      int int0 = Util.greatestMultiple(29, (-1961));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      int int0 = Util.greatestMultiple(27, 27);
      assertEquals(27, int0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      int int0 = Util.greatestMultiple((-232), (-232));
      assertEquals((-232), int0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      int int0 = Util.bits(0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.unpackw((int[]) null, (-320), (int[]) null, (-320), (-320));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      int[] intArray0 = new int[33];
      // Undeclared exception!
      try { 
        Util.unpackw(intArray0, 0, intArray0, 0, 0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.unpack((int[]) null, 1, (int[]) null, 1, 1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.packw((int[]) null, 1, (int[]) null, 1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.packsizew(0, 0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.packsize((-1456), (-1456));
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.pack((int[]) null, 2147483639, (int[]) null, 2147483639, 2147483639, 2147483639);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        Util.pack(intArray0, (-77), intArray0, (-77), (-77), (-77));
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.maxdiffbits(2, (int[]) null, 2, 2);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.maxbits32((int[]) null, 2147481903);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Util.packw(intArray0, 5, intArray0, 5, 5);
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Util.packw(intArray0, 3, intArray0, (-879), 3);
      assertEquals(4, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      int int0 = Util.bits(1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      int[] intArray0 = new int[3];
      int int0 = Util.unpackw(intArray0, 0, intArray0, 0, (-8));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Util.packw(intArray0, 0, intArray0, 0, (-4));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        Util.packw(intArray0, 0, intArray0, 1, 0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      int int0 = Util.packsizew(1, 1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      int int0 = Util.packsizew(0, (-9));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Util.unpack(intArray0, 1, intArray0, 1, 1, 1);
      assertEquals(2, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      int int0 = Util.packsize(1, 21);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = Util.maxdiffbits(2, intArray0, 2, 2);
      assertEquals(32, int0);
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.maxbits((int[]) null, 23, 23);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      boolean boolean0 = Util.smallerorequalthan(1, 136);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      boolean boolean0 = Util.smallerorequalthan(41, 22);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      int[] intArray0 = new int[41];
      int int0 = Util.maxbits32(intArray0, 1);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      Util util0 = new Util();
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      // Undeclared exception!
      try { 
        Util.greatestMultiple(0, 0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }
}
