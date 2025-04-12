
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
import me.lemire.integercompression.FastPFOR;
import me.lemire.integercompression.FastPFOR128;
import me.lemire.integercompression.GroupSimple9;
import me.lemire.integercompression.IntCompressor;
import me.lemire.integercompression.Simple16;
import me.lemire.integercompression.SkippableIntegerCODEC;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntCompressor_ESTest extends IntCompressor_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      GroupSimple9 groupSimple9_0 = new GroupSimple9();
      IntCompressor intCompressor0 = new IntCompressor((-273), groupSimple9_0);
      int[] intArray0 = new int[2];
      intArray0[0] = (-273);
      intCompressor0.codec = (SkippableIntegerCODEC) groupSimple9_0;
      int[] intArray1 = intCompressor0.compress(intArray0);
      // Undeclared exception!
      try { 
        intCompressor0.uncompress(intArray1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.GroupSimple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(0);
      IntCompressor intCompressor0 = new IntCompressor(0, fastPFOR128_0);
      // Undeclared exception!
      try { 
        intCompressor0.uncompress((int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.IntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      BinaryPacking binaryPacking0 = new BinaryPacking();
      IntCompressor intCompressor0 = new IntCompressor((-3912), binaryPacking0);
      int[] intArray0 = new int[1];
      intArray0[0] = (-3912);
      // Undeclared exception!
      try { 
        intCompressor0.uncompress(intArray0);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -3912
         //
         verifyException("me.lemire.integercompression.IntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = FastPFOR128.FastPFOR1281();
      IntCompressor intCompressor0 = new IntCompressor((-1), fastPFOR128_0);
      int[] intArray0 = new int[4];
      intArray0[0] = 65536;
      intArray0[1] = (-1);
      intCompressor0.codec = (SkippableIntegerCODEC) fastPFOR128_0;
      // Undeclared exception!
      try { 
        intCompressor0.uncompress(intArray0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(80);
      IntCompressor intCompressor0 = new IntCompressor(6, fastPFOR0);
      int[] intArray0 = new int[8];
      intArray0[0] = 256;
      intArray0[1] = 80;
      // Undeclared exception!
      try { 
        intCompressor0.uncompress(intArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      IntCompressor intCompressor0 = new IntCompressor(256, fastPFOR0);
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        intCompressor0.uncompress(intArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.IntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(40);
      IntCompressor intCompressor0 = new IntCompressor(40, fastPFOR128_0);
      int[] intArray0 = new int[1];
      intCompressor0.codec = (SkippableIntegerCODEC) fastPFOR128_0;
      intArray0[0] = 65536;
      int[] intArray1 = intCompressor0.uncompress(intArray0);
      // Undeclared exception!
      intCompressor0.compress(intArray1);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntCompressor intCompressor0 = new IntCompressor(Integer.MAX_VALUE, simple16_0);
      int[] intArray0 = new int[6];
      intArray0[0] = Integer.MAX_VALUE;
      intCompressor0.codec = (SkippableIntegerCODEC) simple16_0;
      // Undeclared exception!
      try { 
        intCompressor0.compress(intArray0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      IntCompressor intCompressor0 = new IntCompressor(256, fastPFOR0);
      // Undeclared exception!
      try { 
        intCompressor0.compress((int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.IntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      FastPFOR128 fastPFOR128_0 = new FastPFOR128(40);
      IntCompressor intCompressor0 = new IntCompressor(40, fastPFOR128_0);
      int[] intArray0 = new int[1];
      int[] intArray1 = intCompressor0.uncompress(intArray0);
      assertEquals(0, intArray1.length);
  }
}
