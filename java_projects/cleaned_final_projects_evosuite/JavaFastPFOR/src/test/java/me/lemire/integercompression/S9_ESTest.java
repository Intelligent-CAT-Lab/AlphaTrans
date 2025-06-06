
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
import me.lemire.integercompression.S9;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class S9_ESTest extends S9_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[11];
      intArray0[4] = 2;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, 2, intArray0, 7, 1954);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[11];
      intArray0[4] = 1;
      S9.compress(intArray0, 1, 7, intArray0, 1);
      S9.uncompress(intArray0, 1, 1, intArray0, 1, 7);
      assertEquals(11, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[0] = 395;
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 0, 1385, intArray0, 0, 395);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 6, 6, intArray0, Integer.MIN_VALUE, (-3481));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 0, (-1364), intArray0, (-3636), 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3636 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[12];
      S9.uncompress(intArray0, (-3155), 968, intArray0, 4442, (-3140));
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[12];
      int int0 = S9.compress(intArray0, 3, (-1038), intArray0, 4442);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[4] = 268435456;
      // Undeclared exception!
      try { 
        S9.estimatecompress(intArray0, 3, 3);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[9];
      int int0 = S9.estimatecompress(intArray0, (-1071), (-2465));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[3];
      int int0 = S9.estimatecompress(intArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        S9.uncompress((int[]) null, 815, 815, (int[]) null, 815, 815);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        S9.estimatecompress((int[]) null, 9, 9);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        S9.estimatecompress(intArray0, 7, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        S9.compress((int[]) null, 1, 7, intArray0, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        S9.compress(intArray0, 7, 9, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[4] = (-1002);
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, (-1002), intArray0, 3, 3);
      assertArrayEquals(new int[] {0, 0, 1879048192, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[5] = (-1039);
      S9.compress(intArray0, 2, 4, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, (-1039), intArray0, (-3456), 8);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3456 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[16];
      intArray0[4] = 53;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, 7, intArray0, 6, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[14];
      intArray0[4] = 31;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, 31, intArray0, (-1155), 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1155 out of bounds for length 14
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[4] = 10;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, 1269, intArray0, 28, 2587);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 28 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[4] = 5;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, 5, intArray0, 1, 1);
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[4] = 2;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, 2, intArray0, 2, 7);
      assertArrayEquals(new int[] {0, 0, 0, 0, 2, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[0] = (-6276);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 0, (-6276), intArray0, (-6276), 23);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[4] = 4442;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, 2, intArray0, 2, 1);
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[5] = (-1039);
      S9.compress(intArray0, 2, 4, intArray0, 2);
      assertArrayEquals(new int[] {0, 0, 1610612736, (-1039), 0, (-1039), 0, 0}, intArray0);
      
      S9.uncompress(intArray0, 2, (-1039), intArray0, 2, 2);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, (-1039), 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[14];
      intArray0[4] = 20;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, 20, intArray0, 2, 2);
      assertEquals(14, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[4] = 10;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, 10, intArray0, 1, 1);
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[4] = 5;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, 2, intArray0, 1772, 25);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1772 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[5] = 2;
      S9.compress(intArray0, 2, 4, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.uncompress(intArray0, 2, 0, intArray0, 1, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[4] = 2;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.compress(intArray0, 2, 7, intArray0, 2);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[16];
      intArray0[4] = 53;
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, 53, intArray0, 2, 2);
      assertEquals(16, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int[] intArray0 = new int[12];
      intArray0[3] = (-4155);
      S9.compress(intArray0, 2, 7, intArray0, 2);
      S9.uncompress(intArray0, 2, (-4155), intArray0, 3, 3);
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[13];
      intArray0[4] = 2;
      S9.compress(intArray0, 2, 11, intArray0, 2);
      // Undeclared exception!
      try { 
        S9.estimatecompress(intArray0, 2, 11);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      int[] intArray0 = new int[15];
      intArray0[6] = (-1926);
      int int0 = S9.estimatecompress(intArray0, 4, 4);
      assertEquals(3, int0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      S9 s9_0 = new S9();
  }
}
