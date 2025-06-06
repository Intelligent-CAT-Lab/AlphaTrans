
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
import me.lemire.integercompression.BinaryPacking;
import me.lemire.integercompression.IntWrapper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BinaryPacking_ESTest extends BinaryPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[5];
      intArray0[0] = 793;
      intArray0[1] = 268435455;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        binaryPacking0.uncompress0(intArray0, intWrapper0, 32467, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[2];
      intArray1[0] = (-2653);
      BinaryPacking binaryPacking0 = new BinaryPacking();
      // Undeclared exception!
      try { 
        binaryPacking0.headlessUncompress(intArray1, intWrapper0, (-2457), intArray0, intWrapper0, 3287);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[3];
      intArray0[0] = 2327;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        binaryPacking0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 2327);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 32
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper((-2854));
      // Undeclared exception!
      try { 
        binaryPacking0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper1, 2327);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: -2854
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(1);
      binaryPacking0.uncompress0(intArray0, intWrapper0, (-3007), intArray0, intWrapper0);
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
      assertEquals((short)2, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(Integer.MAX_VALUE);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        binaryPacking0.headlessCompress(intArray0, intWrapper0, (-193), (int[]) null, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483617 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      binaryPacking0.compress0(intArray0, intWrapper1, (-3025), intArray0, intWrapper1);
      binaryPacking0.compress0(intArray0, intWrapper0, (-1226), intArray0, intWrapper1);
      assertArrayEquals(new int[] {(-3008), (-1216), 0, 0, 0}, intArray0);
      assertEquals((-1215), intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray1 = new int[2];
      binaryPacking0.compress0(intArray0, intWrapper0, (-3025), intArray1, intWrapper0);
      assertEquals("2", intWrapper0.toString());
      assertArrayEquals(new int[] {0, (-3008)}, intArray1);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(110);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      intArray0[0] = 110;
      intArray0[1] = 817;
      // Undeclared exception!
      try { 
        binaryPacking0.uncompress0(intArray0, intWrapper1, 817, (int[]) null, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[4];
      intArray0[0] = 96;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        binaryPacking0.headlessUncompress(intArray0, intWrapper0, 96, intArray0, intWrapper0, 39);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(127);
      // Undeclared exception!
      try { 
        binaryPacking0.headlessCompress((int[]) null, intWrapper0, 127, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(1190);
      // Undeclared exception!
      try { 
        binaryPacking0.compress0(intArray0, intWrapper0, 1190, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1190 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.BinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(127);
      // Undeclared exception!
      try { 
        binaryPacking0.headlessUncompress((int[]) null, intWrapper0, 127, (int[]) null, intWrapper0, 127);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper((-2216));
      binaryPacking0.headlessUncompress(intArray0, intWrapper0, 575, intArray0, intWrapper0, 23);
      assertEquals((-2216.0), intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(110);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      intArray0[0] = 110;
      // Undeclared exception!
      try { 
        binaryPacking0.uncompress0(intArray0, intWrapper1, 817, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(1626);
      binaryPacking0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(3, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(110);
      binaryPacking0.headlessCompress((int[]) null, intWrapper0, 8, (int[]) null, intWrapper0);
      assertEquals(110, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper((-2216));
      binaryPacking0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((-2216.0), intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper((-1));
      // Undeclared exception!
      try { 
        binaryPacking0.compress0(intArray0, intWrapper0, (-3545), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      String string0 = binaryPacking0.toString();
      assertEquals("BinaryPacking", string0);
  }
}
