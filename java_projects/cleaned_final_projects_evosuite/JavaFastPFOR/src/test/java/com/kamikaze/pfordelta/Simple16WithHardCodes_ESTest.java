
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
import com.kamikaze.pfordelta.Simple16WithHardCodes;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Simple16WithHardCodes_ESTest extends Simple16WithHardCodes_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[15];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated2(intArray0, 1, 1021, 1, intArray0, 1021);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 15
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 0, (-2220), 0, (-1714), intArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[10];
      int[] intArray1 = new int[5];
      intArray1[0] = (-12);
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray1, 8, (-3137), 0, 38, intArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 0, (-188), 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegratedBackup(intArray0, 0, 6, 735, intArray0, 2826);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegratedBackup(intArray0, 27, (-1), 1, intArray0, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 27 out of bounds for length 4
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated(intArray0, 0, 1321, 2546, intArray0, 1321);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[13];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated(intArray0, 5, (-805306368), (-204), intArray0, (-1577));
      assertEquals(3, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferBackup(intArray0, (-1597), (-1), 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1597 out of bounds for length 3
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[4];
      Simple16WithHardCodes.s16Compress(intArray0, 0, intArray0, 0, 1, 5400, 0, (int[]) null);
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16Decompress((int[]) null, 4421, intArray0, 0, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[3] = 626;
      int int0 = Simple16WithHardCodes.s16CompressBackup(intArray0, 0, intArray0, 0, 1019, 667, 0, intArray0);
      assertArrayEquals(new int[] {(-805306368), 0, 0, 626}, intArray0);
      assertEquals(3, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[14];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferBackup(intArray0, 6, 6, 2);
      assertEquals(2, int0);
      
      int int1 = Simple16WithHardCodes.s16CompressBackup(intArray0, 2, intArray0, 6, 6, 1, (-4145), intArray0);
      assertEquals(6, int1);
      
      int int2 = Simple16WithHardCodes.s16Compress(intArray0, 6, intArray0, 0, 27, 2, 27, intArray0);
      assertEquals(6, int2);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated2(intArray0, 0, (-3190), 8, intArray0, 511);
      assertEquals(1, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 0, 2113, 14, (-6), intArray0);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[19];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 12, 12, 12, (-1114), intArray0);
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 1, 204, 11, 204, intArray0);
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 1, 10, 10, (-150), intArray0);
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 1, 1, 9, 9, intArray0);
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[10];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 1, 1, 7, (-1392), intArray0);
      assertEquals(7, int0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 0, (-1223), 6, 26, intArray0);
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[14];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 0, 13, 5, 157, intArray0);
      assertEquals(9, int0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[22];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 1, 1, 1, (-4), intArray0);
      assertEquals(21, int0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferWithHardCodes(intArray0, 268435229, (-227), (-227));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 268435229 out of bounds for length 2
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 0, 32, 13);
      assertEquals(3, int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[19];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 4, 26, 4);
      assertEquals(14, int0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferIntegratedBackup(intArray0, 0, 0, 0, intArray0, (-1));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferIntegratedBackup(intArray0, (-3), (-3), (-3), intArray0, (-3));
      assertEquals((-3), int0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int[] intArray0 = new int[31];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated2(intArray0, 1, 1, 1, intArray0, 1);
      assertEquals(28, int0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferBackup(intArray0, 25, 2043, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferBackup(intArray0, 2, (-2636), (-2636));
      assertEquals((-2636), int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16WithHardCodes.s16Decompress(intArray0, 0, intArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16WithHardCodes.s16Decompress(intArray0, 0, intArray0, 0, (-1));
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16WithHardCodes.s16CompressBackup(intArray0, 0, intArray0, 0, 0, 0, 0, intArray0);
      assertArrayEquals(new int[] {0, 0, 0, 0}, intArray0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferWithHardCodes((int[]) null, 5, 5, 5);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegratedBackup((int[]) null, 4, 4, 4, (int[]) null, 4);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated2((int[]) null, 5, 5, 5, (int[]) null, 5);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferIntegrated((int[]) null, 5, 5, 5, (int[]) null, 5);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int[] intArray0 = new int[15];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferBackup(intArray0, 0, 0, 1623);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 15
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBuffer((int[]) null, 5, 5, 5);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBuffer(intArray0, (-1337), 8, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1337 out of bounds for length 16
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes((int[]) null, 9, 9, 9);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16Decompress(intArray0, 2739, intArray0, 4, 2739);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2739 out of bounds for length 13
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16CompressBackup((int[]) null, 5, (int[]) null, 5, 5, 5, 5, (int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16CompressBackup(intArray0, 2, intArray0, 28, 28, 37, 28, intArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 28 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16Compress((int[]) null, 5, (int[]) null, 5, 5, 5, 5, (int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16Compress(intArray0, 0, intArray0, (-2893), 206, 4, 4, intArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2893 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      int[] intArray0 = new int[20];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 50, 2452, 32, 50, intArray0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      int[] intArray0 = new int[22];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 13, 13, 13, (-1367), intArray0);
      assertEquals(3, int0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated((int[]) null, 12, 12, 12, 12, (int[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      int[] intArray0 = new int[20];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 8, 8, 8, 8, intArray0);
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      int[] intArray0 = new int[18];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 4, 4, 4, 4, intArray0);
      assertEquals(14, int0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      int[] intArray0 = new int[24];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 3, 1, 3, 1236, intArray0);
      assertEquals(21, int0);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      int[] intArray0 = new int[27];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodesIntegrated(intArray0, 2, 2, 2, (-1), intArray0);
      assertEquals(21, int0);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes((int[]) null, 3753, 2, 1780);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 0, 0, 14);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 0, 0, 12);
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      int[] intArray0 = new int[19];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 11, 17, 11);
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 1, 1, 10);
      assertEquals(5, int0);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      int[] intArray0 = new int[15];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 9, 9, 9);
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      int[] intArray0 = new int[16];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 4, 4, 8);
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      int[] intArray0 = new int[19];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 3, 560, 7);
      assertEquals(7, int0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      int[] intArray0 = new int[17];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 6, 6, 6);
      assertEquals(8, int0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      int[] intArray0 = new int[14];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 5, 5, 5);
      assertEquals(9, int0);
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      int[] intArray0 = new int[25];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 3, 3, 3);
      assertEquals(21, int0);
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      int[] intArray0 = new int[22];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 1, (-83), 2);
      assertEquals(21, int0);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      int[] intArray0 = new int[22];
      int int0 = Simple16WithHardCodes.s16DecompressOneNumberWithHardCodes(intArray0, 1, (-1), 1);
      assertEquals(21, int0);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      int[] intArray0 = new int[40];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferWithHardCodes(intArray0, 4, 4, 1);
      assertEquals(28, int0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      int[] intArray0 = new int[16];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferIntegratedBackup(intArray0, 4, 4, 4, intArray0, 4);
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      int[] intArray0 = new int[91];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBuffer(intArray0, 53, Integer.MIN_VALUE, 53);
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      int[] intArray0 = new int[7];
      int int0 = Simple16WithHardCodes.s16DecompressWithIntBufferBackup(intArray0, 1, (-536870912), 20);
      assertEquals(2, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16WithHardCodes.s16DecompressWithIntBufferBackup((int[]) null, 5, 5, 5);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16WithHardCodes", e);
      }
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      int[] intArray0 = new int[23];
      int[] intArray1 = new int[5];
      intArray1[3] = 2;
      int int0 = Simple16WithHardCodes.s16CompressBackup(intArray0, 2, intArray1, 2, 2, 1533, 2429, intArray1);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = Simple16WithHardCodes.s16CompressBackup(intArray0, 2, intArray0, (-4749), (-4749), (-4749), (-4749), intArray0);
      assertArrayEquals(new int[] {0, 0, (-268435456), 0, 0, 0, 0, 0}, intArray0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      int[] intArray0 = new int[20];
      int int0 = Simple16WithHardCodes.s16Compress(intArray0, 8, intArray0, 8, 8, 8, 8, intArray0);
      assertEquals(6, int0);
      
      int int1 = Simple16WithHardCodes.s16Decompress(intArray0, 6, intArray0, 8, 8);
      assertEquals(6, int1);
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = Simple16WithHardCodes.s16Compress(intArray0, 0, intArray0, 0, 0, 0, 0, intArray0);
      assertEquals((-1), int0);
      assertArrayEquals(new int[] {(-268435456), 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      Simple16WithHardCodes simple16WithHardCodes0 = new Simple16WithHardCodes();
  }
}
