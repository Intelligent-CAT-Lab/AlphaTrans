
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


package me.lemire.longcompression;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.nio.ByteBuffer;
import me.lemire.integercompression.IntWrapper;
import me.lemire.longcompression.LongVariableByte;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongVariableByte_ESTest extends LongVariableByte_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      longArray0[0] = (-2101L);
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray1 = new long[1];
      // Undeclared exception!
      try { 
        longVariableByte0.headlessUncompress(longArray0, intWrapper0, 1063, longArray1, intWrapper0, 101);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[3];
      longArray0[2] = (-1023L);
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.add(1);
      longVariableByte0.headlessUncompress(longArray0, intWrapper0, (-2054114792), longArray0, intWrapper0, 1);
      assertEquals(3, intWrapper0.intValue());
      assertArrayEquals(new long[] {0L, 72057594037927936L, (-1023L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[19];
      IntWrapper intWrapper0 = new IntWrapper(1617);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      longVariableByte0.headlessUncompress(longArray0, intWrapper0, (-1121), longArray0, intWrapper1, 0);
      assertEquals((byte)0, intWrapper1.byteValue());
      assertEquals((byte)81, intWrapper0.byteValue());
      assertEquals(1617.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      LongVariableByte longVariableByte0 = new LongVariableByte();
      byte[] byteArray0 = new byte[5];
      byteArray0[2] = (byte)64;
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)14, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[18];
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte)6;
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)1, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[3];
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[7];
      IntWrapper intWrapper1 = new IntWrapper(0);
      intWrapper1.increment();
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, 16, longArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[18];
      byte[] byteArray0 = new byte[3];
      byteArray0[0] = (byte)1;
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)1, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      longVariableByte0.uncompress1((byte[]) null, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray1 = new long[9];
      longArray1[0] = (-2101L);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(longArray1, intWrapper0, 1625, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[3];
      longArray0[2] = (-1023L);
      IntWrapper intWrapper0 = new IntWrapper(0);
      intWrapper0.increment();
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(longArray0, intWrapper0, 56, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[4];
      IntWrapper intWrapper0 = new IntWrapper((-2856));
      longVariableByte0.uncompress1(longArray0, intWrapper0, (-2856), longArray0, intWrapper0);
      assertEquals((-5712L), intWrapper0.longValue());
      assertEquals((-5712.0), intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray0 = new long[7];
      longArray0[1] = (long) 137;
      longArray0[2] = 2097141L;
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 42, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[6];
      longArray0[0] = 3253L;
      longArray0[1] = 3253L;
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 2629, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      long[] longArray0 = new long[8];
      longArray0[0] = 16384L;
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 21, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray0 = new long[3];
      longVariableByte0.headlessCompress(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      intWrapper0.set(1);
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, (byte)52, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[18];
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[1];
      longVariableByte0.compress1(longArray0, intWrapper0, 1, byteArray0, intWrapper0);
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
      assertEquals((short)2, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[4];
      IntWrapper intWrapper0 = new IntWrapper(8);
      byte[] byteArray0 = new byte[1];
      IntWrapper intWrapper1 = new IntWrapper(456);
      longVariableByte0.compress1(longArray0, intWrapper1, (-799), byteArray0, intWrapper0);
      assertEquals((byte) (-87), intWrapper1.byteValue());
      assertEquals((short) (-343), intWrapper1.shortValue());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[19];
      IntWrapper intWrapper0 = new IntWrapper(1617);
      long[] longArray1 = new long[6];
      longArray1[4] = 128L;
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        longVariableByte0.compress0(longArray1, intWrapper1, 35, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      ByteBuffer byteBuffer0 = longVariableByte0.makeBuffer(63);
      assertEquals(63, byteBuffer0.capacity());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      longArray0[0] = (-1L);
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[23];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 1113, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1((long[]) null, intWrapper0, 2002, (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1((byte[]) null, intWrapper0, 2846, longArray0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      // Undeclared exception!
      try { 
        longVariableByte0.makeBuffer((-1));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-1 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longVariableByte0.headlessUncompress((long[]) null, intWrapper0, 1, (long[]) null, intWrapper0, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-2146320959));
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress((long[]) null, intWrapper0, (-2146320959), (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      longArray0[1] = (-1556L);
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 1, longArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      long[] longArray0 = new long[11];
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, (-25), longArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-400 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 1, (byte[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[3];
      // Undeclared exception!
      try { 
        longVariableByte0.compress0(longArray0, (IntWrapper) null, 1074, longArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[2];
      longArray0[1] = (-1L);
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longVariableByte0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-2743));
      // Undeclared exception!
      try { 
        longVariableByte0.compress0((long[]) null, intWrapper0, (-2743), (long[]) null, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-43888 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      longArray0[0] = 4398046511104L;
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 1873, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      longArray0[4] = 562949953421312L;
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 1873, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      longArray0[5] = 4398046511085L;
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 1873, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[8];
      longArray0[2] = 34359738355L;
      IntWrapper intWrapper0 = new IntWrapper((-1758));
      intWrapper0.set(0);
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 1773, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[9];
      longArray0[7] = 2097152L;
      IntWrapper intWrapper0 = new IntWrapper(7);
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 7, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = new IntWrapper(2);
      longVariableByte0.compress0(longArray0, intWrapper0, 2, longArray0, intWrapper0);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper1, 1672, longArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[8];
      longArray0[1] = 4146L;
      IntWrapper intWrapper0 = new IntWrapper((-1758));
      intWrapper0.set(0);
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 1773, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = new IntWrapper((-4665));
      longVariableByte0.headlessCompress(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals((-4665), intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray0 = new long[3];
      longVariableByte0.headlessUncompress(longArray0, intWrapper0, 1, longArray0, intWrapper0, (-1128));
      assertEquals("1", intWrapper0.toString());
      assertEquals(1, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[11];
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[11];
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, 1063, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray0 = new long[3];
      byte[] byteArray0 = new byte[9];
      byteArray0[8] = (byte) (-1);
      longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)6, longArray0, intWrapper0);
      assertEquals(11.0F, intWrapper0.floatValue(), 0.01F);
      assertArrayEquals(new long[] {0L, 71494644084506624L, 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[6];
      byte[] byteArray0 = new byte[7];
      byteArray0[6] = (byte) (-59);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, 22, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[3];
      byte[] byteArray0 = new byte[6];
      byteArray0[5] = (byte) (-101);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)58, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      LongVariableByte longVariableByte0 = new LongVariableByte();
      byte[] byteArray0 = new byte[5];
      byteArray0[4] = (byte) (-44);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)14, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[2];
      byte[] byteArray0 = new byte[5];
      byteArray0[0] = (byte) (-1);
      byteArray0[4] = (byte) (-49);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)75, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[11];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte) (-4);
      // Undeclared exception!
      try { 
        longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)4, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[18];
      byte[] byteArray0 = new byte[3];
      byteArray0[2] = (byte) (-126);
      longVariableByte0.uncompress1(byteArray0, intWrapper0, (int) (byte)1, longArray0, intWrapper0);
      assertEquals(4.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(4, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      longVariableByte0.uncompress1(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[2];
      longArray0[1] = 72057594037927936L;
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 1601, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      byte[] byteArray0 = new byte[8];
      longVariableByte0.compress1(longArray0, intWrapper0, (byte)0, byteArray0, intWrapper0);
      assertEquals(0, intWrapper0.intValue());
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      longArray0[0] = 4398046511067L;
      byte[] byteArray0 = new byte[6];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 1693, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[2];
      longArray0[1] = 72057594037927915L;
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 196, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[2];
      longArray0[0] = 2097152L;
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 4, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      long[] longArray0 = new long[8];
      longArray0[1] = 268435456L;
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        longVariableByte0.compress1(longArray0, intWrapper0, 1844, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[2];
      longArray0[0] = 72057594037927936L;
      longVariableByte0.headlessCompress(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      assertEquals((short)3, intWrapper0.shortValue());
      assertArrayEquals(new long[] {0L, 32769L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[7];
      longArray0[0] = 4398046511104L;
      // Undeclared exception!
      try { 
        longVariableByte0.headlessCompress(longArray0, intWrapper0, 1873, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      String string0 = longVariableByte0.toString();
      assertEquals("LongVariableByte", string0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[3];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      longVariableByte0.compress0(longArray0, intWrapper0, (-2105376124), longArray0, intWrapper0);
      assertEquals((short) (-32124), intWrapper0.shortValue());
      assertEquals((byte) (-124), intWrapper0.byteValue());
  }
}
