
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
import com.kamikaze.pfordelta.Simple16;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Simple16_ESTest extends Simple16_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[1];
      int[] intArray1 = new int[5];
      intArray1[0] = 624;
      // Undeclared exception!
      try { 
        Simple16.s16Decompress(intArray0, 0, intArray1, 0, 624);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = (-1763);
      // Undeclared exception!
      try { 
        Simple16.s16Decompress(intArray0, Integer.MIN_VALUE, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483648 out of bounds for length 5
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        Simple16.s16Decompress(intArray0, 1, intArray0, 0, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[2] = 1;
      int int0 = Simple16.s16Compress(intArray0, 1, intArray0, 0, 25, 1);
      assertArrayEquals(new int[] {0, 4, 1, 0}, intArray0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = Simple16.s16Compress(intArray0, 0, intArray0, 1, 1, (-471));
      assertEquals(1, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[51];
      int[] intArray1 = new int[2];
      int int0 = Simple16.s16Compress(intArray0, 0, intArray1, 0, 19, 19);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = Simple16.s16Decompress(intArray0, 0, intArray0, 0, (-1784));
      assertEquals((-1784), int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[1];
      int int0 = Simple16.s16Compress(intArray0, 0, intArray0, 0, 0, 0);
      assertEquals(0, int0);
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16.s16Decompress((int[]) null, (-1342177280), (int[]) null, (-1342177280), (-1342177280));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[6];
      int int0 = Simple16.s16Decompress(intArray0, 0, intArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[3] = 622;
      int int0 = Simple16.s16Compress(intArray0, 1, intArray0, 1, 8, (-30441472));
      assertEquals(2, int0);
      assertArrayEquals(new int[] {0, (-536870912), 0, 622}, intArray0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[1];
      Simple16.s16Compress(intArray0, 0, intArray0, 31, (-2424), (-2424));
      assertArrayEquals(new int[] {(-268435456)}, intArray0);
      
      int int0 = Simple16.s16Decompress(intArray0, 0, intArray0, 0, 31);
      assertArrayEquals(new int[] {0}, intArray0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
  }
}
