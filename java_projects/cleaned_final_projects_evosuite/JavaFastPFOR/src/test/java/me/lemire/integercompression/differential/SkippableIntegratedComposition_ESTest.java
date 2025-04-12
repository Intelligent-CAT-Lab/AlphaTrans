
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
import me.lemire.integercompression.differential.IntegratedVariableByte;
import me.lemire.integercompression.differential.SkippableIntegratedComposition;
import me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SkippableIntegratedComposition_ESTest extends SkippableIntegratedComposition_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[3];
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray1 = new int[6];
      skippableIntegratedComposition0.headlessUncompress(intArray1, intWrapper0, 170, intArray0, intWrapper0, 1, intWrapper0);
      assertEquals((short)2, intWrapper0.shortValue());
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[3];
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      SkippableIntegratedComposition skippableIntegratedComposition1 = new SkippableIntegratedComposition(skippableIntegratedComposition0, integratedVariableByte0);
      skippableIntegratedComposition1.headlessUncompress(intArray0, intWrapper0, 1, intArray0, intWrapper0, (-944), intWrapper0);
      assertEquals("2", intWrapper0.toString());
      assertEquals(2L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(5);
      IntWrapper intWrapper1 = new IntWrapper((-1069));
      skippableIntegratedComposition0.headlessUncompress(intArray0, intWrapper0, 96, intArray0, intWrapper0, 0, intWrapper1);
      assertEquals((byte)6, intWrapper0.byteValue());
      assertEquals(6.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      intWrapper0.increment();
      int[] intArray0 = new int[12];
      IntWrapper intWrapper1 = new IntWrapper(1);
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      skippableIntegratedComposition0.headlessCompress((int[]) null, intWrapper1, 1, intArray0, intWrapper0, intWrapper0);
      assertEquals((byte)3, intWrapper0.byteValue());
      assertEquals(3L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[12];
      IntWrapper intWrapper1 = new IntWrapper(1);
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      skippableIntegratedComposition0.headlessCompress(intArray0, intWrapper1, (-1), intArray0, intWrapper1, intWrapper0);
      assertEquals(2L, intWrapper1.longValue());
      assertEquals(2.0F, intWrapper1.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[4];
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      SkippableIntegratedComposition skippableIntegratedComposition1 = new SkippableIntegratedComposition(skippableIntegratedComposition0, integratedBinaryPacking0);
      skippableIntegratedComposition1.headlessCompress(intArray0, intWrapper0, (-18), intArray0, intWrapper0, intWrapper0);
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(1, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[12];
      IntWrapper intWrapper1 = new IntWrapper(1);
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.headlessCompress(intArray0, intWrapper0, 790, intArray0, intWrapper1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 768 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      SkippableIntegratedComposition skippableIntegratedComposition1 = new SkippableIntegratedComposition(skippableIntegratedComposition0, integratedBinaryPacking0);
      String string0 = skippableIntegratedComposition1.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition((SkippableIntegratedIntegerCODEC) null, (SkippableIntegratedIntegerCODEC) null);
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntWrapper intWrapper0 = new IntWrapper(1118);
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.headlessUncompress((int[]) null, intWrapper0, 1118, (int[]) null, intWrapper0, 1118, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[2];
      intArray0[1] = (-3653);
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper((-434));
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.headlessUncompress(intArray0, intWrapper0, (-3653), intArray0, intWrapper1, 0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1930);
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.headlessUncompress(intArray0, intWrapper0, 1930, intArray0, intWrapper0, 1930, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1930 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      IntWrapper intWrapper0 = new IntWrapper(9);
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.headlessCompress((int[]) null, intWrapper0, 9, (int[]) null, intWrapper0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.SkippableIntegratedComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedVariableByte0, integratedVariableByte0);
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        skippableIntegratedComposition0.headlessCompress(intArray0, intWrapper0, 1, intArray0, intWrapper0, intWrapper0);
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
      IntWrapper intWrapper0 = new IntWrapper(1);
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      skippableIntegratedComposition0.headlessUncompress((int[]) null, intWrapper0, 0, (int[]) null, intWrapper0, 0, intWrapper0);
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[6];
      SkippableIntegratedComposition skippableIntegratedComposition0 = new SkippableIntegratedComposition(integratedBinaryPacking0, integratedBinaryPacking0);
      skippableIntegratedComposition0.headlessCompress((int[]) null, intWrapper0, 0, intArray0, intWrapper0, intWrapper0);
      assertEquals(1L, intWrapper0.longValue());
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }
}
