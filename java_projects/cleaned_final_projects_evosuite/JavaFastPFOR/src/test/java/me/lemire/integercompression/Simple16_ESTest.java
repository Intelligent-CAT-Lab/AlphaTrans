
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
import me.lemire.integercompression.Simple16;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Simple16_ESTest extends Simple16_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[5];
      simple16_0.uncompress0(intArray0, intWrapper0, (-1037), intArray0, intWrapper0);
      assertEquals((short)2, intWrapper0.shortValue());
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray1 = new int[6];
      simple16_0.compress0(intArray1, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals(3, intWrapper0.intValue());
      assertEquals(3L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[5];
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(1044);
      int[] intArray1 = new int[5];
      // Undeclared exception!
      try { 
        simple16_0.compress0(intArray0, intWrapper0, 1, intArray1, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        Simple16.uncompress(intArray0, 2, 3811, intArray0, 41, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[5];
      Simple16.uncompress(intArray0, 1, 1, intArray0, 1, 2);
      assertEquals(5, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[5];
      int[] intArray1 = new int[3];
      // Undeclared exception!
      try { 
        Simple16.uncompress(intArray1, 490, 1636, intArray0, (-2699), 1259);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 490 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[8];
      Simple16.uncompress(intArray0, (-9), (-9), intArray0, (-9), (-9));
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper((-2142));
      IntWrapper intWrapper1 = new IntWrapper((-802));
      simple16_0.headlessUncompress(intArray0, intWrapper0, (-1), intArray0, intWrapper1, (-802));
      assertEquals((-2142.0F), intWrapper0.floatValue(), 0.01F);
      assertEquals((-802.0F), intWrapper1.floatValue(), 0.01F);
      assertEquals((-2142), intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(4);
      IntWrapper intWrapper1 = new IntWrapper(4);
      int[] intArray0 = new int[7];
      intArray0[4] = 27;
      intArray0[5] = (-1064);
      // Undeclared exception!
      try { 
        simple16_0.uncompress0(intArray0, intWrapper0, 9, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        Simple16.uncompress(intArray0, 1, 15, intArray0, 1, 1847);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(27);
      int[] intArray0 = new int[7];
      intArray0[1] = 27;
      IntWrapper intWrapper1 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        simple16_0.uncompress0(intArray0, intWrapper1, 1, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[8];
      intArray0[2] = 11;
      // Undeclared exception!
      try { 
        simple16_0.headlessCompress(intArray0, intWrapper0, 544, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(0);
      Simple16 simple16_0 = new Simple16();
      // Undeclared exception!
      try { 
        simple16_0.headlessCompress(intArray0, intWrapper0, 28, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[3];
      IntWrapper intWrapper1 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        simple16_0.compress0(intArray0, intWrapper0, 2092, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(0);
      Simple16 simple16_0 = new Simple16();
      simple16_0.headlessCompress(intArray0, intWrapper0, 2, intArray0, intWrapper0);
      assertEquals(1.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals("1", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(1567);
      IntWrapper intWrapper1 = new IntWrapper(1);
      Simple16 simple16_0 = new Simple16();
      simple16_0.compress0(intArray0, intWrapper0, (-1882), intArray0, intWrapper1);
      assertEquals((short)2, intWrapper1.shortValue());
      assertArrayEquals(new int[] {0, (-1882)}, intArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Simple16.decompressblock((int[]) null, 27, intArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[4];
      int int0 = Simple16.decompressblock(intArray0, (-575), intArray0, 0, (-1082));
      assertEquals((-1082), int0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Simple16.compressblock(intArray0, 0, intArray0, 0, 0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16.uncompress((int[]) null, 14, 14, (int[]) null, 14, 14);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      // Undeclared exception!
      try { 
        simple16_0.headlessUncompress((int[]) null, (IntWrapper) null, 13, (int[]) null, (IntWrapper) null, 13);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(5);
      // Undeclared exception!
      try { 
        simple16_0.headlessCompress((int[]) null, intWrapper0, 5, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16.decompressblock((int[]) null, 2256, (int[]) null, 2256, 2256);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      // Undeclared exception!
      try { 
        Simple16.compressblock((int[]) null, 4443, (int[]) null, 4443, 4443);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[0] = (-1);
      // Undeclared exception!
      try { 
        Simple16.decompressblock(intArray0, (-253), intArray0, 0, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -253 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Simple16.compressblock(intArray0, 0, intArray0, 1, 2);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[2] = 2;
      // Undeclared exception!
      try { 
        Simple16.compressblock(intArray0, 1, intArray0, 2, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(0);
      simple16_0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[5];
      Simple16 simple16_0 = new Simple16();
      IntWrapper intWrapper0 = new IntWrapper(241);
      simple16_0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals("241", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        simple16_0.headlessUncompress(intArray0, intWrapper0, 214, intArray0, intWrapper0, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[5];
      int int0 = Simple16.decompressblock(intArray0, 0, intArray0, 0, 2);
      assertEquals(2, int0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int[] intArray0 = new int[40];
      // Undeclared exception!
      try { 
        Simple16.compressblock(intArray0, 36, intArray0, 36, 36);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 40 out of bounds for length 40
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[12];
      Simple16.compressblock(intArray0, 10, intArray0, (-365), (-365));
      // Undeclared exception!
      try { 
        Simple16.uncompress(intArray0, 10, 9, intArray0, 9, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.Simple16", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Simple16 simple16_0 = new Simple16();
      String string0 = simple16_0.toString();
      assertEquals("Simple16", string0);
  }
}
