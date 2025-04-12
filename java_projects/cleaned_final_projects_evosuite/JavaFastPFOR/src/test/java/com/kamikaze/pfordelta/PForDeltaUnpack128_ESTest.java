
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
import com.kamikaze.pfordelta.PForDeltaUnpack128;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PForDeltaUnpack128_ESTest extends PForDeltaUnpack128_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = (-1901);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray0, 8);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[10];
      int[] intArray1 = new int[9];
      intArray1[1] = (-1050);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray1, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = (-1473);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray0, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[11];
      int[] intArray1 = new int[9];
      intArray1[1] = (-1628);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray1, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[7];
      intArray1[1] = (-644);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray1, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = (-1581);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray0, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = (-3053);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[143];
      int[] intArray1 = new int[7];
      intArray1[1] = 2;
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray1, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = (-753);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack(intArray0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        PForDeltaUnpack128.unpack((int[]) null, (int[]) null, 11);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[157];
      PForDeltaUnpack128.unpack(intArray0, intArray0, (-1901));
      assertEquals(157, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 28);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[10];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 27);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[8];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 26);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[0];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 25);
      assertEquals(0, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[11];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 24);
      assertEquals(11, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[1];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 23);
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      PForDeltaUnpack128.unpack((int[]) null, (int[]) null, 22);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[8];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 21);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 20);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[8];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 19);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[11];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 18);
      assertEquals(11, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      PForDeltaUnpack128.unpack((int[]) null, (int[]) null, 17);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 16);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[11];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 15);
      assertEquals(11, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[4];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 14);
      assertEquals(4, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 13);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int[] intArray0 = new int[152];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 12);
      assertEquals(152, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 11);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[133];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 10);
      assertEquals(133, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 9);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int[] intArray0 = new int[157];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 8);
      assertEquals(157, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[139];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 7);
      assertEquals(139, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 6);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 4);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 3);
      assertEquals(143, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      int[] intArray0 = new int[162];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 2);
      assertEquals(162, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int[] intArray0 = new int[152];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 1);
      assertEquals(152, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      int[] intArray0 = new int[157];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 5);
      assertEquals(157, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      PForDeltaUnpack128 pForDeltaUnpack128_0 = new PForDeltaUnpack128();
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      int[] intArray0 = new int[143];
      PForDeltaUnpack128.unpack(intArray0, intArray0, 0);
      assertEquals(143, intArray0.length);
  }
}
