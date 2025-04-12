
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


package me.lemire.integercompression.differential;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.differential.IntegratedBinaryPacking;
import me.lemire.integercompression.differential.IntegratedComposition;
import me.lemire.integercompression.differential.IntegratedIntegerCODEC;
import me.lemire.integercompression.differential.IntegratedVariableByte;
import me.lemire.integercompression.differential.XorBinaryPacking;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntegratedComposition_ESTest extends IntegratedComposition_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedVariableByte0, integratedVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper((-1009));
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[1];
      IntegratedComposition integratedComposition1 = new IntegratedComposition(integratedComposition0, integratedBinaryPacking0);
      integratedComposition1.uncompress0((int[]) null, intWrapper0, (-1009), intArray0, intWrapper0);
      assertEquals((-2018), intWrapper0.get());
      assertEquals((-2018.0), intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedVariableByte0, integratedVariableByte0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper((-1519));
      integratedComposition0.uncompress0(intArray0, intWrapper0, (-1351), intArray0, intWrapper0);
      assertEquals("-2870", intWrapper0.toString());
      assertEquals((-2870), intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[1];
      integratedComposition0.uncompress0(intArray0, intWrapper0, 2818, intArray1, intWrapper0);
      assertEquals(2, intWrapper0.get());
      assertEquals(2, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(2674);
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition((IntegratedIntegerCODEC) null, xorBinaryPacking0);
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        integratedComposition0.uncompress0(intArray0, intWrapper0, (-813), intArray0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(0);
      integratedComposition0.uncompress0(intArray0, intWrapper0, 5603, intArray0, intWrapper1);
      assertEquals("2", intWrapper0.toString());
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(127);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      integratedComposition0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper1);
      assertEquals(1L, intWrapper1.longValue());
      assertEquals(1, intWrapper1.intValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[1];
      integratedComposition0.compress0(intArray0, intWrapper0, (-1), intArray1, intWrapper0);
      assertEquals("1", intWrapper0.toString());
      assertEquals(1, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntegratedComposition integratedComposition1 = new IntegratedComposition(integratedComposition0, integratedBinaryPacking0);
      String string0 = integratedComposition1.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[5];
      intArray0[0] = 2369;
      intArray0[1] = (-1);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        integratedComposition0.uncompress0(intArray0, intWrapper0, (-1), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        integratedComposition0.uncompress0(intArray0, intWrapper0, 5603, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegratedComposition integratedComposition0 = new IntegratedComposition((IntegratedIntegerCODEC) null, (IntegratedIntegerCODEC) null);
      // Undeclared exception!
      try { 
        integratedComposition0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedVariableByte0, integratedVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper(956);
      // Undeclared exception!
      try { 
        integratedComposition0.compress0((int[]) null, intWrapper0, 956, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedVariableByte0, integratedVariableByte0);
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(2191);
      // Undeclared exception!
      try { 
        integratedComposition0.compress0(intArray0, intWrapper0, Integer.MIN_VALUE, intArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedVariableByte0, integratedVariableByte0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1315);
      // Undeclared exception!
      try { 
        integratedComposition0.compress0(intArray0, intWrapper0, (-1), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-8 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(127);
      // Undeclared exception!
      try { 
        integratedComposition0.compress0(intArray0, intWrapper0, 16, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 127 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(0);
      integratedComposition0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[6];
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      integratedComposition0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntegratedComposition integratedComposition1 = new IntegratedComposition(integratedComposition0, integratedComposition0);
      integratedComposition1.compress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      assertEquals((short)4, intWrapper0.shortValue());
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedComposition integratedComposition0 = new IntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntWrapper intWrapper0 = new IntWrapper(1);
      integratedComposition0.F2 = (IntegratedIntegerCODEC) integratedComposition0;
      int[] intArray0 = new int[4];
      integratedComposition0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals((byte)2, intWrapper0.byteValue());
      assertEquals(2.0F, intWrapper0.floatValue(), 0.01F);
  }
}
