
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


package me.lemire.integercompression.differential;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.differential.IntegratedBinaryPacking;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntegratedBinaryPacking_ESTest extends IntegratedBinaryPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[69];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[6];
      intArray1[0] = 52;
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray1, intWrapper0, 24, intArray0, intWrapper0, 130, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 96
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[69];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.increment();
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 813, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 97
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[35];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[4];
      intArray1[0] = 701;
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray1, intWrapper0, 1145, intArray0, intWrapper0, 701, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 64
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[5];
      intArray0[0] = 705;
      intArray0[1] = 1073741823;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.uncompress0(intArray0, intWrapper0, 1933, intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[69];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(4104);
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 813, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 96
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[1];
      intArray0[0] = (-598);
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray0, intWrapper0, 351, intArray0, intWrapper0, 351, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(31);
      IntWrapper intWrapper1 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress((int[]) null, intWrapper0, 16, (int[]) null, intWrapper1, 238, intWrapper1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[43];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper((-797));
      int[] intArray1 = new int[7];
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.compress0(intArray0, intWrapper1, 813, intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -797 out of bounds for length 43
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(4194303);
      integratedBinaryPacking0.uncompress0(intArray0, intWrapper0, 511, intArray0, intWrapper1);
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
      assertEquals((short)1, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray0 = new int[7];
      integratedBinaryPacking0.uncompress0(intArray0, intWrapper0, 1, (int[]) null, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[8];
      intArray0[1] = 578;
      IntWrapper intWrapper0 = new IntWrapper(578);
      IntWrapper intWrapper1 = new IntWrapper(578);
      integratedBinaryPacking0.headlessCompress(intArray0, intWrapper0, (-598), intArray0, intWrapper1, intWrapper0);
      int[] intArray1 = new int[8];
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.compress0(intArray1, intWrapper1, 1953, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2529 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[34];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray0, intWrapper0, 118, intArray0, intWrapper0, 118, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 34 out of bounds for length 34
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[15];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(4);
      IntWrapper intWrapper1 = new IntWrapper(131);
      integratedBinaryPacking0.compress0(intArray0, intWrapper1, (-139), intArray0, intWrapper0);
      assertEquals("3", intWrapper1.toString());
      assertEquals(5.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.uncompress0((int[]) null, (IntWrapper) null, 33, (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[4];
      intArray0[0] = 96;
      intArray0[1] = 96;
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.uncompress0(intArray0, intWrapper0, (-1649), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper((-1036));
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.uncompress0(intArray0, intWrapper0, (-1036), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1036 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[35];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(2147483616);
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessUncompress(intArray0, intWrapper0, (-1872), intArray0, intWrapper1, 2468, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(2147483616) > toIndex(-2147483648)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[9];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessCompress(intArray0, (IntWrapper) null, 255, intArray0, (IntWrapper) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[35];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(168);
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.headlessCompress(intArray0, intWrapper0, 62, intArray0, intWrapper1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 168 out of bounds for length 35
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper((-387));
      // Undeclared exception!
      try { 
        integratedBinaryPacking0.compress0((int[]) null, intWrapper0, (-387), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[35];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      integratedBinaryPacking0.headlessUncompress(intArray0, intWrapper0, 64, intArray0, intWrapper0, 0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[35];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(0);
      integratedBinaryPacking0.headlessCompress(intArray0, intWrapper0, 62, intArray0, intWrapper0, intWrapper0);
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(1, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[43];
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper(146);
      integratedBinaryPacking0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, intWrapper0);
      assertEquals(146.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(0);
      integratedBinaryPacking0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper((-487));
      integratedBinaryPacking0.compress0(intArray0, intWrapper0, (-1), intArray0, intWrapper0);
      assertEquals((short) (-487), intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      IntegratedBinaryPacking integratedBinaryPacking0 = new IntegratedBinaryPacking();
      String string0 = integratedBinaryPacking0.toString();
      assertEquals("IntegratedBinaryPacking", string0);
  }
}
