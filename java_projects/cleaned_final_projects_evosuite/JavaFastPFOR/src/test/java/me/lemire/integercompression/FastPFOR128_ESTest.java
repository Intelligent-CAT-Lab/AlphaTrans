
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
import java.nio.ByteBuffer;
import me.lemire.integercompression.FastPFOR128;
import me.lemire.integercompression.IntWrapper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FastPFOR128_ESTest extends FastPFOR128_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(255);
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper((-1));
      // Undeclared exception!
      try { 
        fastPFOR128_0.compress0(intArray0, intWrapper0, (-2403), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(255);
      ByteBuffer byteBuffer0 = fastPFOR128_0.makeBuffer(28);
      assertEquals(28, byteBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      // Undeclared exception!
      try { 
        fastPFOR128_0.uncompress0((int[]) null, intWrapper0, (-43), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(0);
      int[] intArray0 = new int[7];
      intArray0[0] = 128;
      intArray0[2] = 65536;
      intArray0[4] = 1;
      intArray0[5] = 128;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        fastPFOR128_0.uncompress0(intArray0, intWrapper0, 128, intArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      // Undeclared exception!
      try { 
        fastPFOR128_0.makeBuffer((-488));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-488 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        fastPFOR128_0.headlessUncompress((int[]) null, intWrapper0, 65536, (int[]) null, intWrapper0, 65536);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[3];
      intArray0[1] = 1;
      intArray0[2] = 8191;
      IntWrapper intWrapper1 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        fastPFOR128_0.headlessUncompress(intArray0, intWrapper1, 1, intArray0, intWrapper0, 8191);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      IntWrapper intWrapper0 = new IntWrapper(128);
      // Undeclared exception!
      try { 
        fastPFOR128_0.headlessCompress((int[]) null, intWrapper0, 3294, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[151];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[2];
      // Undeclared exception!
      try { 
        fastPFOR128_0.headlessCompress(intArray0, intWrapper0, 160, intArray1, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        fastPFOR128_0.compress0((int[]) null, intWrapper0, 65536, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[135];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(149);
      int[] intArray1 = new int[3];
      // Undeclared exception!
      try { 
        fastPFOR128_0.compress0(intArray0, intWrapper0, 65536, intArray1, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = null;
      try {
        fastPFOR128_0 = new FastPFOR128(Integer.MIN_VALUE);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -268435456
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = null;
      try {
        fastPFOR128_0 = new FastPFOR128((-735));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-752 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[137];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      fastPFOR128_0.headlessUncompress(intArray0, intWrapper0, 128, intArray0, intWrapper0, 128);
      assertEquals("128", intWrapper0.toString());
      assertEquals(128.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(255);
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper((-1));
      fastPFOR128_0.headlessCompress(intArray0, intWrapper0, 31, intArray0, intWrapper0);
      assertEquals("-1", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[16];
      IntWrapper intWrapper0 = new IntWrapper(128);
      fastPFOR128_0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(128, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(29);
      fastPFOR128_0.compress0(intArray0, intWrapper0, 29, intArray0, intWrapper0);
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[148];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        fastPFOR128_0.headlessUncompress(intArray0, intWrapper0, (-3229), intArray0, intWrapper0, 1156);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 161
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(0);
      int[] intArray0 = new int[7];
      intArray0[0] = 128;
      intArray0[2] = 65536;
      intArray0[3] = 65536;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        fastPFOR128_0.uncompress0(intArray0, intWrapper0, 128, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 34820 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[150];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper2 = IntWrapper.IntWrapper1();
      fastPFOR128_0.compress0(intArray0, intWrapper1, 128, intArray0, intWrapper0);
      fastPFOR128_0.uncompress0(intArray0, intWrapper2, 65536, intArray0, intWrapper2);
      assertEquals("129", intWrapper2.toString());
      assertEquals(129L, intWrapper2.longValue());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(0);
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      fastPFOR128_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[151];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        fastPFOR128_0.headlessCompress(intArray0, intWrapper0, 160, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 151 out of bounds for length 151
         //
         verifyException("me.lemire.integercompression.FastPFOR128", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      int[] intArray0 = new int[150];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper2 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper3 = IntWrapper.IntWrapper1();
      fastPFOR128_0.compress0(intArray0, intWrapper1, 128, intArray0, intWrapper0);
      fastPFOR128_0.compress0(intArray0, intWrapper2, 128, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        fastPFOR128_0.compress0(intArray0, intWrapper3, 128, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 150 out of bounds for length 150
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      String string0 = fastPFOR128_0.toString();
      assertEquals("FastPFOR128", string0);
  }
}
