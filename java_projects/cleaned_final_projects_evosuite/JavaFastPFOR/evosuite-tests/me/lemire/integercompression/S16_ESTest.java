
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
import me.lemire.integercompression.S16;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class S16_ESTest extends S16_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[10];
      int[] intArray1 = new int[2];
      intArray1[1] = (-3064);
      // Undeclared exception!
      try { 
        S16.uncompress(intArray1, 1, 864, intArray0, 1, 2280);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[7];
      // Undeclared exception!
      try { 
        S16.uncompress(intArray0, 5, 929, intArray1, 10, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[2];
      S16.uncompress(intArray0, (-14), (-14), intArray0, (-14), (-14));
      assertArrayEquals(new int[] {0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[3] = 2249;
      // Undeclared exception!
      try { 
        S16.uncompress(intArray0, 3, 1560, intArray0, 3, 920);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[17];
      intArray0[0] = (-1);
      // Undeclared exception!
      try { 
        S16.uncompress(intArray0, 0, 5, intArray0, (-1), 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 17
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 14;
      // Undeclared exception!
      try { 
        S16.estimatecompress(intArray0, 0, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[4] = 5;
      // Undeclared exception!
      try { 
        S16.compress(intArray0, 0, 14, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 2222;
      // Undeclared exception!
      try { 
        S16.estimatecompress(intArray0, 0, 94);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = S16.estimatecompress(intArray0, 5, 1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[3];
      int int0 = S16.estimatecompress(intArray0, (-1669), (-1669));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = 1122;
      // Undeclared exception!
      try { 
        S16.compress(intArray0, 0, 1122, intArray0, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[2];
      int int0 = S16.compress(intArray1, 0, 2, intArray0, 0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = S16.decompressblock(intArray0, 0, intArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = S16.decompressblock(intArray0, 22, intArray0, 3, (-975));
      assertEquals((-975), int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = S16.compressblock(intArray0, 1, intArray0, 2481, 0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = S16.compress(intArray0, (-705), (-705), intArray0, 10);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      // Undeclared exception!
      try { 
        S16.uncompress((int[]) null, 1, 1, (int[]) null, 1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        S16.decompressblock((int[]) null, 3, (int[]) null, 3, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[36];
      // Undeclared exception!
      try { 
        S16.decompressblock(intArray0, 2622, intArray0, 2622, 2622);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2622 out of bounds for length 36
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        S16.compress((int[]) null, 2674, 2674, (int[]) null, 2674);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[8];
      int[] intArray1 = new int[9];
      intArray1[0] = (-93);
      int int0 = S16.decompressblock(intArray0, 0, intArray1, 0, 5);
      assertEquals(1, int0);
      assertArrayEquals(new int[] {268435363, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = S16.compressblock(intArray0, 1, intArray0, 1, 1);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[11];
      int[] intArray1 = new int[7];
      intArray1[0] = 5;
      // Undeclared exception!
      try { 
        S16.compressblock(intArray0, 0, intArray1, 0, 107);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[8];
      int int0 = S16.compressblock(intArray0, 5, intArray0, 5, (-93));
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, (-268435456), 0, 0}, intArray0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      // Undeclared exception!
      try { 
        S16.compressblock((int[]) null, 1455, (int[]) null, 1455, 1455);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[11];
      S16.uncompress(intArray0, 5, 5, intArray0, 5, 5);
      assertEquals(11, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[22];
      intArray0[2] = 1;
      int int0 = S16.compress(intArray0, 0, 9, intArray0, 1);
      assertEquals(1, int0);
      
      int int1 = S16.estimatecompress(intArray0, 1, 1);
      assertEquals(1, int1);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      // Undeclared exception!
      try { 
        S16.estimatecompress((int[]) null, 481, 481);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[22];
      intArray0[2] = 1;
      int int0 = S16.compress(intArray0, 0, 9, intArray0, 1);
      assertEquals(1, int0);
      
      int int1 = S16.compress(intArray0, 1, 2, intArray0, 19);
      assertEquals(1, int1);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        S16.estimatecompress(intArray0, Integer.MIN_VALUE, Integer.MIN_VALUE);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        S16.compress(intArray0, Integer.MIN_VALUE, Integer.MIN_VALUE, intArray0, 0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      S16 s16_0 = new S16();
  }
}
