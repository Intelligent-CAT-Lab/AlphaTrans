
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
import me.lemire.integercompression.DeltaZigzagBinaryPacking;
import me.lemire.integercompression.IntWrapper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DeltaZigzagBinaryPacking_ESTest extends DeltaZigzagBinaryPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[9];
      deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[6];
      intArray1[0] = 1;
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0(intArray1, intWrapper1, 1, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.DeltaZigzagEncoding$Decoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[8];
      intArray0[0] = 3218;
      intArray0[1] = 871;
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, 871, intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray1 = new int[7];
      intArray1[0] = 243;
      intArray1[1] = 262143;
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0(intArray1, intWrapper0, (-2176), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[9];
      intArray0[0] = 3943;
      intArray0[1] = 67108863;
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, 548, intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[4];
      intArray0[1] = 513;
      intArray0[2] = (-988);
      IntWrapper intWrapper0 = new IntWrapper(0);
      deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, (-145), intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, (-1385), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[4];
      intArray0[1] = 513;
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper((-3316));
      deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, (-145), intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, (-1385), intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3316 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.DeltaZigzagEncoding$Decoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[4];
      intArray0[0] = (-4231);
      IntWrapper intWrapper0 = new IntWrapper(0);
      deltaZigzagBinaryPacking0.uncompress0(intArray0, intWrapper0, 622, intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals((short)1, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[6];
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.compress0(intArray1, intWrapper0, 1861, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.DeltaZigzagEncoding$Encoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper((-793));
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.compress0(intArray0, intWrapper1, 1731, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -793 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.DeltaZigzagEncoding$Encoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[6];
      deltaZigzagBinaryPacking0.compress0(intArray0, intWrapper0, (-2039), intArray1, intWrapper0);
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
      assertArrayEquals(new int[] {(-1920), 0, 0, 0, 0, 0}, intArray1);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1759);
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.uncompress0((int[]) null, intWrapper0, 1759, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.DeltaZigzagBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(814);
      // Undeclared exception!
      try { 
        deltaZigzagBinaryPacking0.compress0((int[]) null, intWrapper0, 814, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.DeltaZigzagBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(1);
      deltaZigzagBinaryPacking0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DeltaZigzagBinaryPacking deltaZigzagBinaryPacking0 = new DeltaZigzagBinaryPacking();
      String string0 = deltaZigzagBinaryPacking0.toString();
      assertEquals("DeltaZigzagBinaryPacking", string0);
  }
}
