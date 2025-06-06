
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
import me.lemire.integercompression.differential.IntegratedBinaryPacking;
import me.lemire.integercompression.differential.IntegratedIntCompressor;
import me.lemire.integercompression.differential.IntegratedVariableByte;
import me.lemire.integercompression.differential.SkippableIntegratedComposition;
import me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntegratedIntCompressor_ESTest extends IntegratedIntCompressor_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor(400, integratedVariableByte0);
      int[] intArray0 = new int[1];
      intArray0[0] = 400;
      int[] intArray1 = integratedIntCompressor0.uncompress(intArray0);
      int[] intArray2 = integratedIntCompressor0.compress(intArray1);
      assertEquals(8, intArray2.length);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedVariableByte0, integratedBinaryPacking0);
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-1), skippableIntegratedComposition0);
      int[] intArray0 = new int[2];
      int[] intArray1 = integratedIntCompressor0.compress(intArray0);
      int[] intArray2 = integratedIntCompressor0.uncompress(intArray1);
      assertArrayEquals(new int[] {0, 0}, intArray2);
      assertArrayEquals(new int[] {2, 0, 32896}, intArray1);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-1062), integratedVariableByte0);
      // Undeclared exception!
      try { 
        integratedIntCompressor0.uncompress((int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedIntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-518), integratedVariableByte0);
      int[] intArray0 = new int[1];
      intArray0[0] = (-518);
      // Undeclared exception!
      try { 
        integratedIntCompressor0.uncompress(intArray0);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -518
         //
         verifyException("me.lemire.integercompression.differential.IntegratedIntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor(100, integratedVariableByte0);
      int[] intArray0 = new int[2];
      intArray0[0] = 100;
      intArray0[1] = 100;
      // Undeclared exception!
      try { 
        integratedIntCompressor0.uncompress(intArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[4];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-2919), integratedVariableByte0);
      // Undeclared exception!
      try { 
        integratedIntCompressor0.uncompress(intArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-1325), integratedBinaryPacking0);
      integratedIntCompressor0.codec = (SkippableIntegratedIntegerCODEC) integratedBinaryPacking0;
      int[] intArray0 = new int[1];
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      integratedIntCompressor0.codec = (SkippableIntegratedIntegerCODEC) skippableIntegratedComposition0;
      skippableIntegratedComposition0.F2 = integratedIntCompressor0.codec;
      // Undeclared exception!
      try { 
        integratedIntCompressor0.compress(intArray0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Your input is too poorly compressible with the current codec : me.lemire.integercompression.differential.IntegratedBinaryPacking@0000000001 + me.lemire.integercompression.differential.SkippableIntegratedComposition@0000000006
         //
         verifyException("me.lemire.integercompression.differential.IntegratedIntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedVariableByte0, integratedBinaryPacking0);
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-1), skippableIntegratedComposition0);
      int[] intArray0 = new int[2];
      integratedIntCompressor0.codec = (SkippableIntegratedIntegerCODEC) integratedBinaryPacking0;
      integratedIntCompressor0.codec = (SkippableIntegratedIntegerCODEC) skippableIntegratedComposition0;
      skippableIntegratedComposition0.F1 = (SkippableIntegratedIntegerCODEC) integratedBinaryPacking0;
      skippableIntegratedComposition0.F1 = integratedIntCompressor0.codec;
      // Undeclared exception!
      try { 
        integratedIntCompressor0.compress(intArray0);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor((-1062), integratedVariableByte0);
      // Undeclared exception!
      try { 
        integratedIntCompressor0.compress((int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedIntCompressor", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor(0, integratedBinaryPacking0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntegratedIntCompressor integratedIntCompressor0 = new IntegratedIntCompressor(400, integratedVariableByte0);
      int[] intArray0 = new int[1];
      int[] intArray1 = integratedIntCompressor0.uncompress(intArray0);
      assertEquals(0, intArray1.length);
  }
}
