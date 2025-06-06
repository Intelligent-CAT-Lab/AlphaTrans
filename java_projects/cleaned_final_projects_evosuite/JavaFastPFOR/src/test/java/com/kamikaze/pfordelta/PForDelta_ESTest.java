
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


package com.kamikaze.pfordelta;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import com.kamikaze.pfordelta.PForDelta;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PForDelta_ESTest extends PForDelta_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = (-939);
      intArray0[1] = 4207;
      int int0 = PForDelta.readBits(intArray0, 0, 3338);
      assertEquals(127, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = 2699;
      int int0 = PForDelta.readBits(intArray0, 13, 817);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[0] = (-345);
      int int0 = PForDelta.readBits(intArray0, 12, 16);
      assertEquals(65535, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = 821;
      PForDelta.writeBits(intArray0, 3, 0, 583);
      assertArrayEquals(new int[] {3, 823, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[8];
      PForDelta.writeBits(intArray0, (-3790), 26, 32);
      assertArrayEquals(new int[] {(-939524096), 67108804, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = (-1607);
      PForDelta.writeBits(intArray0, 2041, 19, 3);
      assertArrayEquals(new int[] {(-1607), 0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlockOpt(intArray0, (-2147483624));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483625 out of bounds for length 7
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        PForDelta.checkBigNumbers(intArray0, 0, 1708);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = 21;
      int[] intArray1 = PForDelta.compressOneBlock(intArray0, 2, 2);
      int int0 = PForDelta.decompressOneBlock(intArray1, intArray1, 3);
      assertArrayEquals(new int[] {0, 0, 0, 0}, intArray1);
      assertEquals(128, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[3];
      int[] intArray1 = new int[6];
      intArray1[0] = 18;
      intArray1[3] = (-6813);
      int int0 = PForDelta.decompressOneBlock(intArray0, intArray1, 18);
      assertEquals(160, int0);
      assertArrayEquals(new int[] {0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = (-939);
      // Undeclared exception!
      try { 
        PForDelta.decompressOneBlock(intArray0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[19];
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlockOpt(intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 19
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[0] = (-744);
      int int0 = PForDelta.readBits(intArray0, 0, 0);
      assertEquals((-744), int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = PForDelta.estimateCompressedSize(intArray0, 0, (-2272));
      assertEquals(64, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = PForDelta.estimateCompressedSize(intArray0, 4739, (-1262));
      assertEquals((-5980554), int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[3];
      int int0 = PForDelta.decompressBlockByS16(intArray0, intArray0, 0, (-2519));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = PForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 0, 583);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = PForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 932, 536870911);
      assertEquals(2147482716, int0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = PForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 1023, (-1));
      assertEquals((-1023), int0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int int0 = PForDelta.decompressBBitSlots((int[]) null, (int[]) null, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = PForDelta.decompressBBitSlots(intArray0, intArray0, (-661), 27);
      assertEquals((-17847), int0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[6];
      int[] intArray1 = PForDelta.compressOneBlock(intArray0, (-35), 2);
      assertEquals(0, intArray1.length);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        PForDelta.writeBits(intArray0, (-12923), (-12923), (-12923));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 134217324 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.readBits((int[]) null, 26, 26);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        PForDelta.readBits(intArray0, (-2007), (-2007));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 134217665 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.decompressOneBlock((int[]) null, (int[]) null, 12);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        PForDelta.decompressOneBlock(intArray0, intArray0, (-939));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1878
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        PForDelta.decompressBlockByS16(intArray0, intArray0, 64, 64);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        PForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 970, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 0
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.decompressBBitSlots((int[]) null, (int[]) null, 80, 80);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlockOpt((int[]) null, 19);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlockOpt(intArray0, (-939));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1878
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlock((int[]) null, 69, 69);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlock(intArray0, (-741), (-741));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1482
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      int[] intArray0 = new int[20];
      PForDelta.writeBits(intArray0, 103, 20, 64);
      int[] intArray1 = PForDelta.compressOneBlockOpt(intArray0, 19);
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlock(intArray1, 64, 23);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 64 out of bounds for length 33
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.writeBits((int[]) null, 1023, 1023, 1023);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      int[] intArray0 = new int[4];
      PForDelta.writeBits(intArray0, 108, 0, 0);
      assertArrayEquals(new int[] {0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      int int0 = PForDelta.decompressBlockByS16((int[]) null, (int[]) null, (-939), (-939));
      assertEquals(11, int0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.decompressBlockByS16((int[]) null, (int[]) null, 19, 19);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        PForDelta.decompressBBitSlots(intArray0, intArray0, 980, 980);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 32 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      int int0 = PForDelta.decompressBBitSlots((int[]) null, (int[]) null, (-939), (-939));
      assertEquals(881721, int0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = 64;
      boolean boolean0 = PForDelta.checkBigNumbers(intArray0, 2, 64);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      int[] intArray0 = new int[4];
      boolean boolean0 = PForDelta.checkBigNumbers(intArray0, 0, (-3061));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[0] = 1502;
      // Undeclared exception!
      try { 
        PForDelta.estimateCompressedSize(intArray0, 0, 1502);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = PForDelta.estimateCompressedSize(intArray0, 64, (-1));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.estimateCompressedSize((int[]) null, 22, 22);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      int[] intArray0 = new int[20];
      int[] intArray1 = PForDelta.compressOneBlock(intArray0, 20, 20);
      // Undeclared exception!
      try { 
        PForDelta.decompressOneBlock(intArray0, intArray1, 4000);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 15
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = PForDelta.decompressOneBlock(intArray0, intArray0, 729);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(64, int0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      int[] intArray0 = new int[43];
      intArray0[0] = 12;
      int[] intArray1 = PForDelta.compressOneBlockOpt(intArray0, 12);
      // Undeclared exception!
      try { 
        PForDelta.compressOneBlockOpt(intArray1, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDelta.decompressBBitSlotsWithHardCodes((int[]) null, (int[]) null, 12, 12);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      PForDelta pForDelta0 = new PForDelta();
  }
}
