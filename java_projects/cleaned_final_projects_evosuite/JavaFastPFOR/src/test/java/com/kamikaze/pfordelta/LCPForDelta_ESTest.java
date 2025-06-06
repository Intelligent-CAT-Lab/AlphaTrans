
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
import com.kamikaze.pfordelta.LCPForDelta;
import java.nio.BufferUnderflowException;
import java.nio.IntBuffer;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LCPForDelta_ESTest extends LCPForDelta_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[0] = (-2039);
      intArray0[1] = (-2039);
      int int0 = LCPForDelta.readBitsWithBuffer(intArray0, 0, 4157553);
      assertEquals(129033, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 2;
      int int0 = LCPForDelta.readBitsWithBuffer(intArray0, 2, 2315);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        LCPForDelta.readBitsWithBuffer(intArray0, (-6093), 2861);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 134217537 out of bounds for length 2
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = (-18467);
      intArray0[2] = 2047;
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlots(intArray0, intArray0, 587, 1119);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 35 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[52];
      int int0 = LCPForDelta.readBits(intArray0, 29, 3);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[0] = (-222);
      int int0 = LCPForDelta.readBits(intArray0, 22, 0);
      assertEquals(1023, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        LCPForDelta.readBits(intArray0, (-522), 18);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 134217711 out of bounds for length 0
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 23;
      LCPForDelta.writeBits(intArray0, 3482, 23, 23);
      assertArrayEquals(new int[] {(-855638016), 23, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[0] = (-222);
      LCPForDelta.writeBits(intArray0, (-222), 18, (-222));
      assertArrayEquals(new int[] {(-222), 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore(intArray0, 9, (-1191));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 134217691 out of bounds for length 29
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[7];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      LCPForDelta.decompressBlockByS16WithIntBufferIntegrated(intArray0, intBuffer0, 0, intArray0, 31);
      assertEquals("java.nio.HeapIntBuffer[pos=0 lim=7 cap=7]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[7];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      LCPForDelta.decompressBlockByS16WithIntBuffer(intArray0, intBuffer0, 0);
      assertEquals(0, intBuffer0.position());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 2;
      intArray0[1] = (-18467);
      LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, 32767, intArray0, intArray0, 1);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[6] = 7;
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int int0 = lCPForDelta0.compressOneBlockCore(intArray0, 7, 2);
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[48];
      int[] intArray1 = new int[8];
      intArray1[0] = 1;
      intArray1[1] = (-786520);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, intBuffer0, (-696), intArray0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 267648936 out of bounds for length 48
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[0] = (-659);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, (-659), intArray0, intArray0, 742);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 134217091 out of bounds for length 2
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = (-1191);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlock(intArray0, intArray0, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[8];
      intArray0[0] = (-703);
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore2(intArray0, 13, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[2];
      intArray0[1] = 4;
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore2(intArray0, 4, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[3];
      intArray0[1] = (-490);
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore(intArray0, 31, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 2;
      intArray0[2] = 2;
      LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, 2, intArray0, intArray0, 2);
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore(intArray0, 4095, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[7];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      int[] intArray1 = new int[4];
      intBuffer0.put(0, (-498));
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16WithIntBufferIntegrated(intArray0, intBuffer0, 1410, intArray1, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[0] = (-222);
      int int0 = LCPForDelta.readBitsWithBuffer(intArray0, 6, 255);
      assertEquals(67108860, int0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[0] = (-2039);
      int int0 = LCPForDelta.readBitsWithBuffer(intArray0, 0, 32);
      assertEquals((-2039), int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 268435455;
      int int0 = LCPForDelta.readBits(intArray0, 5, 32);
      assertEquals((-134217728), int0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[0];
      lCPForDelta0.setCompBuffer(intArray0);
      int[] intArray1 = lCPForDelta0.getCompBuffer();
      assertSame(intArray1, intArray0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = LCPForDelta.estimateCompressedSize(intArray0, 6, 6);
      assertEquals(68, int0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = LCPForDelta.decompressBlockByS16(intArray0, intArray0, 0, (-503));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[1];
      int int0 = LCPForDelta.decompressBBitSlotsWithHardCodesWithIntBuffer(intArray0, (IntBuffer) null, 18, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[28];
      int int0 = LCPForDelta.decompressBBitSlotsWithHardCodesWithIntBuffer(intArray0, (IntBuffer) null, 8191, 8191);
      assertEquals(67092481, int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[7];
      IntBuffer intBuffer0 = IntBuffer.allocate(53);
      int int0 = LCPForDelta.decompressBBitSlotsWithHardCodesWithIntBuffer(intArray0, intBuffer0, 375, (-549));
      assertEquals((-205875), int0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int[] intArray0 = new int[0];
      int int0 = LCPForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 0, (-1765));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[0];
      int int0 = LCPForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 3102, 3102);
      assertEquals(9622404, int0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      int[] intArray0 = new int[2];
      int int0 = LCPForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 4, (-2039));
      assertEquals((-8156), int0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      int[] intArray0 = new int[2];
      int int0 = LCPForDelta.decompressBBitSlots(intArray0, intArray0, 0, (-2039));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      int[] intArray0 = new int[2];
      int int0 = LCPForDelta.decompressBBitSlots(intArray0, intArray0, (-2039), 17);
      assertEquals((-34663), int0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.writeBits((int[]) null, 3868, 3868, 1723);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        LCPForDelta.writeBits(intArray0, 131071, 131071, 131071);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4095 out of bounds for length 1
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.readBitsWithBuffer((int[]) null, 2072, 2072);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.readBits((int[]) null, 65535, 28);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      int[] intArray0 = new int[6];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      intBuffer0.compact();
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, intBuffer0, 0, intArray0, intArray0, 0);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, (IntBuffer) null, 3113, intArray0, intArray0, 3113);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      int[] intArray0 = new int[6];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, intBuffer0, (-247), intArray0, intArray0, (-247));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(0) > toIndex(-247)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSize((int[]) null, (int[]) null, 25, (int[]) null, (int[]) null, 25);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, (-1930), intArray0, intArray0, (-1930));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(0) > toIndex(-1930)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlock((int[]) null, (int[]) null, (-1577));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlock(intArray0, intArray0, (-2002));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2002
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      int[] intArray0 = new int[7];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      intBuffer0.compact();
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16WithIntBuffer(intArray0, intBuffer0, 6);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16WithIntBuffer(intArray0, (IntBuffer) null, 23);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      int[] intArray0 = new int[3];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16WithIntBuffer(intArray0, intBuffer0, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16(intArray0, intArray0, 6, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 0
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      IntBuffer intBuffer0 = IntBuffer.allocate(15);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlotsWithHardCodesWithIntBuffer((int[]) null, intBuffer0, (-310), 20);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      int[] intArray0 = new int[15];
      IntBuffer intBuffer0 = IntBuffer.allocate(9);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlotsWithHardCodesWithIntBuffer(intArray0, intBuffer0, 9, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 15
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlotsWithHardCodes(intArray0, intArray0, 2, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore2((int[]) null, 20, 20);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      int[] intArray0 = new int[2];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore2(intArray0, Integer.MIN_VALUE, Integer.MIN_VALUE);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2147483648
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore2(intArray0, 16, 16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore((int[]) null, 2, 2);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      int[] intArray0 = new int[8];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compressOneBlockCore(intArray0, Integer.MIN_VALUE, 3211);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2147483648
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compress((int[]) null, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        LCPForDelta.checkBigNumbers(intArray0, 31, 64);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      int[] intArray0 = new int[1];
      LCPForDelta.writeBits(intArray0, 0, 0, 0);
      assertEquals(1, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16((int[]) null, (int[]) null, 509, 509);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      int[] intArray0 = new int[10];
      int int0 = LCPForDelta.decompressBlockByS16(intArray0, intArray0, (-842), (-842));
      assertEquals(10, int0);
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlots((int[]) null, (int[]) null, 555, 65535);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = LCPForDelta.decompressBBitSlots(intArray0, intArray0, (-317), (-2353));
      assertEquals(745901, int0);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[1] = 2597;
      boolean boolean0 = LCPForDelta.checkBigNumbers(intArray0, 2597, (-2039));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.checkBigNumbers((int[]) null, 9, (-2039));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      boolean boolean0 = LCPForDelta.checkBigNumbers((int[]) null, (-310), (-1253));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 33554431;
      // Undeclared exception!
      try { 
        LCPForDelta.estimateCompressedSize(intArray0, 19, (-3375));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = LCPForDelta.estimateCompressedSize(intArray0, 6, (-498));
      assertEquals((-2956), int0);
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.estimateCompressedSize((int[]) null, 1152, 256);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      int[] intArray0 = new int[6];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int int0 = lCPForDelta0.compressOneBlockCore(intArray0, 2, (-17));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = LCPForDelta.readBitsWithBuffer(intArray0, 8, 8);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16WithIntBufferIntegrated(intArray0, (IntBuffer) null, 8191, intArray0, 8191);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      int[] intArray0 = new int[5];
      LCPForDelta.decompressBlockByS16WithIntBufferIntegrated(intArray0, (IntBuffer) null, (-1567), intArray0, (-1567));
      assertEquals(5, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      int[] intArray0 = new int[66];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      LCPForDelta.decompressBlockByS16WithIntBuffer(intArray0, intBuffer0, 3);
      assertEquals(1, intBuffer0.position());
      assertEquals(65, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test77()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 2;
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int int0 = lCPForDelta0.compress(intArray0, 2);
      assertArrayEquals(new int[] {2, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test78()  throws Throwable  {
      int[] intArray0 = new int[1];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, intBuffer0, 0, intArray0, intArray0, 0);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBlockByS16WithIntBufferIntegrated(intArray0, intBuffer0, 886, intArray0, 886);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test79()  throws Throwable  {
      int[] intArray0 = new int[3];
      int[] intArray1 = new int[7];
      intArray1[0] = (-633);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, intBuffer0, (-90), intArray0, intArray1, (-738));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test80()  throws Throwable  {
      int[] intArray0 = new int[56];
      int[] intArray1 = new int[8];
      intArray1[0] = 34;
      intArray1[3] = 237;
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      LCPForDelta.decompressOneBlockWithSizeWithIntBuffer(intArray0, intBuffer0, 34, intArray0, intArray1, 34);
      LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, 34, intArray0, intArray0, 34);
      assertEquals(56, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test81()  throws Throwable  {
      int[] intArray0 = new int[56];
      LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, 34, intArray0, intArray0, 34);
      assertEquals(56, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test82()  throws Throwable  {
      int[] intArray0 = new int[8];
      LCPForDelta.writeBits(intArray0, (-2641), 6, 262144);
      // Undeclared exception!
      try { 
        LCPForDelta.decompressOneBlockWithSize(intArray0, intArray0, 334, intArray0, intArray0, 334);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test83()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 1;
      LCPForDelta.decompressOneBlock(intArray0, intArray0, 1);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test84()  throws Throwable  {
      int[] intArray0 = new int[56];
      LCPForDelta.decompressOneBlock(intArray0, intArray0, 1);
      assertEquals(56, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test85()  throws Throwable  {
      int[] intArray0 = new int[6];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int int0 = lCPForDelta0.compressOneBlockCore2(intArray0, 1, (-35));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test86()  throws Throwable  {
      int[] intArray0 = new int[55];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int int0 = lCPForDelta0.compressOneBlockCore2(intArray0, 31, 31);
      assertEquals(40, int0);
  }

  @Test(timeout = 4000)
  public void test87()  throws Throwable  {
      int[] intArray0 = new int[5];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      // Undeclared exception!
      try { 
        lCPForDelta0.compress(intArray0, Integer.MIN_VALUE);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2147483648
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test88()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = new int[6];
      intArray0[5] = 536870911;
      // Undeclared exception!
      try { 
        lCPForDelta0.compress(intArray0, 5751);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.LCPForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test89()  throws Throwable  {
      int[] intArray0 = new int[6];
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      lCPForDelta0.setCompBuffer(intArray0);
      int[] intArray1 = lCPForDelta0.getCompBuffer();
      assertEquals(6, intArray1.length);
  }

  @Test(timeout = 4000)
  public void test90()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlotsWithHardCodesWithIntBuffer(intArray0, (IntBuffer) null, 3, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test91()  throws Throwable  {
      LCPForDelta lCPForDelta0 = new LCPForDelta();
      int[] intArray0 = lCPForDelta0.getCompBuffer();
      assertNull(intArray0);
  }

  @Test(timeout = 4000)
  public void test92()  throws Throwable  {
      // Undeclared exception!
      try { 
        LCPForDelta.decompressBBitSlotsWithHardCodes((int[]) null, (int[]) null, 1506, 16);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }
}
