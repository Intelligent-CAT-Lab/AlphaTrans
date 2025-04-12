
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
import me.lemire.integercompression.GroupSimple9;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.Kamikaze;
import me.lemire.integercompression.NewPFD;
import me.lemire.integercompression.NewPFDS9;
import me.lemire.integercompression.Simple16;
import me.lemire.integercompression.SkippableComposition;
import me.lemire.integercompression.SkippableIntegerCODEC;
import me.lemire.integercompression.VariableByte;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SkippableComposition_ESTest extends SkippableComposition_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      GroupSimple9 groupSimple9_0 = new GroupSimple9();
      NewPFD newPFD0 = new NewPFD();
      SkippableComposition skippableComposition0 = new SkippableComposition(groupSimple9_0, newPFD0);
      String string0 = skippableComposition0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      GroupSimple9 groupSimple9_0 = new GroupSimple9();
      NewPFD newPFD0 = new NewPFD();
      SkippableComposition skippableComposition0 = new SkippableComposition(groupSimple9_0, newPFD0);
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[1];
      skippableComposition0.headlessUncompress(intArray1, intWrapper0, (-78), intArray0, intWrapper0, 0);
      assertEquals(1L, intWrapper0.longValue());
      assertEquals(1, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      GroupSimple9 groupSimple9_0 = new GroupSimple9();
      NewPFD newPFD0 = new NewPFD();
      SkippableComposition skippableComposition0 = new SkippableComposition(groupSimple9_0, newPFD0);
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[1];
      skippableComposition0.headlessCompress(intArray0, intWrapper0, (-78), intArray1, intWrapper0);
      assertEquals(1.0F, intWrapper0.floatValue(), 0.01F);
      assertArrayEquals(new int[] {0}, intArray1);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      SkippableComposition skippableComposition0 = new SkippableComposition((SkippableIntegerCODEC) null, (SkippableIntegerCODEC) null);
      // Undeclared exception!
      try { 
        skippableComposition0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      SkippableComposition skippableComposition0 = new SkippableComposition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[3];
      intArray0[0] = (-3676);
      intArray0[1] = (-3676);
      // Undeclared exception!
      try { 
        skippableComposition0.headlessUncompress(intArray0, intWrapper0, (-3676), intArray0, intWrapper0, 448);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(834);
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      SkippableComposition skippableComposition0 = new SkippableComposition(fastPFOR0, fastPFOR0);
      // Undeclared exception!
      try { 
        skippableComposition0.headlessUncompress((int[]) null, intWrapper0, 834, (int[]) null, intWrapper0, 65536);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      SkippableComposition skippableComposition0 = new SkippableComposition(kamikaze0, kamikaze0);
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(2224);
      // Undeclared exception!
      try { 
        skippableComposition0.headlessUncompress(intArray0, intWrapper0, 1298, intArray0, intWrapper0, (-2147483647));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -4608
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      SkippableComposition skippableComposition0 = new SkippableComposition(kamikaze0, kamikaze0);
      IntWrapper intWrapper0 = new IntWrapper((-56));
      int[] intArray0 = new int[8];
      intArray0[2] = (-56);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      skippableComposition0.headlessCompress(intArray0, intWrapper0, (-56), intArray0, intWrapper1);
      BinaryPacking binaryPacking0 = new BinaryPacking();
      SkippableComposition skippableComposition1 = new SkippableComposition(kamikaze0, binaryPacking0);
      // Undeclared exception!
      try { 
        skippableComposition1.headlessUncompress(intArray0, intWrapper1, 0, intArray0, intWrapper0, 0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      GroupSimple9 groupSimple9_0 = new GroupSimple9();
      SkippableComposition skippableComposition0 = new SkippableComposition(groupSimple9_0, groupSimple9_0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper((-1782));
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        skippableComposition0.headlessUncompress(intArray0, intWrapper0, 1053, intArray0, intWrapper1, (-5120));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -6902 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.GroupSimple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[9];
      intArray0[5] = 536870911;
      SkippableComposition skippableComposition0 = new SkippableComposition(simple16_0, newPFDS9_0);
      // Undeclared exception!
      try { 
        skippableComposition0.headlessCompress(intArray0, intWrapper0, 405, intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      SkippableComposition skippableComposition0 = new SkippableComposition((SkippableIntegerCODEC) null, (SkippableIntegerCODEC) null);
      IntWrapper intWrapper0 = new IntWrapper(361);
      // Undeclared exception!
      try { 
        skippableComposition0.headlessCompress((int[]) null, intWrapper0, 361, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.SkippableComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper((-713));
      VariableByte variableByte0 = new VariableByte();
      Kamikaze kamikaze0 = new Kamikaze();
      SkippableComposition skippableComposition0 = new SkippableComposition(variableByte0, kamikaze0);
      // Undeclared exception!
      try { 
        skippableComposition0.headlessCompress((int[]) null, intWrapper0, (-713), (int[]) null, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-5704 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      SkippableComposition skippableComposition0 = new SkippableComposition(newPFDS9_0, newPFDS9_0);
      IntWrapper intWrapper0 = new IntWrapper((-713));
      SkippableComposition skippableComposition1 = new SkippableComposition(skippableComposition0, newPFDS9_0);
      skippableComposition1.headlessUncompress((int[]) null, intWrapper0, (-713), (int[]) null, intWrapper0, (-713));
      assertEquals((byte)56, intWrapper0.byteValue());
      assertEquals("-712", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      SkippableComposition skippableComposition0 = new SkippableComposition(kamikaze0, kamikaze0);
      IntWrapper intWrapper0 = new IntWrapper((-56));
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        skippableComposition0.headlessCompress(intArray0, intWrapper0, (-56), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -56 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.SkippableComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      GroupSimple9 groupSimple9_0 = new GroupSimple9();
      SkippableComposition skippableComposition0 = new SkippableComposition(groupSimple9_0, groupSimple9_0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray0 = new int[8];
      skippableComposition0.headlessCompress(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals("1", intWrapper0.toString());
  }
}
