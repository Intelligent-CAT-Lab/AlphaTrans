
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
import java.nio.ByteBuffer;
import me.lemire.integercompression.FastPFOR;
import me.lemire.integercompression.IntWrapper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FastPFOR_ESTest extends FastPFOR_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[258];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        fastPFOR0.compress0(intArray0, intWrapper0, (-3805), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 258 out of bounds for length 258
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[12];
      intArray0[5] = 65536;
      FastPFOR fastPFOR0 = new FastPFOR(4);
      // Undeclared exception!
      try { 
        fastPFOR0.headlessUncompress(intArray0, intWrapper0, 65536, intArray0, intWrapper0, 256);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(4);
      // Undeclared exception!
      try { 
        fastPFOR0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, (-2029));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(0);
      ByteBuffer byteBuffer0 = fastPFOR0.makeBuffer(65536);
      assertEquals(65536, byteBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(0);
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(2);
      fastPFOR0.uncompress0(intArray0, intWrapper0, (-2777), intArray0, intWrapper0);
      assertEquals(3L, intWrapper0.longValue());
      assertEquals(3.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(2755);
      IntWrapper intWrapper0 = new IntWrapper(2755);
      // Undeclared exception!
      try { 
        fastPFOR0.uncompress0((int[]) null, intWrapper0, 2755, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      // Undeclared exception!
      try { 
        fastPFOR0.makeBuffer((-710));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-710 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[196];
      // Undeclared exception!
      try { 
        fastPFOR0.headlessUncompress(intArray0, (IntWrapper) null, 65536, intArray0, (IntWrapper) null, 65536);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[6];
      intArray0[0] = 1;
      intArray0[1] = 65536;
      // Undeclared exception!
      try { 
        fastPFOR0.headlessUncompress(intArray0, intWrapper0, 256, intArray0, intWrapper0, 256);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(151);
      IntWrapper intWrapper0 = new IntWrapper(256);
      // Undeclared exception!
      try { 
        fastPFOR0.headlessCompress((int[]) null, intWrapper0, (-1645), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[68];
      // Undeclared exception!
      try { 
        fastPFOR0.compress0(intArray0, (IntWrapper) null, 65536, intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[258];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        fastPFOR0.compress0(intArray0, intWrapper0, 65536, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 258 out of bounds for length 258
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      FastPFOR fastPFOR0 = null;
      try {
        fastPFOR0 = new FastPFOR(Integer.MIN_VALUE);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -268435456
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      FastPFOR fastPFOR0 = null;
      try {
        fastPFOR0 = new FastPFOR((-1621));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-1639 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(0);
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper((-538));
      fastPFOR0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((-538L), intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      FastPFOR fastPFOR0 = new FastPFOR(1048);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(4);
      // Undeclared exception!
      try { 
        fastPFOR0.headlessCompress(intArray0, intWrapper0, 65536, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(256);
      fastPFOR0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals("256", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(256);
      // Undeclared exception!
      try { 
        fastPFOR0.uncompress0(intArray0, intWrapper0, 1863, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 256 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(32);
      fastPFOR0.compress0(intArray0, intWrapper0, 32, intArray0, intWrapper0);
      assertEquals("32", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[4];
      intArray0[1] = 256;
      intArray0[2] = 65536;
      // Undeclared exception!
      try { 
        fastPFOR0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 65536);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 33
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[10];
      intArray0[1] = 65536;
      // Undeclared exception!
      try { 
        fastPFOR0.headlessUncompress(intArray0, intWrapper0, 65536, intArray0, intWrapper0, 65536);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 33
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[258];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      fastPFOR0.headlessUncompress(intArray0, intWrapper0, 65536, intArray0, intWrapper0, 256);
      assertEquals((short)256, intWrapper0.shortValue());
      assertEquals(256, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[258];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      fastPFOR0.compress0(intArray0, intWrapper0, 256, intArray0, intWrapper1);
      IntWrapper intWrapper2 = IntWrapper.IntWrapper1();
      fastPFOR0.headlessUncompress(intArray0, intWrapper1, 65536, intArray0, intWrapper2, 256);
      assertEquals(9, intWrapper1.intValue());
      assertEquals(9.0, intWrapper1.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      int[] intArray0 = new int[258];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      fastPFOR0.compress0(intArray0, intWrapper0, 256, intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals(257, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      String string0 = fastPFOR0.toString();
      assertEquals("FastPFOR", string0);
  }
}
