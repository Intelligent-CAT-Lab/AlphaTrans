
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
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.Simple9;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Simple9_ESTest extends Simple9_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[6];
      simple9_0.uncompress0(intArray1, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals("1", intWrapper0.toString());
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntWrapper intWrapper1 = new IntWrapper((-1642));
      simple9_0.uncompress0(intArray0, intWrapper0, (-1), intArray0, intWrapper1);
      assertEquals("3", intWrapper0.toString());
      assertEquals((-1642L), intWrapper1.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(27);
      int[] intArray1 = new int[8];
      // Undeclared exception!
      try { 
        simple9_0.uncompress0(intArray1, intWrapper0, 30, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 27 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[12];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[6];
      // Undeclared exception!
      try { 
        simple9_0.compress0(intArray0, intWrapper0, 937, intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[16];
      intArray0[0] = 3369;
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-3897), intArray0, intWrapper0, 3342);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      simple9_0.headlessUncompress(intArray0, intWrapper0, (-630), intArray0, intWrapper0, 0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[4];
      intArray0[0] = 1638;
      intArray0[1] = 268431544;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        simple9_0.uncompress0(intArray0, intWrapper0, 720, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(1);
      simple9_0.uncompress0(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      intArray0[3] = 1;
      IntWrapper intWrapper1 = new IntWrapper(1);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 1042, intArray0, intWrapper0, 1082);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 1, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper1, (-1079), intArray0, intWrapper1, 2157);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      int[] intArray1 = new int[6];
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-1079), intArray1, intWrapper0, 2157);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[11];
      IntWrapper intWrapper0 = new IntWrapper(2);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 6, intArray0, intWrapper0, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[3];
      int[] intArray1 = new int[6];
      intArray1[0] = 3657;
      // Undeclared exception!
      try { 
        simple9_0.headlessCompress(intArray1, intWrapper0, 2663, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[4];
      intArray0[0] = (-1495);
      intArray0[3] = 3657;
      // Undeclared exception!
      try { 
        simple9_0.headlessCompress(intArray0, intWrapper0, 3657, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[3] = 3671;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      Simple9 simple9_0 = new Simple9();
      // Undeclared exception!
      try { 
        simple9_0.compress0(intArray0, intWrapper0, 3671, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      Simple9 simple9_0 = new Simple9();
      // Undeclared exception!
      try { 
        simple9_0.compress0(intArray0, intWrapper0, 28, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 30;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      IntWrapper intWrapper2 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-1379), intArray0, intWrapper2, 1381);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[18];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 2;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 2, intArray0, intWrapper1, Integer.MIN_VALUE);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[39];
      Simple9 simple9_0 = new Simple9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-1), intArray0, intWrapper0, 1317);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 39 out of bounds for length 39
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[2];
      intArray0[0] = 9;
      intArray0[1] = (-1);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        simple9_0.uncompress0(intArray0, intWrapper0, (-1), intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      // Undeclared exception!
      try { 
        simple9_0.uncompress0((int[]) null, (IntWrapper) null, 54, (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[10];
      Simple9 simple9_0 = new Simple9();
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, (IntWrapper) null, 128, intArray0, (IntWrapper) null, 128);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      // Undeclared exception!
      try { 
        simple9_0.headlessCompress((int[]) null, (IntWrapper) null, 3, (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      IntWrapper intWrapper0 = new IntWrapper(137);
      // Undeclared exception!
      try { 
        simple9_0.compress0((int[]) null, intWrapper0, 137, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 30;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-1), intArray0, intWrapper1, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(0);
      intArray0[1] = 2;
      IntWrapper intWrapper1 = new IntWrapper(0);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessCompress(intArray0, intWrapper0, 2, intArray0, intWrapper1);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[4];
      intArray0[3] = 1381;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        simple9_0.headlessCompress(intArray0, intWrapper0, 20, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      intArray0[1] = 2;
      IntWrapper intWrapper0 = new IntWrapper(0);
      simple9_0.compress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        simple9_0.headlessCompress(intArray0, intWrapper1, 30, intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.headlessCompress(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      assertEquals(3L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals("2", intWrapper0.toString());
      assertEquals((short)2, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[39];
      Simple9 simple9_0 = new Simple9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      simple9_0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      intArray0[3] = (-1379);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, (-1379), intArray0, intWrapper0, 1);
      assertArrayEquals(new int[] {0, 0, 2, 6144, 2, 0, 0, 0}, intArray0);
      assertEquals(4, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(2);
      intArray0[3] = (-1383);
      IntWrapper intWrapper1 = new IntWrapper(0);
      intWrapper1.increment();
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 2);
      assertEquals(3.0F, intWrapper0.floatValue(), 0.01F);
      assertArrayEquals(new int[] {0, 2, 256, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(1);
      simple9_0.uncompress0(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      intArray0[3] = 48;
      IntWrapper intWrapper1 = new IntWrapper(1);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 1, intArray0, intWrapper0, 1);
      assertArrayEquals(new int[] {0, 2, 0, 48, 0, 0, 0}, intArray0);
      assertEquals(3L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      intArray0[3] = (-1399);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 905969664, intArray0, intWrapper1, 2);
      assertEquals(4L, intWrapper0.longValue());
      assertArrayEquals(new int[] {0, 0, 2, 905969664, 6, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[11];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 6;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 245, intArray0, intWrapper1, 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[23];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper0);
      simple9_0.headlessUncompress(intArray0, intWrapper1, 2, intArray0, intWrapper1, 14);
      assertEquals((byte)5, intWrapper1.byteValue());
      assertEquals(5.0F, intWrapper1.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      int[] intArray0 = new int[10];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      Simple9 simple9_0 = new Simple9();
      simple9_0.compress0(intArray0, intWrapper0, (-26), intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-26), intArray0, intWrapper1, 9);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, (-2147467251), intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 2, intArray0, intWrapper0, 2);
      assertEquals((short)4, intWrapper0.shortValue());
      assertEquals(4.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      intArray0[3] = (-1379);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 1979711488, intArray0, intWrapper1, 2);
      assertEquals((byte)4, intWrapper0.byteValue());
      assertEquals((short)6, intWrapper1.shortValue());
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(2);
      intArray0[3] = (-1383);
      IntWrapper intWrapper1 = new IntWrapper(1);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 54;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 4, intArray0, intWrapper1, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 30;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 2, intArray0, intWrapper1, 2);
      assertEquals((short)6, intWrapper1.shortValue());
      assertArrayEquals(new int[] {0, 0, 2, 1105199104, 30, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[10];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      intArray0[3] = (-1395);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 723, intArray0, intWrapper0, 25);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[11];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 6;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 641728512, intArray0, intWrapper1, 2);
      assertEquals(4.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals((short)6, intWrapper1.shortValue());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[11];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      simple9_0.headlessUncompress(intArray0, intWrapper0, 641728512, intArray0, intWrapper1, 2);
      assertEquals(4.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(4.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper0, (-2147467251), intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 2, intArray0, intWrapper0, 1528);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      intArray0[3] = (-1383);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-786), intArray0, intWrapper0, 6144);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(2);
      intArray0[2] = (-1399);
      intArray0[3] = (-1399);
      IntWrapper intWrapper1 = new IntWrapper(0);
      intWrapper1.increment();
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 256, intArray0, intWrapper1, 1811939328);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[10];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = 70;
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 70);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[12];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[4] = 2;
      intArray0[3] = (-1396);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-2367), intArray0, intWrapper1, 870);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[14];
      IntWrapper intWrapper0 = new IntWrapper(2);
      intArray0[1] = 6;
      IntWrapper intWrapper1 = new IntWrapper(0);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      IntWrapper intWrapper2 = new IntWrapper(0);
      simple9_0.compress0(intArray0, intWrapper0, (-1), intArray0, intWrapper2);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper2, 3, intArray0, intWrapper1, 637534208);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 14 out of bounds for length 14
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      intArray0[3] = (-1383);
      // Undeclared exception!
      try { 
        simple9_0.headlessUncompress(intArray0, intWrapper0, (-786), intArray0, intWrapper0, 6144);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen: limited to 28-bit integers
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      int[] intArray0 = new int[13];
      IntWrapper intWrapper0 = new IntWrapper(2);
      simple9_0.uncompress0(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(2);
      simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        simple9_0.compress0(intArray0, intWrapper1, 2, intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // Too big a number
         //
         verifyException("me.lemire.integercompression.Simple9", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      Simple9 simple9_0 = new Simple9();
      String string0 = simple9_0.toString();
      assertEquals("Simple9", string0);
  }
}
